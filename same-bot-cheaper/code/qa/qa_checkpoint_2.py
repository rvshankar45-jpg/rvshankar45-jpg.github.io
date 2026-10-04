"""QA gate 2 - pipeline dry run. Run after eval.dry_run:
    .\\.venv\\Scripts\\python.exe -m qa.qa_checkpoint_2
Reads results/dryrun/calls.csv, re-derives everything it can from the stored raw API
usage records (results/cache/calls/*.json), and prints PASS/FAIL per check.
"""
import hashlib
import json
import sys
from datetime import date, datetime

import numpy as np
import pandas as pd
import yaml

from src import claude_cli
from src.common import ROOT, config, path
from src.llm import LLM

CFG = config()
STRONG, CHEAP, JUDGE = CFG["models"]["strong"], CFG["models"]["cheap"], CFG["models"]["judge"]
DRY = ROOT / CFG["paths"]["results"] / "dryrun"
STORE = ROOT / CFG["paths"]["results"] / "cache" / "calls"
REPORTS = path("qa_reports")
CACHE = REPORTS / "cache"
CACHE.mkdir(parents=True, exist_ok=True)

results, lines = [], []
qa_spend = {"calls": 0, "tokens_in": 0, "tokens_out": 0}


def check(name, ok, reason):
    results.append((name, ok, reason))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {reason}", flush=True)
    lines.append(f"- **{'PASS' if ok else 'FAIL'}** {name}: {reason}")


def note(msg):
    print("      " + msg)
    lines.append("    - " + msg)


df = pd.read_csv(DRY / "calls.csv", keep_default_na=False, na_values=[""])
meta = json.loads((DRY / "meta.json").read_text())
df["seq"] = range(len(df))
ans = df[df.call_type == "answer"].copy()
called = df[df.cache_hit != True].copy()  # rows backed by a real model call  # noqa: E712
v1 = ans[ans.variant == "v1_naive"].set_index("query_id")

# ---------------------------------------------------------------- 1. required fields
req = ["variant", "query_id", "model", "input_tokens", "output_tokens", "cache_read_tokens", "cache_write_tokens",
       "cost_usd", "latency_ms", "routed_by", "cache_hit"]
nulls = {c: int(df[c].isna().sum()) for c in req if df[c].isna().any()}
laya_rows = df[df.routed_by == "laya"]
laya_nulls = int(laya_rows[["laya_score", "laya_ms"]].isna().any(axis=1).sum())
empty_ans = df[(df.answer.isna() | (df.answer.astype(str).str.strip() == "")) & (df.capped != True)]  # noqa: E712
check("every call logged all required fields", not nulls and laya_nulls == 0 and empty_ans.empty,
      f"{len(df)} rows ({len(ans)} answers, {int((df.call_type == 'summary').sum())} summaries, "
      f"{int((df.cache_hit == True).sum())} response-cache hits); nulls={nulls}; laya rows missing score/latency={laya_nulls}; "  # noqa: E712
      f"empty uncapped answers={len(empty_ans)}")

# ---------------------------------------------------------------- 2. token counts are real
mism, rows_checked = [], 0
for r in called.itertuples():
    rec = json.loads((STORE / f"{r.request_key}.json").read_text(encoding="utf-8"))
    u = rec["raw_usage"]
    raw_total = u["input_tokens"] + (u.get("cache_creation_input_tokens") or 0) + (u.get("cache_read_input_tokens") or 0)
    logged_payload = r.input_tokens + r.cache_read_tokens + r.cache_write_tokens
    out_ok = (u["output_tokens"] == r.raw_output_tokens and
              (r.output_tokens == r.raw_output_tokens if not r.cap_emulated else r.output_tokens == r.max_tokens < r.raw_output_tokens))
    if raw_total - rec["overhead"] != logged_payload or not out_ok:
        mism.append(r.Index)
    rows_checked += 1
check("token counts come from the API usage block", not mism,
      f"all {rows_checked} called rows: logged input+cache = raw usage total - calibrated overhead; output = raw output "
      f"(or = max_tokens where the API cap was emulated: {int(called.cap_emulated.sum())} rows); mismatches={mism}")
