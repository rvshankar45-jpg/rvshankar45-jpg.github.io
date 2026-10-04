"""Phase 5b - routing head-to-head. Routing is the only variable: every strategy uses the same
fixed setup (retrieve + tight_prompt + output_cap, no response cache), so each query's prompt and
retrieved chunks are identical whichever model answers.

Each query is answered ONCE by the strong model and ONCE by the cheap model; a strategy is then a
choice between those two answers (plus its own router cost). That makes the threshold sweep free.

Strategies: always_strong, always_cheap, laya (P(complex) >= threshold), llm_router (cheap model
classifies first), oracle (hand labels).

  .\\.venv\\Scripts\\python.exe -m eval.run_routing_eval    # generate (reusing stored calls), judge, summarise
"""
import json
import re
from concurrent.futures import ThreadPoolExecutor

import numpy as np
import pandas as pd

from src.common import ROOT, config, path
from src.v2_optimized import Pipeline

FIXED = ["retrieve", "tight_prompt", "output_cap"]
ROUTER_PROMPT = """You route customer messages for an online plant store's support copilot.
Reply with JSON only, no other text: {"label": "simple"} or {"label": "complex"}.
simple = a single-fact policy lookup a small, fast model can answer well.
complex = needs several policy facts combined, rules applied to the customer's specific situation, an edge case, several issues, or an upset customer."""
VARIANCE_N = 20
RESULTS = ROOT / config()["paths"]["results"]


def variance_ids(q: pd.DataFrame) -> list[str]:
    """20 queries stratified like the test set (12 simple / 8 complex), fixed seed."""
    s = q[q.label == "simple"].sample(12, random_state=11).index.tolist()
    c = q[q.label == "complex"].sample(8, random_state=11).index.tolist()
    return sorted(s + c)


def effort_ids(q: pd.DataFrame) -> list[str]:
    """Phase 5c sample: stratified (default 30 simple / 20 complex), fixed seed."""
    s = config()["effort_eval"]["sample"]
    return sorted(q[q.label == "simple"].sample(s["simple"], random_state=s["seed"]).index.tolist()
                  + q[q.label == "complex"].sample(s["complex"], random_state=s["seed"]).index.tolist())


def generate(llm, router, q: pd.DataFrame, workers: int) -> dict:
    cfg = config()
    strong, cheap = cfg["models"]["strong"], cfg["models"]["cheap"]
    pipe = Pipeline(FIXED, "rt_fixed", llm)
    laya = {}

    def one(qid):
        text = q.loc[qid, "query"]
        laya[qid] = router.score(text)
        pipe.answer(qid, text, force_model=strong, variant="rt_strong")
        pipe.answer(qid, text, force_model=cheap, variant="rt_cheap")
        llm.complete(variant="llm_router", query_id=qid, model=cheap, system_static=ROUTER_PROMPT, user=text,
                     max_tokens=50, routed_by="fixed", call_type="router")

    with ThreadPoolExecutor(workers) as ex:
        list(ex.map(one, q.index))

    def rep(qid):  # run-to-run variance: fresh generations of the same requests
        text = q.loc[qid, "query"]
        pipe.answer(qid, text, force_model=strong, variant="rt_strong_rep2", replicate=2)
        pipe.answer(qid, text, force_model=cheap, variant="rt_cheap_rep2", replicate=2)

    with ThreadPoolExecutor(workers) as ex:
        list(ex.map(rep, variance_ids(q)))

    ec = cfg["effort_eval"]  # Phase 5c: Sonnet with thinking on, at each effort level

    def eff(args):
        qid, lvl = args
        pipe.answer(qid, q.loc[qid, "query"], force_model=strong, variant=f"sonnet_{lvl}", thinking=True,
                    effort=lvl, max_tokens=ec["max_tokens"])

    with ThreadPoolExecutor(workers) as ex:
        list(ex.map(eff, [(i, lvl) for lvl in ec["levels"] for i in effort_ids(q)]))
    pd.DataFrame([{"query_id": k, **v} for k, v in laya.items()]).to_csv(RESULTS / "laya_scores.csv", index=False)
    return laya


def parse_router(text: str) -> str | None:
    m = re.search(r'"label"\s*:\s*"(simple|complex)"', str(text))
    return m.group(1) if m else None


# --------------------------------------------------------------------------- analysis
def _pct(x, p):
    return float(np.percentile(x, p)) if len(x) else float("nan")


