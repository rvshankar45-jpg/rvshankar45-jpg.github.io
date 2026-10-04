"""Response cache: exact match on normalised text, then semantic match (cosine >= threshold)."""
import re
import time
from functools import lru_cache

import numpy as np

from src.common import config


@lru_cache(maxsize=1)
def _embedder():
    from sentence_transformers import SentenceTransformer
    return SentenceTransformer(config()["qa"]["embedding_model"])


def normalise(text: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[^\w\s$]", "", text.lower())).strip()


class ResponseCache:
    def __init__(self, threshold: float | None = None):
        self.threshold = threshold or config()["response_cache"]["semantic_cosine"]
        self.exact: dict[str, dict] = {}
        self.keys: list[str] = []
        self.vecs: list[np.ndarray] = []
        self.lookups = 0
        self.hits = {"exact": 0, "semantic": 0}

    def get(self, query: str) -> dict | None:
        """Returns {'entry', 'kind', 'similarity', 'lookup_ms'} or None."""
        t0 = time.perf_counter()
        self.lookups += 1
        key = normalise(query)
        if key in self.exact:
            self.hits["exact"] += 1
            return {"entry": self.exact[key], "kind": "exact", "similarity": 1.0,
                    "lookup_ms": (time.perf_counter() - t0) * 1000}
        if self.vecs:
            v = _embedder().encode([query], normalize_embeddings=True)[0]
            sims = np.stack(self.vecs) @ v
            i = int(sims.argmax())
            if sims[i] >= self.threshold:
                self.hits["semantic"] += 1
                return {"entry": self.exact[self.keys[i]], "kind": "semantic", "similarity": float(sims[i]),
                        "lookup_ms": (time.perf_counter() - t0) * 1000}
        return None

    def put(self, query: str, entry: dict) -> None:
        key = normalise(query)
        if key not in self.exact:
            self.exact[key] = entry
            self.keys.append(key)
            self.vecs.append(_embedder().encode([query], normalize_embeddings=True)[0])

    @property
    def hit_rate(self) -> float:
        return (self.hits["exact"] + self.hits["semantic"]) / self.lookups if self.lookups else 0.0