for r in called.sample(3, random_state=7).itertuples():
    rec = json.loads((STORE / f"{r.request_key}.json").read_text(encoding="utf-8"))
    u = rec["raw_usage"]
    note(f"spot check {r.variant}/{r.query_id} ({r.model}): raw usage input={u['input_tokens']} "
         f"cache_write={u.get('cache_creation_input_tokens')} cache_read={u.get('cache_read_input_tokens')} "
         f"output={u['output_tokens']} | overhead {rec['overhead']} -> logged payload "
         f"{r.input_tokens + r.cache_read_tokens + r.cache_write_tokens} (in {r.input_tokens} / cr {r.cache_read_tokens} / cw {r.cache_write_tokens}), out {r.output_tokens}")

# harness overhead must not depend on the output cap env var (answers run with a cap, calibration without)
a = claude_cli.call(STRONG, ".", ".")
b = claude_cli.call(STRONG, ".", ".", max_output_tokens=CFG["generation"]["max_tokens_capped"])
qa_spend["calls"] += 2
check("harness overhead is independent of the output cap setting", a["total_input_tokens"] == b["total_input_tokens"],
      f"total input without cap={a['total_input_tokens']}, with cap={b['total_input_tokens']}; "
      f"run start overhead={meta['overhead']} (re-verified unchanged at run end by the dry run)")

# ---------------------------------------------------------------- 3. cost math
raw_cfg = yaml.safe_load((ROOT / "config.yaml").read_text(encoding="utf-8"))["pricing"]
recomp = [(r.input_tokens * raw_cfg[r.model]["input"] + r.output_tokens * raw_cfg[r.model]["output"]
           + r.cache_read_tokens * raw_cfg[r.model]["cache_read"] + r.cache_write_tokens * raw_cfg[r.model]["cache_write"]) / 1e6
          for r in df.itertuples()]
diff = np.abs(np.array(recomp) - df.cost_usd.to_numpy())
check("cost math: independent recompute matches every row", diff.max() <= 0.0001,
      f"{len(df)} rows, max |diff| = ${diff.max():.2e} (limit $0.0001)")

# ---------------------------------------------------------------- 4. pricing current
snap = yaml.safe_load((ROOT / "qa" / "pricing_snapshot.yaml").read_text(encoding="utf-8"))
diffs = {m: {k: (raw_cfg[m][k], v) for k, v in p.items() if raw_cfg[m][k] != v} for m, p in snap["prices_usd_per_mtok"].items()}
diffs = {m: d for m, d in diffs.items() if d}
age = (date.today() - date.fromisoformat(snap["checked_on"])).days
check("pricing in config matches the provider's pricing page", not diffs and age <= 7,
      f"config == snapshot of {snap['source']} checked {snap['checked_on']} ({age} days ago) by {snap['checked_by']}; diffs={diffs}")

# ---------------------------------------------------------------- 5. full KB vs retrieved chunks
llm = LLM()
kb_static_tokens = None
v1_calls = ans[ans.variant == "v1_naive"]
v1_ok = (v1_calls.chunk_ids == '["full_kb"]').all()
ret = ans[ans.variant.isin(["only_retrieve", "v2_full"]) & (ans.cache_hit != True)]  # noqa: E712
ret_ids = ret.chunk_ids.map(json.loads)
ret_ok = ret_ids.map(lambda ids: len(ids) == CFG["retrieval"]["top_k"] and all(i.startswith("s") for i in ids)).all()
smaller = []
for r in ans[ans.variant == "only_retrieve"].itertuples():
    smaller.append(r.payload_input_tokens < v1.loc[r.query_id, "payload_input_tokens"])
check("v1 sends the full KB every call; v2 sends only retrieved chunks", v1_ok and ret_ok and all(smaller),
      f"v1: {len(v1_calls)}/{len(v1_calls)} calls chunk_ids=full_kb, payload min {int(v1_calls.payload_input_tokens.min())} tokens; "
      f"retrieve: {len(ret)} calls with {CFG['retrieval']['top_k']} section ids each "
      f"(e.g. {ret.iloc[0].query_id}: {ret.iloc[0].chunk_ids}); retrieve-alone payload < v1 on {sum(smaller)}/{len(smaller)} queries")

# ---------------------------------------------------------------- 6. Laya actually ran
L = df[df.routed_by == "laya"]
t = CFG["router"]["threshold"]
rule_bad = L[(L.laya_score >= t) != (L.model == STRONG)]
check("Laya ran: varied scores in [0,1], latency logged, routing follows the threshold",
      L.laya_score.nunique() > 1 and L.laya_score.between(0, 1).all() and L.laya_ms.notna().all() and rule_bad.empty,
      f"{len(L)} routed rows, {L.laya_score.nunique()} distinct scores, range {L.laya_score.min():.3f}-{L.laya_score.max():.3f}, "
      f"std {L.laya_score.std():.3f}; laya latency median {L.laya_ms.median():.0f} ms on {meta['laya_device']}; "
      f"threshold {t}: {int((L.model == STRONG).sum())} strong / {int((L.model == CHEAP).sum())} cheap; rule violations={len(rule_bad)}")

