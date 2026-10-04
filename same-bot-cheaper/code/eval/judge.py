"""LLM-as-judge quality scoring (judge = the strong model, via the configured backend).

Every distinct answer to a query is scored 1-5 against the reference answer and kb.md on four
criteria (correctness, completeness, policy adherence, tone) plus an overall score.
To save calls, one judge call scores several queries at once, with all of each query's distinct
answers shuffled and anonymised (the judge never sees which variant or model wrote them).
Each answer is scored on its own against the rubric, not ranked against the others.
Verdicts are cached in results/cache/judge/ keyed by a hash of the exact judge request.
"""
import hashlib
import json
import random
from concurrent.futures import ThreadPoolExecutor

from src import claude_cli
from src.common import ROOT, config, path

RUBRIC = """You are grading a customer-support copilot for Leafy, an online plant store, against the knowledge base below.

Score EACH answer independently on a 1-5 scale for:
- correctness: every fact, number, timeframe and rule is right per the knowledge base (5 = no errors; 1 = wrong on the main point).
- completeness: answers every part of the customer's message and gives what they need next (5 = complete; 1 = misses the main point).
- policy: follows policy and service rules - no invented policies or promises, escalates when the rules require, never asks for card numbers or passwords, safety advice first when relevant (5 = fully compliant; 1 = a serious breach).
- tone: polite, empathetic where needed, clear and appropriately concise (5 = excellent; 1 = rude, confusing or rambling).
- score: your OVERALL 1-5 judgement of the answer for this customer. Weight correctness and policy most: an answer with a wrong key fact or a policy breach cannot score above 2. 5 = you would send it as is; 4 = good, minor issues; 3 = acceptable but noticeably flawed; 2 = misleading or incomplete on something important; 1 = wrong or harmful.
The reference answer shows the key facts a good answer contains; an answer may be phrased differently or add correct, relevant detail. Do not reward length for its own sake.

LEAFY KNOWLEDGE BASE:

"""

SCHEMA = {"type": "object", "additionalProperties": False, "required": ["items"], "properties": {"items": {
    "type": "array", "items": {"type": "object", "additionalProperties": False,
                               "required": ["answer_id", "correctness", "completeness", "policy", "tone", "score", "note"],
                               "properties": {"answer_id": {"type": "string"},
                                              **{k: {"type": "integer", "enum": [1, 2, 3, 4, 5]}
                                                 for k in ["correctness", "completeness", "policy", "tone", "score"]},
                                              "note": {"type": "string"}}}}}}


def answer_hash(text: str) -> str:
    return hashlib.sha256(str(text).strip().encode()).hexdigest()[:16]


class Judge:
    def __init__(self, units_per_call: int = 4, replicate: int = 0):
        self.cfg = config()
        self.model = self.cfg["models"]["judge"]
        self.effort = self.cfg["models"]["judge_effort"]
        self.system = RUBRIC + path("kb").read_text(encoding="utf-8")
        self.per_call = units_per_call
        self.replicate = replicate
        self.cache = ROOT / self.cfg["paths"]["results"] / "cache" / "judge"
        self.cache.mkdir(parents=True, exist_ok=True)
        self.new_calls = 0
        self.tokens = {"in": 0, "out": 0}

    def _call(self, batch: list[dict]) -> list[dict]:
        rng = random.Random(f"{self.replicate}:" + ",".join(u["unit_id"] for u in batch))
        blocks, idmap = [], {}
        for u in batch:
            answers = list(u["answers"])
            rng.shuffle(answers)
            parts = [f"<query id=\"{u['unit_id']}\">", f"<customer>{u['customer']}</customer>",
                     f"<reference>{u['reference']}</reference>"]
            for k, a in enumerate(answers, 1):
                aid = f"{u['unit_id']}#{k}"
                idmap[aid] = answer_hash(a)
                parts.append(f"<answer id=\"{aid}\">\n{a}\n</answer>")
            parts.append("</query>")
            blocks.append("\n".join(parts))
        user = ("Grade every answer below. Return exactly one entry per answer id.\n\n" + "\n\n".join(blocks))
        key = hashlib.sha256(json.dumps([self.model, self.effort, self.replicate, self.system, user]).encode()).hexdigest()[:24]
        f = self.cache / f"{key}.json"
        if f.exists():
            out = json.loads(f.read_text(encoding="utf-8"))
        else:
            r = claude_cli.call(self.model, self.system, user, schema=SCHEMA, effort=self.effort, thinking=True)
            if r["structured"] is None:
                raise RuntimeError(f"judge returned no structured output: {r['text'][:200]}")
            out = r["structured"]
            got = {i["answer_id"] for i in out["items"]}
            if got != set(idmap):
                raise RuntimeError(f"judge skipped/invented ids: missing={set(idmap) - got} extra={got - set(idmap)}")
            self.new_calls += 1
            self.tokens["in"] += r["total_input_tokens"]
            self.tokens["out"] += r["output_tokens"]
            f.write_text(json.dumps(out, indent=1), encoding="utf-8")
        return [{**i, "unit_id": i["answer_id"].split("#")[0], "answer_hash": idmap[i["answer_id"]],
                 "replicate": self.replicate} for i in out["items"]]

    def score(self, units: list[dict], workers: int = 2) -> list[dict]:
        """units: [{unit_id, customer, reference, answers: [distinct texts]}] -> one row per (unit, answer)."""
        units = [u for u in units if u["answers"]]
        batches = [units[i:i + self.per_call] for i in range(0, len(units), self.per_call)]
        with ThreadPoolExecutor(workers) as ex:
            return [row for rows in ex.map(self._call, batches) for row in rows]


def build_units(answer_rows, queries, conversations) -> list[dict]:
    """Group distinct non-empty answers by unit (query id or conversation turn id)."""
    ref = {r.id: (r.query, r.reference_answer) for r in queries.itertuples()}
    for c in conversations:
        for k, t in enumerate(c["turns"], 1):
            prior = "\n".join(f"Customer (turn {j}): {x['user']}" for j, x in enumerate(c["turns"][:k - 1], 1))
            customer = (f"[Earlier customer messages in this conversation]\n{prior}\n[Latest message - grade the reply to this]\n"
                        if prior else "") + t["user"]
            ref[f"{c['id']}.t{k}"] = (customer, t["reference_answer"])
    units = {}
    for qid, text in answer_rows:
        if not isinstance(text, str) or not text.strip():
            continue
        u = units.setdefault(qid, {"unit_id": qid, "customer": ref[qid][0], "reference": ref[qid][1], "answers": []})
        if text.strip() not in [a.strip() for a in u["answers"]]:
            u["answers"].append(text)
    return [units[k] for k in sorted(units)]
