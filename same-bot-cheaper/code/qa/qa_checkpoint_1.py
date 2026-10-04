"""QA gate 1 - data. Run:  .\.venv\Scripts\python.exe -m qa.qa_checkpoint_1

Every check prints PASS/FAIL with a one-line reason. Model checks use the judge
model (Sonnet 5.5) through the Claude Code CLI backend (src/claude_cli.py),
graded in batches of 25 items per call to save usage; a spot check confirms
batched verdicts agree with single-item verdicts. Verdicts are cached in
qa/reports/cache/ keyed by a hash of the exact inputs, so a re-run only pays
for rows whose data changed.
"""
import hashlib
import json
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

import numpy as np
import pandas as pd
import yaml

from src import claude_cli
from src.common import ROOT, config, cost_usd, path

CFG = config()
JUDGE = CFG["models"]["judge"]
CHEAP = CFG["models"]["cheap"]
EFFORT = CFG["models"]["judge_effort"]
BATCH = 25
REPORTS = path("qa_reports")
CACHE = REPORTS / "cache"
CACHE.mkdir(parents=True, exist_ok=True)

spend = {"calls": 0, "cached": 0, "usd": 0.0, "tokens_in": 0, "tokens_out": 0}
results, lines = [], []


def check(name, ok, reason):
    results.append((name, ok, reason))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {reason}", flush=True)
    lines.append(f"- **{'PASS' if ok else 'FAIL'}** {name}: {reason}")


def track(r):
    spend["calls"] += 1
    spend["tokens_in"] += r["total_input_tokens"]
    spend["tokens_out"] += r["output_tokens"]
    spend["usd"] += cost_usd(r["model"], r["input_tokens"], r["output_tokens"], r["cache_read_tokens"], r["cache_write_tokens"])


def judge_json(system, user, schema, tag):
    """One structured-output judge call, cached on disk by input hash."""
    key = hashlib.sha256(json.dumps([JUDGE, EFFORT, system, user, schema], sort_keys=True).encode()).hexdigest()[:24]
    f = CACHE / f"{tag}_{key}.json"
    if f.exists():
        spend["cached"] += 1
        return json.loads(f.read_text(encoding="utf-8"))
    r = claude_cli.call(JUDGE, system, user, schema=schema, effort=EFFORT, thinking=True)
    track(r)
    if r["structured"] is None:
        raise RuntimeError(f"{tag}: no structured output; text={r['text'][:200]}")
    f.write_text(json.dumps(r["structured"], indent=1), encoding="utf-8")
    return r["structured"]


def batched(items, fn, tag):
    """items: list of (id, text). fn builds the prompt for one batch. Returns {id: verdict}."""
    chunks = [items[i:i + BATCH] for i in range(0, len(items), BATCH)]
    with ThreadPoolExecutor(4) as ex:
        outs = list(ex.map(lambda c: fn(c, tag), chunks))
    got = {v["id"]: v for out in outs for v in out["items"]}
    missing = [i for i, _ in items if i not in got]
    if missing:
        raise RuntimeError(f"{tag}: judge skipped ids {missing}")
    return got


def item_schema(props, required):
    return {"type": "object", "additionalProperties": False, "required": ["items"],
            "properties": {"items": {"type": "array", "items": {
                "type": "object", "additionalProperties": False, "required": ["id", *required],
                "properties": {"id": {"type": "string"}, **props}}}}}


kb = path("kb").read_text(encoding="utf-8")
df = pd.read_csv(path("queries"), dtype=str, keep_default_na=False)
convs = json.loads(path("conversations").read_text(encoding="utf-8"))
KB_SYSTEM = "You audit test data for a customer-support copilot. LEAFY KNOWLEDGE BASE:\n\n" + kb

# ---------------------------------------------------------------- structure
req = ["id", "query", "label", "category", "reference_answer"]
missing_cols = [c for c in req if c not in df.columns]
n_empty = sum(int((df[c].str.strip() == "").sum()) for c in req if c in df.columns)
check("queries.csv structure", len(df) == 100 and df["id"].is_unique and not missing_cols and n_empty == 0,
      f"{len(df)} rows, unique ids={df['id'].is_unique}, missing cols={missing_cols}, empty fields={n_empty}")

