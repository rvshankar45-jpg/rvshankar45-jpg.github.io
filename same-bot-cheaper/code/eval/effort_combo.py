"""Routing x effort combinations on the Phase 5c sample (50 queries), from answers already
generated - no model calls. A combination picks, per query, the answer its rules would have
produced: Haiku's 5b answer, Sonnet's thinking-off 5b answer, or Sonnet's low-effort 5c answer.

  .\\.venv\\Scripts\\python.exe -m eval.effort_combo     -> results/effort_combo.csv
"""
import numpy as np
import pandas as pd

from src.common import ROOT, config

R = ROOT / "results"


def main():
    b = pd.read_csv(R / "routing_base.csv", index_col=0)
    e = pd.read_csv(R / "effort_per_query.csv", index_col=0)
    low = e[e.strategy == "sonnet_low"]
    B = b.loc[low.index]
    t = config()["router"]["threshold"]
    head = pd.read_csv(R / "router_head_decisions.csv", index_col=0).loc[low.index, "laya_head"].astype(bool)
    rows = []

    def add(name, to_sonnet, s_cost, s_q):
        cost = np.where(to_sonnet, s_cost, B.cheap_cost).sum()
        q = np.where(to_sonnet, s_q, B.cheap_quality)
        lab = B.label.values
        rows.append({"setup": name, "cost_usd": cost, "quality": q.mean(), "quality_simple": q[lab == "simple"].mean(),
                     "quality_complex": q[lab == "complex"].mean(), "share_to_sonnet": np.mean(to_sonnet)})

    on = np.ones(len(B), bool)
    add("sonnet_thinking_off", on, B.strong_cost, B.strong_quality)
    add("sonnet_low", on, low.cost_usd, low.quality)
    add("laya_zero_shot + sonnet_off", (B.laya_score >= t).values, B.strong_cost, B.strong_quality)
    add("laya_zero_shot + sonnet_low", (B.laya_score >= t).values, low.cost_usd, low.quality)
    add("laya_head + sonnet_low", ~head.values, low.cost_usd, low.quality)
    add("oracle + sonnet_low", (B.label == "complex").values, low.cost_usd, low.quality)
    add("hindsight + sonnet_low", ~(B.cheap_quality >= low.quality).values, low.cost_usd, low.quality)
    add("always_haiku", ~on, B.strong_cost, B.strong_quality)
    df = pd.DataFrame(rows)
    df["saving_vs_sonnet_off"] = 1 - df.cost_usd / df.loc[0, "cost_usd"]
    df.to_csv(R / "effort_combo.csv", index=False)
    print(df.round(3).to_string(index=False))


if __name__ == "__main__":
    main()
