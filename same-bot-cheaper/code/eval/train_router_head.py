"""Train a small routing head and test it on the 100 held-out test queries (option A).

The head is a logistic regression that predicts haiku_ok ("Haiku's answer is at least as good as
Sonnet's") from a frozen text encoder's representation of the customer message:
  - laya_head : Laya's own encoder (ModernBERT, frozen), mean-pooled over the message
  - minilm_head: the same head on a small general embedding model (all-MiniLM-L6-v2) - fairness check
  - length_rule: word count only (a trivial baseline)

Rules fixed BEFORE looking at test results:
  - Everything (head weights, regularisation, routing cut-off) is chosen on the training set only.
  - Routing cut-off: send to Haiku when P(haiku_ok) >= tau; tau = the cheapest setting whose
    out-of-fold training quality stays within 0.1 of always-Sonnet's training quality.
  - The 100 test queries are scored once, with the strong/cheap answers and judge scores already
    produced by the main eval (results/routing_base.csv), so test costs/qualities are directly
    comparable with laya zero-shot, the oracle and the hindsight ceiling.

  .\\.venv\\Scripts\\python.exe -m eval.train_router_head      (local only: no Claude calls)
"""
import json

import numpy as np
import pandas as pd
import torch
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, cross_val_predict
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from src.common import ROOT, config, path

R = ROOT / config()["paths"]["results"]
QUALITY_GUARD = 0.1


@torch.no_grad()
def laya_features(texts: list[str]) -> np.ndarray:
    import laya
    agent = laya.load(config()["router"]["laya_model"], device="cuda" if torch.cuda.is_available() else "cpu")
    enc, tok = agent.model.encoder, agent.tok
    dev = next(enc.parameters()).device
    out = []
    for i in range(0, len(texts), 16):
        b = tok(texts[i:i + 16], padding=True, truncation=True, max_length=256, return_tensors="pt").to(dev)
        h = enc(input_ids=b["input_ids"], attention_mask=b["attention_mask"]).last_hidden_state.float()
        m = b["attention_mask"].unsqueeze(-1).float()
        out.append(((h * m).sum(1) / m.sum(1)).cpu().numpy())
    del agent
    torch.cuda.empty_cache()
    return np.concatenate(out)


def minilm_features(texts):
    from src.cache import _embedder
    return _embedder().encode(texts, normalize_embeddings=True)


def length_features(texts):
    return np.array([[len(t.split())] for t in texts], dtype=float)


def auc(score, pos):
    s, c = score[~pos], score[pos]
    return float(np.mean([(ci > si) + 0.5 * (ci == si) for ci in c for si in s]))


def route(p_ok, tau, strong, cheap):
    to_cheap = p_ok >= tau
    return np.where(to_cheap, cheap, strong), to_cheap


def pick_tau(p_oof, lab):
    """Cheapest tau whose training quality stays within QUALITY_GUARD of always-Sonnet (training data only)."""
    base_q = lab.strong_quality.mean()
    best = (1.01, lab.strong_cost.sum())
    for tau in np.unique(np.round(p_oof, 4)):
        q, _ = route(p_oof, tau, lab.strong_quality.values, lab.cheap_quality.values)
        c, _ = route(p_oof, tau, lab.strong_cost.values, lab.cheap_cost.values)
        if q.mean() >= base_q - QUALITY_GUARD and c.sum() < best[1]:
            best = (float(tau), float(c.sum()))
    return best[0]


