"""The copilot pipeline. Each optimization is an independent flag (config.yaml: flags):

  route          Laya scores P(complex); >= threshold -> strong model, else cheap model
  retrieve       send only the top-k kb.md sections (BM25) instead of the whole KB
  trim_history   last N turns verbatim + a running summary written by the cheap model
  prompt_cache   mark the static system prefix cacheable
  tight_prompt   ~150-token system prompt instead of the ~600-token persona
  output_cap     max_tokens cap + "be concise" instruction
  response_cache exact then semantic (cosine >= 0.92) cache of first-turn answers

With no flags on, this is exactly the naive v1 build (src/v1_naive.py).
"""
from src import prompts
from src.cache import ResponseCache
from src.common import config, path
from src.llm import LLM
from src.retriever import retrieve


class Pipeline:
    def __init__(self, flags, variant: str, llm: LLM, router=None, response_cache: ResponseCache | None = None,
                 threshold: float | None = None):
        cfg = config()
        self.cfg, self.flags, self.variant, self.llm = cfg, set(flags), variant, llm
        unknown = self.flags - set(cfg["flags"])
        if unknown:
            raise ValueError(f"unknown flags {unknown}")
        if "route" in self.flags and router is None:
            raise ValueError("route flag needs a LayaRouter")
        self.router = router
        self.threshold = cfg["router"]["threshold"] if threshold is None else threshold
        self.rcache = (response_cache or ResponseCache()) if "response_cache" in self.flags else None
        self.kb = path("kb").read_text(encoding="utf-8")
        self.strong, self.cheap = cfg["models"]["strong"], cfg["models"]["cheap"]

    # ------------------------------------------------------------------ prompt assembly
    def system_parts(self, context_query: str):
        """Returns (static, dynamic, chunk_ids). Static = everything identical across calls."""
        f = self.flags
        static = prompts.TIGHT_PROMPT if "tight_prompt" in f else prompts.LONG_PERSONA
        if "output_cap" in f:
            static += "\n\n" + self.cfg["generation"]["concise_instruction"]
        if "retrieve" in f:
            chunks = retrieve(context_query)
            dynamic = f"# {prompts.CHUNKS_HEADER}\n\n" + "\n\n".join(c["text"] for c in chunks)
            return static, dynamic, [c["id"] for c in chunks]
        return static + f"\n\n# {prompts.KB_HEADER}\n\n{self.kb}", "", ["full_kb"]

    @staticmethod
    def render_user(message: str, history: list[tuple[str, str]], summary: str | None) -> tuple[str, str]:
        if not history and not summary:
            return message, "none"
        parts, mode = [], "full"
        if summary:
            parts.append(f"[Summary of the earlier conversation]\n{summary}")
            mode = "trimmed"
        if history:
            turns = "\n".join(f"Customer: {u}\nAssistant: {a}" for u, a in history)
            parts.append(("[Most recent turns]\n" if summary else "[Conversation so far]\n") + turns)
        parts.append(f"[Customer's new message]\n{message}")
        return "\n\n".join(parts), mode

    # ------------------------------------------------------------------ one answer
    def answer(self, query_id: str, message: str, history=(), summary=None, turn=None, prev_user: str = "",
               force_model: str | None = None, replicate: int = 0, variant: str | None = None,
               thinking: bool | None = None, effort: str | None = None, max_tokens: int | None = None) -> dict:
        """force_model pins the answer model (routing head-to-head); replicate>0 forces a fresh call."""
        history = list(history)
        ctx = f"{prev_user}\n{message}" if prev_user else message  # routing / retrieval sees the last user turn too
        first_turn = turn in (None, 1)
        if self.rcache is not None and first_turn:  # checked first: a hit needs no routing and no model call
            hit = self.rcache.get(message)
            if hit:
                return self.llm.log_cache_hit(variant=self.variant, query_id=query_id, hit=hit,
                                              routed_by="response_cache", turn=turn)
        laya_score = laya_ms = None
        if force_model:
            model, routed_by = force_model, "forced"
        elif "route" in self.flags:
            s = self.router.score(ctx)
            laya_score, laya_ms = s["p_complex"], s["laya_ms"]
            model = self.strong if laya_score >= self.threshold else self.cheap
            routed_by = "laya"
        else:
            model, routed_by = self.strong, "fixed"


        static, dynamic, chunk_ids = self.system_parts(ctx)
        user, hmode = self.render_user(message, history, summary)
        g = self.cfg["generation"]
        max_tokens = max_tokens or (g["max_tokens_capped"] if "output_cap" in self.flags else g["max_tokens_uncapped"])
        row = self.llm.complete(variant=variant or self.variant, query_id=query_id, model=model, system_static=static,
                                system_dynamic=dynamic, user=user, max_tokens=max_tokens,
                                prompt_cache="prompt_cache" in self.flags, routed_by=routed_by,
                                laya_score=laya_score, laya_ms=laya_ms, turn=turn, chunk_ids=chunk_ids,
                                history_mode=hmode, replicate=replicate, thinking=thinking, effort=effort)
        if self.rcache is not None and first_turn and row["answer"] and not row["capped"]:
            self.rcache.put(message, {"answer": row["answer"], "model": model})
        return row

    # ------------------------------------------------------------------ conversations
    def _summarise(self, conv_id: str, turn: int, summary: str | None, dropped: tuple[str, str]) -> str:
        h = self.cfg["history"]
        user = (f"Current summary:\n{summary or '(none yet)'}\n\nTurn to add:\n"
                f"Customer: {dropped[0]}\nAssistant: {dropped[1]}")
        row = self.llm.complete(variant=self.variant, query_id=conv_id, model=self.cheap,
                                system_static=prompts.SUMMARY_PROMPT.format(max_words=h["summary_max_words"]),
                                user=user, max_tokens=300, routed_by="fixed", call_type="summary", turn=turn)
        return row["answer"].strip()

    def run_conversation(self, conv: dict) -> list[dict]:
        """Turns run in order; each turn's history is this variant's OWN earlier answers."""
        keep = self.cfg["history"]["keep_last_turns"]
        history, summary, rows, prev_user = [], None, [], ""
        for k, t in enumerate(conv["turns"], 1):
            if "trim_history" in self.flags and len(history) > keep:
                while len(history) > keep:  # fold turns that leave the window into the running summary
                    summary = self._summarise(conv["id"], k, summary, history.pop(0))
            row = self.answer(f"{conv['id']}.t{k}", t["user"], history, summary, turn=k, prev_user=prev_user)
            rows.append(row)
            history.append((t["user"], row["answer"]))
            prev_user = t["user"]
        return rows
