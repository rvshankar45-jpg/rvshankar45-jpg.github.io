"""Generates README.md. All result tables are read from results/*.csv so the README always
matches summary.csv (definition-of-done item).

  .\\.venv\\Scripts\\python.exe -m report.build_readme
"""
import pandas as pd

from blog.make_card import SLUG
from src.common import ROOT, config

R = ROOT / "results"


def table(df, cols, fmt):
    head = "| " + " | ".join(cols) + " |\n|" + "---|" * len(cols) + "\n"
    return head + "\n".join("| " + " | ".join(fmt[c](r) for c in cols) + " |" for _, r in df.iterrows())


def main():
    cfg = config()
    s = pd.read_csv(R / "summary.csv")
    rs = pd.read_csv(R / "routing_summary.csv")
    rh = pd.read_csv(R / "router_head_summary.csv")
    eff = pd.read_csv(R / "effort_summary.csv")
    v1 = s.set_index("variant").loc["v1_naive", "total_cost_usd"]
    t5 = table(s, ["variant", "flags", "total cost", "input tokens", "output tokens", "p50 / p95 latency", "quality", "% ≥ 4"], {
        "variant": lambda r: f"`{r.variant}`", "flags": lambda r: r["flags"].replace("+", ", "),
        "total cost": lambda r: f"${r.total_cost_usd:.3f} ({100 * (r.total_cost_usd / v1 - 1):+.0f}%)",
        "input tokens": lambda r: f"{r.total_input_tokens:,}", "output tokens": lambda r: f"{r.output_tokens:,}",
        "p50 / p95 latency": lambda r: f"{r.p50_latency_ms / 1000:.1f}s / {r.p95_latency_ms / 1000:.1f}s",
        "quality": lambda r: f"{r.mean_quality:.2f}", "% ≥ 4": lambda r: f"{100 * r.pct_quality_ge4:.0f}%"})
    t5b = table(rs, ["strategy", "total cost", "quality", "simple", "complex", "router efficiency"], {
        "strategy": lambda r: f"`{r.strategy}`", "total cost": lambda r: f"${r.total_cost_usd:.3f}",
        "quality": lambda r: f"{r.mean_quality:.2f}", "simple": lambda r: f"{r.quality_simple:.2f}",
        "complex": lambda r: f"{r.quality_complex:.2f}", "router efficiency": lambda r: f"{r.router_efficiency:.2f}"})
    th = table(rh, ["router", "saving vs always-Sonnet", "quality", "AUC (Haiku ok)"], {
        "router": lambda r: f"`{r.router}`", "saving vs always-Sonnet": lambda r: f"{100 * r.saving_vs_always_sonnet:.0f}%",
        "quality": lambda r: f"{r.quality:.2f}", "AUC (Haiku ok)": lambda r: "" if pd.isna(r.auc_haiku_ok) else f"{r.auc_haiku_ok:.2f}"})
    te = table(eff, ["strategy", "thinking", "cost (50 q)", "thinking tokens", "quality", "complex"], {
        "strategy": lambda r: f"`{r.strategy}`", "thinking": lambda r: r.thinking, "cost (50 q)": lambda r: f"${r.total_cost_usd:.3f}",
        "thinking tokens": lambda r: f"{int(r.thinking_tokens):,}", "quality": lambda r: f"{r.mean_quality:.2f}",
        "complex": lambda r: f"{r.quality_complex:.2f}"})
    charts = sorted(p.name for p in (ROOT / "report").glob("[0-9][0-9]_*.png"))

    md = f"""# Support Copilot Token Lab

The same AI support copilot built twice, naive (v1) and optimised (v2), to measure where LLM token spend goes and what each
optimisation buys. **v2 answers the same 140 questions {100 * (1 - s.set_index('variant').loc['v2_full', 'total_cost_usd'] / v1):.0f}% cheaper.**

Write-up: **https://rvshankar45-jpg.github.io/{SLUG}/** · all data is synthetic (a fictional plant shop, "Leafy").

## Architecture

```mermaid
flowchart LR
  Q[Customer message] --> C{{Answer cache}}
  C -- repeat --> A[Answer]
  C -- new --> L[Laya router<br/>local GPU]
  L -- "P(complex) < {cfg['router']['threshold']}" --> H[{cfg['models']['cheap']}]
  L -- "P(complex) >= {cfg['router']['threshold']}" --> S[{cfg['models']['strong']}]
  K[(kb.md)] -- "top {cfg['retrieval']['top_k']} sections (BM25 + MiniLM)" --> P[Tight prompt + last {cfg['history']['keep_last_turns']} turns + summary]
  P --> H & S
  H & S --> A
  A --> J[Judge: {cfg['models']['judge']}, 1-5]
```

Every optimisation is an independent flag in `config.yaml` (`route`, `retrieve`, `trim_history`, `prompt_cache`,
`tight_prompt`, `output_cap`, `response_cache`). With every flag off, the pipeline *is* v1.

## Results - waterfall (100 queries + 10 conversations = 140 answers)

{t5}

`cache_full_kb` is an extra variant (route + tight prompt + prompt cache, **full KB instead of retrieval**): it scored best.

## Results - routing head-to-head (100 queries; routing is the only variable)

{t5b}

Recommended Laya threshold by the pre-registered rule (cheapest cost with complex-query quality within 0.2 of always-strong):
see `results/threshold_sweep.csv`. Laya saves **cost, not tokens**: the same prompt goes to a cheaper model.

## Results - trained routing head (270 separate training questions, 100 held-out test queries)

{th}

## Results - thinking effort within Sonnet (50 stratified queries)

{te}

## Charts

{chr(10).join(f"![{c}](report/{c})" for c in charts)}

## Setup (Windows PowerShell)

```powershell
py -3.12 -m venv .venv
.\\.venv\\Scripts\\python.exe -m pip install -r requirements.txt
# optional GPU for Laya (RTX-class, CUDA 13 driver):
.\\.venv\\Scripts\\python.exe -m pip install torch==2.14.1 --index-url https://download.pytorch.org/whl/cu130
```

**Model access.** `config.yaml: backend` selects how models are called:

- `cli` (used for these results): Claude Code headless (`claude -p`) on a Claude subscription. Each run first measures the
  fixed hidden overhead Claude Code adds to every request (constant within a run, re-checked at the end) and subtracts it, so
  logged tokens are the API's own usage counts minus that overhead. Caching is priced by the documented API rules, and the
  output cap is applied exactly as the API would.
- `api`: the Anthropic API directly. Put `ANTHROPIC_API_KEY` in `.env` (git-ignored) and set `backend: api`.

## Run

```powershell
.\\.venv\\Scripts\\python.exe -m qa.qa_checkpoint_1      # data QA gate
.\\.venv\\Scripts\\python.exe -m eval.dry_run            # 10-query dry run, then: python -m qa.qa_checkpoint_2
.\\.venv\\Scripts\\python.exe -m eval.run_eval           # full eval: variants, routing, effort, judge -> results/*.csv
.\\.venv\\Scripts\\python.exe -m qa.qa_eval              # eval QA gate
.\\.venv\\Scripts\\python.exe -m eval.router_head_data   # training data for the routing head
.\\.venv\\Scripts\\python.exe -m eval.train_router_head  # train + test the head (local, no API calls)
.\\.venv\\Scripts\\python.exe -m report.make_charts      # charts -> report/*.png, then: python -m qa.qa_charts
.\\.venv\\Scripts\\python.exe -m blog.build_site         # article page -> blog/site/
```

Every model call is stored in `results/cache/` by request hash, so a re-run reproduces every CSV from a clean clone
without new model calls (only the overhead calibration runs).

## Limitations

- Synthetic data; one model wrote both the test and the router-training questions, which flatters the trained router.
- Quality is an LLM judge (re-scoring the same answers gives the identical score ~78% of the time); differences under ~0.1 in
  mean quality are noise. 20 answers were hand-checked (`qa/reports/judge_handcheck.md`).
- 100 queries is a small sample; the effort comparison uses 50.
- Measured through Claude Code's CLI with its overhead subtracted; latency is the API time it reports (comparative only).
- Prompt-cache savings are priced by API rules on the CLI backend, not observed.

## Next steps

- Streamlit side-by-side demo app (`app.py`).
- Router trained on real traffic, labelled by whether the cheap model's answer held up.
- Per-intent routing rules and a weekly quality guardrail on sampled production answers.

QA reports for every gate are in `qa/reports/`.
"""
    (ROOT / "README.md").write_text(md, encoding="utf-8")
    print("README.md written")


if __name__ == "__main__":
    main()
