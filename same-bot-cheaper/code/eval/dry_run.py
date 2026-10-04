"""Dry run (Phase 2): v1 and v2_full on 10 queries + one 5-turn conversation, plus every
flag switched on alone on a small set, so QA gate 2 can check logging, cost math, routing,
caching, output cap and toggle isolation before the full eval.

  .\\.venv\\Scripts\\python.exe -m eval.dry_run
Writes results/dryrun/calls.csv and results/dryrun/meta.json.
"""
import json
import time
from concurrent.futures import ThreadPoolExecutor

import pandas as pd

from src.common import ROOT, config, path
from src.llm import LLM
from src.router import LayaRouter
from src.v1_naive import build as build_v1
from src.v2_optimized import Pipeline

DRY_QUERIES = ["q001", "q013", "q024", "q045", "q060", "q077", "q063", "q088", "q091", "q099"]  # 6 simple / 4 complex
TOGGLE_QUERIES = ["q001", "q063", "q091"]                                                        # simple / medium / complex
CONV = "c05"                                                                                     # 5 turns: trimming kicks in at turn 4
# Only for the response-cache test: an exact-after-normalisation repeat and a paraphrase of q001.
REPEATS = [("dup_exact", "whats your return window"), ("dup_paraphrase", "What is your return window?")]


def main():
    cfg = config()
    out_dir = ROOT / cfg["paths"]["results"] / "dryrun"
    out_dir.mkdir(parents=True, exist_ok=True)
    q = pd.read_csv(path("queries")).set_index("id")
    conv = next(c for c in json.loads(path("conversations").read_text(encoding="utf-8")) if c["id"] == CONV)

    llm = LLM()
    t0 = time.time()
    overhead_start = llm.start()
    print("harness overhead:", overhead_start, flush=True)
    router = LayaRouter()
    print(f"laya loaded on {router.device} in {router.load_ms/1000:.1f}s", flush=True)

    def singles(pipe, ids):
        with ThreadPoolExecutor(cfg["run"]["workers"]) as ex:
            list(ex.map(lambda i: pipe.answer(i, q.loc[i, "query"]), ids))

    # full variants
    v1 = build_v1(llm)
    singles(v1, DRY_QUERIES)
    v1.run_conversation(conv)
    print("v1 done", flush=True)

    v2 = Pipeline(cfg["variants"]["v2_full"], "v2_full", llm, router=router)
    singles(v2, DRY_QUERIES)
    for rid, text in REPEATS:
        v2.answer(rid, text)
    v2.run_conversation(conv)
    print("v2_full done", flush=True)

    # each flag alone
    for flag in cfg["flags"]:
        p = Pipeline([flag], f"only_{flag}", llm, router=router)
        if flag == "trim_history":
            p.run_conversation(conv)
        elif flag == "response_cache":
            p.answer("q001", q.loc["q001", "query"])
            for rid, text in REPEATS:
                p.answer(rid, text)
        else:
            singles(p, TOGGLE_QUERIES)
        print(f"only_{flag} done", flush=True)

    llm.verify_overhead_unchanged()
    llm.save(out_dir / "calls.csv")
    meta = {"overhead": overhead_start, "new_calls": llm.new_calls, "seconds": round(time.time() - t0),
            "laya_device": router.device, "laya_load_ms": round(router.load_ms),
            "rcache_hit_rate_v2_full": v2.rcache.hit_rate, "rcache_hits_v2_full": v2.rcache.hits,
            "dry_queries": DRY_QUERIES, "toggle_queries": TOGGLE_QUERIES, "conversation": CONV, "repeats": REPEATS}
    (out_dir / "meta.json").write_text(json.dumps(meta, indent=1))
    print(json.dumps(meta, indent=1))


if __name__ == "__main__":
    main()
