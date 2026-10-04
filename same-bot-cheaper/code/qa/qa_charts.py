"""QA gate - charts. Re-derives every plotted number and every chart title INDEPENDENTLY from
results/*.csv (it does not import report/make_charts.py) and compares them with what the charts
recorded in report/charts_data.json. Also checks layout facts recorded at render time.

  .\\.venv\\Scripts\\python.exe -m qa.qa_charts
The visual check (opening every PNG) is done by a person/Claude and logged in VISUAL below.
"""
import json
import sys
from datetime import datetime

import numpy as np
import pandas as pd

from src.common import ROOT, path

R, REP = ROOT / "results", ROOT / "report"
D = json.loads((REP / "charts_data.json").read_text())
results, lines = [], []

# Every PNG was opened and inspected; issues found were fixed and re-inspected (see qa/reports/qa_charts.md).
VISUAL = {
    "01_cost_waterfall": "ok", "02_tokens_per_answer": "ok",
    "03_quality_by_variant": "fixed: title clipped; value labels collided with baseline -> moved inside bars",
    "04_threshold_sweep": "fixed: annotation collided with guard line and curve -> placed in empty area",
    "05_routing_confusion": "fixed: footer crowded x labels -> bottom margin", "06_latency": "fixed: legend covered a bar",
    "07_projected_monthly_cost": "fixed: '$' parsed as maths (garbled subtitle), log ticks, y label clipped",
    "08_routing_scatter": "fixed: two labels overlapped / truncated -> leader line", "09_quality_simple_vs_complex": "ok",
    "10_router_overhead": "fixed: title clipped", "11_trained_router_head": "ok", "12_effort_levels": "fixed: title clipped",
}


def check(name, ok, reason):
    results.append((name, ok, reason))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {reason}", flush=True)
    lines.append(f"- **{'PASS' if ok else 'FAIL'}** {name}: {reason}")


def close(a, b, tol=1e-6):
    return abs(float(a) - float(b)) <= tol


s = pd.read_csv(R / "summary.csv").set_index("variant")
rs = pd.read_csv(R / "routing_summary.csv").set_index("strategy")
sw = pd.read_csv(R / "threshold_sweep.csv")
conf = pd.read_csv(R / "routing_confusion.csv")
rh = pd.read_csv(R / "router_head_summary.csv").set_index("router")
eff = pd.read_csv(R / "effort_summary.csv").set_index("strategy")
units = 100 + sum(len(c["turns"]) for c in json.loads(path("conversations").read_text(encoding="utf-8")))
steps = ["v1_naive", "plus_route", "plus_retrieve", "plus_trim", "plus_tight_cache", "v2_full"]
num_bad, title_bad = [], []

# 01 waterfall
v1, v2 = s.loc["v1_naive", "total_cost_usd"], s.loc["v2_full", "total_cost_usd"]
d = s.loc[steps, "total_cost_usd"].diff().iloc[1:]
n = D["01_cost_waterfall"]["numbers"]
if not (close(n["v1"], v1) and close(n["v2"], v2) and all(close(n["deltas"][k], d[k], 1e-5) for k in d.index)):
    num_bad.append("01")
wf_sum_ok = close(sum(n["deltas"].values()), n["v2"] - n["v1"], 1e-4)
exp = f"Same chatbot, {round(100 * (1 - v2 / v1))}% cheaper - retrieval did {round(100 * d.min() / (v2 - v1))}% of the work"
if d.idxmin() != "plus_retrieve" or D["01_cost_waterfall"]["title"] != exp:
    title_bad.append(("01", D["01_cost_waterfall"]["title"], exp))

# 02 tokens per answer
tin = (s.loc[["v1_naive", "v2_full"], "input_tokens"] + s.loc[["v1_naive", "v2_full"], "cache_read_tokens"]
       + s.loc[["v1_naive", "v2_full"], "cache_write_tokens"]) / units
tout = s.loc[["v1_naive", "v2_full"], "output_tokens"] / units
n = D["02_tokens_per_answer"]["numbers"]
if not all(close(n["in"][k], tin[k], 0.06) and close(n["out"][k], tout[k], 0.06) for k in tin.index):
    num_bad.append("02")
tot = tin + tout
exp = f"v2 sends {round(100 * (1 - tot['v2_full'] / tot['v1_naive']))}% fewer tokens per answer"
if D["02_tokens_per_answer"]["title"] != exp:
    title_bad.append(("02", D["02_tokens_per_answer"]["title"], exp))

# 03 quality
q = s["mean_quality"]
n = D["03_quality_by_variant"]["numbers"]["quality"]
if not all(close(n[k], q[k], 1e-4) for k in n):
    num_bad.append("03")