def main():
    tr = pd.read_csv(ROOT / "data" / "router_train.csv")
    lab = pd.read_csv(R / "router_train_labels.csv").set_index("id").loc[tr.id].reset_index()
    test_q = pd.read_csv(path("queries")).set_index("id")
    base = pd.read_csv(R / "routing_base.csv", index_col=0).loc[test_q.index]
    y_tr = lab.haiku_ok.values.astype(int)
    y_te = (base.cheap_quality >= base.strong_quality).values.astype(int)

    # QA: held-out integrity
    from src.cache import _embedder
    m = _embedder()
    sim = (m.encode(tr["query"].tolist(), normalize_embeddings=True) @ m.encode(test_q["query"].tolist(), normalize_embeddings=True).T)
    qa = {"train_n": len(tr), "test_n": len(test_q), "train_haiku_ok_rate": float(y_tr.mean()), "test_haiku_ok_rate": float(y_te.mean()),
          "max_train_test_similarity": float(sim.max()), "test_ids_in_train": int(tr.id.isin(test_q.index).sum()),
          "missing_train_labels": int(lab[["strong_quality", "cheap_quality"]].isna().any(axis=1).sum())}
    print("QA:", qa, flush=True)
    assert qa["test_ids_in_train"] == 0 and qa["max_train_test_similarity"] < 0.90 and qa["missing_train_labels"] == 0

    feats = {"laya_head": laya_features, "minilm_head": minilm_features, "length_rule": length_features}
    rows, sweeps, decisions = [], [], {}
    S, Cq = base.strong_quality.values, base.cheap_quality.values
    Sc, Cc = base.strong_cost.values, base.cheap_cost.values
    strong_cost = Sc.sum()

    def add_row(name, p_ok_test, tau, note):
        q, to_cheap = route(p_ok_test, tau, S, Cq)
        c, _ = route(p_ok_test, tau, Sc, Cc)
        decisions[name] = to_cheap
        lab_cx = (base.label == "complex").values
        rows.append({"router": name, "tau": tau, "cost_usd": c.sum(), "saving_vs_always_sonnet": 1 - c.sum() / strong_cost,
                     "quality": q.mean(), "quality_simple": q[~lab_cx].mean(), "quality_complex": q[lab_cx].mean(),
                     "share_to_haiku": to_cheap.mean(), "auc_haiku_ok": auc(p_ok_test, y_te.astype(bool)) if p_ok_test.std() else np.nan,
                     "note": note})

    for name, f in feats.items():
        X_tr, X_te = f(tr["query"].tolist()), f(test_q["query"].tolist())
        clf = make_pipeline(StandardScaler(), LogisticRegression(C=0.05 if name != "length_rule" else 1.0,
                                                                  class_weight="balanced", max_iter=5000))
        cv = StratifiedKFold(5, shuffle=True, random_state=0)
        p_oof = cross_val_predict(clf, X_tr, y_tr, cv=cv, method="predict_proba")[:, 1]
        tau = pick_tau(p_oof, lab)
        clf.fit(X_tr, y_tr)
        p_te = clf.predict_proba(X_te)[:, 1]
        add_row(name, p_te, tau, f"train OOF AUC {auc(p_oof, y_tr.astype(bool)):.2f}; tau chosen on train")
        for t in np.round(np.arange(0.05, 1.0, 0.05), 2):  # post-hoc sweep on test, for the chart only
            q, to_cheap = route(p_te, t, S, Cq)
            c, _ = route(p_te, t, Sc, Cc)
            sweeps.append({"router": name, "tau": t, "cost_usd": c.sum(), "quality": q.mean(), "share_to_haiku": to_cheap.mean()})

    # reference points on the same 100 test queries
    add_row("always_sonnet", np.zeros(len(base)), 0.5, "")
    add_row("always_haiku", np.ones(len(base)), 0.5, "")
    add_row("laya_zero_shot@0.50", 1 - base.laya_score.values, 0.5, "P(haiku_ok) taken as 1 - P(complex)")
    add_row("oracle_labels", (base.label == "simple").values.astype(float), 0.5, "hand labels")
    add_row("hindsight_ceiling", y_te.astype(float), 0.5, "uses test quality scores - not buildable")
    res = pd.DataFrame(rows)
    res.to_csv(R / "router_head_summary.csv", index=False)
    pd.DataFrame(sweeps).to_csv(R / "router_head_sweep.csv", index=False)
    pd.DataFrame({k: v.astype(int) for k, v in decisions.items()}, index=base.index).to_csv(R / "router_head_decisions.csv")
    (R / "router_head_qa.json").write_text(json.dumps(qa, indent=1))
    pd.set_option("display.width", 200)
    print(res.round(3).to_string(index=False))


if __name__ == "__main__":
    main()
