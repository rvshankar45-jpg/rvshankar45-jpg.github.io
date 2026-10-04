# QA gate 2 (pipeline dry run) - 2026-10-01 21:09

13/13 checks passed.

- **PASS** every call logged all required fields: 59 rows (55 answers, 4 summaries, 4 response-cache hits); nulls={}; laya rows missing score/latency=0; empty uncapped answers=0
- **PASS** token counts come from the API usage block: all 55 called rows: logged input+cache = raw usage total - calibrated overhead; output = raw output (or = max_tokens where the API cap was emulated: 0 rows); mismatches=[]
    - spot check v2_full/q088 (claude-sonnet-5-5): raw usage input=2 cache_write=440 cache_read=1397 output=210 | overhead 448 -> logged payload 1391 (in 1391 / cr 0 / cw 0), out 210
    - spot check v2_full/c05.t3 (claude-sonnet-5-5): raw usage input=2 cache_write=2199 cache_read=0 output=144 | overhead 448 -> logged payload 1753 (in 1753 / cr 0 / cw 0), out 144
    - spot check only_route/q091 (claude-sonnet-5-5): raw usage input=2 cache_write=448 cache_read=4338 output=1356 | overhead 448 -> logged payload 4340 (in 4340 / cr 0 / cw 0), out 1356
- **PASS** harness overhead is independent of the output cap setting: total input without cap=488, with cap=488; run start overhead={'claude-sonnet-5-5': 448, 'claude-haiku-4-5-20251001': 379} (re-verified unchanged at run end by the dry run)
- **PASS** cost math: independent recompute matches every row: 59 rows, max |diff| = $0.00e+00 (limit $0.0001)
- **PASS** pricing in config matches the provider's pricing page: config == snapshot of https://platform.claude.com/docs/en/about-claude/pricing checked 2026-09-30 (1 days ago) by Claude (WebFetch of the pricing page during the build session); diffs={}
- **PASS** v1 sends the full KB every call; v2 sends only retrieved chunks: v1: 15/15 calls chunk_ids=full_kb, payload min 4313 tokens; retrieve: 18 calls with 3 section ids each (e.g. q001: ["s2", "s4", "s5"]); retrieve-alone payload < v1 on 3/3 queries
- **PASS** Laya ran: varied scores in [0,1], latency logged, routing follows the threshold: 18 routed rows, 15 distinct scores, range 0.336-0.721, std 0.114; laya latency median 205 ms on cuda; threshold 0.5: 15 strong / 3 cheap; rule violations=0
- **PASS** prompt caching: 2nd+ calls read the cached prefix wherever the prefix is cacheable: 1 cacheable groups behave (first call writes, later calls read); violations=[]
    - not cacheable by API rules: v2_full/claude-haiku-4-5-20251001: static prefix 140 < min 4096
    - not cacheable by API rules: v2_full/claude-sonnet-5-5: static prefix 203 < min 512
    - brief's literal check - v2_full Sonnet calls with cache_read > 0: 0/13
    - observed server-side evidence: Claude Code's own cache read 13/14 of v1's 2nd+ calls -> the static persona+KB prefix is byte-stable across calls
- **PASS** output cap: no capped-variant answer exceeds max_tokens: 18 capped calls, max output 798 / 1000; hit the cap: 0; uncapped calls hitting the 4000 ceiling: 0
- **PASS** answer sanity: non-empty, no error text, addresses the query (judge): 42 distinct answers judged, 42 address the query; error-text answers=0
- **PASS** each flag switched on alone changes what it should and nothing else: route: 3 rows; retrieve: 3 rows; tight_prompt: 3 rows; output_cap: 3 rows; prompt_cache: 3 rows; trim_history: 5 turns, 2 summary calls; response_cache: hits {'dup_exact': 'exact', 'dup_paraphrase': 'semantic'}
- **PASS** system prompt sizes match the spec (~600 naive, ~150 tight): persona 652 tokens, tight 170 tokens on claude-sonnet-5-5
- **PASS** spend reported and full-run projection computed: dry run: 1 new model calls, 2,543 input / 104 output tokens consumed (incl. harness overhead), product cost at API prices $0.005; QA gate calls 2
    - projected v1_naive (product cost of one full pass): $1.87
    - projected v2_full (product cost of one full pass): $0.73
    - projected full eval (Phases 5+5b): ~867 new calls, ~2.4M input + ~0.40M output tokens of subscription usage; share routed strong by Laya in the dry run = 87%