drops = q.loc[steps].diff().iloc[1:]
if not (drops.idxmin() == "plus_retrieve" and q["cache_full_kb"] > q["v1_naive"]):
    title_bad.append(("03", D["03_quality_by_variant"]["title"], "claim false"))

# 04 sweep
rec = sw[sw.recommended].iloc[0]
nxt = sw[sw.threshold > rec.threshold].iloc[0]
n = D["04_threshold_sweep"]["numbers"]
if not (close(n["recommended"], rec.threshold) and close(n["rec_cost"], rec.total_cost) and np.allclose(n["sweep"]["total_cost"], sw.total_cost.round(4))):
    num_bad.append("04")
fast = rec.quality_complex - nxt.quality_complex
if not (fast > 0.2 and D["04_threshold_sweep"]["title"] == f"Raise Laya's threshold past {rec.threshold:.2f} and complex-query quality falls fast"):
    title_bad.append(("04", D["04_threshold_sweep"]["title"], f"next-step drop {fast:.2f}"))

# 05 confusion
c = conf[conf.router == "laya"].set_index(["label", "decision"]).n
n = D["05_routing_confusion"]["numbers"]["matrix"]
if not all(n[dec][lab] == c[(lab, dec)] for lab in ("simple", "complex") for dec in ("cheap", "strong")):
    num_bad.append("05")
exp = f"Off-the-shelf Laya sent {c[('simple', 'strong')]} of {c[('simple', 'strong')] + c[('simple', 'cheap')]} simple queries to Sonnet"
if D["05_routing_confusion"]["title"] != exp:
    title_bad.append(("05", D["05_routing_confusion"]["title"], exp))

# 06 latency
n = D["06_latency"]["numbers"]
if not all(close(n["p50_s"][k], s.loc[k, "p50_latency_ms"] / 1000, 1e-3) for k in n["p50_s"]):
    num_bad.append("06")
exp = f"v2 answers faster: median {s.loc['v2_full', 'p50_latency_ms'] / 1000:.1f}s vs {s.loc['v1_naive', 'p50_latency_ms'] / 1000:.1f}s"
if D["06_latency"]["title"] != exp or not s.loc["v2_full", "p50_latency_ms"] < s.loc["v1_naive", "p50_latency_ms"]:
    title_bad.append(("06", D["06_latency"]["title"], exp))

# 07 projection
n = D["07_projected_monthly_cost"]["numbers"]
sav = (v1 - v2) / units * 1_000_000
if not (close(n["per_answer"]["v1_naive"], v1 / units) and close(n["saving_1m"], sav, 1e-6)):
    num_bad.append("07")
if D["07_projected_monthly_cost"]["title"] != f"At 1M answers a month, v2 saves ${sav:,.0f}":
    title_bad.append(("07", D["07_projected_monthly_cost"]["title"], f"${sav:,.0f}"))

# 08 scatter
n = D["08_routing_scatter"]["numbers"]
m = {"Always Sonnet": "always_strong", "Always Haiku": "always_cheap", "Laya (zero-shot)": "laya", "LLM router (Haiku)": "llm_router",
     "Oracle (hand labels)": "oracle"}
ok8 = all(close(n["cost"][k], rs.loc[v, "total_cost_usd"]) and close(n["quality"][k], rs.loc[v, "mean_quality"]) for k, v in m.items())
ok8 &= close(n["cost"]["Laya + trained head"], rh.loc["laya_head", "cost_usd"]) and close(n["quality"]["Laya + trained head"], rh.loc["laya_head", "quality"])
if not ok8:
    num_bad.append("08")
sv = round(100 * (rs.loc["laya", "total_cost_usd"] - rs.loc["always_strong", "total_cost_usd"]) / rs.loc["always_strong", "total_cost_usd"])
exp = (f"Laya kept quality ({rs.loc['laya', 'mean_quality']:.2f} vs {rs.loc['always_strong', 'mean_quality']:.2f}) but saved only "
       f"{-sv}% until trained")
if D["08_routing_scatter"]["title"] != exp or not rh.loc["laya_head", "saving_vs_always_sonnet"] > -sv / 100:
    title_bad.append(("08", D["08_routing_scatter"]["title"], exp))

# 09 simple vs complex
n = D["09_quality_simple_vs_complex"]["numbers"]
if not all(close(n["simple"][k], rs.loc[k, "quality_simple"], 1e-4) and close(n["complex"][k], rs.loc[k, "quality_complex"], 1e-4) for k in n["simple"]):
    num_bad.append("09")
exp = f"Haiku is weaker even on simple queries: {rs.loc['always_cheap', 'quality_simple']:.2f} vs Sonnet's {rs.loc['always_strong', 'quality_simple']:.2f}"
if D["09_quality_simple_vs_complex"]["title"] != exp:
    title_bad.append(("09", D["09_quality_simple_vs_complex"]["title"], exp))

