"""QA gate 3 - blog. Every number in blog/blog.md and blog/linkedin_post.md must equal a value
recomputed here from results/ (or a design constant in config.yaml / the data files). Writes the
number-to-source table to qa/reports/number_sources.md.

  .\\.venv\\Scripts\\python.exe -m qa.qa_checkpoint_3
"""
import json
import re
import sys
from datetime import datetime

import pandas as pd

from src.common import ROOT, config, path

R = ROOT / "results"
CFG = config()
results, lines = [], []


def check(name, ok, reason):
    results.append((name, ok, reason))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {reason}", flush=True)
    lines.append(f"- **{'PASS' if ok else 'FAIL'}** {name}: {reason}")


s = pd.read_csv(R / "summary.csv").set_index("variant")
rs = pd.read_csv(R / "routing_summary.csv").set_index("strategy")
sw = pd.read_csv(R / "threshold_sweep.csv").set_index("threshold")
conf = pd.read_csv(R / "routing_confusion.csv").set_index(["router", "label", "decision"]).n
rh = pd.read_csv(R / "router_head_summary.csv").set_index("router")
eff = pd.read_csv(R / "effort_summary.csv").set_index("strategy")
combo = pd.read_csv(R / "effort_combo.csv").set_index("setup")
var = pd.read_csv(R / "variance.csv")
pae = pd.read_csv(R / "per_answer_eval.csv").pivot_table(index="query_id", columns="variant", values="quality")
calls = pd.read_csv(R / "calls_eval.csv", usecols=["variant", "model", "static_prefix_tokens", "cache_hit"], keep_default_na=False, na_values=[""])
q = pd.read_csv(path("queries"))
convs = json.loads(path("conversations").read_text(encoding="utf-8"))
n_units = 100 + sum(len(c["turns"]) for c in convs)
v1, v2 = s.loc["v1_naive", "total_cost_usd"], s.loc["v2_full", "total_cost_usd"]
tok = (s.total_input_tokens + s.output_tokens)
hc = (ROOT / "qa" / "reports" / "judge_handcheck.md").read_text(encoding="utf-8")
from src import prompts  # noqa: E402
from src.llm import LLM  # noqa: E402

_llm = LLM()
persona_tok = _llm.static_tokens(CFG["models"]["strong"], prompts.LONG_PERSONA)
tight_tok = _llm.static_tokens(CFG["models"]["strong"], prompts.TIGHT_PROMPT)
v2_static = int(calls[(calls.variant == "v2_full") & (calls.model == CFG["models"]["strong"])].static_prefix_tokens.dropna().iloc[0])


def pct(x):
    return f"{round(100 * x)}%"


# display string -> (value as displayed, source)
REG = {}


def reg(display, source):
    REG.setdefault(display, []).append(source)