# ---------------------------------------------------------------- 7. prompt caching
pc = df[(df.prompt_cache == True) & (df.cache_hit != True)].sort_values("seq")  # noqa: E712
bad, eligible_groups, ineligible = [], 0, []
for (var, model, sh), g in pc.groupby(["variant", "model", "static_hash"], sort=False):
    n_static = int(g.static_prefix_tokens.iloc[0])
    if n_static >= CFG["cache"]["min_tokens"][model]:
        eligible_groups += 1
        if not (g.cache_write_tokens.iloc[0] > 0 and (g.cache_read_tokens.iloc[1:] > 0).all()):
            bad.append((var, model))
    else:
        ineligible.append(f"{var}/{model}: static prefix {n_static} < min {CFG['cache']['min_tokens'][model]}")
        if (g.cache_read_tokens > 0).any() or (g.cache_write_tokens > 0).any():
            bad.append((var, model, "cached below minimum"))
check("prompt caching: 2nd+ calls read the cached prefix wherever the prefix is cacheable", not bad and eligible_groups > 0,
      f"{eligible_groups} cacheable groups behave (first call writes, later calls read); violations={bad}")
for s in ineligible:
    note(f"not cacheable by API rules: {s}")
v2s = df[(df.variant == "v2_full") & (df.model == STRONG) & (df.cache_hit != True)]  # noqa: E712
note(f"brief's literal check - v2_full Sonnet calls with cache_read > 0: {int((v2s.cache_read_tokens > 0).sum())}/{len(v2s)}")
v1r = [json.loads((STORE / f"{k}.json").read_text())["raw_usage"].get("cache_read_input_tokens") or 0
       for k in v1_calls.sort_values("seq").request_key]
note(f"observed server-side evidence: Claude Code's own cache read {sum(x > 0 for x in v1r[1:])}/{len(v1r) - 1} of v1's 2nd+ calls "
     f"-> the static persona+KB prefix is byte-stable across calls")

# ---------------------------------------------------------------- 8. output cap
capped_cfg = df[df.max_tokens == CFG["generation"]["max_tokens_capped"]]
over = capped_cfg[capped_cfg.output_tokens > CFG["generation"]["max_tokens_capped"]]
check("output cap: no capped-variant answer exceeds max_tokens", over.empty and len(capped_cfg) > 0,
      f"{len(capped_cfg)} capped calls, max output {int(capped_cfg.output_tokens.max())} / {CFG['generation']['max_tokens_capped']}; "
      f"hit the cap: {int(capped_cfg.capped.sum())}; uncapped calls hitting the {CFG['generation']['max_tokens_uncapped']} ceiling: "
      f"{int(df[df.max_tokens == CFG['generation']['max_tokens_uncapped']].capped.sum())}")

# ---------------------------------------------------------------- 9. answer sanity (judge)
qtext = pd.read_csv(path("queries")).set_index("id")["query"].to_dict()
conv = next(c for c in json.loads(path("conversations").read_text(encoding="utf-8")) if c["id"] == meta["conversation"])
for k, tt in enumerate(conv["turns"], 1):
    prior = " / ".join(x["user"] for x in conv["turns"][:k - 1])
    qtext[f"{conv['id']}.t{k}"] = (f"(earlier customer messages: {prior}) " if prior else "") + tt["user"]
qtext.update(dict(meta["repeats"]))
errtext = ans[ans.answer.astype(str).str.contains(r"API Error|Traceback|exceeded the .* output token", regex=True)]
uniq = ans.drop_duplicates("answer")[["query_id", "answer"]]
S_SCHEMA = {"type": "object", "additionalProperties": False, "required": ["items"], "properties": {"items": {
    "type": "array", "items": {"type": "object", "additionalProperties": False, "required": ["id", "addresses", "reason"],
                               "properties": {"id": {"type": "string"}, "addresses": {"type": "boolean"},
                                              "reason": {"type": "string"}}}}}}
