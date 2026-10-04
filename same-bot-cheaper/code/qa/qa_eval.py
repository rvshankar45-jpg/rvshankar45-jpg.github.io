"""QA gate - full eval (Phases 5 and 5b). Run after eval.run_eval:
    .\\.venv\\Scripts\\python.exe -m qa.qa_eval
Writes qa/reports/qa_eval.md and qa/reports/judge_handcheck.md (20 answers stratified by score).
"""
import json
import sys
from datetime import datetime

import numpy as np
import pandas as pd

from eval.judge import answer_hash
from src.common import ROOT, config, path

CFG = config()
R = ROOT / CFG["paths"]["results"]
REPORTS = path("qa_reports")
STRONG, CHEAP = CFG["models"]["strong"], CFG["models"]["cheap"]
results, lines = [], []


def check(name, ok, reason):
    results.append((name, ok, reason))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {reason}", flush=True)
    lines.append(f"- **{'PASS' if ok else 'FAIL'}** {name}: {reason}")


def note(msg):
    print("      " + msg)
    lines.append("    - " + msg)


calls = pd.read_csv(R / "calls_eval.csv", keep_default_na=False, na_values=[""])
scores = pd.read_csv(R / "scores.csv")
summary = pd.read_csv(R / "summary.csv")
rsum = pd.read_csv(R / "routing_summary.csv")
rpq = pd.read_csv(R / "routing_per_query.csv", index_col=0)
sweep = pd.read_csv(R / "threshold_sweep.csv")
var = pd.read_csv(R / "variance.csv")
iso = json.loads((R / "routing_isolation.json").read_text())
q = pd.read_csv(path("queries")).set_index("id")
convs = json.loads(path("conversations").read_text(encoding="utf-8"))
n_turns = sum(len(c["turns"]) for c in convs)
variants = list(CFG["variants"]) + list(CFG.get("extra_variants", {}))
ans = calls[calls.call_type == "answer"]

# ---------------------------------------------------------------- 1. completeness
expected = {v: 100 + n_turns for v in variants} | {"rt_strong": 100, "rt_cheap": 100, "rt_strong_rep2": 20, "rt_cheap_rep2": 20}
n_eff = sum(CFG["effort_eval"]["sample"][k] for k in ("simple", "complex"))
expected |= {f"sonnet_{lvl}": n_eff for lvl in CFG["effort_eval"]["levels"]}
got = ans.groupby("variant").size().to_dict()
got["llm_router"] = int((calls.variant == "llm_router").sum())
expected["llm_router"] = 100
missing = {v: (got.get(v, 0), n) for v, n in expected.items() if got.get(v, 0) != n}
empty = ans[ans.answer.isna() | (ans.answer.astype(str).str.strip() == "")]
s0 = scores[scores.replicate == 0].set_index(["unit_id", "answer_hash"]).score
unscored = [(r.variant, r.query_id) for r in ans.itertuples() if (r.query_id, answer_hash(r.answer)) not in s0.index]
dup_units = ans.groupby(["variant", "query_id"]).size().max()
check("every variant and strategy has all 100 queries + all conversation turns", not missing and empty.empty and not unscored and dup_units == 1,
      f"expected rows per variant met (variants: 100 + {n_turns} turns; 5b: 100; variance: 20); missing={missing}; "
      f"empty answers={len(empty)}; answers without a judge score={len(unscored)}; max rows per variant/unit={dup_units}")

# ---------------------------------------------------------------- 2. totals
bad = []
for r in summary.itertuples():
    x = calls[calls.variant == r.variant]
    for col, val in [("total_cost_usd", x.cost_usd.sum()), ("input_tokens", x.input_tokens.sum()),
                     ("output_tokens", x.output_tokens.sum()), ("cache_read_tokens", x.cache_read_tokens.sum())]:
        if abs(getattr(r, col) - val) > 1e-9:
            bad.append((r.variant, col))
for r in rsum.itertuples():
    d = rpq[rpq.strategy == r.strategy]
    for col, val in [("total_cost_usd", d.total_cost.sum()), ("answer_input_tokens", d.answer_in.sum()),
                     ("router_input_tokens", d.router_in.sum())]:
        if abs(getattr(r, col) - val) > 1e-9:
            bad.append((r.strategy, col))
# and per-query 5b answer cost equals the underlying call rows
rt = ans[ans.variant.isin(["rt_strong", "rt_cheap"])].set_index(["variant", "query_id"]).cost_usd
a_s = rpq[rpq.strategy == "always_strong"]
if not np.allclose(a_s.answer_cost.to_numpy(), rt.loc["rt_strong"].loc[a_s.index].to_numpy()):
    bad.append(("always_strong", "per-query cost vs calls"))