def summarise(calls: pd.DataFrame, scores: pd.DataFrame, q: pd.DataFrame) -> dict:
    cfg = config()
    strong, cheap = cfg["models"]["strong"], cfg["models"]["cheap"]
    s0 = scores[scores.replicate == 0].set_index(["unit_id", "answer_hash"]).score
    from eval.judge import answer_hash

    def answers(variant):
        a = calls[(calls.variant == variant) & (calls.call_type == "answer")].set_index("query_id")
        a = a.loc[q.index]
        a["quality"] = [s0.get((i, answer_hash(t)), np.nan) for i, t in zip(a.index, a.answer)]
        return a

    S, C = answers("rt_strong"), answers("rt_cheap")
    rt = calls[calls.variant == "llm_router"].set_index("query_id").loc[q.index]
    laya = pd.read_csv(RESULTS / "laya_scores.csv").set_index("query_id").loc[q.index]

    base = pd.DataFrame(index=q.index)
    base["label"] = q.label
    base["laya_score"] = laya.p_complex
    base["laya_ms"] = laya.laya_ms
    base["llm_router_label"] = [parse_router(t) for t in rt.answer]
    base["llm_router_parse_failed"] = base.llm_router_label.isna()
    for side, df_ in (("strong", S), ("cheap", C)):
        base[f"{side}_cost"] = df_.cost_usd
        base[f"{side}_in"] = df_.input_tokens + df_.cache_read_tokens + df_.cache_write_tokens
        base[f"{side}_out"] = df_.output_tokens
        base[f"{side}_ms"] = df_.latency_ms
        base[f"{side}_quality"] = df_.quality
        base[f"{side}_answer"] = df_.answer
        base[f"{side}_chunks"] = df_.chunk_ids
        base[f"{side}_system_hash"] = df_.system_hash
        base[f"{side}_user_hash"] = df_.user_hash

    def strategy(name, to_strong, r_in=0, r_out=0, r_cost=0.0, r_ms=0.0):
        d = pd.DataFrame(index=q.index)
        d["strategy"] = name
        d["label"] = base.label
        d["decision"] = np.where(to_strong, "strong", "cheap")
        d["router_in"], d["router_out"], d["router_cost"], d["router_ms"] = r_in, r_out, r_cost, r_ms
        for col in ["cost", "in", "out", "ms", "quality"]:
            d[f"answer_{col}"] = np.where(to_strong, base[f"strong_{col}"], base[f"cheap_{col}"])
        d["total_cost"] = d.answer_cost + d.router_cost
        d["e2e_ms"] = d.answer_ms + d.router_ms
        return d

    t = cfg["router"]["threshold"]
    rt_tokens_in = rt.input_tokens + rt.cache_read_tokens + rt.cache_write_tokens
    llm_strong = (base.llm_router_label != "simple").to_numpy()  # parse failure -> strong (safe default)
    per_query = {
        "always_strong": strategy("always_strong", np.ones(len(q), bool)),
        "always_cheap": strategy("always_cheap", np.zeros(len(q), bool)),
        "laya": strategy("laya", (base.laya_score >= t).to_numpy(), r_ms=base.laya_ms),
        "llm_router": strategy("llm_router", llm_strong, rt_tokens_in, rt.output_tokens, rt.cost_usd, rt.latency_ms),
        "oracle": strategy("oracle", (base.label == "complex").to_numpy()),
    }

    # threshold sweep (laya), and the recommended threshold
    sweep = []
    a_s = per_query["always_strong"]
    strong_cx_q = a_s[a_s.label == "complex"].answer_quality.mean()
    for th in np.round(np.arange(cfg["router"]["sweep"]["start"], cfg["router"]["sweep"]["stop"] + 1e-9,
                                 cfg["router"]["sweep"]["step"]), 2):
        d = strategy(f"laya@{th:.2f}", (base.laya_score >= th).to_numpy(), r_ms=base.laya_ms)
        sweep.append({"threshold": th, "total_cost": d.total_cost.sum(), "mean_quality": d.answer_quality.mean(),
                      "quality_simple": d[d.label == "simple"].answer_quality.mean(),
                      "quality_complex": d[d.label == "complex"].answer_quality.mean(),
                      "share_strong": (d.decision == "strong").mean(),
                      "complex_to_cheap": int(((d.label == "complex") & (d.decision == "cheap")).sum()),
                      "simple_to_strong": int(((d.label == "simple") & (d.decision == "strong")).sum())})
    sweep = pd.DataFrame(sweep)
    sweep["complex_quality_gap_vs_strong"] = strong_cx_q - sweep.quality_complex
    ok = sweep[sweep.complex_quality_gap_vs_strong <= 0.2]
    rec = ok.sort_values(["total_cost", "threshold"]).iloc[0] if len(ok) else None
    sweep["recommended"] = sweep.threshold == (rec.threshold if rec is not None else -1)
    if rec is not None:
        per_query["laya_recommended"] = strategy(f"laya@{rec.threshold:.2f}",
                                                 (base.laya_score >= rec.threshold).to_numpy(), r_ms=base.laya_ms)

    cost_strong = per_query["always_strong"].total_cost.sum()
    cost_oracle = per_query["oracle"].total_cost.sum()
    rows = []
    for key, d in per_query.items():
        pos = d.label == "complex"
        pred = d.decision == "strong"
        cx_cheap = d[pos & ~pred]
        sm_strong = d[~pos & pred]
        rows.append({
            "strategy": d.strategy.iloc[0],
            "total_cost_usd": d.total_cost.sum(), "answer_cost_usd": d.answer_cost.sum(), "router_cost_usd": d.router_cost.sum(),
            "answer_input_tokens": int(d.answer_in.sum()), "answer_output_tokens": int(d.answer_out.sum()),
            "router_input_tokens": int(d.router_in.sum()), "router_output_tokens": int(d.router_out.sum()),
            "mean_quality": d.answer_quality.mean(), "quality_simple": d[~pos].answer_quality.mean(),
            "quality_complex": d[pos].answer_quality.mean(),
            "quality_drop_vs_always_strong": per_query["always_strong"].answer_quality.mean() - d.answer_quality.mean(),
            "pct_quality_ge4": (d.answer_quality >= 4).mean(),
            "p50_e2e_ms": _pct(d.e2e_ms, 50), "p95_e2e_ms": _pct(d.e2e_ms, 95),
            "p50_router_ms": _pct(d.router_ms, 50), "p95_router_ms": _pct(d.router_ms, 95),
            "share_strong": pred.mean(),
            "routing_accuracy": (pred == pos).mean() if key in ("laya", "llm_router", "laya_recommended") else np.nan,
            "precision_complex": (pred & pos).sum() / pred.sum() if key in ("laya", "llm_router", "laya_recommended") and pred.sum() else np.nan,
            "recall_complex": (pred & pos).sum() / pos.sum() if key in ("laya", "llm_router", "laya_recommended") else np.nan,
            "costly_misroutes": len(cx_cheap), "costly_misroute_mean_quality": cx_cheap.answer_quality.mean(),
            "wasted_spend_queries": len(sm_strong),
            "wasted_spend_usd": float((base.loc[sm_strong.index, "strong_cost"] - base.loc[sm_strong.index, "cheap_cost"]).sum()),
            "router_efficiency": (cost_strong - d.total_cost.sum()) / (cost_strong - cost_oracle) if cost_strong != cost_oracle else np.nan,
        })
    summary = pd.DataFrame(rows)

    # confusion matrices (rows = hand label, cols = decision)
    conf = []
    for key in ("laya", "laya_recommended", "llm_router"):
        if key in per_query:
            d = per_query[key]
            for lab in ("simple", "complex"):
                for dec in ("cheap", "strong"):
                    conf.append({"router": d.strategy.iloc[0], "label": lab, "decision": dec,
                                 "n": int(((d.label == lab) & (d.decision == dec)).sum())})

    # misroutes (laya at the configured threshold) and side-by-side examples
    L = per_query["laya"]
    mis = base.loc[L.index[(L.label == "complex") & (L.decision == "cheap")]].assign(type="complex_to_cheap")
    mis = pd.concat([mis, base.loc[L.index[(L.label == "simple") & (L.decision == "strong")]].assign(type="simple_to_strong")])
    mis.insert(0, "query", q.loc[mis.index, "query"])

    # variance: (a) fresh generations, judged; (b) the judge re-scoring the same answers
    var_rows = []
    s1 = scores[scores.replicate == 1].set_index(["unit_id", "answer_hash"]).score
    for side, rep_var in (("strong", "rt_strong_rep2"), ("cheap", "rt_cheap_rep2")):
        r2 = calls[(calls.variant == rep_var) & (calls.call_type == "answer")].set_index("query_id")
        for qid, r in r2.iterrows():
            a1 = base.loc[qid, f"{side}_answer"]
            var_rows.append({"query_id": qid, "model_side": side, "label": base.loc[qid, "label"],
                             "score_run1": s0.get((qid, answer_hash(a1)), np.nan),
                             "score_run2": s0.get((qid, answer_hash(r.answer)), np.nan),
                             "judge_rescore_run1": s1.get((qid, answer_hash(a1)), np.nan),
                             "cost_run1": base.loc[qid, f"{side}_cost"], "cost_run2": r.cost_usd})
    var = pd.DataFrame(var_rows)

    # Phase 5c: effort within Sonnet vs routing between models, on the same 50 queries
    eids = effort_ids(q)
    eff_rows, eff_pq = [], []
    for key in ("always_strong", "always_cheap", "laya", "llm_router", "oracle"):
        d = per_query[key].loc[eids]
        eff_rows.append({"strategy": d.strategy.iloc[0], "thinking": "off", "n": len(d), "total_cost_usd": d.total_cost.sum(),
                         "output_tokens": int(d.answer_out.sum()), "thinking_tokens": 0,
                         "mean_quality": d.answer_quality.mean(), "quality_simple": d[d.label == "simple"].answer_quality.mean(),
                         "quality_complex": d[d.label == "complex"].answer_quality.mean(),
                         "pct_quality_ge4": (d.answer_quality >= 4).mean(),
                         "p50_e2e_ms": _pct(d.e2e_ms, 50), "p95_e2e_ms": _pct(d.e2e_ms, 95)})
    for lvl in cfg["effort_eval"]["levels"]:
        e = calls[(calls.variant == f"sonnet_{lvl}") & (calls.call_type == "answer")].set_index("query_id").loc[eids]
        e["quality"] = [s0.get((i, answer_hash(t)), np.nan) for i, t in zip(e.index, e.answer)]
        e["label"] = q.loc[eids, "label"]
        eff_pq.append(e.assign(strategy=f"sonnet_{lvl}")[["strategy", "label", "cost_usd", "output_tokens", "thinking_tokens",
                                                          "latency_ms", "quality", "capped"]])
        eff_rows.append({"strategy": f"sonnet_{lvl}", "thinking": f"on ({lvl})", "n": len(e), "total_cost_usd": e.cost_usd.sum(),
                         "output_tokens": int(e.output_tokens.sum()), "thinking_tokens": int(e.thinking_tokens.sum()),
                         "mean_quality": e.quality.mean(), "quality_simple": e[e.label == "simple"].quality.mean(),
                         "quality_complex": e[e.label == "complex"].quality.mean(),
                         "pct_quality_ge4": (e.quality >= 4).mean(),
                         "p50_e2e_ms": _pct(e.latency_ms, 50), "p95_e2e_ms": _pct(e.latency_ms, 95)})
    effort = pd.DataFrame(eff_rows)

    # isolation evidence: identical prompts and chunks for both models on every query
    iso = {"system_identical": bool((base.strong_system_hash == base.cheap_system_hash).all()),
           "user_identical": bool((base.strong_user_hash == base.cheap_user_hash).all()),
           "chunks_identical": bool((base.strong_chunks == base.cheap_chunks).all())}
    return {"per_query": pd.concat(per_query.values()), "summary": summary, "sweep": sweep, "confusion": pd.DataFrame(conf),
            "misroutes": mis, "variance": var, "base": base, "isolation": iso, "effort": effort,
            "effort_per_query": pd.concat(eff_pq) if eff_pq else pd.DataFrame(),
            "recommended_threshold": None if rec is None else float(rec.threshold)}


