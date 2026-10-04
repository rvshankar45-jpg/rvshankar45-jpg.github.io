"""Single LLM wrapper. Every model call in the project goes through LLM.complete(), which
logs: variant, query_id, model, input/output/cache tokens, cost, latency, routing info,
response-cache info and the answer.

Token counts always come from the API's usage block (never estimated):
- backend=api: the usage fields of the Messages API response.
- backend=cli: the usage block Claude Code returns for its API call, minus the harness
  overhead calibrated at the start of the run (src/claude_cli.py). Claude Code caches on its
  own, so the input is split into uncached / cache-read / cache-write by the documented
  caching rules (cache_source=modeled).

Identical requests are answered once: the raw result is stored under results/cache/calls/
keyed by a hash of the exact request, and reused (reused=True) when another variant sends
the same bytes to the same model. Cost is recomputed per variant from the stored tokens.
"""
import hashlib
import json
import threading
import time
from pathlib import Path

from src import claude_cli
from src.common import ROOT, config
from src.pricing import cost_usd

FIELDS = ["variant", "query_id", "turn", "call_type", "model", "input_tokens", "output_tokens",
          "cache_read_tokens", "cache_write_tokens", "cost_usd", "latency_ms", "routed_by", "laya_score",
          "laya_ms", "cache_hit", "cache_kind", "cache_similarity", "answer",
          # extras for QA
          "payload_input_tokens", "static_prefix_tokens", "prompt_cache", "cache_source", "capped", "cap_emulated",
          "raw_output_tokens", "thinking_tokens", "effort", "thinking",
          "stop_reason", "max_tokens", "chunk_ids", "history_mode", "backend", "reused", "request_key",
          "overhead_tokens", "raw_total_input_tokens", "wall_ms", "system_hash", "static_hash", "user_hash"]