check("summary totals equal the sum of per-call rows", not bad,
      f"{len(summary)} variants x 4 totals and {len(rsum)} strategies x 3 totals re-summed from per-call / per-query rows; mismatches={bad}")

# ---------------------------------------------------------------- 2b. Phase 5c ran as specified
eff = ans[ans.variant.str.startswith("sonnet_")]
base5b = ans[ans.variant == "rt_strong"].set_index("query_id")
eff_iso = all((eff.system_hash == eff.query_id.map(base5b.system_hash)) & (eff.user_hash == eff.query_id.map(base5b.user_hash)))
think = eff.groupby("variant").thinking_tokens.agg(["sum", "mean", lambda s: (s > 0).mean()])
check("5c effort runs: thinking on, same prompts as 5b, only effort differs", eff_iso and (eff.model == STRONG).all()
      and set(eff.effort) == set(CFG["effort_eval"]["levels"]) and (eff.thinking.astype(str) == "True").all(),
      f"{len(eff)} calls; prompts identical to 5b={eff_iso}; thinking tokens per level (total / mean / share>0): "
      + "; ".join(f"{v}: {int(r['sum'])} / {r['mean']:.0f} / {r['<lambda_0>']:.0%}" for v, r in think.iterrows())
      + f"; capped={int(eff.capped.astype(str).eq('True').sum())}")

# ---------------------------------------------------------------- 3. isolation in 5b
check("5b isolation: strategies differ only in the answering model", all(iso[k] for k in ("system_identical", "user_identical", "chunks_identical")),
      f"for all 100 queries, strong vs cheap requests have identical system prompt={iso['system_identical']}, "
      f"user message={iso['user_identical']}, retrieved chunks={iso['chunks_identical']}")

# ---------------------------------------------------------------- 4. oracle / fixed strategies
orc = rpq[rpq.strategy == "oracle"]
ok_orc = ((orc.label == "complex") == (orc.decision == "strong")).all()
ok_fixed = (rpq[rpq.strategy == "always_strong"].decision == "strong").all() and (rpq[rpq.strategy == "always_cheap"].decision == "cheap").all()
ok_models = (ans[ans.variant == "rt_strong"].model == STRONG).all() and (ans[ans.variant == "rt_cheap"].model == CHEAP).all()
check("oracle follows the hand labels; always_strong / always_cheap use only their model", ok_orc and ok_fixed and ok_models,
      f"oracle={ok_orc} ({int((orc.decision == 'strong').sum())} strong = {int((q.label == 'complex').sum())} complex labels); "
      f"fixed strategies={ok_fixed}; underlying call models={ok_models}")

# ---------------------------------------------------------------- 5. router efficiency
eff = rsum.set_index("strategy").router_efficiency
out_of_range = eff[(eff < 0) | (eff > 1)].round(3).to_dict()
check("router efficiency within [0,1] (or explained)", True,
      f"{eff.round(3).to_dict()}" + (f"; OUT OF RANGE {out_of_range} - see explanation" if out_of_range else ""))
for k, v in out_of_range.items():
    if v > 1:
        note(f"{k} efficiency {v} > 1: it is CHEAPER than the oracle, i.e. it sends some complex queries to the cheap model "
             f"(the oracle never does). Read it together with its complex-query quality.")
    elif v < 0:
        note(f"{k} efficiency {v} < 0: it costs MORE than always_strong (router overhead or more strong calls).")

# ---------------------------------------------------------------- 6. judge reliability
j1 = var.dropna(subset=["judge_rescore_run1", "score_run1"])
judge_agree = (j1.judge_rescore_run1 == j1.score_run1).mean()
judge_mad = (j1.judge_rescore_run1 - j1.score_run1).abs().mean()
gen = var.dropna(subset=["score_run1", "score_run2"])
gen_mad = (gen.score_run2 - gen.score_run1).abs().mean()
gen_same = (gen.score_run2 == gen.score_run1).mean()
cost_cv = ((gen.cost_run2 - gen.cost_run1).abs() / gen.cost_run1).mean()
# 20 answers stratified by score for the human hand-check
pool = scores[scores.replicate == 0].merge(
    ans.assign(answer_hash=[answer_hash(t) for t in ans.answer])[["query_id", "answer_hash", "answer", "variant", "model"]]
    .drop_duplicates(["query_id", "answer_hash"]), left_on=["unit_id", "answer_hash"], right_on=["query_id", "answer_hash"])
picked = []
for sc in [1, 2, 3, 4, 5]:
    p = pool[pool.score == sc]
    picked.append(p.sample(min(4, len(p)), random_state=5))
picked = pd.concat(picked)
if len(picked) < 20:
    picked = pd.concat([picked, pool.drop(picked.index).sample(20 - len(picked), random_state=5)])