bad_labels = sorted(set(df["label"]) - {"simple", "complex"})
t = CFG["qa"]["label_target"]
n_s, n_c = int((df["label"] == "simple").sum()), int((df["label"] == "complex").sum())
check("label values and mix",
      not bad_labels and abs(n_s - t["simple"]) <= t["tolerance"] and abs(n_c - t["complex"]) <= t["tolerance"],
      f"simple={n_s}, complex={n_c} (target {t['simple']}/{t['complex']} +/-{t['tolerance']}); invalid={bad_labels}; "
      f"tiers={df['tier'].value_counts().to_dict()}")

# ---------------------------------------------------------------- near duplicates
from sentence_transformers import SentenceTransformer  # noqa: E402

emb = SentenceTransformer(CFG["qa"]["embedding_model"]).encode(df["query"].tolist(), normalize_embeddings=True)
sim = emb @ emb.T
np.fill_diagonal(sim, -1)
thr = CFG["qa"]["near_duplicate_cosine"]
i, j = np.unravel_index(sim.argmax(), sim.shape)
dupes = [(df.id[a], df.id[b]) for a in range(len(df)) for b in range(a + 1, len(df)) if sim[a, b] > thr]
exact = int(df["query"].str.lower().str.strip().duplicated().sum())
check("no duplicate / near-duplicate queries", not dupes and exact == 0,
      f"exact dupes={exact}, pairs over {thr}={len(dupes)}; max cosine={sim[i, j]:.3f} ({df.id[i]} vs {df.id[j]})")

# ---------------------------------------------------------------- token measurement method + kb size
ovh = {m: [claude_cli.call(m, ".", claude_cli.PROBE_USER) for _ in range(3)] for m in (JUDGE, CHEAP)}
for rs in ovh.values():
    for r in rs:
        track(r)