def write(res: dict):
    res["summary"].to_csv(RESULTS / "routing_summary.csv", index=False)
    res["per_query"].to_csv(RESULTS / "routing_per_query.csv")
    res["sweep"].to_csv(RESULTS / "threshold_sweep.csv", index=False)
    res["confusion"].to_csv(RESULTS / "routing_confusion.csv", index=False)
    res["misroutes"].to_csv(RESULTS / "misroutes.csv")
    res["variance"].to_csv(RESULTS / "variance.csv", index=False)
    res["base"].to_csv(RESULTS / "routing_base.csv")
    res["effort"].to_csv(RESULTS / "effort_summary.csv", index=False)
    res["effort_per_query"].to_csv(RESULTS / "effort_per_query.csv")
    (RESULTS / "routing_isolation.json").write_text(json.dumps(
        {**res["isolation"], "recommended_threshold": res["recommended_threshold"]}, indent=1))
    lines = ["# Misroute examples (Laya at the configured threshold): cheap answer vs strong answer\n"]
    for typ in ("complex_to_cheap", "simple_to_strong"):
        m = res["misroutes"][res["misroutes"].type == typ].head(5)
        lines.append(f"\n## {typ} ({len(res['misroutes'][res['misroutes'].type == typ])} total, first 5)\n")
        for qid, r in m.iterrows():
            lines.append(f"\n### {qid} [{r.label}] Laya P(complex)={r.laya_score:.3f}\n\n**Customer:** {r.query}\n\n"
                         f"**Cheap model** (quality {r.cheap_quality}, ${r.cheap_cost:.4f}):\n\n{r.cheap_answer}\n\n"
                         f"**Strong model** (quality {r.strong_quality}, ${r.strong_cost:.4f}):\n\n{r.strong_answer}\n")
    (RESULTS / "misroute_examples.md").write_text("\n".join(lines), encoding="utf-8")


def main():
    from eval.run_eval import run_all
    run_all(phase5=False)


if __name__ == "__main__":
    main()
