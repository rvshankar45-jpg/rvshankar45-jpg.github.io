"""Phase 5 - full evaluation. Runs all 100 queries + 10 conversations through the waterfall
variants (each adds one optimization), the extra cache_full_kb variant, then the routing
head-to-head (eval/run_routing_eval.py), judges every distinct answer, and writes results/*.csv.

  .\\.venv\\Scripts\\python.exe -m eval.run_eval

Re-running is cheap: every model call is stored by request hash and reused, and judge verdicts
are cached, so an interrupted run resumes where it stopped and a clean re-run reproduces the CSVs.
"""
import json
import time
from concurrent.futures import ThreadPoolExecutor

import numpy as np
import pandas as pd

from eval import run_routing_eval as rre
from eval.judge import Judge, answer_hash, build_units
from src.common import ROOT, config, path
from src.llm import LLM
from src.router import LayaRouter
from src.v2_optimized import Pipeline

RESULTS = ROOT / config()["paths"]["results"]


class MemoRouter:
    """Laya is deterministic for a given text: score each text once, reuse it across variants
    (the logged laya_ms is that text's measured latency)."""

    def __init__(self, router: LayaRouter):
        self.router, self.memo = router, {}
        self.threshold, self.device = router.threshold, router.device

    def score(self, text: str) -> dict:
        if text not in self.memo:
            self.memo[text] = self.router.score(text)
        return self.memo[text]


def phase5(llm, router, q, convs, workers):
    cfg = config()
    variants = {**cfg["variants"], **cfg.get("extra_variants", {})}
    hit_rates = {}
    for name, flags in variants.items():
        t0 = time.time()
        pipe = Pipeline(flags, name, llm, router=router)
        with ThreadPoolExecutor(workers) as ex:
            list(ex.map(lambda i: pipe.answer(i, q.loc[i, "query"]), q.index))
        with ThreadPoolExecutor(workers) as ex:
            list(ex.map(pipe.run_conversation, convs))
        hit_rates[name] = pipe.rcache.hit_rate if pipe.rcache else None
        print(f"  {name}: done in {time.time() - t0:.0f}s (new calls so far {llm.new_calls})", flush=True)
    return hit_rates


def summarise_phase5(calls, scores, hit_rates):
    cfg = config()
    variants = list(cfg["variants"]) + list(cfg.get("extra_variants", {}))
    s0 = scores[scores.replicate == 0].set_index(["unit_id", "answer_hash"]).score
    rows, per_unit = [], []
    for v in variants:
        x = calls[calls.variant == v]
        a = x[x.call_type == "answer"].copy()
        a["quality"] = [s0.get((i, answer_hash(t)), np.nan) for i, t in zip(a.query_id, a.answer)]
        summ = x[x.call_type == "summary"]
        # end-to-end latency per answer: answer call + Laya + any summary call made for that turn
        extra = summ.groupby([summ.query_id + ".t" + summ.turn.astype(int).astype(str)]).latency_ms.sum()
        a["e2e_ms"] = a.latency_ms + a.laya_ms.fillna(0) + a.query_id.map(extra).fillna(0)
        per_unit.append(a.assign(variant=v)[["variant", "query_id", "model", "cost_usd", "input_tokens", "output_tokens",
                                             "cache_read_tokens", "cache_write_tokens", "e2e_ms", "quality", "cache_hit"]])
        is_conv = a.query_id.str.contains(r"\.t")
        rows.append({
            "variant": v, "flags": "+".join({**cfg["variants"], **cfg.get("extra_variants", {})}[v]) or "none",
            "answers": len(a), "model_calls": int((x.cache_hit != True).sum()),  # noqa: E712
            "total_cost_usd": x.cost_usd.sum(),
            "cost_singles_usd": a[~is_conv].cost_usd.sum(),
            "cost_conversations_usd": a[is_conv].cost_usd.sum() + summ.cost_usd.sum(),
            "summary_cost_usd": summ.cost_usd.sum(),
            "input_tokens": int(x.input_tokens.sum()), "cache_read_tokens": int(x.cache_read_tokens.sum()),
            "cache_write_tokens": int(x.cache_write_tokens.sum()),
            "total_input_tokens": int(x.input_tokens.sum() + x.cache_read_tokens.sum() + x.cache_write_tokens.sum()),
            "output_tokens": int(x.output_tokens.sum()),
            "p50_latency_ms": float(a.e2e_ms.median()), "p95_latency_ms": float(a.e2e_ms.quantile(0.95)),
            "mean_quality": a.quality.mean(), "pct_quality_ge4": (a.quality >= 4).mean(),
            "unscored_answers": int(a.quality.isna().sum()),
            "share_strong": (a[a.cache_hit != True].model == cfg["models"]["strong"]).mean(),  # noqa: E712
            "response_cache_hit_rate": hit_rates.get(v) if hit_rates else None,
            "prompt_cache_read_share": x.cache_read_tokens.sum() / max(1, (x.input_tokens + x.cache_read_tokens + x.cache_write_tokens).sum()),
            "capped_answers": int(a.capped.fillna(False).astype(bool).sum()),
        })
    return pd.DataFrame(rows), pd.concat(per_unit)


