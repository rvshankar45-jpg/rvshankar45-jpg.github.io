"""Phase 6 charts. Every number plotted and every number in a title is computed here from
results/*.csv and recorded in report/charts_data.json, so qa/qa_charts.py can re-check them.

  .\\.venv\\Scripts\\python.exe -m report.make_charts
"""
import json

import matplotlib
import matplotlib.text
import matplotlib.ticker

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from src.common import ROOT, config  # noqa: E402

R = ROOT / "results"
OUT = ROOT / "report"
# Reference palette (dataviz skill, light mode): slots 1-2 validated as a pair.
SURFACE, INK, INK2, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#e4e3de"
BLUE, ORANGE, AQUA = "#2a78d6", "#eb6834", "#1baf7a"
MUTED = "#a8a7a1"
LABEL = {"v1_naive": "v1 naive", "plus_route": "+ Laya routing", "plus_retrieve": "+ retrieval",
         "plus_trim": "+ trim history", "plus_tight_cache": "+ tight prompt\n+ prompt cache",
         "v2_full": "v2 (+ output cap\n+ response cache)", "cache_full_kb": "full KB, cached\n(no retrieval)"}

plt.rcParams.update({"font.size": 15, "axes.titlesize": 21, "axes.titleweight": "bold", "axes.labelsize": 15,
                     "axes.edgecolor": GRID, "axes.labelcolor": INK2, "xtick.color": INK2, "ytick.color": INK2,
                     "axes.spines.top": False, "axes.spines.right": False, "figure.facecolor": SURFACE,
                     "axes.facecolor": SURFACE, "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.8,
                     "axes.axisbelow": True, "font.family": "DejaVu Sans", "legend.frameon": False,
                     "text.parse_math": False})  # '$' is currency here, never maths
DATA = {}


def fig(title, subtitle=None):
    f, ax = plt.subplots(figsize=(12, 6.75), dpi=150)
    f.suptitle(title, x=0.04, y=0.97, ha="left", fontsize=21, fontweight="bold", color=INK)
    if subtitle:
        f.text(0.04, 0.895, subtitle, ha="left", fontsize=13.5, color=INK2)
    return f, ax


def save(f, name, title, numbers):
    f.text(0.04, 0.015, "Leafy Support Copilot Token Lab - synthetic data; quality = LLM judge, 1-5", fontsize=10.5, color=MUTED)
    f.canvas.draw()  # layout check: every text element must sit inside the image
    fw = f.bbox.width
    hidden = set()  # tick labels outside an axis' view range are never drawn - skip them
    for ax_ in f.axes:
        for axis, lim in ((ax_.xaxis, ax_.get_xlim()), (ax_.yaxis, ax_.get_ylim())):
            lo, hi = min(lim), max(lim)
            for tk in axis.get_major_ticks():
                if not lo - 1e-9 <= tk.get_loc() <= hi + 1e-9:
                    hidden.update(map(id, (tk.label1, tk.label2)))
    clipped = [t.get_text()[:40] for t in f.findobj(matplotlib.text.Text)
               if id(t) not in hidden and t.get_visible() and t.get_text()
               and (t.get_window_extent().x1 > fw + 1 or t.get_window_extent().x0 < -1)]
    sizes = [t.get_fontsize() for t in f.findobj(matplotlib.text.Text) if id(t) not in hidden and t.get_visible() and t.get_text()]
    numbers = {**numbers, "_clipped_text": clipped, "_min_font_pt": min(sizes),
               "_axis_labels": [[a.get_xlabel(), a.get_ylabel()] for a in f.axes],
               # value axis = x for horizontal bars (equal heights, varying widths), else y
               "_ylims": [list(map(float, a.get_xlim() if a.patches and len({round(pp.get_height(), 6) for pp in a.patches}) == 1
                                   and len({round(pp.get_width(), 6) for pp in a.patches}) > 1 else a.get_ylim())) for a in f.axes],
               "_bar_axes": [bool(a.patches) for a in f.axes]}
    f.savefig(OUT / f"{name}.png", facecolor=SURFACE)
    plt.close(f)
    DATA[name] = {"title": title, "numbers": numbers}


