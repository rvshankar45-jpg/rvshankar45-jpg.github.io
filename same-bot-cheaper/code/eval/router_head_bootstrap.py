"""Is the trained Laya head's extra saving real? Resamples the 100 held-out test queries with
replacement and recomputes, for each resample, the saving (vs always-strong) and the mean quality
of Laya zero-shot and Laya + trained head. No model calls.

  .\\.venv\\Scripts\\python.exe -m eval.router_head_bootstrap   -> results/router_head_bootstrap.json
"""
import json

import numpy as np
import pandas as pd

from src.common import ROOT

R = ROOT / "results"
N_RESAMPLES, SEED = 2000, 0


def main():
    d = pd.read_csv(R / "router_head_decisions.csv", index_col=0)
    b = pd.read_csv(R / "routing_base.csv", index_col=0).loc[d.index]
    sc, cc, sq, cq = (b[c].to_numpy() for c in ["strong_cost", "cheap_cost", "strong_quality", "cheap_quality"])

    def stats(key, idx):
        cheap = d[key].to_numpy().astype(bool)[idx]
        cost = np.where(cheap, cc[idx], sc[idx]).sum()
        return 1 - cost / sc[idx].sum(), np.where(cheap, cq[idx], sq[idx]).mean()

    rng = np.random.default_rng(SEED)
    extra, dq = [], []
    for _ in range(N_RESAMPLES):
        idx = rng.integers(0, len(d), len(d))
        (s_h, q_h), (s_z, q_z) = stats("laya_head", idx), stats("laya_zero_shot@0.50", idx)
        extra.append(100 * (s_h - s_z))
        dq.append(q_h - q_z)
    extra, dq = np.array(extra), np.array(dq)
    out = {"resamples": N_RESAMPLES, "seed": SEED,
           "extra_saving_points_median": float(np.median(extra)),
           "extra_saving_points_ci95": [float(np.percentile(extra, 2.5)), float(np.percentile(extra, 97.5))],
           "share_resamples_extra_saving_positive": float(np.mean(extra > 0)),
           "quality_change_median": float(np.median(dq)),
           "quality_change_ci95": [float(np.percentile(dq, 2.5)), float(np.percentile(dq, 97.5))]}
    (R / "router_head_bootstrap.json").write_text(json.dumps(out, indent=1))
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
