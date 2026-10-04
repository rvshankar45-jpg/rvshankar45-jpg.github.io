# QA gate - full eval - 2026-10-03 12:06

9/9 checks passed.

- **PASS** every variant and strategy has all 100 queries + all conversation turns: expected rows per variant met (variants: 100 + 40 turns; 5b: 100; variance: 20); missing={}; empty answers=0; answers without a judge score=0; max rows per variant/unit=1
- **PASS** summary totals equal the sum of per-call rows: 7 variants x 4 totals and 6 strategies x 3 totals re-summed from per-call / per-query rows; mismatches=[]
- **PASS** 5c effort runs: thinking on, same prompts as 5b, only effort differs: 150 calls; prompts identical to 5b=True; thinking tokens per level (total / mean / share>0): sonnet_high: 8335 / 167 / 84%; sonnet_low: 1683 / 34 / 16%; sonnet_medium: 3433 / 69 / 28%; capped=0
- **PASS** 5b isolation: strategies differ only in the answering model: for all 100 queries, strong vs cheap requests have identical system prompt=True, user message=True, retrieved chunks=True
- **PASS** oracle follows the hand labels; always_strong / always_cheap use only their model: oracle=True (38 strong = 38 complex labels); fixed strategies=True; underlying call models=True
- **PASS** router efficiency within [0,1] (or explained): {'always_strong': 0.0, 'always_cheap': 2.006, 'laya': 0.338, 'llm_router': 1.082, 'oracle': 1.0, 'laya@0.50': 0.338}; OUT OF RANGE {'always_cheap': 2.006, 'llm_router': 1.082} - see explanation
    - always_cheap efficiency 2.006 > 1: it is CHEAPER than the oracle, i.e. it sends some complex queries to the cheap model (the oracle never does). Read it together with its complex-query quality.
    - llm_router efficiency 1.082 > 1: it is CHEAPER than the oracle, i.e. it sends some complex queries to the cheap model (the oracle never does). Read it together with its complex-query quality.
- **PASS** judge reliability measured: same answers re-judged: identical score 78%, mean |diff| 0.23 (n=40); fresh generations of the same request: identical score 85%, mean |diff| 0.17, mean |cost diff| 4% (n=40); 20 stratified answers written to qa/reports/judge_handcheck.md
- **PASS** threshold sweep: cost never rises as the threshold rises: 11 thresholds 0.30-0.80, cost $0.511 -> $0.155; breaks=[]
- **PASS** surprise check run (contradictions are flagged, not smoothed over): 1 result(s) contradict the brief's expectations
    - SURPRISE: Laya cost sits 83% of the way from always_cheap to always_strong (expected near cheap)