def pct(a, b):
    return round(100 * (a - b) / b)


def main():
    cfg = config()
    s = pd.read_csv(R / "summary.csv").set_index("variant")
    rs = pd.read_csv(R / "routing_summary.csv").set_index("strategy")
    sw = pd.read_csv(R / "threshold_sweep.csv")
    conf = pd.read_csv(R / "routing_confusion.csv")
    rh = pd.read_csv(R / "router_head_summary.csv").set_index("router")
    eff = pd.read_csv(R / "effort_summary.csv").set_index("strategy")
    units = int(s.loc["v1_naive", "answers"])
    steps = ["v1_naive", "plus_route", "plus_retrieve", "plus_trim", "plus_tight_cache", "v2_full"]

    # 1 ---- cost waterfall
    cost = s.loc[steps, "total_cost_usd"]
    v1, v2 = cost.iloc[0], cost.iloc[-1]
    deltas = cost.diff().iloc[1:]
    biggest = deltas.idxmin()
    share_big = deltas[biggest] / (v2 - v1)
    title = f"Same chatbot, {-pct(v2, v1)}% cheaper - retrieval did {round(100 * share_big)}% of the work"
    f, ax = fig(title, f"Total cost for 100 queries + 10 conversations ({units} answers), US$ at list API prices")
    x = np.arange(len(steps))
    ax.bar(0, v1, color=ORANGE, width=0.62)
    for i, st in enumerate(steps[1:], 1):
        lo, hi = cost.iloc[i], cost.iloc[i - 1]
        ax.bar(i, hi - lo, bottom=lo, color=BLUE, width=0.62)
        ax.text(i, hi + 0.03, f"-${hi - lo:.2f}", ha="center", va="bottom", fontsize=13, color=INK)
    ax.bar(len(steps), v2, color=BLUE, width=0.62, edgecolor=INK, linewidth=1.2)
    ax.text(0, v1 + 0.03, f"${v1:.2f}", ha="center", va="bottom", fontsize=14, fontweight="bold", color=INK)
    ax.text(len(steps), v2 + 0.03, f"${v2:.2f}", ha="center", va="bottom", fontsize=14, fontweight="bold", color=INK)
    ax.set_xticks(list(x) + [len(steps)], [LABEL[k] for k in steps[:1]] + [LABEL[k].split("\n")[0] for k in steps[1:]] + ["v2 total"],
                  fontsize=12.5)
    ax.set_xticklabels(["v1 naive", "+ Laya\nrouting", "+ retrieval", "+ trim\nhistory", "+ tight prompt\n+ cache",
                        "+ output cap\n+ resp. cache", "v2 total"], fontsize=12.5)
    ax.set_ylabel("Cost (US$)")
    ax.set_ylim(0, v1 * 1.18)
    ax.grid(axis="x", visible=False)
    f.subplots_adjust(top=0.84, bottom=0.17, left=0.08, right=0.98)
    save(f, "01_cost_waterfall", title, {"v1": v1, "v2": v2, "deltas": deltas.round(6).to_dict(),
                                          "pct_cheaper": -pct(v2, v1), "biggest_step": biggest, "biggest_share_pct": round(100 * share_big)})

    # 2 ---- tokens per answer, stacked input/output
    tin = s.loc[["v1_naive", "v2_full"], "total_input_tokens"] / units
    tout = s.loc[["v1_naive", "v2_full"], "output_tokens"] / units
    tot = tin + tout
    red = -pct(tot["v2_full"], tot["v1_naive"])
    title = f"v2 sends {red}% fewer tokens per answer"
    f, ax = fig(title, "Average tokens per answer (input incl. cached, + output), same 140 answers")
    y = [1, 0]
    ax.barh(y, tin.values, color=[ORANGE, BLUE], height=0.5, label="input")
    ax.barh(y, tout.values, left=tin.values, color=[ORANGE, BLUE], alpha=0.45, height=0.5, label="output")
    for yi, k in zip(y, ["v1_naive", "v2_full"]):
        ax.text(tin[k] / 2, yi, f"in {tin[k]:,.0f}", ha="center", va="center", color="white", fontsize=14, fontweight="bold")
        ax.text(tot[k] + 60, yi, f"out {tout[k]:,.0f}  |  total {tot[k]:,.0f}", ha="left", va="center", color=INK, fontsize=14)
    ax.set_yticks(y, ["v1 naive", "v2 optimized"], fontsize=15)
    ax.set_xlabel("Tokens per answer")
    ax.set_xlim(0, tot.max() * 1.45)
    ax.grid(axis="y", visible=False)
    f.subplots_adjust(top=0.82, bottom=0.14, left=0.16, right=0.97)
    save(f, "02_tokens_per_answer", title, {"in": tin.round(1).to_dict(), "out": tout.round(1).to_dict(),
                                             "total": tot.round(1).to_dict(), "pct_fewer": red})

    # 3 ---- quality by variant
    order = steps + ["cache_full_kb"]
    q = s.loc[order, "mean_quality"]
    title = f"Retrieval cost the most quality; the cached full KB beat v1"
    f, ax = fig(title, "Mean judge score (1-5) per variant, 140 answers each; dashed line = v1 baseline")
    cols = [ORANGE] + [BLUE] * (len(steps) - 1) + [AQUA]
    ax.bar(range(len(order)), q.values, color=cols, width=0.62)
    ax.axhline(q["v1_naive"], color=INK2, linestyle="--", linewidth=1.5)
    for i, v in enumerate(q.values):  # value inside the bar top, clear of the baseline line
        ax.text(i, v - 0.22, f"{v:.2f}", ha="center", va="top", fontsize=14, color="white", fontweight="bold")
    ax.set_xticks(range(len(order)), ["v1 naive", "+ routing", "+ retrieval", "+ trim", "+ tight\n+ cache",
                                      "v2 full", "full KB\ncached"], fontsize=12.5)
    ax.set_ylim(1, 5)
    ax.set_ylabel("Quality (1-5)")
    ax.grid(axis="x", visible=False)
    f.subplots_adjust(top=0.84, bottom=0.15, left=0.08, right=0.98)
    save(f, "03_quality_by_variant", title, {"quality": q.round(4).to_dict()})

    # 4 ---- threshold sweep: cost vs complex-query quality (one axis each, a curve)
    rec = sw[sw.recommended].iloc[0]
    strong_cx = rs.loc["always_strong", "quality_complex"]
    nxt = sw[sw.threshold > rec.threshold].iloc[0]
    title = f"Raise Laya's threshold past {rec.threshold:.2f} and complex-query quality falls fast"
    f, ax = fig(title, "Each point = one routing threshold (100 queries). Lower cost to the left.")
    ax.plot(sw.total_cost, sw.quality_complex, color=BLUE, linewidth=2, marker="o", markersize=8)
    for r in sw.itertuples():
        if r.threshold in (0.3, 0.5, 0.55, 0.6, 0.7, 0.8):
            ax.annotate(f"{r.threshold:.2f}", (r.total_cost, r.quality_complex), textcoords="offset points",
                        xytext=(8, 6), fontsize=12.5, color=INK2)
    ax.scatter([rec.total_cost], [rec.quality_complex], s=260, facecolor="none", edgecolor=INK, linewidth=2, zorder=5)
    ax.annotate(f"chosen threshold {rec.threshold:.2f}\n${rec.total_cost:.3f}, complex quality {rec.quality_complex:.2f}",
                (rec.total_cost, rec.quality_complex), textcoords="data", xytext=(0.19, 3.95), fontsize=13, color=INK,
                arrowprops=dict(arrowstyle="-", color=INK2, linewidth=1))
    ax.axhline(strong_cx - 0.2, color=INK2, linestyle="--", linewidth=1.2)
    ax.text(sw.total_cost.min(), strong_cx - 0.2 + 0.03, "quality guard: always-Sonnet - 0.2", fontsize=12, color=INK2)
    ax.set_xlabel("Total cost, 100 queries (US$)")
    ax.set_ylabel("Quality on complex queries (1-5)")
    f.subplots_adjust(top=0.84, bottom=0.13, left=0.09, right=0.97)
    save(f, "04_threshold_sweep", title, {"recommended": float(rec.threshold), "rec_cost": float(rec.total_cost),
                                           "rec_cx_quality": float(rec.quality_complex), "next_cx_quality": float(nxt.quality_complex),
                                           "sweep": sw[["threshold", "total_cost", "quality_complex"]].round(4).to_dict("list")})

    # 5 ---- confusion matrix
    c = conf[conf.router == "laya"].pivot(index="label", columns="decision", values="n").loc[["simple", "complex"], ["cheap", "strong"]]
    title = f"Off-the-shelf Laya sent {c.loc['simple', 'strong']} of {c.loc['simple'].sum()} simple queries to Sonnet"
    f, ax = fig(title, "Laya zero-shot at threshold 0.50 vs hand labels (100 test queries)")
    ax.imshow(c.values, cmap=matplotlib.colors.LinearSegmentedColormap.from_list("b", ["#cde2fb", "#184f95"]), vmin=0, vmax=c.values.max())
    for i in range(2):
        for j in range(2):
            v = c.values[i, j]
            ax.text(j, i, str(v), ha="center", va="center", fontsize=28, fontweight="bold", color="white" if v > c.values.max() * 0.5 else INK)
    ax.set_xticks([0, 1], ["routed to Haiku", "routed to Sonnet"], fontsize=15)
    ax.set_yticks([0, 1], ["labelled simple", "labelled complex"], fontsize=15)
    ax.grid(False)
    f.subplots_adjust(top=0.84, bottom=0.12, left=0.2, right=0.8)
    save(f, "05_routing_confusion", title, {"matrix": c.to_dict()})

    # 6 ---- latency p50/p95 by variant
    lat = s.loc[order, ["p50_latency_ms", "p95_latency_ms"]] / 1000
    title = f"v2 answers faster: median {lat.loc['v2_full', 'p50_latency_ms']:.1f}s vs {lat.loc['v1_naive', 'p50_latency_ms']:.1f}s"
    f, ax = fig(title, "End-to-end model time per answer, seconds (API time reported per call + Laya + summaries)")
    w = 0.38
    xx = np.arange(len(order))
    ax.bar(xx - w / 2, lat.p50_latency_ms, w, color=BLUE, label="median (p50)")
    ax.bar(xx + w / 2, lat.p95_latency_ms, w, color=ORANGE, label="slow tail (p95)")
    ax.set_xticks(xx, ["v1 naive", "+ routing", "+ retrieval", "+ trim", "+ tight\n+ cache", "v2 full", "full KB\ncached"], fontsize=12.5)
    ax.set_ylabel("Seconds")
    ax.legend(loc="upper center", fontsize=13, ncol=2)
    ax.set_ylim(0, lat.values.max() * 1.25)
    ax.grid(axis="x", visible=False)
    f.subplots_adjust(top=0.84, bottom=0.15, left=0.08, right=0.98)
    save(f, "06_latency", title, {"p50_s": lat.p50_latency_ms.round(3).to_dict(), "p95_s": lat.p95_latency_ms.round(3).to_dict()})

    # 7 ---- projected monthly cost
    per = {"v1_naive": v1 / units, "v2_full": v2 / units}
    vols = [10_000, 100_000, 1_000_000]
    proj = {k: [p * n for n in vols] for k, p in per.items()}
    save_1m = proj["v1_naive"][2] - proj["v2_full"][2]
    title = f"At 1M answers a month, v2 saves ${save_1m:,.0f}"
    f, ax = fig(title, f"Projected monthly model cost from measured cost per answer (v1 ${per['v1_naive']:.4f}, v2 ${per['v2_full']:.4f})")
    xx = np.arange(3)
    ax.bar(xx - w / 2, proj["v1_naive"], w, color=ORANGE, label="v1 naive")
    ax.bar(xx + w / 2, proj["v2_full"], w, color=BLUE, label="v2 optimized")
    for i in range(3):
        ax.text(i - w / 2, proj["v1_naive"][i], f"${proj['v1_naive'][i]:,.0f}", ha="center", va="bottom", fontsize=13)
        ax.text(i + w / 2, proj["v2_full"][i], f"${proj['v2_full'][i]:,.0f}", ha="center", va="bottom", fontsize=13)
    ax.set_yscale("log")
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"${v:,.0f}"))
    ax.set_xticks(xx, ["10k / month", "100k / month", "1M / month"])
    ax.set_ylabel("US$ per month (log scale)")
    ax.legend(loc="upper left", fontsize=13)
    ax.grid(axis="x", visible=False)
    f.subplots_adjust(top=0.84, bottom=0.12, left=0.14, right=0.98)
    save(f, "07_projected_monthly_cost", title, {"per_answer": per, "volumes": vols, "proj": proj, "saving_1m": save_1m})

    # 8 ---- routing head-to-head scatter
    pts = {"Always Sonnet": rs.loc["always_strong"], "Always Haiku": rs.loc["always_cheap"],
           "Laya (zero-shot)": rs.loc["laya"], "LLM router (Haiku)": rs.loc["llm_router"], "Oracle (hand labels)": rs.loc["oracle"]}
    xs = {k: v.total_cost_usd for k, v in pts.items()}
    ys = {k: v.mean_quality for k, v in pts.items()}
    xs["Laya + trained head"], ys["Laya + trained head"] = rh.loc["laya_head", "cost_usd"], rh.loc["laya_head", "quality"]
    title = (f"Laya kept quality ({ys['Laya (zero-shot)']:.2f} vs {ys['Always Sonnet']:.2f}) but saved only "
             f"{-pct(xs['Laya (zero-shot)'], xs['Always Sonnet'])}% until trained")
    f, ax = fig(title, "Routing strategies on the same 100 queries: cost vs quality. Top-left is best.")
    for k in xs:
        hl = k.startswith("Laya")
        ax.scatter(xs[k], ys[k], s=220 if hl else 140, color=BLUE if hl else MUTED, edgecolor=SURFACE, linewidth=2, zorder=4)
        off = {"Always Sonnet": (-10, 12), "Always Haiku": (10, 6), "Laya (zero-shot)": (12, -48), "LLM router (Haiku)": (10, -22),
               "Oracle (hand labels)": (10, 8), "Laya + trained head": (-215, -52)}[k]
        if k == "Laya + trained head":  # placed in the empty area up-left, with a leader line
            ax.annotate(f"{k}\n${xs[k]:.3f} | {ys[k]:.2f}", (xs[k], ys[k]), textcoords="data", xytext=(0.255, 4.64),
                        fontsize=12.5, color=INK, fontweight="bold", arrowprops=dict(arrowstyle="-", color=INK2, linewidth=1))
            continue
        ax.annotate(f"{k}\n${xs[k]:.3f} | {ys[k]:.2f}", (xs[k], ys[k]), textcoords="offset points", xytext=off,
                    fontsize=12.5, color=INK if hl else INK2, fontweight="bold" if hl else "normal")
    ax.set_xlabel("Total cost, 100 queries (US$) - lower is better")
    ax.set_ylabel("Mean quality (1-5) - higher is better")
    ax.set_xlim(0.1, 0.58)
    ax.set_ylim(3.8, 4.75)
    f.subplots_adjust(top=0.84, bottom=0.13, left=0.09, right=0.97)
    save(f, "08_routing_scatter", title, {"cost": {k: float(v) for k, v in xs.items()}, "quality": {k: float(v) for k, v in ys.items()},
                                           "laya_pct_saving": -pct(xs["Laya (zero-shot)"], xs["Always Sonnet"])})

    # 9 ---- quality by strategy, simple vs complex
    names = ["always_strong", "always_cheap", "laya", "llm_router", "oracle"]
    lbl = ["Always\nSonnet", "Always\nHaiku", "Laya\n(zero-shot)", "LLM\nrouter", "Oracle\n(labels)"]
    qs_, qc_ = rs.loc[names, "quality_simple"], rs.loc[names, "quality_complex"]
    title = f"Haiku is weaker even on simple queries: {qs_['always_cheap']:.2f} vs Sonnet's {qs_['always_strong']:.2f}"
    f, ax = fig(title, "Mean judge score by query type and routing strategy (62 simple, 38 complex)")
    xx = np.arange(len(names))
    ax.bar(xx - w / 2, qs_, w, color=BLUE, label="simple queries")
    ax.bar(xx + w / 2, qc_, w, color=ORANGE, label="complex queries")
    for i in range(len(names)):
        ax.text(i - w / 2, qs_.iloc[i] + 0.03, f"{qs_.iloc[i]:.2f}", ha="center", fontsize=12)
        ax.text(i + w / 2, qc_.iloc[i] + 0.03, f"{qc_.iloc[i]:.2f}", ha="center", fontsize=12)
    ax.set_xticks(xx, lbl, fontsize=13)
    ax.set_ylim(1, 5.2)
    ax.set_ylabel("Quality (1-5)")
    ax.legend(loc="upper right", fontsize=13, ncol=2)
    ax.grid(axis="x", visible=False)
    f.subplots_adjust(top=0.84, bottom=0.15, left=0.08, right=0.98)
    save(f, "09_quality_simple_vs_complex", title, {"simple": qs_.round(4).to_dict(), "complex": qc_.round(4).to_dict()})

    # 10 ---- router overhead: two small panels (no dual axis)
    lm = rs.loc["laya", "p50_router_ms"]
    ll = rs.loc["llm_router", "p50_router_ms"]
    tok_l = rs.loc["laya", "router_input_tokens"] + rs.loc["laya", "router_output_tokens"]
    tok_ll = (rs.loc["llm_router", "router_input_tokens"] + rs.loc["llm_router", "router_output_tokens"]) / 100
    title = f"Laya adds no API tokens; the LLM router adds {tok_ll:,.0f} per query"
    f, (a1, a2) = plt.subplots(1, 2, figsize=(12, 6.75), dpi=150)
    f.suptitle(title, x=0.04, y=0.97, ha="left", fontsize=21, fontweight="bold", color=INK)
    f.text(0.04, 0.895, "Router overhead per query (median). Laya runs locally on a 4 GB laptop GPU.", fontsize=13.5, color=INK2)
    a1.bar([0, 1], [lm, ll], color=[BLUE, MUTED], width=0.55)
    a1.set_xticks([0, 1], ["Laya", "LLM router"])
    a1.set_title("Added latency (ms)", fontsize=16)
    for i, v in enumerate([lm, ll]):
        a1.text(i, v, f"{v:,.0f} ms", ha="center", va="bottom", fontsize=14)
    a2.bar([0, 1], [tok_l / 100, tok_ll], color=[BLUE, MUTED], width=0.55)
    a2.set_xticks([0, 1], ["Laya", "LLM router"])
    a2.set_title("API tokens per query", fontsize=16)
    for i, v in enumerate([tok_l / 100, tok_ll]):
        a2.text(i, v, f"{v:,.0f}", ha="center", va="bottom", fontsize=14)
    for a in (a1, a2):
        a.grid(axis="x", visible=False)
    f.subplots_adjust(top=0.78, bottom=0.12, left=0.08, right=0.97, wspace=0.3)
    save(f, "10_router_overhead", title, {"laya_ms": float(lm), "llm_router_ms": float(ll), "laya_tokens_per_q": float(tok_l / 100),
                                          "llm_router_tokens_per_q": float(tok_ll)})

    # 11 ---- trained routing head
    order11 = [("laya_zero_shot@0.50", "Laya\noff the shelf"), ("length_rule", "Message-length\nrule"),
               ("minilm_head", "MiniLM +\ntrained head"), ("laya_head", "Laya +\ntrained head"), ("hindsight_ceiling", "Perfect\n(hindsight)")]
    sv = [100 * rh.loc[k, "saving_vs_always_sonnet"] for k, _ in order11]
    zs, tr = sv[0], sv[3]
    title = f"270 labelled examples took Laya from {zs:.0f}% to {tr:.0f}% savings"
    f, ax = fig(title, "Cost saving vs always-Sonnet on 100 held-out queries. Trained heads learn 'will Haiku's answer hold up?'")
    cols = [MUTED, MUTED, MUTED, BLUE, AQUA]
    ax.bar(range(5), sv, color=cols, width=0.6)
    for i, (k, _) in enumerate(order11):
        ax.text(i, sv[i] + 0.6, f"{sv[i]:.0f}%\nquality {rh.loc[k, 'quality']:.2f}", ha="center", va="bottom", fontsize=12.5, color=INK)
    ax.set_xticks(range(5), [n for _, n in order11], fontsize=13)
    ax.set_ylabel("Saving vs always-Sonnet (%)")
    ax.set_ylim(0, max(sv) * 1.35)
    ax.grid(axis="x", visible=False)
    f.subplots_adjust(top=0.84, bottom=0.15, left=0.08, right=0.98)
    save(f, "11_trained_router_head", title, {"saving_pct": dict(zip([k for k, _ in order11], [round(v, 2) for v in sv])),
                                               "quality": {k: float(rh.loc[k, "quality"]) for k, _ in order11}})

    # 12 ---- effort within Sonnet (Phase 5c)
    en = ["always_strong", "sonnet_low", "sonnet_medium", "sonnet_high"]
    el = ["Thinking off", "Low effort", "Medium effort", "High effort"]
    ec = eff.loc[en, "total_cost_usd"]
    et = eff.loc[en, "thinking_tokens"]
    title = f"Sonnet on low effort was cheapest; high effort cost {pct(ec['sonnet_high'], ec['sonnet_low'])}% more"
    f, ax = fig(title, "Sonnet 5.5 on 50 stratified queries: cost and hidden thinking tokens by effort level")
    ax.bar(range(4), ec.values, color=[MUTED, BLUE, BLUE, BLUE], width=0.6)
    for i, k in enumerate(en):
        ax.text(i, ec[k] + 0.004, f"${ec[k]:.3f}\nquality {eff.loc[k, 'mean_quality']:.2f}\n{int(et[k]):,} thinking tok",
                ha="center", va="bottom", fontsize=12.5, color=INK)
    ax.set_xticks(range(4), el, fontsize=14)
    ax.set_ylabel("Cost, 50 queries (US$)")
    ax.set_ylim(0, ec.max() * 1.4)
    ax.grid(axis="x", visible=False)
    f.subplots_adjust(top=0.84, bottom=0.1, left=0.09, right=0.98)
    save(f, "12_effort_levels", title, {"cost": ec.round(6).to_dict(), "thinking_tokens": et.to_dict(),
                                         "quality": eff.loc[en, "mean_quality"].round(4).to_dict()})

    (OUT / "charts_data.json").write_text(json.dumps(DATA, indent=1, default=float))
    print("\n".join(f"{k}: {v['title']}" for k, v in DATA.items()))


if __name__ == "__main__":
    main()