items = [(f"a{i}", qtext[r.query_id], r.answer) for i, r in enumerate(uniq.itertuples())]
verdict = {}
for s in range(0, len(items), 25):
    chunk = items[s:s + 25]
    prompt = ("For each item, decide whether the support answer ADDRESSES the customer's message: it responds to what was "
              "asked (every part), is not empty, not an error message and not off-topic. Do not judge policy accuracy here. "
              "Return one entry per id.\n\n" + "\n\n".join(
                  f"<item id=\"{i}\">\n<customer>{q}</customer>\n<answer>{a}</answer>\n</item>" for i, q, a in chunk))
    key = hashlib.sha256(json.dumps([JUDGE, prompt]).encode()).hexdigest()[:24]
    f = CACHE / f"sanity_{key}.json"
    if f.exists():
        out = json.loads(f.read_text())
    else:
        r = claude_cli.call(JUDGE, "You audit support answers.", prompt, schema=S_SCHEMA,
                            effort=CFG["models"]["judge_effort"], thinking=True)
        qa_spend["calls"] += 1
        qa_spend["tokens_in"] += r["total_input_tokens"]
        qa_spend["tokens_out"] += r["output_tokens"]
        out = r["structured"]
        f.write_text(json.dumps(out, indent=1))
    verdict.update({v["id"]: v for v in out["items"]})
fails = [(i, q, verdict.get(i, {}).get("reason", "missing")) for i, q, _ in items if not verdict.get(i, {}).get("addresses")]
check("answer sanity: non-empty, no error text, addresses the query (judge)", not fails and errtext.empty,
      f"{len(items)} distinct answers judged, {len(items) - len(fails)} address the query; error-text answers={len(errtext)}")
for i, q, why in fails:
    note(f"{i}: {q[:70]} -> {why}")

# ---------------------------------------------------------------- 10. toggle isolation
iso_bad = []


def same(a_, b_, cols):
    return [c for c in cols if a_[c] != b_[c]]


expect = {  # flag: (columns that MUST match v1, columns that MUST differ)
    "route": (["system_hash", "user_hash", "max_tokens", "chunk_ids"], ["routed_by"]),
    "retrieve": (["user_hash", "model", "max_tokens"], ["system_hash", "chunk_ids"]),
    "tight_prompt": (["user_hash", "model", "max_tokens", "chunk_ids"], ["static_hash"]),
    "output_cap": (["user_hash", "model", "chunk_ids"], ["max_tokens", "static_hash"]),
    "prompt_cache": (["request_key", "model", "max_tokens"], ["prompt_cache"]),
}
summ = []
for flag, (must_same, must_diff) in expect.items():
    rows = ans[ans.variant == f"only_{flag}"]
    for r in rows.itertuples():
        base = v1.loc[r.query_id]
        rr = r._asdict()
        s_bad = same(rr, base, must_same)
        d_bad = [c for c in must_diff if rr[c] == base[c]]
        if s_bad or d_bad:
            iso_bad.append((flag, r.query_id, "changed:" + ",".join(s_bad), "unchanged:" + ",".join(d_bad)))
    summ.append(f"{flag}: {len(rows)} rows")
# trim_history: turns within the window are byte-identical to v1; later turns differ only in the user message
tr = ans[ans.variant == "only_trim_history"].set_index("query_id")
keep = CFG["history"]["keep_last_turns"]
for qid, r in tr.iterrows():
    k = int(qid.split(".t")[1])
    base = v1.loc[qid]
    if k <= keep + 1 and r.request_key != base.request_key:
        iso_bad.append(("trim_history", qid, "early turn changed"))
    if k > keep + 1 and (r.user_hash == base.user_hash or r.system_hash != base.system_hash or r.history_mode != "trimmed"):
        iso_bad.append(("trim_history", qid, "late turn not trimmed only"))
n_sum = int(((df.variant == "only_trim_history") & (df.call_type == "summary")).sum())
summ.append(f"trim_history: {len(tr)} turns, {n_sum} summary calls")
rc = ans[ans.variant == "only_response_cache"].set_index("query_id")
if rc.loc["q001", "request_key"] != v1.loc["q001", "request_key"] or not rc.loc[[x for x, _ in meta["repeats"]], "cache_hit"].all():
    iso_bad.append(("response_cache", "q001/dups", "miss not identical to v1 or repeats not served from cache"))