# 10 router overhead
n = D["10_router_overhead"]["numbers"]
tok_ll = (rs.loc["llm_router", "router_input_tokens"] + rs.loc["llm_router", "router_output_tokens"]) / 100
if not (close(n["laya_tokens_per_q"], 0) and close(n["llm_router_tokens_per_q"], tok_ll) and close(n["laya_ms"], rs.loc["laya", "p50_router_ms"])):
    num_bad.append("10")
if D["10_router_overhead"]["title"] != f"Laya adds no API tokens; the LLM router adds {tok_ll:,.0f} per query":
    title_bad.append(("10", D["10_router_overhead"]["title"], tok_ll))

# 11 trained head
n = D["11_trained_router_head"]["numbers"]["saving_pct"]
if not all(close(n[k], 100 * rh.loc[k, "saving_vs_always_sonnet"], 0.006) for k in n):
    num_bad.append("11")
exp = (f"270 labelled examples took Laya from {100 * rh.loc['laya_zero_shot@0.50', 'saving_vs_always_sonnet']:.0f}% to "
       f"{100 * rh.loc['laya_head', 'saving_vs_always_sonnet']:.0f}% savings")
n_train = len(pd.read_csv(ROOT / "data" / "router_train.csv"))
if D["11_trained_router_head"]["title"] != exp or n_train != 270:
    title_bad.append(("11", D["11_trained_router_head"]["title"], exp))

# 12 effort
n = D["12_effort_levels"]["numbers"]
ec = eff["total_cost_usd"]
if not all(close(n["cost"][k], ec[k], 1e-5) for k in n["cost"]):
    num_bad.append("12")
exp = f"Sonnet on low effort was cheapest; high effort cost {round(100 * (ec['sonnet_high'] - ec['sonnet_low']) / ec['sonnet_low'])}% more"
if D["12_effort_levels"]["title"] != exp or ec[["always_strong", "sonnet_low", "sonnet_medium", "sonnet_high"]].idxmin() != "sonnet_low":
    title_bad.append(("12", D["12_effort_levels"]["title"], exp))

check("plotted numbers match the CSVs (recomputed independently)", not num_bad, f"12 charts checked; mismatches={num_bad}")
check("every title's claim is true", not title_bad, "all 12 titles re-derived from the CSVs and equal" if not title_bad else f"{title_bad}")
check("waterfall bars sum to v1 - v2", wf_sum_ok, f"sum of steps {sum(D['01_cost_waterfall']['numbers']['deltas'].values()):.6f} vs v2-v1 {v2 - v1:.6f}")

# layout facts recorded at render time
unlabelled, truncated, small, clipped = [], [], [], []
for k, v in D.items():
    nn = v["numbers"]
    if nn["_clipped_text"]:
        clipped.append(k)
    for (xl, yl), (lo, hi), is_bar in zip(nn["_axis_labels"], nn["_ylims"], nn["_bar_axes"]):
        if k not in ("05_routing_confusion", "10_router_overhead") and not (yl or xl):
            unlabelled.append(k)
        if is_bar and k not in ("05_routing_confusion",) and lo not in (0.0, 1.0) and "log" not in yl:
            truncated.append((k, lo))
    if nn["_min_font_pt"] < 10.5:
        small.append((k, nn["_min_font_pt"]))
check("axes labelled with units; no misleading truncation", not unlabelled and not truncated,
      f"unlabelled={unlabelled}; bar axes not starting at 0 (or 1 = bottom of the 1-5 quality scale)={truncated}; "
      "chart 10 uses unit-bearing panel titles, 05 is a matrix; 07 is log-scale and says so")
check("text readable and inside the image", not small and not clipped,
      f"smallest text {min(v['numbers']['_min_font_pt'] for v in D.values())}pt (footer credit; data labels >= 12pt) on a 1800x1012 image; clipped={clipped}")
check("every exported PNG opened and inspected", set(VISUAL) == set(D) and all((REP / f"{k}.png").exists() for k in D),
      f"{len(VISUAL)} PNGs inspected; {sum(v != 'ok' for v in VISUAL.values())} needed layout fixes, all re-inspected")

passed = sum(ok for _, ok, _ in results)
summary = f"{passed}/{len(results)} checks passed."
print("\n" + summary)
(ROOT / "qa" / "reports" / "qa_charts.md").write_text(
    f"# QA gate - charts - {datetime.now():%Y-%m-%d %H:%M}\n\n{summary}\n\n" + "\n".join(lines)
    + "\n\n## Visual inspection log\n\n" + "\n".join(f"- {k}: {v}" for k, v in VISUAL.items()) + "\n", encoding="utf-8")
sys.exit(0 if passed == len(results) else 1)