const = {m: sorted({r["total_input_tokens"] for r in rs}) for m, rs in ovh.items()}
cut = kb.rfind("\n## ", 0, len(kb) // 2)
parts = {}
for m in (JUDGE, CHEAP):
    base = const[m][0]
    ra, rb, rk = (claude_cli.call(m, s, claude_cli.PROBE_USER) for s in (kb[:cut], kb[cut:], kb))
    for r in (ra, rb, rk):
        track(r)
    parts[m] = [r["total_input_tokens"] - base for r in (ra, rb, rk)]
add_diff = {m: p[2] - (p[0] + p[1]) for m, p in parts.items()}
check("CLI token measurement valid (constant overhead, additive counts)",
      all(len(v) == 1 for v in const.values()) and all(abs(d) <= 2 for d in add_diff.values()),
      f"overhead per model={ {m: v for m, v in const.items()} } over 3 calls; "
      f"tokens(A+B)-tokens(A)-tokens(B)={add_diff} (tolerance 2)")
kb_tokens = parts[JUDGE][2]
lo, hi = CFG["qa"]["kb_token_range"]
check("kb.md token count (server-counted, overhead removed)", lo <= kb_tokens <= hi,
      f"{kb_tokens} tokens on {JUDGE}; {parts[CHEAP][2]} on {CHEAP}; target {lo}-{hi} on the strong model (v1 sends kb.md to it)")

# ---------------------------------------------------------------- grounding
G_SCHEMA = item_schema({"supported": {"type": "boolean"}, "answers_question": {"type": "boolean"},
                        "unsupported_claims": {"type": "array", "items": {"type": "string"}}},
                       ["supported", "answers_question", "unsupported_claims"])
G_PROMPT = """Audit each reference answer below against the knowledge base in your instructions.
For EACH item return:
- supported: true only if EVERY factual claim (numbers, timeframes, rules, conditions) is stated in or directly follows from the knowledge base. Courtesy ("apologise"), and escalating to support/a Support Lead in line with the escalation rules, are fine.
- unsupported_claims: each claim that is missing from or contradicts the knowledge base (empty if none).
- answers_question: true if the reference answer correctly addresses what the customer asked, per the knowledge base.
Judge every item independently. Return one entry per id.

"""


def g_batch(chunk, tag):
    body = "\n\n".join(f"<item id=\"{i}\">\n<customer>{q}</customer>\n<reference>{r}</reference>\n</item>" for i, (q, r) in chunk)
    return judge_json(KB_SYSTEM, G_PROMPT + body, G_SCHEMA, tag)


g_items = [(r.id, (r.query, r.reference_answer)) for r in df.itertuples()]
for c in convs:
    for k, turn in enumerate(c["turns"], 1):
        prior = "\n".join(f"Customer: {t['user']}\nAgent: {t['reference_answer']}" for t in c["turns"][:k - 1])
        q = (f"[Earlier in the conversation]\n{prior}\n[Latest message]\n" if prior else "") + turn["user"]
        g_items.append((f"{c['id']}.t{k}", (q, turn["reference_answer"])))
ground = batched(g_items, g_batch, "ground")
bad = [i for i, _ in g_items if not (ground[i]["supported"] and ground[i]["answers_question"])]
pd.DataFrame([ground[i] for i, _ in g_items]).to_csv(REPORTS / "cp1_grounding.csv", index=False)
check("reference answers grounded in kb.md (judge)", not bad,
      f"{len(g_items) - len(bad)}/{len(g_items)} supported and on-question" + (f"; FAILING: {bad}" if bad else ""))
for b in bad:
    msg = f"    - {b}: answers_question={ground[b]['answers_question']}; unsupported={ground[b]['unsupported_claims']}"
    lines.append(msg)
    print(msg)

# spot check: batched vs single-item verdicts on 3 fixed items (one simple, one medium, one complex)
spot_ids = ["q001", "q065", "q091"]
single = {i: judge_json(KB_SYSTEM, G_PROMPT + f"<item id=\"{i}\">\n<customer>{dict(g_items)[i][0]}</customer>\n"
                        f"<reference>{dict(g_items)[i][1]}</reference>\n</item>", G_SCHEMA, "ground_single")["items"][0]
          for i in spot_ids}
mism = [i for i in spot_ids if (single[i]["supported"], single[i]["answers_question"])
        != (ground[i]["supported"], ground[i]["answers_question"])]
check("batched grading agrees with single-item grading (3 spot checks)", not mism,
      f"mismatches={mism}" if mism else f"{spot_ids} identical verdicts batched vs single")

# ---------------------------------------------------------------- blind re-label
L_SCHEMA = item_schema({"label": {"type": "string", "enum": ["simple", "complex"]}, "reason": {"type": "string"}},
                       ["label", "reason"])
L_PROMPT = """A customer-support copilot for an online plant store must decide which model answers each customer message.
The copilot has the store's policy document available either way.

Label each message:
- "simple": a small, fast model can answer it well. It is a single-fact lookup from the policy document.
- "complex": it needs a stronger model: combining two or more policy facts, applying a rule to the customer's specific dates/amounts/situation, a policy edge case or exception, several issues at once, or an upset/at-risk customer needing careful handling or escalation.
Judge each message independently, with a one-sentence reason. Return one entry per id.

"""


def l_batch(chunk, tag):
    body = "\n".join(f"<message id=\"{i}\">{q}</message>" for i, q in chunk)
    return judge_json("You label customer-support messages.", L_PROMPT + body, L_SCHEMA, tag)


relabel = batched([(r.id, r.query) for r in df.itertuples()], l_batch, "label")
df["judge_label"] = df.id.map(lambda i: relabel[i]["label"])
df["judge_reason"] = df.id.map(lambda i: relabel[i]["reason"])
dis = df[df.label != df.judge_label]
res_file = ROOT / "qa" / "label_resolutions.yaml"
resolutions = (yaml.safe_load(res_file.read_text(encoding="utf-8")) or {}) if res_file.exists() else {}
# A current disagreement is resolved only by a "kept" entry with a reason. A "relabelled" entry
# must no longer disagree (else the label change was never applied).
kept = {i for i, r in resolutions.items() if r.get("decision") == "kept" and r.get("reason")}
unresolved = [i for i in dis.id if i not in kept]
relabelled = sorted(i for i, r in resolutions.items() if r.get("decision") == "relabelled")
dis[["id", "query", "tier", "label", "judge_label", "judge_reason"]].to_csv(REPORTS / "cp1_label_disagreements.csv", index=False)
check("blind re-label: every disagreement resolved", not unresolved,
      f"agreement {(df.label == df.judge_label).mean():.0%} ({len(dis)} disagreements, all kept with written reason: "
      f"{sorted(set(dis.id) & kept)}); unresolved={unresolved}; previously relabelled to match judge: {relabelled}")

# ---------------------------------------------------------------- conversations
lens = [len(c["turns"]) for c in convs]
check("conversations.json structure",
      len(convs) == 10 and all(3 <= n <= 6 for n in lens) and len({c["id"] for c in convs}) == 10
      and all(t["user"].strip() and t["reference_answer"].strip() for c in convs for t in c["turns"]),
      f"{len(convs)} conversations, turns per conversation={lens}")

D_SCHEMA = item_schema({"needs_context": {"type": "boolean"}, "reason": {"type": "string"}}, ["needs_context", "reason"])
D_PROMPT = """Each message below was sent to a plant store's support chat. Each is shown ALONE, WITHOUT the earlier conversation.
needs_context: true if a support agent seeing only that message could NOT answer it correctly because it relies on something said earlier (an unstated subject, "it"/"that", a previously given date, amount, plan or item, a follow-up to an earlier answer). false if it is fully self-contained.
Judge each message independently. Return one entry per id.

"""
dep_items = [(f"{c['id']}.t{k}", t["user"]) for c in convs for k, t in enumerate(c["turns"], 1) if k >= 2]
dep = batched(dep_items, lambda ch, tag: judge_json(
    "You audit test data.", D_PROMPT + "\n".join(f"<message id=\"{i}\">{m}</message>" for i, m in ch), D_SCHEMA, tag), "dep")
standalone = [(i, m, dep[i]["reason"]) for i, m in dep_items if not dep[i]["needs_context"]]
check("later conversation turns depend on earlier context (judge)", not standalone,
      f"{len(dep_items) - len(standalone)}/{len(dep_items)} later turns need prior context"
      + (f"; self-contained: {[s[0] for s in standalone]}" if standalone else ""))
for s in standalone:
    msg = f"    - {s[0]}: \"{s[1]}\" - {s[2]}"
    lines.append(msg)
    print(msg)

# ---------------------------------------------------------------- real names scan
DENY_I = r"\b(amazon|walmart|home depot|ikea|etsy|ebay|shopify|stripe|paypal|klarna|afterpay|" \
         r"mastercard|amex|american express|apple pay|google pay|venmo|zelle|fedex|usps|dhl|" \
         r"royal mail|canada post|the sill|bloomscape|patch plants|greendigs|costco|google|microsoft|" \
         r"openai|anthropic|claude|gmail|hotmail|yahoo)\b"
DENY_CS = r"\b(Target|Lowe'?s|Visa|Discover|Affirm|UPS|Meta|Outlook|Horti)\b"  # also common words: case-sensitive
all_text = kb + "\n" + "\n".join(df["query"] + " " + df["reference_answer"]) + "\n" + json.dumps(convs)
hits = sorted({m.group(0) for m in re.finditer(DENY_I, all_text, flags=re.I)} | {m.group(0) for m in re.finditer(DENY_CS, all_text)})
emails = sorted(set(re.findall(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+", all_text)) - {"help@leafy.example"})
check("denylist scan for real brands / employers", not hits and not emails, f"denylist hits={hits}, other emails={emails}")

N_SCHEMA = {"type": "object", "additionalProperties": False, "required": ["findings"],
            "properties": {"findings": {"type": "array", "items": {
                "type": "object", "additionalProperties": False, "required": ["text", "kind"],
                "properties": {"text": {"type": "string"}, "kind": {"type": "string"}}}}}}
N_PROMPT = """Scan the text below for any REAL-WORLD named entity: companies, brands, product trade names, payment providers, couriers, retailers, employers, websites, or real people's names.
Do NOT report: the fictional store "Leafy" and its own invented names (Leafy Plus, Plant Club, Starter, Collector, Plant Care Specialist, Support Lead, help@leafy.example), common plant names, generic terms (credit card, digital wallet, courier), or example order numbers.
Return every finding (empty list if none).

<text>
{t}
</text>"""
names = judge_json("You audit data for real-world names.", N_PROMPT.format(t=all_text), N_SCHEMA, "names")["findings"]
check("model scan for real brand / employer / person names", not names, f"findings={names}")

# ---------------------------------------------------------------- summary + report
passed = sum(ok for _, ok, _ in results)
summary = (f"{passed}/{len(results)} checks passed. Usage this run: {spend['calls']} new CLI calls "
           f"({spend['cached']} cached verdicts reused), {spend['tokens_in']:,} input / {spend['tokens_out']:,} output tokens, "
           f"API-equivalent ${spend['usd']:.3f}")
print("\n" + summary)
(REPORTS / "qa_checkpoint_1.md").write_text(
    f"# QA gate 1 (data) - {datetime.now():%Y-%m-%d %H:%M}\n\nBackend: Claude Code CLI (headless), judge {JUDGE} "
    f"effort={EFFORT}, batches of {BATCH}.\n\n{summary}\n\n" + "\n".join(lines) + "\n", encoding="utf-8")
sys.exit(0 if passed == len(results) else 1)
