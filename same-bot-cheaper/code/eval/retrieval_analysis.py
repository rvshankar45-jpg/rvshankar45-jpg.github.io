"""Retrieval analysis for the write-up (local, no model calls).

1. results/retrieval_recall.csv  - how often the right section is in the top k (k = 1..5), with the
   share of the manual sent. "Right section" is a proxy: the section that best matches each question's
   reference answer by keyword or by meaning (the same proxy used to choose hybrid retrieval).
2. results/retrieval_example.csv - every section's keyword score/rank, meaning score/rank and fused
   score for one question the search got wrong, in final order.

  .\\.venv\\Scripts\\python.exe -m eval.retrieval_analysis
"""
import numpy as np
import pandas as pd

from src.cache import _embedder
from src.common import ROOT, config, path
from src.retriever import _chunk_vecs, _index, _rank, _tokens, chunks, retrieve

R = ROOT / "results"
EXAMPLE = "whats ur price adjustment policy"


def main():
    C, m = chunks(), _embedder()
    ids = [c["id"] for c in C]
    q = pd.read_csv(path("queries"))

    def gold(ref):
        b = _index().get_scores(_tokens(ref))
        e = _chunk_vecs() @ m.encode([ref], normalize_embeddings=True)[0]
        return {ids[int(np.argmax(b))], ids[int(np.argmax(e))]}

    G = [gold(r) for r in q.reference_answer]
    rows = []
    for k in range(1, 6):
        hit = np.mean([bool(g & {c["id"] for c in retrieve(t, k)}) for g, t in zip(G, q["query"])])
        rows.append({"k": k, "right_section_found": hit, "share_of_manual_sent": k / len(C)})
    pd.DataFrame(rows).to_csv(R / "retrieval_recall.csv", index=False)

    k_rrf = config()["retrieval"].get("rrf_k", 60)
    bm = _index().get_scores(_tokens(EXAMPLE))
    em = _chunk_vecs() @ m.encode([EXAMPLE], normalize_embeddings=True)[0]
    pb = {i: r + 1 for r, i in enumerate(_rank(bm))}
    pe = {i: r + 1 for r, i in enumerate(_rank(em))}
    fused = [1 / (k_rrf + pb[i]) + 1 / (k_rrf + pe[i]) for i in range(len(C))]
    final = {i: r + 1 for r, i in enumerate(_rank(fused))}
    sent = {c["id"] for c in retrieve(EXAMPLE)}
    ex = pd.DataFrame([{"section_id": C[i]["id"], "section": C[i]["title"], "keyword_score": bm[i], "keyword_rank": pb[i],
                        "meaning_score": em[i], "meaning_rank": pe[i], "combined_score": fused[i], "combined_rank": final[i],
                        "sent": C[i]["id"] in sent} for i in range(len(C))]).sort_values("combined_rank")
    ex.to_csv(R / "retrieval_example.csv", index=False)
    print(pd.DataFrame(rows).round(3).to_string(index=False))
    print(ex.round(4).to_string(index=False))
    print("embedding dimensions:", m.get_sentence_embedding_dimension())


if __name__ == "__main__":
    main()