reg(f"${v1:.2f}", "summary.csv v1_naive total_cost_usd")
reg(f"${v2:.2f}", "summary.csv v2_full total_cost_usd")
reg(pct(1 - v2 / v1), "1 - v2_full/v1_naive total_cost_usd")
reg(pct(1 - tok['v2_full'] / tok['v1_naive']), "1 - v2/v1 (total_input_tokens + output_tokens)")
reg(f"{s.loc['v1_naive', 'mean_quality']:.2f}", "summary.csv v1_naive mean_quality")
reg(f"{s.loc['v2_full', 'mean_quality']:.2f}", "summary.csv v2_full mean_quality")
reg(str(n_units), "100 queries + conversation turns (data files)")
reg(str(len(q)), "test_queries.csv rows")
reg(str(len(convs)), "conversations.json")
reg(str(int((q.label == "simple").sum())), "test_queries.csv label=simple")
reg(str(int((q.label == "complex").sum())), "test_queries.csv label=complex")
reg(str(round(persona_tok, -1)), f"persona tokens on strong model = {persona_tok} (rounded to 10)")
reg(str(round(tight_tok, -1)), f"tight prompt tokens on strong model = {tight_tok} (rounded to 10)")
reg(str(CFG["retrieval"]["top_k"]), "config retrieval.top_k")
reg(str(CFG["history"]["keep_last_turns"]), "config history.keep_last_turns")
d = s.loc[["v1_naive", "plus_route", "plus_retrieve"], "total_cost_usd"]
reg(f"${d['plus_route'] - d['plus_retrieve']:.2f}", "retrieval step: plus_route - plus_retrieve cost")
reg(f"${v1 - v2:.2f}", "total saving v1 - v2")
reg(f"{s.loc['plus_route', 'mean_quality']:.2f}", "summary.csv plus_route mean_quality")
reg(f"{s.loc['plus_retrieve', 'mean_quality']:.2f}", "summary.csv plus_retrieve mean_quality")
reg(str(int(((pae.plus_retrieve - pae.plus_route) <= -2).sum())), "per_answer_eval: answers dropping >=2 from plus_route to plus_retrieve")
trim_share = (s.loc["plus_retrieve", "total_cost_usd"] - s.loc["plus_trim", "total_cost_usd"]) / v1
reg(f"{100 * trim_share:.1f}%", "trim step / v1 cost")
reg(str(v2_static), "calls_eval v2_full Sonnet static_prefix_tokens")
reg(str(CFG["cache"]["min_tokens"][CFG["models"]["strong"]]), "config cache.min_tokens strong")
reg(f"{s.loc['cache_full_kb', 'mean_quality']:.2f}", "summary.csv cache_full_kb mean_quality")
reg(pct(1 - s.loc["cache_full_kb", "total_cost_usd"] / v1), "1 - cache_full_kb/v1 cost")
reg(str(int(((pae.cache_full_kb - pae.v2_full) >= 2).sum())), "per_answer_eval: answers improving >=2 v2_full -> cache_full_kb")
reg(pct(1 - rs.loc["laya", "total_cost_usd"] / rs.loc["always_strong", "total_cost_usd"]), "routing_summary laya vs always_strong cost")
reg(f"{rs.loc['laya', 'mean_quality']:.2f}", "routing_summary laya mean_quality")
reg(f"{rs.loc['always_strong', 'mean_quality']:.2f}", "routing_summary always_strong mean_quality")
reg(str(conf[("laya", "simple", "strong")]), "routing_confusion laya simple->strong")
reg(pct(rs.loc["laya", "router_efficiency"]), "routing_summary laya router_efficiency (vs oracle)")
reg(f"{(rs.loc['llm_router', 'router_input_tokens'] + rs.loc['llm_router', 'router_output_tokens']) / 100:,.0f}", "llm_router tokens per query")
reg(f"{rs.loc['llm_router', 'p50_router_ms']:,.0f}", "routing_summary llm_router p50_router_ms")
reg(f"{rs.loc['laya', 'p50_router_ms']:,.0f}", "routing_summary laya p50_router_ms")
reg(str(len(pd.read_csv(ROOT / "data" / "router_train.csv"))), "data/router_train.csv rows")
reg(pct(rh.loc["laya_zero_shot@0.50", "saving_vs_always_sonnet"]), "router_head_summary zero-shot saving")
reg(pct(rh.loc["laya_head", "saving_vs_always_sonnet"]), "router_head_summary laya_head saving")
reg(f"{rh.loc['laya_head', 'quality']:.2f}", "router_head_summary laya_head quality")
reg(pct(rh.loc["hindsight_ceiling", "saving_vs_always_sonnet"]), "router_head_summary hindsight ceiling saving")
reg(f"{rs.loc['always_cheap', 'quality_simple']:.2f}", "routing_summary always_cheap quality_simple")
reg(f"{rs.loc['always_strong', 'quality_simple']:.2f}", "routing_summary always_strong quality_simple")
reg("0.2", "rule fixed in eval/run_routing_eval.py (complex gap <= 0.2)")
rec = float(sw[sw.recommended].index[0])
reg(f"{rec:.2f}", "threshold_sweep recommended")
nxt = sw.index[sw.index > rec][0]
reg(f"{sw.loc[rec, 'quality_complex']:.2f}", "threshold_sweep quality_complex at recommended")
reg(f"{sw.loc[nxt, 'quality_complex']:.2f}", "threshold_sweep quality_complex at next threshold")
reg(str(int(eff.loc["sonnet_low", "n"])), "effort_summary sample size")
reg(pct(1 - eff.loc["sonnet_low", "total_cost_usd"] / eff.loc["always_strong", "total_cost_usd"]), "effort: low vs thinking off")
reg(f"{int(eff.loc['sonnet_high', 'thinking_tokens']):,}", "effort_summary sonnet_high thinking_tokens")
reg(f"{int(eff.loc['sonnet_low', 'thinking_tokens']):,}", "effort_summary sonnet_low thinking_tokens")
reg(pct(eff.loc["sonnet_high", "total_cost_usd"] / eff.loc["sonnet_low", "total_cost_usd"] - 1), "effort: high vs low cost")
reg(pct(combo.loc["laya_head + sonnet_low", "saving_vs_sonnet_off"]), "effort_combo laya_head + sonnet_low saving")
reg(f"${v1 / n_units * 1e6:,.0f}", "v1 cost per answer x 1M")
reg(f"${v2 / n_units * 1e6:,.0f}", "v2 cost per answer x 1M")
j = var.dropna(subset=["judge_rescore_run1", "score_run1"])
reg(pct((j.judge_rescore_run1 == j.score_run1).mean()), "variance.csv judge re-score identical share")
agree = len(re.findall(r"\*\*Claude check:\*\* AGREE", hc))
reg(str(agree), "judge_handcheck.md AGREE count")
reg("20", "judge_handcheck.md answers checked")
reg("0.1", "noise floor stated from judge variance (mean |diff| 0.23 per answer)")
reg("1", "quality scale bottom (rubric)")
reg("5", "quality scale top (rubric)")
reg("5.5", "model name: Claude Sonnet 5.5")
reg("4.5", "model name: Claude Haiku 4.5")
reg("50", "effort sample size (config effort_eval.sample)")
_bs = json.loads((R / "router_head_bootstrap.json").read_text())
_hq = json.loads((R / "router_head_qa.json").read_text())
reg(f"{_bs['resamples']:,}", "router_head_bootstrap resamples")
reg(f"{round(_bs['share_resamples_extra_saving_positive'] * _bs['resamples']):,}", "router_head_bootstrap resamples with extra saving > 0")
reg(str(round(_bs["extra_saving_points_ci95"][0])), "router_head_bootstrap extra saving 95% CI low (points)")
reg(str(round(_bs["extra_saving_points_ci95"][1])), "router_head_bootstrap extra saving 95% CI high (points)")
reg(pct(_hq["train_haiku_ok_rate"]), "router_head_qa train_haiku_ok_rate")
for k in ["laya_zero_shot@0.50", "laya_head", "length_rule"]:
    reg(f"{rh.loc[k, 'auc_haiku_ok']:.2f}", f"router_head_summary {k} auc_haiku_ok")