ref = {r.Index: (r.query, r.reference_answer) for r in q.itertuples()}
for c in convs:
    for k, t in enumerate(c["turns"], 1):
        ref[f"{c['id']}.t{k}"] = (" / ".join(x["user"] for x in c["turns"][:k]), t["reference_answer"])
md = ["# Judge hand-check: 20 answers stratified by judge score\n",
      "For each: do you agree with the score? Claude's own review is in the 'Claude check' line.\n"]
for i, r in enumerate(picked.sort_values("score").itertuples(), 1):
    md.append(f"\n## {i}. {r.unit_id} - judge score {r.score} (C{r.correctness}/Co{r.completeness}/P{r.policy}/T{r.tone}) - {r.variant}, {r.model}\n")
    md.append(f"**Customer:** {ref[r.unit_id][0]}\n\n**Reference:** {ref[r.unit_id][1]}\n\n**Answer:**\n\n{r.answer}\n\n**Judge note:** {r.note}\n\n**Claude check:** _pending_\n")
(REPORTS / "judge_handcheck.md").write_text("\n".join(md), encoding="utf-8")
check("judge reliability measured", len(j1) > 0 and len(gen) > 0,
      f"same answers re-judged: identical score {judge_agree:.0%}, mean |diff| {judge_mad:.2f} (n={len(j1)}); "
      f"fresh generations of the same request: identical score {gen_same:.0%}, mean |diff| {gen_mad:.2f}, "
      f"mean |cost diff| {cost_cv:.0%} (n={len(gen)}); 20 stratified answers written to qa/reports/judge_handcheck.md")

# ---------------------------------------------------------------- 7. threshold sweep sanity
sw = sweep.sort_values("threshold")
breaks = [(round(a.threshold, 2), round(b.threshold, 2)) for a, b in zip(sw.iloc[:-1].itertuples(), sw.iloc[1:].itertuples())
          if b.total_cost > a.total_cost + 1e-12]
check("threshold sweep: cost never rises as the threshold rises", not breaks,
      f"{len(sw)} thresholds {sw.threshold.min():.2f}-{sw.threshold.max():.2f}, cost ${sw.total_cost.max():.3f} -> ${sw.total_cost.min():.3f}; "
      f"breaks={breaks}")

# ---------------------------------------------------------------- 8. surprise check vs the brief's expectations
rs = rsum.set_index("strategy")
L, S, C = rs.loc["laya"], rs.loc["always_strong"], rs.loc["always_cheap"]
cost_pos = (L.total_cost_usd - C.total_cost_usd) / (S.total_cost_usd - C.total_cost_usd)  # 0 = at cheap, 1 = at strong
tok_change = (L.answer_input_tokens + L.answer_output_tokens) / (S.answer_input_tokens + S.answer_output_tokens) - 1
cost_change = L.total_cost_usd / S.total_cost_usd - 1
surprises = []
if abs(L.mean_quality - S.mean_quality) > 0.2:
    surprises.append(f"Laya quality {L.mean_quality:.2f} is not near always_strong {S.mean_quality:.2f}")
if cost_pos > 0.5:
    surprises.append(f"Laya cost sits {cost_pos:.0%} of the way from always_cheap to always_strong (expected near cheap)")
if abs(tok_change) >= abs(cost_change):
    surprises.append(f"Laya's token change ({tok_change:+.0%}) is not smaller than its cost change ({cost_change:+.0%})")
if rs.loc["llm_router"].total_cost_usd < L.total_cost_usd and rs.loc["llm_router"].mean_quality >= L.mean_quality:
    surprises.append("llm_router is both cheaper and at least as good as Laya")
w = summary.set_index("variant")
if w.loc["v2_full", "mean_quality"] < w.loc["v1_naive", "mean_quality"] - 0.2:
    surprises.append(f"v2_full quality {w.loc['v2_full', 'mean_quality']:.2f} dropped >0.2 below v1 {w.loc['v1_naive', 'mean_quality']:.2f}")
check("surprise check run (contradictions are flagged, not smoothed over)", True,
      f"{len(surprises)} result(s) contradict the brief's expectations" + ("" if surprises else " - none"))
for s in surprises:
    note("SURPRISE: " + s)

passed = sum(ok for _, ok, _ in results)
summary_line = f"{passed}/{len(results)} checks passed."
print("\n" + summary_line)
(REPORTS / "qa_eval.md").write_text(f"# QA gate - full eval - {datetime.now():%Y-%m-%d %H:%M}\n\n{summary_line}\n\n"
                                    + "\n".join(lines) + "\n", encoding="utf-8")
sys.exit(0 if passed == len(results) else 1)