summ.append(f"response_cache: hits {rc.cache_kind.replace('', np.nan).dropna().to_dict()}")
check("each flag switched on alone changes what it should and nothing else", not iso_bad,
      "; ".join(summ) + (f"; violations={iso_bad}" if iso_bad else ""))

# ---------------------------------------------------------------- 11. prompt sizes
from src import prompts  # noqa: E402

persona = llm.static_tokens(STRONG, prompts.LONG_PERSONA)
tight = llm.static_tokens(STRONG, prompts.TIGHT_PROMPT)
check("system prompt sizes match the spec (~600 naive, ~150 tight)", 500 <= persona <= 700 and 100 <= tight <= 200,
      f"persona {persona} tokens, tight {tight} tokens on {STRONG}")

# ---------------------------------------------------------------- 12. spend + projection
new = called[called.reused == False]  # noqa: E712
consumed_in = int(new.raw_total_input_tokens.sum())
consumed_out = int(new.output_tokens.sum())
product_cost = new.cost_usd.sum()


def per_query_cost(var):
    x = ans[(ans.variant == var) & (~ans.query_id.str.startswith("dup"))]
    s = df[(df.variant == var) & (df.call_type == "summary")]
    singles = x[~x.query_id.str.contains(r"\.t")]
    turns = x[x.query_id.str.contains(r"\.t")]
    return singles.cost_usd.mean(), (turns.cost_usd.sum() + s.cost_usd.sum()) / max(len(turns), 1)


n_single, n_turns = 100, sum(len(c["turns"]) for c in json.loads(path("conversations").read_text(encoding="utf-8")))
v1s, v1t = per_query_cost("v1_naive")
v2s_, v2t = per_query_cost("v2_full")
share_strong = (L[L.variant == "v2_full"].model == STRONG).mean()
proj = {
    "v1_naive (product cost of one full pass)": v1s * n_single + v1t * n_turns,
    "v2_full (product cost of one full pass)": v2s_ * n_single + v2t * n_turns,
}
# Subscription consumption for the full Phase 5 + 5b plan, in tokens (includes harness overhead):
tok_per_call = {"full_kb": called[called.chunk_ids == '["full_kb"]'].raw_total_input_tokens.mean(),  # all called rows,
                "retrieved": called[called.chunk_ids.str.startswith('["s')].raw_total_input_tokens.mean(),  # reused or not
                "out": called[called.call_type == "answer"].raw_output_tokens.mean()}
planned = {  # new (non-reused) answer calls in the full run, per the reuse plan
    "full_kb": n_single + n_turns                    # v1
    + (n_single + n_turns) * (1 - share_strong),     # +route: cheap-routed only (strong reuses v1)
    "retrieved": (n_single + n_turns) * 3            # +retrieve, +tight_cache, v2_full
    + n_single * share_strong + n_single * (1 - share_strong) + 30  # 5b both models on the fixed config (part reused) + trim turns
    + 20,                                            # variance re-runs
}
calls_total = sum(planned.values()) + 100 + 28 + 10   # + llm_router + judge batches + calibration/QA
tok_in = planned["full_kb"] * tok_per_call["full_kb"] + planned["retrieved"] * tok_per_call["retrieved"] + 100 * 900 + 28 * 15000
tok_out = sum(planned.values()) * tok_per_call["out"] + 100 * 20 + 28 * 3000
check("spend reported and full-run projection computed", True,
      f"dry run: {len(new)} new model calls, {consumed_in:,} input / {consumed_out:,} output tokens consumed "
      f"(incl. harness overhead), product cost at API prices ${product_cost:.3f}; QA gate calls {qa_spend['calls']}")
for k, v in proj.items():
    note(f"projected {k}: ${v:.2f}")
note(f"projected full eval (Phases 5+5b): ~{calls_total:.0f} new calls, ~{tok_in/1e6:.1f}M input + ~{tok_out/1e6:.2f}M output tokens "
     f"of subscription usage; share routed strong by Laya in the dry run = {share_strong:.0%}")

# ---------------------------------------------------------------- summary
passed = sum(ok for _, ok, _ in results)
summary = f"{passed}/{len(results)} checks passed."
print("\n" + summary)
(REPORTS / "qa_checkpoint_2.md").write_text(
    f"# QA gate 2 (pipeline dry run) - {datetime.now():%Y-%m-%d %H:%M}\n\n{summary}\n\n" + "\n".join(lines) + "\n",
    encoding="utf-8")
sys.exit(0 if passed == len(results) else 1)
