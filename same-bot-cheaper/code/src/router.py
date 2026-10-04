"""Laya complexity router. Loads the Laya decision model once and scores P(complex) locally.

API confirmed against the installed laya 0.3.22 README and source (agent.py): laya.load(repo)
returns an Agent; agent.predict(state, questions) returns {"answers": {qid: {...}}}, and a
"choice" answer carries "probabilities": {option: p}. If Laya fails to load we raise: no
silent fallback to another router.
"""
import threading
import time

from src.common import config


class LayaLoadError(RuntimeError):
    pass


class LayaRouter:
    def __init__(self, device: str | None = None):
        cfg = config()
        try:
            import laya
            import torch
            self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
            t0 = time.perf_counter()
            self.agent = laya.load(cfg["router"]["laya_model"], device=self.device)
            self.load_ms = (time.perf_counter() - t0) * 1000
        except Exception as e:  # fail loudly
            raise LayaLoadError(f"Laya failed to load ({cfg['router']['laya_model']}): {e!r}") from e
        q = cfg["laya"]["question"]
        self.questions = {"route": {"type": "choice", "instructions": q["instructions"],
                                    "criteria": dict(q["criteria"])}}
        self.threshold = cfg["router"]["threshold"]
        self._lock = threading.Lock()  # one forward pass at a time on the GPU

    def score(self, text: str) -> dict:
        with self._lock:
            t0 = time.perf_counter()
            res = self.agent.predict(text, self.questions)
            ms = (time.perf_counter() - t0) * 1000
        ans = res["answers"]["route"]
        p = float(ans["probabilities"]["complex"])
        if not 0.0 <= p <= 1.0:
            raise ValueError(f"Laya returned P(complex)={p}")
        return {"p_complex": p, "laya_ms": ms, "laya_choice": ans["choice"]}

    def decide(self, p_complex: float, threshold: float | None = None) -> str:
        t = self.threshold if threshold is None else threshold
        return "strong" if p_complex >= t else "cheap"
