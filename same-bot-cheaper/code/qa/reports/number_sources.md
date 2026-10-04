# Number-to-source table (blog + LinkedIn post)

| file | line | number | source |
|---|---|---|---|
| blog | 1 | `64%` | 1 - v2_full/v1_naive total_cost_usd |
| blog | 3 | `140` | 100 queries + conversation turns (data files) |
| blog | 9 | `3,600` | kb.md tokens on strong model = 3636 (QA gate 1), rounded to 100 |
| blog | 11 | `1` | quality scale bottom (rubric) |
| blog | 11 | `5.5` | model name: Claude Sonnet 5.5 |
| blog | 11 | `2` | config history.keep_last_turns |
| blog | 13 | `100` | test_queries.csv rows |
| blog | 13 | `62` | test_queries.csv label=simple |
| blog | 13 | `38` | test_queries.csv label=complex |
| blog | 13 | `10` | conversations.json |
| blog | 13 | `140` | 100 queries + conversation turns (data files) |
| blog | 15 | `5.5` | model name: Claude Sonnet 5.5 |
| blog | 15 | `$2` | config pricing claude-sonnet-5-5 input per MTok |
| blog | 15 | `$10` | config pricing claude-sonnet-5-5 output per MTok |
| blog | 15 | `4.5` | model name: Claude Haiku 4.5 |
| blog | 15 | `$1` | config pricing claude-haiku-4-5-20251001 input per MTok |
| blog | 15 | `$5` | config pricing claude-haiku-4-5-20251001 output per MTok |
| blog | 15 | `140` | 100 queries + conversation turns (data files) |
| blog | 17 | `1` | quality scale bottom (rubric) |
| blog | 17 | `5` | quality scale top (rubric) |
| blog | 17 | `5` | quality scale top (rubric) |
| blog | 17 | `3` | config retrieval.top_k |
| blog | 19 | `2` | config history.keep_last_turns |
| blog | 19 | `140` | 100 queries + conversation turns (data files) |
| blog | 19 | `$0.69` | summary.csv v2_full total_cost_usd |
| blog | 19 | `$1.95` | summary.csv v1_naive total_cost_usd |
| blog | 19 | `64%` | 1 - v2_full/v1_naive total_cost_usd |
| blog | 19 | `66%` | 1 - v2/v1 (total_input_tokens + output_tokens) |
| blog | 19 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| blog | 19 | `4.49` | summary.csv v2_full mean_quality |
| blog | 30 | `650` | persona tokens on strong model = 652 (rounded to 10) |
| blog | 30 | `170` | tight prompt tokens on strong model = 170 (rounded to 10) |
| blog | 38 | `140` | 100 queries + conversation turns (data files) |
| blog | 40 | `$1.95` | summary.csv v1_naive total_cost_usd |
| blog | 40 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| blog | 41 | `$1.75` | summary.csv plus_route total_cost_usd |
| blog | 41 | `4.56` | summary.csv plus_route mean_quality; summary.csv plus_route mean_quality |
| blog | 42 | `3` | config retrieval.top_k |
| blog | 42 | `$1.12` | summary.csv plus_retrieve total_cost_usd; summary.csv plus_trim total_cost_usd |
| blog | 42 | `4.34` | summary.csv plus_retrieve mean_quality; summary.csv plus_retrieve mean_quality |
| blog | 43 | `2` | config history.keep_last_turns |
| blog | 43 | `$1.12` | summary.csv plus_retrieve total_cost_usd; summary.csv plus_trim total_cost_usd |
| blog | 43 | `4.39` | summary.csv plus_trim mean_quality |
| blog | 44 | `$0.91` | summary.csv plus_tight_cache total_cost_usd |
| blog | 44 | `4.40` | summary.csv plus_tight_cache mean_quality |
| blog | 45 | `$0.69` | summary.csv v2_full total_cost_usd |
| blog | 45 | `4.49` | summary.csv v2_full mean_quality |
| blog | 52 | `4.5` | model name: Claude Haiku 4.5 |
| blog | 53 | `5.5` | model name: Claude Sonnet 5.5 |
| blog | 54 | `3` | config retrieval.top_k |
| blog | 54 | `2` | config history.keep_last_turns |
| blog | 61 | `$0.63` | retrieval step: plus_route - plus_retrieve cost |
| blog | 61 | `$1.26` | total saving v1 - v2 |
| blog | 61 | `14` | per_answer_eval: answers dropping >=2 from plus_route to plus_retrieve |
| blog | 63 | `0.5%` | trim step / v1 cost |
| blog | 63 | `203` | calls_eval v2_full Sonnet static_prefix_tokens |
| blog | 63 | `512` | config cache.min_tokens strong |
| blog | 65 | `4.80` | summary.csv cache_full_kb mean_quality |
| blog | 65 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| blog | 65 | `62%` | 1 - cache_full_kb/v1 cost |
| blog | 65 | `20` | per_answer_eval: answers improving >=2 v2_full -> cache_full_kb; judge_handcheck.md answers checked |
| blog | 71 | `12%` | routing_summary laya vs always_strong cost; router_head_summary zero-shot saving |
| blog | 71 | `4.60` | routing_summary laya mean_quality |
| blog | 71 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| blog | 71 | `45` | routing_confusion laya simple->strong |
| blog | 71 | `62` | test_queries.csv label=simple |
| blog | 73 | `136` | llm_router tokens per query |
| blog | 73 | `1,176` | routing_summary llm_router p50_router_ms |
| blog | 73 | `194` | routing_summary laya p50_router_ms |
| blog | 75 | `270` | data/router_train.csv rows |
| blog | 75 | `12%` | routing_summary laya vs always_strong cost; router_head_summary zero-shot saving |
| blog | 75 | `20%` | router_head_summary laya_head saving |
| blog | 75 | `4.54` | router_head_summary laya_head quality |
| blog | 75 | `38%` | router_head_summary hindsight ceiling saving; router_head_summary hindsight_ceiling saving |
| blog | 77 | `4.42` | routing_summary always_cheap quality_simple |
| blog | 77 | `4.79` | routing_summary always_strong quality_simple |
| blog | 81 | `0.2` | rule fixed in eval/run_routing_eval.py (complex gap <= 0.2) |
| blog | 81 | `0.50` | threshold_sweep recommended |
| blog | 81 | `4.32` | threshold_sweep quality_complex at recommended |
| blog | 81 | `4.00` | threshold_sweep quality_complex at next threshold |
| blog | 83 | `50` | effort_summary sample size; effort sample size (config effort_eval.sample) |
| blog | 83 | `9%` | effort: low vs thinking off |
| blog | 83 | `8,335` | effort_summary sonnet_high thinking_tokens |
| blog | 83 | `1,683` | effort_summary sonnet_low thinking_tokens |
| blog | 83 | `28%` | effort: high vs low cost |
| blog | 83 | `26%` | effort_combo laya_head + sonnet_low saving |
| blog | 87 | `8%` | cache_full_kb vs v2_full cost |
| blog | 87 | `140` | 100 queries + conversation turns (data files) |
| blog | 87 | `$5,368` | cache_full_kb cost per answer x 1M |
| blog | 87 | `$13,946` | v1 cost per answer x 1M |
| blog | 109 | `78%` | variance.csv judge re-score identical share |
| blog | 109 | `17` | judge_handcheck.md AGREE count |
| blog | 109 | `20` | per_answer_eval: answers improving >=2 v2_full -> cache_full_kb; judge_handcheck.md answers checked |
| blog | 109 | `100` | test_queries.csv rows |
| blog | 109 | `0.1` | noise floor stated from judge variance (mean |diff| 0.23 per answer) |
| blog | 109 | `140` | 100 queries + conversation turns (data files) |
| linkedin | 1 | `64%` | 1 - v2_full/v1_naive total_cost_usd |
| linkedin | 3 | `140` | 100 queries + conversation turns (data files) |
| linkedin | 7 | `$1.95` | summary.csv v1_naive total_cost_usd |
| linkedin | 7 | `$0.69` | summary.csv v2_full total_cost_usd |
| linkedin | 7 | `140` | 100 queries + conversation turns (data files) |
| linkedin | 7 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| linkedin | 7 | `4.49` | summary.csv v2_full mean_quality |
| linkedin | 7 | `5` | quality scale top (rubric) |
| linkedin | 9 | `12%` | routing_summary laya vs always_strong cost; router_head_summary zero-shot saving |
| linkedin | 9 | `270` | data/router_train.csv rows |
| linkedin | 9 | `20%` | router_head_summary laya_head saving |
| linkedin | 11 | `4.42` | routing_summary always_cheap quality_simple |
| linkedin | 11 | `4.79` | routing_summary always_strong quality_simple |
| linkedin | 13 | `4.80` | summary.csv cache_full_kb mean_quality |
| linkedin | 13 | `62%` | 1 - cache_full_kb/v1 cost |
| web page | 5 | `140` | 100 queries + conversation turns (data files) |
| web page | 6 | `64%` | 1 - v2_full/v1_naive total_cost_usd |
| web page | 8 | `5.5` | model name: Claude Sonnet 5.5 |
| web page | 8 | `4.5` | model name: Claude Haiku 4.5 |
| web page | 9 | `2026` | publication year (byline) |
| web page | 11 | `3,600` | kb.md tokens on strong model = 3636 (QA gate 1), rounded to 100 |
| web page | 11 | `1` | quality scale bottom (rubric) |
| web page | 11 | `5.5` | model name: Claude Sonnet 5.5 |
| web page | 11 | `2` | config history.keep_last_turns |
| web page | 11 | `100` | test_queries.csv rows |
| web page | 11 | `62` | test_queries.csv label=simple |
| web page | 11 | `38` | test_queries.csv label=complex |
| web page | 11 | `10` | conversations.json |
| web page | 11 | `140` | 100 queries + conversation turns (data files) |
| web page | 11 | `5.5` | model name: Claude Sonnet 5.5 |
| web page | 11 | `$2` | config pricing claude-sonnet-5-5 input per MTok |
| web page | 11 | `$10` | config pricing claude-sonnet-5-5 output per MTok |
| web page | 11 | `4.5` | model name: Claude Haiku 4.5 |
| web page | 11 | `$1` | config pricing claude-haiku-4-5-20251001 input per MTok |
| web page | 11 | `$5` | config pricing claude-haiku-4-5-20251001 output per MTok |
| web page | 11 | `140` | 100 queries + conversation turns (data files) |
| web page | 11 | `1` | quality scale bottom (rubric) |
| web page | 11 | `5` | quality scale top (rubric) |
| web page | 11 | `5` | quality scale top (rubric) |
| web page | 11 | `3` | config retrieval.top_k |
| web page | 11 | `2` | config history.keep_last_turns |
| web page | 11 | `140` | 100 queries + conversation turns (data files) |
| web page | 11 | `$0.69` | summary.csv v2_full total_cost_usd |
| web page | 11 | `$1.95` | summary.csv v1_naive total_cost_usd |
| web page | 11 | `64%` | 1 - v2_full/v1_naive total_cost_usd |
| web page | 11 | `66%` | 1 - v2/v1 (total_input_tokens + output_tokens) |
| web page | 11 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| web page | 11 | `4.49` | summary.csv v2_full mean_quality |
| web page | 13 | `64%` | 1 - v2_full/v1_naive total_cost_usd |
| web page | 13 | `140` | 100 queries + conversation turns (data files) |
| web page | 14 | `$1.95` | summary.csv v1_naive total_cost_usd |
| web page | 14 | `$0.69` | summary.csv v2_full total_cost_usd |
| web page | 14 | `66%` | 1 - v2/v1 (total_input_tokens + output_tokens) |
| web page | 15 | `$0.69` | summary.csv v2_full total_cost_usd |
| web page | 15 | `140` | 100 queries + conversation turns (data files) |
| web page | 15 | `$1.95` | summary.csv v1_naive total_cost_usd |
| web page | 16 | `66%` | 1 - v2/v1 (total_input_tokens + output_tokens) |
| web page | 17 | `4.49` | summary.csv v2_full mean_quality |
| web page | 17 | `5` | quality scale top (rubric) |
| web page | 17 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| web page | 18 | `20%` | router_head_summary laya_head saving |
| web page | 20 | `50%` | retrieval share of total saving |
| web page | 21 | `4.80` | summary.csv cache_full_kb mean_quality |
| web page | 21 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| web page | 21 | `62%` | 1 - cache_full_kb/v1 cost |
| web page | 22 | `12%` | routing_summary laya vs always_strong cost; router_head_summary zero-shot saving |
| web page | 22 | `20%` | router_head_summary laya_head saving |
| web page | 22 | `270` | data/router_train.csv rows |
| web page | 22 | `38%` | router_head_summary hindsight ceiling saving; router_head_summary hindsight_ceiling saving |
| web page | 23 | `4.42` | routing_summary always_cheap quality_simple |
| web page | 23 | `4.79` | routing_summary always_strong quality_simple |
| web page | 24 | `9%` | effort: low vs thinking off |
| web page | 29 | `650` | persona tokens on strong model = 652 (rounded to 10) |
| web page | 29 | `170` | tight prompt tokens on strong model = 170 (rounded to 10) |
| web page | 37 | `140` | 100 queries + conversation turns (data files) |
| web page | 44 | `$1.95` | summary.csv v1_naive total_cost_usd |
| web page | 45 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| web page | 49 | `$1.75` | summary.csv plus_route total_cost_usd |
| web page | 50 | `4.56` | summary.csv plus_route mean_quality; summary.csv plus_route mean_quality |
| web page | 53 | `3` | config retrieval.top_k |
| web page | 54 | `$1.12` | summary.csv plus_retrieve total_cost_usd; summary.csv plus_trim total_cost_usd |
| web page | 55 | `4.34` | summary.csv plus_retrieve mean_quality; summary.csv plus_retrieve mean_quality |
| web page | 58 | `2` | config history.keep_last_turns |
| web page | 59 | `$1.12` | summary.csv plus_retrieve total_cost_usd; summary.csv plus_trim total_cost_usd |
| web page | 60 | `4.39` | summary.csv plus_trim mean_quality |
| web page | 64 | `$0.91` | summary.csv plus_tight_cache total_cost_usd |
| web page | 65 | `4.40` | summary.csv plus_tight_cache mean_quality |
| web page | 69 | `$0.69` | summary.csv v2_full total_cost_usd |
| web page | 70 | `4.49` | summary.csv v2_full mean_quality |
| web page | 79 | `4.5` | model name: Claude Haiku 4.5 |
| web page | 80 | `5.5` | model name: Claude Sonnet 5.5 |
| web page | 82 | `3` | config retrieval.top_k |
| web page | 82 | `2` | config history.keep_last_turns |
| web page | 89 | `140` | 100 queries + conversation turns (data files) |
| web page | 89 | `5` | quality scale top (rubric) |
| web page | 90 | `$1.95` | summary.csv v1_naive total_cost_usd |
| web page | 90 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| web page | 91 | `$1.75` | summary.csv plus_route total_cost_usd |
| web page | 91 | `4.56` | summary.csv plus_route mean_quality; summary.csv plus_route mean_quality |
| web page | 92 | `$1.12` | summary.csv plus_retrieve total_cost_usd; summary.csv plus_trim total_cost_usd |
| web page | 92 | `4.34` | summary.csv plus_retrieve mean_quality; summary.csv plus_retrieve mean_quality |
| web page | 93 | `$1.12` | summary.csv plus_retrieve total_cost_usd; summary.csv plus_trim total_cost_usd |
| web page | 93 | `4.39` | summary.csv plus_trim mean_quality |
| web page | 94 | `$0.91` | summary.csv plus_tight_cache total_cost_usd |
| web page | 94 | `4.40` | summary.csv plus_tight_cache mean_quality |
| web page | 95 | `$0.69` | summary.csv v2_full total_cost_usd |
| web page | 95 | `4.49` | summary.csv v2_full mean_quality |
| web page | 96 | `$0.75` | summary.csv cache_full_kb total_cost_usd |
| web page | 96 | `4.80` | summary.csv cache_full_kb mean_quality |
| web page | 97 | `$0.63` | retrieval step: plus_route - plus_retrieve cost |
| web page | 97 | `$1.26` | total saving v1 - v2 |
| web page | 97 | `14` | per_answer_eval: answers dropping >=2 from plus_route to plus_retrieve |
| web page | 98 | `0.5%` | trim step / v1 cost |
| web page | 98 | `203` | calls_eval v2_full Sonnet static_prefix_tokens |
| web page | 98 | `512` | config cache.min_tokens strong |
| web page | 99 | `4.80` | summary.csv cache_full_kb mean_quality |
| web page | 99 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| web page | 99 | `62%` | 1 - cache_full_kb/v1 cost |
| web page | 99 | `20` | per_answer_eval: answers improving >=2 v2_full -> cache_full_kb; judge_handcheck.md answers checked |
| web page | 100 | `12%` | routing_summary laya vs always_strong cost; router_head_summary zero-shot saving |
| web page | 100 | `4.60` | routing_summary laya mean_quality |
| web page | 100 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| web page | 100 | `45` | routing_confusion laya simple->strong |
| web page | 100 | `62` | test_queries.csv label=simple |
| web page | 101 | `136` | llm_router tokens per query |
| web page | 101 | `1,176` | routing_summary llm_router p50_router_ms |
| web page | 101 | `194` | routing_summary laya p50_router_ms |
| web page | 102 | `270` | data/router_train.csv rows |
| web page | 102 | `12%` | routing_summary laya vs always_strong cost; router_head_summary zero-shot saving |
| web page | 102 | `20%` | router_head_summary laya_head saving |
| web page | 102 | `4.54` | router_head_summary laya_head quality |
| web page | 102 | `38%` | router_head_summary hindsight ceiling saving; router_head_summary hindsight_ceiling saving |
| web page | 103 | `4.42` | routing_summary always_cheap quality_simple |
| web page | 103 | `4.79` | routing_summary always_strong quality_simple |
| web page | 103 | `100` | test_queries.csv rows |
| web page | 104 | `12%` | routing_summary laya vs always_strong cost; router_head_summary zero-shot saving |
| web page | 104 | `4.60` | routing_summary laya mean_quality |
| web page | 105 | `13%` | router_head_summary length_rule saving |
| web page | 105 | `4.59` | router_head_summary length_rule quality |
| web page | 106 | `15%` | router_head_summary minilm_head saving |
| web page | 106 | `4.58` | router_head_summary minilm_head quality |
| web page | 107 | `20%` | router_head_summary laya_head saving |
| web page | 107 | `4.54` | router_head_summary laya_head quality |
| web page | 108 | `38%` | router_head_summary hindsight ceiling saving; router_head_summary hindsight_ceiling saving |
| web page | 108 | `4.68` | router_head_summary hindsight_ceiling quality |
| web page | 109 | `0.2` | rule fixed in eval/run_routing_eval.py (complex gap <= 0.2) |
| web page | 109 | `0.50` | threshold_sweep recommended |
| web page | 109 | `4.32` | threshold_sweep quality_complex at recommended |
| web page | 109 | `4.00` | threshold_sweep quality_complex at next threshold |
| web page | 110 | `50` | effort_summary sample size; effort sample size (config effort_eval.sample) |
| web page | 110 | `9%` | effort: low vs thinking off |
| web page | 110 | `8,335` | effort_summary sonnet_high thinking_tokens |
| web page | 110 | `1,683` | effort_summary sonnet_low thinking_tokens |
| web page | 110 | `28%` | effort: high vs low cost |
| web page | 110 | `26%` | effort_combo laya_head + sonnet_low saving |
| web page | 110 | `50` | effort_summary sample size; effort sample size (config effort_eval.sample) |
| web page | 111 | `$0.264` | effort_summary always_strong total_cost_usd |
| web page | 111 | `4.62` | effort_summary always_strong mean_quality; effort_summary sonnet_medium mean_quality |
| web page | 112 | `$0.241` | effort_summary sonnet_low total_cost_usd |
| web page | 112 | `4.66` | effort_summary sonnet_low mean_quality; effort_summary sonnet_high mean_quality |
| web page | 113 | `$0.259` | effort_summary sonnet_medium total_cost_usd |
| web page | 113 | `4.62` | effort_summary always_strong mean_quality; effort_summary sonnet_medium mean_quality |
| web page | 114 | `$0.307` | effort_summary sonnet_high total_cost_usd |
| web page | 114 | `4.66` | effort_summary sonnet_low mean_quality; effort_summary sonnet_high mean_quality |
| web page | 115 | `1,683` | effort_summary sonnet_low thinking_tokens |
| web page | 115 | `8,335` | effort_summary sonnet_high thinking_tokens |
| web page | 115 | `8%` | cache_full_kb vs v2_full cost |
| web page | 115 | `140` | 100 queries + conversation turns (data files) |
| web page | 115 | `$5,368` | cache_full_kb cost per answer x 1M |
| web page | 115 | `$13,946` | v1 cost per answer x 1M |
| web page | 129 | `78%` | variance.csv judge re-score identical share |
| web page | 129 | `17` | judge_handcheck.md AGREE count |
| web page | 129 | `20` | per_answer_eval: answers improving >=2 v2_full -> cache_full_kb; judge_handcheck.md answers checked |
| web page | 129 | `100` | test_queries.csv rows |
| web page | 129 | `0.1` | noise floor stated from judge variance (mean |diff| 0.23 per answer) |
| web page | 129 | `140` | 100 queries + conversation turns (data files) |
| web page | 132 | `140` | 100 queries + conversation turns (data files) |
| web page | 132 | `100` | test_queries.csv rows |
| web page | 132 | `10` | conversations.json |
| web page | 132 | `270` | data/router_train.csv rows |