def run_all(phase5_on: bool = True, **kw):
    phase5_on = kw.get("phase5", phase5_on)
    cfg = config()
    workers = cfg["run"]["workers"]
    q = pd.read_csv(path("queries")).set_index("id")
    convs = json.loads(path("conversations").read_text(encoding="utf-8"))
    t0 = time.time()

    llm = LLM()
    llm.max_calls = cfg["run"]["max_calls_eval"]
    print("harness overhead:", llm.start(), flush=True)
    router = MemoRouter(LayaRouter())
    print(f"laya on {router.device}", flush=True)

    hit_rates = phase5(llm, router, q, convs, workers) if phase5_on else {}
    print("routing head-to-head ...", flush=True)
    rre.generate(llm, router, q, workers)
    llm.verify_overhead_unchanged()
    calls_file = RESULTS / ("calls_eval.csv" if phase5_on else "calls_routing.csv")
    llm.save(calls_file)
    calls = pd.read_csv(calls_file, keep_default_na=False, na_values=[""])
    print(f"generation done: {llm.new_calls} new calls, {time.time() - t0:.0f}s", flush=True)

    # ---- judge every distinct answer (one pass, all variants and strategies together)
    judge = Judge()
    ans = calls[calls.call_type == "answer"]
    units = build_units(zip(ans.query_id, ans.answer), q.reset_index(), convs)
    rows = judge.score(units, workers)
    # judge reliability: re-score the run-1 answers of the variance queries with a fresh judge pass
    vids = rre.variance_ids(q)
    base_ans = ans[ans.variant.isin(["rt_strong", "rt_cheap"]) & ans.query_id.isin(vids)]
    rows += Judge(replicate=1).score(build_units(zip(base_ans.query_id, base_ans.answer), q.reset_index(), convs), workers)
    scores = pd.DataFrame(rows)
    scores.to_csv(RESULTS / ("scores.csv" if phase5_on else "scores_routing.csv"), index=False)
    print(f"judging done: {judge.new_calls} new judge calls", flush=True)

    if phase5_on:
        summary, per_unit = summarise_phase5(calls, scores, hit_rates)
        summary.to_csv(RESULTS / "summary.csv", index=False)
        per_unit.to_csv(RESULTS / "per_answer_eval.csv", index=False)
        print(summary[["variant", "total_cost_usd", "total_input_tokens", "output_tokens", "p50_latency_ms",
                       "mean_quality", "pct_quality_ge4"]].to_string(index=False))
    res = rre.summarise(calls, scores, q)
    rre.write(res)
    print(res["summary"][["strategy", "total_cost_usd", "mean_quality", "quality_simple", "quality_complex",
                          "router_efficiency"]].to_string(index=False))
    print(res["effort"][["strategy", "thinking", "total_cost_usd", "thinking_tokens", "mean_quality", "quality_complex",
                         "p50_e2e_ms"]].to_string(index=False))
    print("recommended threshold:", res["recommended_threshold"])
    meta = {"overhead": llm.overhead, "new_model_calls": llm.new_calls, "new_judge_calls": judge.new_calls,
            "seconds": round(time.time() - t0), "laya_device": router.device, "response_cache_hit_rates": hit_rates}
    (RESULTS / "eval_meta.json").write_text(json.dumps(meta, indent=1))


def main():
    run_all(True)


if __name__ == "__main__":
    main()