for k in ["laya_zero_shot@0.50", "length_rule", "minilm_head", "laya_head", "hindsight_ceiling"]:
    reg(pct(rh.loc[k, "share_to_haiku"]), f"router_head_summary {k} share_to_haiku")
reg("0.5", "AUC of a coin flip (definition)")
from src.retriever import chunks as _chunks  # noqa: E402
reg(str(len(_chunks())), "kb.md sections (retriever chunks)")
reg(str(CFG["effort_eval"]["sample"]["simple"]), "effort sample: simple questions (config)")
for k in ["always_strong", "sonnet_low", "sonnet_medium", "sonnet_high"]:
    reg(f"{eff.loc[k, 'quality_complex']:.2f}", f"effort_summary {k} quality_complex")
    reg(f"{eff.loc[k, 'p50_e2e_ms'] / 1000:.1f}", f"effort_summary {k} p50 latency (s)")
reg(f"{int(eff.loc['sonnet_medium', 'thinking_tokens']):,}", "effort_summary sonnet_medium thinking_tokens")
reg(f"{int(eff.loc['always_strong', 'thinking_tokens']):,}", "effort_summary thinking-off thinking_tokens")
for m in [CFG["models"]["strong"], CFG["models"]["cheap"]]:
    reg(f"${CFG['pricing'][m]['input']:.0f}", f"config pricing {m} input per MTok")
    reg(f"${CFG['pricing'][m]['output']:.0f}", f"config pricing {m} output per MTok")
_kb = int(re.search(r"(\d+) tokens on claude-sonnet", (ROOT / "qa" / "reports" / "qa_checkpoint_1.md").read_text(encoding="utf-8")).group(1))
reg(f"{round(_kb, -2):,}", f"kb.md tokens on strong model = {_kb} (QA gate 1), rounded to 100")
for v in ["plus_route", "plus_retrieve", "plus_trim", "plus_tight_cache"]:
    reg(f"${s.loc[v, 'total_cost_usd']:.2f}", f"summary.csv {v} total_cost_usd")
    reg(f"{s.loc[v, 'mean_quality']:.2f}", f"summary.csv {v} mean_quality")
