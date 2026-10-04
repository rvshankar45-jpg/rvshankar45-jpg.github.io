"""Training data for the routing head (option A, added after the eval).

1. The strong model writes ~300 NEW customer questions (with reference answers) from kb.md in
   six styles. It never sees the test set. Questions too similar to any test query
   (cosine >= 0.90) or to each other (>= 0.95) are dropped, so the test set stays held out.
2. Both models answer every question with the 5b setup (retrieve + tight prompt + output cap).
3. The judge scores both answers. Label: haiku_ok = Haiku scored at least as well as Sonnet.

  .\\.venv\\Scripts\\python.exe -m eval.router_head_data
Writes data/router_train.csv and results/router_train_labels.csv. Resumable (calls are stored).
"""
import hashlib
import json
import sys
from concurrent.futures import ThreadPoolExecutor

import numpy as np
import pandas as pd

from eval.judge import Judge, answer_hash
from eval.run_routing_eval import FIXED
from src import claude_cli
from src.common import ROOT, config, path
from src.llm import LLM
from src.v2_optimized import Pipeline

STYLES = [
    "simple single-fact lookups (prices, time windows, yes/no policy facts), spread across ALL sections",
    "very short or sloppy messages: one-liners, typos, no punctuation, texting style - mostly single-fact questions",
    "questions that need TWO policy facts combined, or a fact applied to a number or date the customer gives",
    "customer-specific situations with dates, amounts, membership status or plan details that change the answer",
    "multi-issue messages, upset or impatient customers, repeat contacts, or requests that need escalation",
    "edge cases: exceptions, things the policy excludes, conditions that flip the answer, or questions the KB does not cover",
]
PER_STYLE = 50
GEN_SCHEMA = {"type": "object", "additionalProperties": False, "required": ["items"], "properties": {"items": {
    "type": "array", "items": {"type": "object", "additionalProperties": False,
                               "required": ["query", "reference_answer", "category"],
                               "properties": {"query": {"type": "string"}, "reference_answer": {"type": "string"},
                                              "category": {"type": "string"}}}}}}
GEN_PROMPT = """Write {n} realistic, varied customer messages to Leafy's support chat in this style:
  {style}
Rules: every message must be answerable (or clearly not covered) using ONLY the knowledge base in your instructions;
vary topics, phrasing, length and tone; no real brand, company or person names; no two messages alike.
For each, give a short reference_answer grounded strictly in the knowledge base (say so if the KB does not cover it),
and a one-word category (orders, returns, shipping, guarantee, damaged, payments, refunds, subscriptions, membership, contact, account, plant_safety, multi_issue, escalation)."""


def generate_questions(test_queries: pd.Series) -> pd.DataFrame:
    cfg = config()
    kb = path("kb").read_text(encoding="utf-8")
    cache = ROOT / cfg["paths"]["results"] / "cache" / "router_gen"
    cache.mkdir(parents=True, exist_ok=True)
    rows = []
    for k, style in enumerate(STYLES):
        user = GEN_PROMPT.format(n=PER_STYLE, style=style)
        f = cache / f"{hashlib.sha256((kb + user).encode()).hexdigest()[:20]}.json"
        if f.exists():
            items = json.loads(f.read_text(encoding="utf-8"))
        else:
            r = claude_cli.call(cfg["models"]["judge"], "You write test data for a plant store's support copilot.\n\n"
                                "LEAFY KNOWLEDGE BASE:\n\n" + kb, user, schema=GEN_SCHEMA, thinking=True,
                                effort=cfg["models"]["judge_effort"])
            items = r["structured"]["items"]
            f.write_text(json.dumps(items, indent=1), encoding="utf-8")
        rows += [{**i, "style": k} for i in items]
        print(f"  style {k}: {len(items)} questions", flush=True)
    df = pd.DataFrame(rows)

    from src.cache import _embedder
    m = _embedder()
    e_tr = m.encode(df["query"].tolist(), normalize_embeddings=True)
    e_te = m.encode(test_queries.tolist(), normalize_embeddings=True)
    df["max_sim_to_test"] = (e_tr @ e_te.T).max(axis=1)
    keep, kept_vecs = [], []
    for i, v in enumerate(e_tr):  # drop test look-alikes and near-duplicates within the training set
        if df.max_sim_to_test[i] >= 0.90 or (kept_vecs and max(np.stack(kept_vecs) @ v) >= 0.95):
            continue
        keep.append(i)
        kept_vecs.append(v)
    out = df.iloc[keep].reset_index(drop=True)
    out.insert(0, "id", [f"t{i:03d}" for i in range(len(out))])
    print(f"generated {len(df)}, kept {len(out)} (dropped {len(df) - len(out)} test look-alikes / duplicates)", flush=True)
    return out


def main():
    cfg = config()
    test = pd.read_csv(path("queries"))
    out_q = ROOT / "data" / "router_train.csv"
    tr = pd.read_csv(out_q) if out_q.exists() else generate_questions(test["query"])
    tr.to_csv(out_q, index=False)
    if "--generate-only" in sys.argv:
        return

    llm = LLM()
    llm.max_calls = 800
    print("harness overhead:", llm.start(), flush=True)
    pipe = Pipeline(FIXED, "trn", llm)

    def one(r):
        pipe.answer(r.id, r.query, force_model=cfg["models"]["strong"], variant="trn_strong")
        pipe.answer(r.id, r.query, force_model=cfg["models"]["cheap"], variant="trn_cheap")

    with ThreadPoolExecutor(cfg["run"]["workers"]) as ex:
        list(ex.map(one, list(tr.itertuples())))
    llm.verify_overhead_unchanged()
    calls = pd.DataFrame(llm.rows)
    calls.to_csv(ROOT / cfg["paths"]["results"] / "router_train_calls.csv", index=False)
    print(f"answers done: {llm.new_calls} new calls", flush=True)

    units = []
    for r in tr.itertuples():
        a = calls[calls.query_id == r.id]
        texts = list(dict.fromkeys(t for t in a.answer if isinstance(t, str) and t.strip()))
        units.append({"unit_id": r.id, "customer": r.query, "reference": r.reference_answer, "answers": texts})
    judge = Judge(units_per_call=8)
    sc = pd.DataFrame(judge.score(units, cfg["run"]["workers"])).set_index(["unit_id", "answer_hash"]).score
    print(f"judging done: {judge.new_calls} new judge calls", flush=True)

    lab = []
    for r in tr.itertuples():
        a = calls[calls.query_id == r.id].set_index("variant")
        s, c = a.loc["trn_strong"], a.loc["trn_cheap"]
        qs, qc = sc.get((r.id, answer_hash(s.answer))), sc.get((r.id, answer_hash(c.answer)))
        lab.append({"id": r.id, "strong_quality": qs, "cheap_quality": qc, "haiku_ok": int(qc >= qs),
                    "strong_cost": s.cost_usd, "cheap_cost": c.cost_usd})
    lab = pd.DataFrame(lab)
    lab.to_csv(ROOT / cfg["paths"]["results"] / "router_train_labels.csv", index=False)
    print(f"labels: haiku_ok={lab.haiku_ok.mean():.0%} of {len(lab)}; Sonnet q {lab.strong_quality.mean():.2f}, "
          f"Haiku q {lab.cheap_quality.mean():.2f}", flush=True)


if __name__ == "__main__":
    main()
