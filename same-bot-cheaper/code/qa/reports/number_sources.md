# Number-to-source table (blog + LinkedIn post)

| file | line | number | source |
|---|---|---|---|
| blog | 1 | `64%` | 1 - v2_full/v1_naive total_cost_usd |
| blog | 3 | `100` | test_queries.csv rows |
| blog | 3 | `10` | conversations.json |
| blog | 3 | `140` | 100 queries + conversation turns (data files) |
| blog | 7 | `140` | 100 queries + conversation turns (data files) |
| blog | 7 | `$0.69` | summary.csv v2_full total_cost_usd |
| blog | 7 | `$1.95` | summary.csv v1_naive total_cost_usd |
| blog | 7 | `64%` | 1 - v2_full/v1_naive total_cost_usd |
| blog | 7 | `66%` | 1 - v2/v1 (total_input_tokens + output_tokens) |
| blog | 7 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| blog | 7 | `4.49` | summary.csv v2_full mean_quality |
| blog | 7 | `5` | quality scale top (rubric) |
| blog | 20 | `650` | persona tokens on strong model = 652 (rounded to 10) |
| blog | 20 | `170` | tight prompt tokens on strong model = 170 (rounded to 10) |
| blog | 26 | `100` | test_queries.csv rows |
| blog | 26 | `62` | test_queries.csv label=simple |
| blog | 26 | `38` | test_queries.csv label=complex |
| blog | 26 | `10` | conversations.json |
| blog | 26 | `1` | quality scale bottom (rubric) |
| blog | 26 | `5` | quality scale top (rubric) |
| blog | 26 | `5` | quality scale top (rubric) |
| blog | 26 | `3` | config retrieval.top_k |
| blog | 28 | `140` | 100 queries + conversation turns (data files) |
| blog | 30 | `$1.95` | summary.csv v1_naive total_cost_usd |
| blog | 30 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| blog | 31 | `$1.75` | summary.csv plus_route total_cost_usd |
| blog | 31 | `4.56` | summary.csv plus_route mean_quality; summary.csv plus_route mean_quality |
| blog | 32 | `3` | config retrieval.top_k |
| blog | 32 | `$1.12` | summary.csv plus_retrieve total_cost_usd; summary.csv plus_trim total_cost_usd |
| blog | 32 | `4.34` | summary.csv plus_retrieve mean_quality; summary.csv plus_retrieve mean_quality |
| blog | 33 | `2` | config history.keep_last_turns |
| blog | 33 | `$1.12` | summary.csv plus_retrieve total_cost_usd; summary.csv plus_trim total_cost_usd |
| blog | 33 | `4.39` | summary.csv plus_trim mean_quality |
| blog | 34 | `$0.91` | summary.csv plus_tight_cache total_cost_usd |
| blog | 34 | `4.40` | summary.csv plus_tight_cache mean_quality |
| blog | 35 | `$0.69` | summary.csv v2_full total_cost_usd |
| blog | 35 | `4.49` | summary.csv v2_full mean_quality |
| blog | 42 | `4.5` | model name: Claude Haiku 4.5 |
| blog | 43 | `5.5` | model name: Claude Sonnet 5.5 |
| blog | 44 | `3` | config retrieval.top_k |
| blog | 44 | `2` | config history.keep_last_turns |
| blog | 51 | `$0.63` | retrieval step: plus_route - plus_retrieve cost |
| blog | 51 | `$1.26` | total saving v1 - v2 |
| blog | 51 | `14` | per_answer_eval: answers dropping >=2 from plus_route to plus_retrieve |
| blog | 53 | `0.5%` | trim step / v1 cost |
| blog | 53 | `203` | calls_eval v2_full Sonnet static_prefix_tokens |
| blog | 53 | `512` | config cache.min_tokens strong |
| blog | 55 | `4.80` | summary.csv cache_full_kb mean_quality |
| blog | 55 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| blog | 55 | `62%` | 1 - cache_full_kb/v1 cost |
| blog | 55 | `20` | per_answer_eval: answers improving >=2 v2_full -> cache_full_kb; judge_handcheck.md answers checked |
| blog | 61 | `12%` | routing_summary laya vs always_strong cost; router_head_summary zero-shot saving |
| blog | 61 | `4.60` | routing_summary laya mean_quality |
| blog | 61 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| blog | 61 | `45` | routing_confusion laya simple->strong |
| blog | 61 | `62` | test_queries.csv label=simple |
| blog | 63 | `136` | llm_router tokens per query |
| blog | 63 | `1,176` | routing_summary llm_router p50_router_ms |
| blog | 63 | `194` | routing_summary laya p50_router_ms |
| blog | 65 | `270` | data/router_train.csv rows |
| blog | 65 | `12%` | routing_summary laya vs always_strong cost; router_head_summary zero-shot saving |
| blog | 65 | `20%` | router_head_summary laya_head saving |
| blog | 65 | `4.54` | router_head_summary laya_head quality |
| blog | 65 | `38%` | router_head_summary hindsight ceiling saving; router_head_summary hindsight_ceiling saving |
| blog | 67 | `4.42` | routing_summary always_cheap quality_simple |
| blog | 67 | `4.79` | routing_summary always_strong quality_simple |
| blog | 71 | `0.2` | rule fixed in eval/run_routing_eval.py (complex gap <= 0.2) |
| blog | 71 | `0.50` | threshold_sweep recommended |
| blog | 71 | `4.32` | threshold_sweep quality_complex at recommended |
| blog | 71 | `4.00` | threshold_sweep quality_complex at next threshold |
| blog | 73 | `50` | effort_summary sample size; effort sample size (config effort_eval.sample) |
| blog | 73 | `9%` | effort: low vs thinking off |
| blog | 73 | `8,335` | effort_summary sonnet_high thinking_tokens |
| blog | 73 | `1,683` | effort_summary sonnet_low thinking_tokens |
| blog | 73 | `28%` | effort: high vs low cost |
| blog | 73 | `26%` | effort_combo laya_head + sonnet_low saving |
| blog | 73 | `50` | effort_summary sample size; effort sample size (config effort_eval.sample) |
| blog | 77 | `8%` | cache_full_kb vs v2_full cost |
| blog | 77 | `140` | 100 queries + conversation turns (data files) |
| blog | 77 | `$5,368` | cache_full_kb cost per answer x 1M |
| blog | 77 | `$13,946` | v1 cost per answer x 1M |
| blog | 99 | `78%` | variance.csv judge re-score identical share |
| blog | 99 | `17` | judge_handcheck.md AGREE count |
| blog | 99 | `20` | per_answer_eval: answers improving >=2 v2_full -> cache_full_kb; judge_handcheck.md answers checked |
| blog | 99 | `100` | test_queries.csv rows |
| blog | 99 | `0.1` | noise floor stated from judge variance (mean |diff| 0.23 per answer) |
| blog | 99 | `140` | 100 queries + conversation turns (data files) |
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
| web page | 11 | `140` | 100 queries + conversation turns (data files) |
| web page | 11 | `$0.69` | summary.csv v2_full total_cost_usd |
| web page | 11 | `$1.95` | summary.csv v1_naive total_cost_usd |
| web page | 11 | `64%` | 1 - v2_full/v1_naive total_cost_usd |
| web page | 11 | `66%` | 1 - v2/v1 (total_input_tokens + output_tokens) |
| web page | 11 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| web page | 11 | `4.49` | summary.csv v2_full mean_quality |
| web page | 11 | `5` | quality scale top (rubric) |
| web page | 12 | `64%` | 1 - v2_full/v1_naive total_cost_usd |
| web page | 12 | `140` | 100 queries + conversation turns (data files) |
| web page | 13 | `$1.95` | summary.csv v1_naive total_cost_usd |
| web page | 13 | `$0.69` | summary.csv v2_full total_cost_usd |
| web page | 13 | `66%` | 1 - v2/v1 (total_input_tokens + output_tokens) |
| web page | 14 | `$0.69` | summary.csv v2_full total_cost_usd |
| web page | 14 | `140` | 100 queries + conversation turns (data files) |
| web page | 14 | `$1.95` | summary.csv v1_naive total_cost_usd |
| web page | 15 | `66%` | 1 - v2/v1 (total_input_tokens + output_tokens) |
| web page | 16 | `4.49` | summary.csv v2_full mean_quality |
| web page | 16 | `5` | quality scale top (rubric) |
| web page | 16 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| web page | 17 | `20%` | router_head_summary laya_head saving |
| web page | 19 | `50%` | retrieval share of total saving |
| web page | 20 | `4.80` | summary.csv cache_full_kb mean_quality |
| web page | 20 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| web page | 20 | `62%` | 1 - cache_full_kb/v1 cost |
| web page | 21 | `12%` | routing_summary laya vs always_strong cost; router_head_summary zero-shot saving |
| web page | 21 | `20%` | router_head_summary laya_head saving |
| web page | 21 | `270` | data/router_train.csv rows |
| web page | 21 | `38%` | router_head_summary hindsight ceiling saving; router_head_summary hindsight_ceiling saving |
| web page | 22 | `4.42` | routing_summary always_cheap quality_simple |
| web page | 22 | `4.79` | routing_summary always_strong quality_simple |
| web page | 23 | `9%` | effort: low vs thinking off |
| web page | 28 | `650` | persona tokens on strong model = 652 (rounded to 10) |
| web page | 28 | `170` | tight prompt tokens on strong model = 170 (rounded to 10) |
| web page | 31 | `100` | test_queries.csv rows |
| web page | 31 | `62` | test_queries.csv label=simple |
| web page | 31 | `38` | test_queries.csv label=complex |
| web page | 31 | `10` | conversations.json |
| web page | 31 | `1` | quality scale bottom (rubric) |
| web page | 31 | `5` | quality scale top (rubric) |
| web page | 31 | `5` | quality scale top (rubric) |
| web page | 31 | `3` | config retrieval.top_k |
| web page | 36 | `140` | 100 queries + conversation turns (data files) |
| web page | 43 | `$1.95` | summary.csv v1_naive total_cost_usd |
| web page | 44 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| web page | 48 | `$1.75` | summary.csv plus_route total_cost_usd |
| web page | 49 | `4.56` | summary.csv plus_route mean_quality; summary.csv plus_route mean_quality |
| web page | 52 | `3` | config retrieval.top_k |
| web page | 53 | `$1.12` | summary.csv plus_retrieve total_cost_usd; summary.csv plus_trim total_cost_usd |
| web page | 54 | `4.34` | summary.csv plus_retrieve mean_quality; summary.csv plus_retrieve mean_quality |
| web page | 57 | `2` | config history.keep_last_turns |
| web page | 58 | `$1.12` | summary.csv plus_retrieve total_cost_usd; summary.csv plus_trim total_cost_usd |
| web page | 59 | `4.39` | summary.csv plus_trim mean_quality |
| web page | 63 | `$0.91` | summary.csv plus_tight_cache total_cost_usd |
| web page | 64 | `4.40` | summary.csv plus_tight_cache mean_quality |
| web page | 68 | `$0.69` | summary.csv v2_full total_cost_usd |
| web page | 69 | `4.49` | summary.csv v2_full mean_quality |
| web page | 78 | `4.5` | model name: Claude Haiku 4.5 |
| web page | 79 | `5.5` | model name: Claude Sonnet 5.5 |
| web page | 81 | `3` | config retrieval.top_k |
| web page | 81 | `2` | config history.keep_last_turns |
| web page | 88 | `140` | 100 queries + conversation turns (data files) |
| web page | 88 | `5` | quality scale top (rubric) |
| web page | 89 | `$1.95` | summary.csv v1_naive total_cost_usd |
| web page | 89 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| web page | 90 | `$1.75` | summary.csv plus_route total_cost_usd |
| web page | 90 | `4.56` | summary.csv plus_route mean_quality; summary.csv plus_route mean_quality |
| web page | 91 | `$1.12` | summary.csv plus_retrieve total_cost_usd; summary.csv plus_trim total_cost_usd |
| web page | 91 | `4.34` | summary.csv plus_retrieve mean_quality; summary.csv plus_retrieve mean_quality |
| web page | 92 | `$1.12` | summary.csv plus_retrieve total_cost_usd; summary.csv plus_trim total_cost_usd |
| web page | 92 | `4.39` | summary.csv plus_trim mean_quality |
| web page | 93 | `$0.91` | summary.csv plus_tight_cache total_cost_usd |
| web page | 93 | `4.40` | summary.csv plus_tight_cache mean_quality |
| web page | 94 | `$0.69` | summary.csv v2_full total_cost_usd |
| web page | 94 | `4.49` | summary.csv v2_full mean_quality |
| web page | 95 | `$0.75` | summary.csv cache_full_kb total_cost_usd |
| web page | 95 | `4.80` | summary.csv cache_full_kb mean_quality |
| web page | 96 | `$0.63` | retrieval step: plus_route - plus_retrieve cost |
| web page | 96 | `$1.26` | total saving v1 - v2 |
| web page | 96 | `14` | per_answer_eval: answers dropping >=2 from plus_route to plus_retrieve |
| web page | 97 | `0.5%` | trim step / v1 cost |
| web page | 97 | `203` | calls_eval v2_full Sonnet static_prefix_tokens |
| web page | 97 | `512` | config cache.min_tokens strong |
| web page | 98 | `4.80` | summary.csv cache_full_kb mean_quality |
| web page | 98 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| web page | 98 | `62%` | 1 - cache_full_kb/v1 cost |
| web page | 98 | `20` | per_answer_eval: answers improving >=2 v2_full -> cache_full_kb; judge_handcheck.md answers checked |
| web page | 99 | `12%` | routing_summary laya vs always_strong cost; router_head_summary zero-shot saving |
| web page | 99 | `4.60` | routing_summary laya mean_quality |
| web page | 99 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| web page | 99 | `45` | routing_confusion laya simple->strong |
| web page | 99 | `62` | test_queries.csv label=simple |
| web page | 100 | `136` | llm_router tokens per query |
| web page | 100 | `1,176` | routing_summary llm_router p50_router_ms |
| web page | 100 | `194` | routing_summary laya p50_router_ms |
| web page | 101 | `270` | data/router_train.csv rows |
| web page | 101 | `12%` | routing_summary laya vs always_strong cost; router_head_summary zero-shot saving |
| web page | 101 | `20%` | router_head_summary laya_head saving |
| web page | 101 | `4.54` | router_head_summary laya_head quality |
| web page | 101 | `38%` | router_head_summary hindsight ceiling saving; router_head_summary hindsight_ceiling saving |
| web page | 102 | `4.42` | routing_summary always_cheap quality_simple |
| web page | 102 | `4.79` | routing_summary always_strong quality_simple |
| web page | 102 | `100` | test_queries.csv rows |
| web page | 103 | `12%` | routing_summary laya vs always_strong cost; router_head_summary zero-shot saving |
| web page | 103 | `4.60` | routing_summary laya mean_quality |
| web page | 104 | `13%` | router_head_summary length_rule saving |
| web page | 104 | `4.59` | router_head_summary length_rule quality |
| web page | 105 | `15%` | router_head_summary minilm_head saving |
| web page | 105 | `4.58` | router_head_summary minilm_head quality |
| web page | 106 | `20%` | router_head_summary laya_head saving |
| web page | 106 | `4.54` | router_head_summary laya_head quality |
| web page | 107 | `38%` | router_head_summary hindsight ceiling saving; router_head_summary hindsight_ceiling saving |
| web page | 107 | `4.68` | router_head_summary hindsight_ceiling quality |
| web page | 108 | `0.2` | rule fixed in eval/run_routing_eval.py (complex gap <= 0.2) |
| web page | 108 | `0.50` | threshold_sweep recommended |
| web page | 108 | `4.32` | threshold_sweep quality_complex at recommended |
| web page | 108 | `4.00` | threshold_sweep quality_complex at next threshold |
| web page | 109 | `50` | effort_summary sample size; effort sample size (config effort_eval.sample) |
| web page | 109 | `9%` | effort: low vs thinking off |
| web page | 109 | `8,335` | effort_summary sonnet_high thinking_tokens |
| web page | 109 | `1,683` | effort_summary sonnet_low thinking_tokens |
| web page | 109 | `28%` | effort: high vs low cost |
| web page | 109 | `26%` | effort_combo laya_head + sonnet_low saving |
| web page | 109 | `50` | effort_summary sample size; effort sample size (config effort_eval.sample) |
| web page | 109 | `50` | effort_summary sample size; effort sample size (config effort_eval.sample) |
| web page | 110 | `$0.264` | effort_summary always_strong total_cost_usd |
| web page | 110 | `4.62` | effort_summary always_strong mean_quality; effort_summary sonnet_medium mean_quality |
| web page | 111 | `$0.241` | effort_summary sonnet_low total_cost_usd |
| web page | 111 | `4.66` | effort_summary sonnet_low mean_quality; effort_summary sonnet_high mean_quality |
| web page | 112 | `$0.259` | effort_summary sonnet_medium total_cost_usd |
| web page | 112 | `4.62` | effort_summary always_strong mean_quality; effort_summary sonnet_medium mean_quality |
| web page | 113 | `$0.307` | effort_summary sonnet_high total_cost_usd |
| web page | 113 | `4.66` | effort_summary sonnet_low mean_quality; effort_summary sonnet_high mean_quality |
| web page | 114 | `1,683` | effort_summary sonnet_low thinking_tokens |
| web page | 114 | `8,335` | effort_summary sonnet_high thinking_tokens |
| web page | 114 | `8%` | cache_full_kb vs v2_full cost |
| web page | 114 | `140` | 100 queries + conversation turns (data files) |
| web page | 114 | `$5,368` | cache_full_kb cost per answer x 1M |
| web page | 114 | `$13,946` | v1 cost per answer x 1M |
| web page | 128 | `78%` | variance.csv judge re-score identical share |
| web page | 128 | `17` | judge_handcheck.md AGREE count |
| web page | 128 | `20` | per_answer_eval: answers improving >=2 v2_full -> cache_full_kb; judge_handcheck.md answers checked |
| web page | 128 | `100` | test_queries.csv rows |
| web page | 128 | `0.1` | noise floor stated from judge variance (mean |diff| 0.23 per answer) |
| web page | 128 | `140` | 100 queries + conversation turns (data files) |
| web page | 131 | `140` | 100 queries + conversation turns (data files) |
| web page | 131 | `100` | test_queries.csv rows |
| web page | 131 | `10` | conversations.json |
| web page | 131 | `270` | data/router_train.csv rows |