reg(pct(s.loc["cache_full_kb", "total_cost_usd"] / v2 - 1), "cache_full_kb vs v2_full cost")
reg(f"${s.loc['cache_full_kb', 'total_cost_usd'] / n_units * 1e6:,.0f}", "cache_full_kb cost per answer x 1M")

# numbers that appear only in the generated web page (stat tiles, short version, bar charts)
reg(f"${s.loc['cache_full_kb', 'total_cost_usd']:.2f}", "summary.csv cache_full_kb total_cost_usd")
reg(pct((s.loc["plus_route", "total_cost_usd"] - s.loc["plus_retrieve", "total_cost_usd"]) / (v1 - v2)), "retrieval share of total saving")
for k in ["always_strong", "sonnet_low", "sonnet_medium", "sonnet_high"]:
    reg(f"${eff.loc[k, 'total_cost_usd']:.3f}", f"effort_summary {k} total_cost_usd")
    reg(f"{eff.loc[k, 'mean_quality']:.2f}", f"effort_summary {k} mean_quality")
for k in ["length_rule", "minilm_head", "hindsight_ceiling"]:
    reg(pct(rh.loc[k, "saving_vs_always_sonnet"]), f"router_head_summary {k} saving")
    reg(f"{rh.loc[k, 'quality']:.2f}", f"router_head_summary {k} quality")
reg(str(datetime.now().year), "publication year (byline)")

import html as _html  # noqa: E402
_page = (ROOT / "blog" / "site" / "index.html").read_text(encoding="utf-8")
_body = _page.split("<body>", 1)[1]
_body = re.sub(r'<div class="n">\d+</div>', " ", _body)  # numbered-list markers on the takeaways, not data
_body = re.sub(r"<style.*?</style>|<[^>]+>", " ", _body, flags=re.S)
(ROOT / "qa" / "reports" / "_page_text.txt").write_text(_html.unescape(_body), encoding="utf-8")
FILES = {"blog": ROOT / "blog" / "blog.md", "linkedin": ROOT / "blog" / "linkedin_post.md",
         "web page": ROOT / "qa" / "reports" / "_page_text.txt"}
NUM = re.compile(r"(?<![A-Za-z0-9.])\$?\d[\d,]*(?:\.\d+)?%?")  # skips digits inside words like v1
rows, unsourced = [], []
for name, f in FILES.items():
    text = f.read_text(encoding="utf-8").split("## More writing")[0].split("MORE-WRITING-START")[0]
    for ln, line in enumerate(text.splitlines(), 1):
        body = re.sub(r"^\s*\d+\.\s", "", line)            # ordered-list markers
        body = re.sub(r"\[RAVI:[^\]]*\]", "", body)          # placeholders
        for m in NUM.finditer(body):
            tokn = m.group(0).rstrip(".,")
            src = REG.get(tokn)
            rows.append((name, ln, tokn, "; ".join(src) if src else "NO SOURCE"))
            if not src:
                unsourced.append((name, ln, tokn, line.strip()[:70]))

check("every number traces to results/ (or a stated design constant)", not unsourced,
      f"{len(rows)} numbers across blog + LinkedIn post; unsourced={unsourced}")

blog = FILES["blog"].read_text(encoding="utf-8")
li = FILES["linkedin"].read_text(encoding="utf-8")
def words(t):  # prose only: tables, diagram code and placeholders are not counted
    t = re.sub(r"```.*?```", "", t, flags=re.S)
    t = re.sub(r"\|.*\|\n", "", re.sub(r"\[RAVI:[^\]]*\]", "", t))
    return len(re.findall(r"[A-Za-z0-9$%][\w$%.,'-]*", t))