def _h(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()[:12]


class BudgetExceeded(RuntimeError):
    pass


class LLM:
    def __init__(self, backend: str | None = None):
        cfg = config()
        self.cfg = cfg
        self.backend = backend or cfg["backend"]
        self.rows: list[dict] = []
        self.new_calls = 0
        self.max_calls = cfg["run"]["max_calls_per_run"]
        self.store = ROOT / cfg["paths"]["results"] / "cache" / "calls"
        self.store.mkdir(parents=True, exist_ok=True)
        self._static_file = ROOT / cfg["paths"]["results"] / "cache" / f"static_tokens_{self.backend}.json"
        self._static = json.loads(self._static_file.read_text()) if self._static_file.exists() else {}
        self._clock: dict[tuple, float] = {}
        self._lock = threading.Lock()
        self.overhead: dict[str, int] = {}
        if self.backend == "api":
            import anthropic
            self._client = anthropic.Anthropic()
        elif self.backend != "cli":
            raise ValueError(f"unknown backend {self.backend}")

    # ------------------------------------------------------------------ calibration (cli)
    def calibrate(self, models=None) -> dict:
        """Measure the Claude Code harness overhead per model (system='.', user='.').
        Payload tokens of a call = its total input - this, accurate to ~2 tokens (the two dots)."""
        if self.backend != "cli":
            return {}
        models = models or [self.cfg["models"]["strong"], self.cfg["models"]["cheap"]]
        out = {}
        for m in models:
            r = claude_cli.call(m, ".", ".", max_output_tokens=None)
            self._count_call()
            out[m] = r["total_input_tokens"]
        return out

    def start(self):
        self.cli_version = claude_cli.version() if self.backend == "cli" else "api"
        self.overhead = self.calibrate()
        return self.overhead

    def verify_overhead_unchanged(self):
        """Fail loudly if the harness overhead drifted during the run (payload numbers would be off)."""
        if self.backend != "cli":
            return
        v = claude_cli.version()
        if v != self.cli_version:
            raise RuntimeError(f"Claude Code version changed during run: {self.cli_version} -> {v}")
        now = self.calibrate()
        if now != self.overhead:
            raise RuntimeError(f"harness overhead changed during run: start={self.overhead} end={now}")

    # ------------------------------------------------------------------ helpers
    def _count_call(self):
        with self._lock:
            self.new_calls += 1
            if self.new_calls > self.max_calls:
                raise BudgetExceeded(f"max_calls_per_run={self.max_calls} reached")
            check_version = self.backend == "cli" and self.new_calls % 50 == 0 and getattr(self, "cli_version", None)
        if check_version and claude_cli.version() != self.cli_version:
            # the calibrated overhead belongs to one CLI version: stop rather than log wrong payloads
            raise RuntimeError(f"Claude Code updated mid-run ({self.cli_version} -> {claude_cli.version()}); re-run to resume")

    def static_tokens(self, model: str, text: str) -> int:
        """Server-counted tokens of the static system prefix (cached on disk)."""
        key = f"{model}:{hashlib.sha256(text.encode()).hexdigest()[:16]}"
        if key not in self._static:
            if self.backend == "cli":
                self._count_call()
                self._count_call()  # system_tokens makes a probe call (+ overhead probe once)
                n = claude_cli.system_tokens(model, text)
            else:
                n = self._client.messages.count_tokens(
                    model=model, system=text, messages=[{"role": "user", "content": "."}]).input_tokens - \
                    self._client.messages.count_tokens(
                        model=model, system=".", messages=[{"role": "user", "content": "."}]).input_tokens
            with self._lock:
                self._static[key] = n
                self._static_file.write_text(json.dumps(self._static, indent=1))
        return self._static[key]

    def _raw_call(self, model, system_static, system_dynamic, user, max_tokens, prompt_cache, replicate=0,
                  thinking=None, effort=None):
        overrides = []  # only non-default settings enter the key, so earlier stored calls stay valid
        if thinking is not None and thinking != self.cfg["generation"]["thinking"]:
            overrides.append(f"thinking={thinking}")
        else:
            thinking = self.cfg["generation"]["thinking"]
        if effort:
            overrides.append(f"effort={effort}")
        system_text = system_static + ("\n\n" + system_dynamic if system_dynamic else "")
        key = hashlib.sha256(json.dumps([self.backend, model, system_text, user, max_tokens, thinking,
                                         prompt_cache if self.backend == "api" else None]
                                        + ([f"replicate={replicate}"] if replicate else []) + overrides).encode()).hexdigest()[:32]
        f = self.store / f"{key}.json"
        if f.exists():
            rec = json.loads(f.read_text(encoding="utf-8"))
            rec["reused"] = True
            return key, rec
        self._count_call()
        if self.backend == "cli":
            r = claude_cli.call(model, system_text, user, thinking=thinking, effort=effort, max_output_tokens=max_tokens)
            if r["capped"]:
                raise RuntimeError(f"CLI hit its {max_tokens}-token ceiling; raise generation.cli_output_ceiling")
            rec = {"text": r["text"], "capped": r["capped"], "stop_reason": r["stop_reason"],
                   "raw_usage": r["raw_usage"], "total_input_tokens": r["total_input_tokens"],
                   "output_tokens": r["output_tokens"], "thinking_tokens": r["thinking_tokens"],
                   "latency_ms": r["api_ms"], "wall_ms": r["wall_ms"], "overhead": self.overhead[model],
                   "cli_version": self.cli_version}
        else:
            rec = self._api_call(model, system_static, system_dynamic, user, max_tokens, prompt_cache, thinking)
        rec.update({"backend": self.backend, "model": model, "max_tokens": max_tokens, "recorded_at": time.time()})
        f.write_text(json.dumps(rec, indent=1), encoding="utf-8")
        rec["reused"] = False
        return key, rec

    def _api_call(self, model, system_static, system_dynamic, user, max_tokens, prompt_cache, thinking):
        blocks = [{"type": "text", "text": system_static}]
        if prompt_cache:
            blocks[0]["cache_control"] = {"type": "ephemeral"}
        if system_dynamic:
            blocks.append({"type": "text", "text": system_dynamic})
        kw = {}
        if not thinking and model == self.cfg["models"]["strong"]:
            kw["thinking"] = {"type": "between_tools"}  # Sonnet 5.5 cannot send "disabled"
        t0 = time.perf_counter()
        resp = self._client.messages.create(model=model, max_tokens=max_tokens, system=blocks,
                                            messages=[{"role": "user", "content": user}], **kw)
        ms = (time.perf_counter() - t0) * 1000
        u = resp.usage
        text = "".join(b.text for b in resp.content if b.type == "text")
        return {"text": text, "capped": resp.stop_reason == "max_tokens", "stop_reason": resp.stop_reason,
                "raw_usage": u.to_dict(), "input_tokens": u.input_tokens,
                "cache_read": u.cache_read_input_tokens or 0, "cache_write": u.cache_creation_input_tokens or 0,
                "total_input_tokens": u.input_tokens + (u.cache_read_input_tokens or 0) + (u.cache_creation_input_tokens or 0),
                "output_tokens": u.output_tokens, "thinking_tokens": 0, "latency_ms": ms, "wall_ms": ms, "overhead": 0}

    # ------------------------------------------------------------------ main entry point
    def complete(self, *, variant: str, query_id: str, model: str, system_static: str, system_dynamic: str = "",
                 user: str, max_tokens: int, prompt_cache: bool = False, routed_by: str = "fixed",
                 laya_score: float | None = None, laya_ms: float | None = None, call_type: str = "answer",
                 turn: int | None = None, chunk_ids: list | None = None, history_mode: str = "",
                 replicate: int = 0, thinking: bool | None = None, effort: str | None = None) -> dict:
        """replicate>0 forces a fresh call for the same request (run-to-run variance measurement)."""
        request_max = self.cfg["generation"]["cli_output_ceiling"] if self.backend == "cli" else max_tokens
        key, rec = self._raw_call(model, system_static, system_dynamic, user, request_max, prompt_cache, replicate,
                                  thinking, effort)
        payload = rec["total_input_tokens"] - rec["overhead"]
        out_tokens, text, capped, stop = rec["output_tokens"], rec["text"], rec["capped"], rec["stop_reason"]
        cap_emulated = False
        if self.backend == "cli" and out_tokens > max_tokens:
            # What the API would have done with max_tokens: stop at the cap. Tokens are exact; the text
            # is cut at the same fraction of its length (approximation of the token boundary).
            text = text[: int(len(text) * max_tokens / out_tokens)]
            out_tokens, capped, stop, cap_emulated = max_tokens, True, "max_tokens", True
        static_n = self.static_tokens(model, system_static) if prompt_cache else None

        if self.backend == "api":
            cr, cw, source = rec["cache_read"], rec["cache_write"], "observed"
        else:
            cr = cw = 0
            source = "modeled" if prompt_cache else "none"
            if prompt_cache and static_n >= self.cfg["cache"]["min_tokens"][model]:
                ck = (model, hashlib.sha256(system_static.encode()).hexdigest())
                now = time.time()
                with self._lock:
                    last = self._clock.get(ck)
                    if last is not None and now - last <= self.cfg["cache"]["ttl_seconds"]:
                        cr = static_n
                    else:
                        cw = static_n
                    self._clock[ck] = now
        inp = payload - cr - cw
        row = {
            "variant": variant, "query_id": query_id, "turn": turn, "call_type": call_type, "model": model,
            "input_tokens": inp, "output_tokens": out_tokens, "cache_read_tokens": cr,
            "cache_write_tokens": cw, "cost_usd": cost_usd(model, inp, out_tokens, cr, cw),
            "latency_ms": round(rec["latency_ms"] or 0), "routed_by": routed_by, "laya_score": laya_score,
            "laya_ms": None if laya_ms is None else round(laya_ms, 1), "cache_hit": False, "cache_kind": "",
            "cache_similarity": None, "answer": text,
            "payload_input_tokens": payload, "static_prefix_tokens": static_n, "prompt_cache": prompt_cache,
            "cache_source": source, "capped": capped, "cap_emulated": cap_emulated, "stop_reason": stop,
            "raw_output_tokens": rec["output_tokens"], "thinking_tokens": rec.get("thinking_tokens", 0),
            "effort": effort or "", "thinking": bool(thinking) if thinking is not None else self.cfg["generation"]["thinking"],
            "max_tokens": max_tokens, "chunk_ids": json.dumps(chunk_ids or []), "history_mode": history_mode,
            "backend": self.backend, "reused": rec["reused"], "request_key": key,
            "overhead_tokens": rec["overhead"], "raw_total_input_tokens": rec["total_input_tokens"],
            "wall_ms": rec["wall_ms"],
            "system_hash": _h(system_static + ("\n\n" + system_dynamic if system_dynamic else "")),
            "static_hash": _h(system_static), "user_hash": _h(user),
        }
        with self._lock:
            self.rows.append(row)
        return row

    def log_cache_hit(self, *, variant: str, query_id: str, hit: dict, routed_by: str, laya_score=None,
                      laya_ms=None, turn=None) -> dict:
        """A response-cache hit: no model call, zero tokens, the cached answer is served."""
        e = hit["entry"]
        row = {k: None for k in FIELDS}
        row.update({"variant": variant, "query_id": query_id, "turn": turn, "call_type": "answer",
                    "model": e["model"], "input_tokens": 0, "output_tokens": 0, "cache_read_tokens": 0,
                    "cache_write_tokens": 0, "cost_usd": 0.0, "latency_ms": round(hit["lookup_ms"]),
                    "routed_by": routed_by, "laya_score": laya_score,
                    "laya_ms": None if laya_ms is None else round(laya_ms, 1), "cache_hit": True,
                    "cache_kind": hit["kind"], "cache_similarity": round(hit["similarity"], 4),
                    "answer": e["answer"], "payload_input_tokens": 0, "prompt_cache": False, "cache_source": "none",
                    "capped": False, "backend": self.backend, "reused": False, "chunk_ids": "[]",
                    "wall_ms": round(hit["lookup_ms"])})
        with self._lock:
            self.rows.append(row)
        return row

    def save(self, path: Path):
        import pandas as pd
        pd.DataFrame(self.rows, columns=FIELDS).to_csv(path, index=False)