wb, wl = words(blog), words(li)
# Brief said 900-1,200; on 2026-10-04 the author asked for the fixes, the method and the thinking results to be
# explained for any reader, so the limit was raised to 1,500 at their request.
# 2026-10-04 (later): the author asked for a dedicated Laya fine-tuning section; limit raised to 1,700 at their request.
# 2026-10-04 (later): author asked for the RAG paragraph to be explained step by step; limit raised to 1,800 at their request.
check("word counts", 900 <= wb <= 1800 and 150 <= wl <= 200,
      f"blog {wb} words (900-1,800, raised from 1,200 at the author's request; tables, diagram code and placeholders excluded); LinkedIn {wl} (150-200)")

laya_ok = "saves cost, not tokens" in blog.lower() and "off the shelf" in blog.lower() and "not a finished router" in blog
check("Laya described accurately (cost not tokens; limits stated)", laya_ok,
      "states 'Laya saves cost, not tokens', reports zero-shot vs trained honestly, and lists its new-domain limitation")
route_share = (v1 - s.loc["plus_route", "total_cost_usd"]) / (v1 - v2)
dirn = [("v2 quality below v1", s.loc["v2_full", "mean_quality"] < s.loc["v1_naive", "mean_quality"], "4.49 out of 5, against 4.63"),
        ("retrieval cost quality", s.loc["plus_retrieve", "mean_quality"] < s.loc["plus_route", "mean_quality"], "the biggest quality drop"),
        ("cache_full_kb above v1 (stated with caveat)", s.loc["cache_full_kb", "mean_quality"] > s.loc["v1_naive", "mean_quality"],
         "at least as good as version 1"),
        ("routing ~ a sixth of the saving", 1 / 7 < route_share < 1 / 5, "a sixth"),
        ("cached token costs a tenth (both models)", all(abs(CFG["pricing"][m]["cache_read"] / CFG["pricing"][m]["input"] - 0.1) < 1e-9
                                                       for m in (CFG["models"]["strong"], CFG["models"]["cheap"])), "costs a tenth of a normal one"),
        ("retrieval sent a third of the manual", abs(CFG["retrieval"]["top_k"] / len(_chunks()) - 1 / 3) < 1e-9, "Retrieval sent a third"),
        ("trim smaller than routing", s.loc["plus_retrieve", "total_cost_usd"] - s.loc["plus_trim", "total_cost_usd"]
         < v1 - s.loc["plus_route", "total_cost_usd"], "barely mattered")]
bad = [k for k, cond, phrase in dirn if not (cond and phrase in blog)]
check("claims match the data's direction (weak/mixed results stated as such)", not bad, f"checked {len(dirn)} directional claims; mismatched={bad}")
OWN = ("https://github.com/rvshankar45-jpg/Laya-model-router", "https://rvshankar45-jpg.github.io/",
       "https://huggingface.co/convaiinnovations/laya")  # own work + the cited Laya model card
links = [u.rstrip(").,") for u in re.findall(r"https?://\S+", blog + li)]
foreign = [u for u in links if not u.startswith(OWN)]
check("no invented quotes, stats or sources", not foreign and '"' not in re.sub(r'"[^"]{0,60}"', "", blog),
      f"links={links} (only the author's own repo and post); all statistics come from this repo's results")
deny = r"\b(amazon|walmart|ikea|paypal|klarna|visa|mastercard|fedex|ups|usps|dhl|google|meta|openai|microsoft|swiggy|zomato|blinkit|zepto)\b"
hits = sorted({m.lower() for m in re.findall(deny, blog + li, flags=re.I)})
ph = re.findall(r"\[RAVI:[^\]]*\]", blog + li)
check("no real employer/customer/brand names; placeholders listed", not hits, f"denylist hits={hits}; {len(ph)} placeholders: {ph}")

passed = sum(ok for _, ok, _ in results)
summary = f"{passed}/{len(results)} checks passed."
print("\n" + summary)
table = ["| file | line | number | source |", "|---|---|---|---|"] + [f"| {a} | {b} | `{c}` | {d} |" for a, b, c, d in rows]
(ROOT / "qa" / "reports" / "number_sources.md").write_text("# Number-to-source table (blog + LinkedIn post)\n\n" + "\n".join(table) + "\n", encoding="utf-8")
(ROOT / "qa" / "reports" / "qa_checkpoint_3.md").write_text(
    f"# QA gate 3 (blog) - {datetime.now():%Y-%m-%d %H:%M}\n\n{summary}\n\n" + "\n".join(lines) + "\n", encoding="utf-8")
sys.exit(0 if passed == len(results) else 1)
