# Number-to-source table (blog + LinkedIn post)

| file | line | number | source |
|---|---|---|---|
| blog | 1 | `64%` | 1 - v2_full/v1_naive total_cost_usd |
| blog | 3 | `140` | 100 queries + conversation turns (data files) |
| blog | 9 | `3,600` | kb.md tokens on strong model = 3636 (QA gate 1), rounded to 100 |
| blog | 9 | `9` | kb.md sections (retriever chunks) |
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
| blog | 17 | `1` | quality scale bottom (rubric) |
| blog | 17 | `5` | quality scale top (rubric) |
| blog | 17 | `5` | quality scale top (rubric) |
| blog | 17 | `3` | config retrieval.top_k |
| blog | 21 | `64%` | 1 - v2_full/v1_naive total_cost_usd |
| blog | 21 | `140` | 100 queries + conversation turns (data files) |
| blog | 21 | `$0.69` | summary.csv v2_full total_cost_usd |
| blog | 21 | `$1.95` | summary.csv v1_naive total_cost_usd |
| blog | 21 | `4.49` | summary.csv v2_full mean_quality |
| blog | 21 | `5` | quality scale top (rubric) |
| blog | 21 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| blog | 22 | `3` | config retrieval.top_k |
| blog | 23 | `62%` | 1 - cache_full_kb/v1 cost |
| blog | 23 | `4.80` | summary.csv cache_full_kb mean_quality |
| blog | 24 | `12%` | routing_summary laya vs always_strong cost; router_head_summary zero-shot saving |
| blog | 24 | `270` | data/router_train.csv rows |
| blog | 24 | `20%` | router_head_summary laya_head saving |
| blog | 25 | `28%` | effort: high vs low cost |
| blog | 35 | `2` | config history.keep_last_turns |
| blog | 38 | `3` | config retrieval.top_k |
| blog | 39 | `2` | config history.keep_last_turns |
| blog | 40 | `650` | persona tokens on strong model = 652 (rounded to 10) |
| blog | 40 | `170` | tight prompt tokens on strong model = 170 (rounded to 10) |
| blog | 40 | `170` | tight prompt tokens on strong model = 170 (rounded to 10) |
| blog | 49 | `4.5` | model name: Claude Haiku 4.5 |
| blog | 50 | `5.5` | model name: Claude Sonnet 5.5 |
| blog | 51 | `3` | config retrieval.top_k |
| blog | 51 | `2` | config history.keep_last_turns |
| blog | 60 | `140` | 100 queries + conversation turns (data files) |
| blog | 62 | `1` | quality scale bottom (rubric) |
| blog | 62 | `$1.95` | summary.csv v1_naive total_cost_usd |
| blog | 62 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| blog | 63 | `$1.75` | summary.csv plus_route total_cost_usd |
| blog | 63 | `4.56` | summary.csv plus_route mean_quality; summary.csv plus_route mean_quality |
| blog | 64 | `$1.12` | summary.csv plus_retrieve total_cost_usd; summary.csv plus_trim total_cost_usd |
| blog | 64 | `4.34` | summary.csv plus_retrieve mean_quality; summary.csv plus_retrieve mean_quality |
| blog | 65 | `$1.12` | summary.csv plus_retrieve total_cost_usd; summary.csv plus_trim total_cost_usd |
| blog | 65 | `4.39` | summary.csv plus_trim mean_quality |
| blog | 66 | `$0.91` | summary.csv plus_tight_cache total_cost_usd |
| blog | 66 | `4.40` | summary.csv plus_tight_cache mean_quality |
| blog | 67 | `2` | config history.keep_last_turns |
| blog | 67 | `$0.69` | summary.csv v2_full total_cost_usd |
| blog | 67 | `4.49` | summary.csv v2_full mean_quality |
| blog | 69 | `9` | kb.md sections (retriever chunks) |
| blog | 69 | `3` | config retrieval.top_k |
| blog | 69 | `$0.63` | retrieval step: plus_route - plus_retrieve cost |
| blog | 69 | `$1.26` | total saving v1 - v2 |
| blog | 69 | `14` | per_answer_eval: answers dropping >=2 from plus_route to plus_retrieve |
| blog | 71 | `0.5%` | trim step / v1 cost |
| blog | 71 | `1` | quality scale bottom (rubric) |
| blog | 71 | `203` | calls_eval v2_full Sonnet static_prefix_tokens |
| blog | 71 | `512` | config cache.min_tokens strong |
| blog | 73 | `4.80` | summary.csv cache_full_kb mean_quality |
| blog | 73 | `1` | quality scale bottom (rubric) |
| blog | 73 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| blog | 73 | `62%` | 1 - cache_full_kb/v1 cost |
| blog | 73 | `1` | quality scale bottom (rubric) |
| blog | 73 | `20` | per_answer_eval: answers improving >=2 v2_full -> cache_full_kb; judge_handcheck.md answers checked |
| blog | 79 | `12%` | routing_summary laya vs always_strong cost; router_head_summary zero-shot saving |
| blog | 79 | `4.60` | routing_summary laya mean_quality; effort_summary sonnet_low quality_complex |
| blog | 79 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| blog | 79 | `45` | routing_confusion laya simple->strong |
| blog | 79 | `62` | test_queries.csv label=simple |
| blog | 81 | `136` | llm_router tokens per query |
| blog | 81 | `1,176` | routing_summary llm_router p50_router_ms |
| blog | 81 | `194` | routing_summary laya p50_router_ms |
| blog | 83 | `270` | data/router_train.csv rows |
| blog | 83 | `12%` | routing_summary laya vs always_strong cost; router_head_summary zero-shot saving |
| blog | 83 | `20%` | router_head_summary laya_head saving |
| blog | 83 | `4.54` | router_head_summary laya_head quality |
| blog | 83 | `38%` | router_head_summary hindsight ceiling saving; router_head_summary hindsight_ceiling saving |
| blog | 85 | `4.42` | routing_summary always_cheap quality_simple |
| blog | 85 | `4.79` | routing_summary always_strong quality_simple |
| blog | 87 | `0.2` | rule fixed in eval/run_routing_eval.py (complex gap <= 0.2) |
| blog | 87 | `0.50` | threshold_sweep recommended |
| blog | 87 | `4.32` | threshold_sweep quality_complex at recommended |
| blog | 87 | `4.00` | threshold_sweep quality_complex at next threshold |
| blog | 91 | `50` | effort_summary sample size; effort sample size (config effort_eval.sample) |
| blog | 91 | `30` | effort sample: simple questions (config) |
| blog | 91 | `20` | per_answer_eval: answers improving >=2 v2_full -> cache_full_kb; judge_handcheck.md answers checked |
| blog | 93 | `50` | effort_summary sample size; effort sample size (config effort_eval.sample) |
| blog | 95 | `$0.264` | effort_summary always_strong total_cost_usd |
| blog | 95 | `0` | effort_summary thinking-off thinking_tokens |
| blog | 95 | `4.62` | effort_summary always_strong mean_quality; effort_summary sonnet_medium mean_quality |
| blog | 95 | `4.45` | effort_summary always_strong quality_complex |
| blog | 95 | `2.5` | effort_summary always_strong p50 latency (s) |
| blog | 96 | `$0.241` | effort_summary sonnet_low total_cost_usd |
| blog | 96 | `1,683` | effort_summary sonnet_low thinking_tokens |
| blog | 96 | `4.66` | effort_summary sonnet_low mean_quality; effort_summary sonnet_high mean_quality |
| blog | 96 | `4.60` | routing_summary laya mean_quality; effort_summary sonnet_low quality_complex |
| blog | 96 | `2.3` | effort_summary sonnet_low p50 latency (s) |
| blog | 97 | `$0.259` | effort_summary sonnet_medium total_cost_usd |
| blog | 97 | `3,433` | effort_summary sonnet_medium thinking_tokens |
| blog | 97 | `4.62` | effort_summary always_strong mean_quality; effort_summary sonnet_medium mean_quality |
| blog | 97 | `4.50` | effort_summary sonnet_medium quality_complex |
| blog | 97 | `2.6` | effort_summary sonnet_medium p50 latency (s) |
| blog | 98 | `$0.307` | effort_summary sonnet_high total_cost_usd |
| blog | 98 | `8,335` | effort_summary sonnet_high thinking_tokens |
| blog | 98 | `4.66` | effort_summary sonnet_low mean_quality; effort_summary sonnet_high mean_quality |
| blog | 98 | `4.65` | effort_summary sonnet_high quality_complex |
| blog | 98 | `3.5` | effort_summary sonnet_high p50 latency (s) |
| blog | 100 | `9%` | effort: low vs thinking off |
| blog | 100 | `28%` | effort: high vs low cost |
| blog | 102 | `26%` | effort_combo laya_head + sonnet_low saving |
| blog | 106 | `8%` | cache_full_kb vs v2_full cost |
| blog | 106 | `2` | config history.keep_last_turns |
| blog | 106 | `140` | 100 queries + conversation turns (data files) |
| blog | 106 | `1` | quality scale bottom (rubric) |
| blog | 106 | `$5,368` | cache_full_kb cost per answer x 1M |
| blog | 106 | `1` | quality scale bottom (rubric) |
| blog | 106 | `$13,946` | v1 cost per answer x 1M |
| blog | 125 | `78%` | variance.csv judge re-score identical share |
| blog | 125 | `17` | judge_handcheck.md AGREE count |
| blog | 125 | `20` | per_answer_eval: answers improving >=2 v2_full -> cache_full_kb; judge_handcheck.md answers checked |
| blog | 125 | `100` | test_queries.csv rows |
| blog | 125 | `0.1` | noise floor stated from judge variance (mean |diff| 0.23 per answer) |
| blog | 125 | `140` | 100 queries + conversation turns (data files) |
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
| web page | 12 | `3,600` | kb.md tokens on strong model = 3636 (QA gate 1), rounded to 100 |
| web page | 12 | `9` | kb.md sections (retriever chunks) |
| web page | 12 | `1` | quality scale bottom (rubric) |
| web page | 12 | `5.5` | model name: Claude Sonnet 5.5 |
| web page | 12 | `2` | config history.keep_last_turns |
| web page | 12 | `100` | test_queries.csv rows |
| web page | 12 | `62` | test_queries.csv label=simple |
| web page | 12 | `38` | test_queries.csv label=complex |
| web page | 12 | `10` | conversations.json |
| web page | 12 | `140` | 100 queries + conversation turns (data files) |
| web page | 12 | `5.5` | model name: Claude Sonnet 5.5 |
| web page | 12 | `$2` | config pricing claude-sonnet-5-5 input per MTok |
| web page | 12 | `$10` | config pricing claude-sonnet-5-5 output per MTok |
| web page | 12 | `4.5` | model name: Claude Haiku 4.5 |
| web page | 12 | `$1` | config pricing claude-haiku-4-5-20251001 input per MTok |
| web page | 12 | `$5` | config pricing claude-haiku-4-5-20251001 output per MTok |
| web page | 12 | `1` | quality scale bottom (rubric) |
| web page | 12 | `5` | quality scale top (rubric) |
| web page | 12 | `5` | quality scale top (rubric) |
| web page | 12 | `3` | config retrieval.top_k |
| web page | 14 | `64%` | 1 - v2_full/v1_naive total_cost_usd |
| web page | 14 | `140` | 100 queries + conversation turns (data files) |
| web page | 15 | `$1.95` | summary.csv v1_naive total_cost_usd |
| web page | 15 | `$0.69` | summary.csv v2_full total_cost_usd |
| web page | 15 | `66%` | 1 - v2/v1 (total_input_tokens + output_tokens) |
| web page | 16 | `$0.69` | summary.csv v2_full total_cost_usd |
| web page | 16 | `140` | 100 queries + conversation turns (data files) |
| web page | 16 | `$1.95` | summary.csv v1_naive total_cost_usd |
| web page | 17 | `66%` | 1 - v2/v1 (total_input_tokens + output_tokens) |
| web page | 18 | `4.49` | summary.csv v2_full mean_quality |
| web page | 18 | `5` | quality scale top (rubric) |
| web page | 18 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| web page | 19 | `20%` | router_head_summary laya_head saving |
| web page | 20 | `64%` | 1 - v2_full/v1_naive total_cost_usd |
| web page | 20 | `140` | 100 queries + conversation turns (data files) |
| web page | 20 | `$0.69` | summary.csv v2_full total_cost_usd |
| web page | 20 | `$1.95` | summary.csv v1_naive total_cost_usd |
| web page | 20 | `4.49` | summary.csv v2_full mean_quality |
| web page | 20 | `5` | quality scale top (rubric) |
| web page | 20 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| web page | 20 | `3` | config retrieval.top_k |
| web page | 20 | `62%` | 1 - cache_full_kb/v1 cost |
| web page | 20 | `4.80` | summary.csv cache_full_kb mean_quality |
| web page | 20 | `12%` | routing_summary laya vs always_strong cost; router_head_summary zero-shot saving |
| web page | 20 | `270` | data/router_train.csv rows |
| web page | 20 | `20%` | router_head_summary laya_head saving |
| web page | 20 | `28%` | effort: high vs low cost |
| web page | 26 | `2` | config history.keep_last_turns |
| web page | 36 | `3` | config retrieval.top_k |
| web page | 40 | `2` | config history.keep_last_turns |
| web page | 43 | `650` | persona tokens on strong model = 652 (rounded to 10) |
| web page | 43 | `170` | tight prompt tokens on strong model = 170 (rounded to 10) |
| web page | 44 | `170` | tight prompt tokens on strong model = 170 (rounded to 10) |
| web page | 61 | `4.5` | model name: Claude Haiku 4.5 |
| web page | 62 | `5.5` | model name: Claude Sonnet 5.5 |
| web page | 64 | `3` | config retrieval.top_k |
| web page | 64 | `2` | config history.keep_last_turns |
| web page | 76 | `140` | 100 queries + conversation turns (data files) |
| web page | 82 | `1` | quality scale bottom (rubric) |
| web page | 83 | `$1.95` | summary.csv v1_naive total_cost_usd |
| web page | 84 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| web page | 88 | `$1.75` | summary.csv plus_route total_cost_usd |
| web page | 89 | `4.56` | summary.csv plus_route mean_quality; summary.csv plus_route mean_quality |
| web page | 93 | `$1.12` | summary.csv plus_retrieve total_cost_usd; summary.csv plus_trim total_cost_usd |
| web page | 94 | `4.34` | summary.csv plus_retrieve mean_quality; summary.csv plus_retrieve mean_quality |
| web page | 98 | `$1.12` | summary.csv plus_retrieve total_cost_usd; summary.csv plus_trim total_cost_usd |
| web page | 99 | `4.39` | summary.csv plus_trim mean_quality |
| web page | 103 | `$0.91` | summary.csv plus_tight_cache total_cost_usd |
| web page | 104 | `4.40` | summary.csv plus_tight_cache mean_quality |
| web page | 107 | `2` | config history.keep_last_turns |
| web page | 108 | `$0.69` | summary.csv v2_full total_cost_usd |
| web page | 109 | `4.49` | summary.csv v2_full mean_quality |
| web page | 113 | `9` | kb.md sections (retriever chunks) |
| web page | 113 | `3` | config retrieval.top_k |
| web page | 113 | `$0.63` | retrieval step: plus_route - plus_retrieve cost |
| web page | 113 | `$1.26` | total saving v1 - v2 |
| web page | 113 | `14` | per_answer_eval: answers dropping >=2 from plus_route to plus_retrieve |
| web page | 114 | `0.5%` | trim step / v1 cost |
| web page | 114 | `1` | quality scale bottom (rubric) |
| web page | 114 | `203` | calls_eval v2_full Sonnet static_prefix_tokens |
| web page | 114 | `512` | config cache.min_tokens strong |
| web page | 115 | `4.80` | summary.csv cache_full_kb mean_quality |
| web page | 115 | `1` | quality scale bottom (rubric) |
| web page | 115 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| web page | 115 | `62%` | 1 - cache_full_kb/v1 cost |
| web page | 115 | `1` | quality scale bottom (rubric) |
| web page | 115 | `20` | per_answer_eval: answers improving >=2 v2_full -> cache_full_kb; judge_handcheck.md answers checked |
| web page | 115 | `140` | 100 queries + conversation turns (data files) |
| web page | 115 | `5` | quality scale top (rubric) |
| web page | 116 | `1` | quality scale bottom (rubric) |
| web page | 116 | `$1.95` | summary.csv v1_naive total_cost_usd |
| web page | 116 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| web page | 117 | `$1.75` | summary.csv plus_route total_cost_usd |
| web page | 117 | `4.56` | summary.csv plus_route mean_quality; summary.csv plus_route mean_quality |
| web page | 118 | `$1.12` | summary.csv plus_retrieve total_cost_usd; summary.csv plus_trim total_cost_usd |
| web page | 118 | `4.34` | summary.csv plus_retrieve mean_quality; summary.csv plus_retrieve mean_quality |
| web page | 119 | `$1.12` | summary.csv plus_retrieve total_cost_usd; summary.csv plus_trim total_cost_usd |
| web page | 119 | `4.39` | summary.csv plus_trim mean_quality |
| web page | 120 | `$0.91` | summary.csv plus_tight_cache total_cost_usd |
| web page | 120 | `4.40` | summary.csv plus_tight_cache mean_quality |
| web page | 121 | `2` | config history.keep_last_turns |
| web page | 121 | `$0.69` | summary.csv v2_full total_cost_usd |
| web page | 121 | `4.49` | summary.csv v2_full mean_quality |
| web page | 122 | `$0.75` | summary.csv cache_full_kb total_cost_usd |
| web page | 122 | `4.80` | summary.csv cache_full_kb mean_quality |
| web page | 124 | `12%` | routing_summary laya vs always_strong cost; router_head_summary zero-shot saving |
| web page | 124 | `4.60` | routing_summary laya mean_quality; effort_summary sonnet_low quality_complex |
| web page | 124 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| web page | 124 | `45` | routing_confusion laya simple->strong |
| web page | 124 | `62` | test_queries.csv label=simple |
| web page | 125 | `136` | llm_router tokens per query |
| web page | 125 | `1,176` | routing_summary llm_router p50_router_ms |
| web page | 125 | `194` | routing_summary laya p50_router_ms |
| web page | 126 | `270` | data/router_train.csv rows |
| web page | 126 | `12%` | routing_summary laya vs always_strong cost; router_head_summary zero-shot saving |
| web page | 126 | `20%` | router_head_summary laya_head saving |
| web page | 126 | `4.54` | router_head_summary laya_head quality |
| web page | 126 | `38%` | router_head_summary hindsight ceiling saving; router_head_summary hindsight_ceiling saving |
| web page | 127 | `4.42` | routing_summary always_cheap quality_simple |
| web page | 127 | `4.79` | routing_summary always_strong quality_simple |
| web page | 128 | `0.2` | rule fixed in eval/run_routing_eval.py (complex gap <= 0.2) |
| web page | 128 | `0.50` | threshold_sweep recommended |
| web page | 128 | `4.32` | threshold_sweep quality_complex at recommended |
| web page | 128 | `4.00` | threshold_sweep quality_complex at next threshold |
| web page | 128 | `100` | test_queries.csv rows |
| web page | 129 | `12%` | routing_summary laya vs always_strong cost; router_head_summary zero-shot saving |
| web page | 129 | `4.60` | routing_summary laya mean_quality; effort_summary sonnet_low quality_complex |
| web page | 130 | `13%` | router_head_summary length_rule saving |
| web page | 130 | `4.59` | router_head_summary length_rule quality |
| web page | 131 | `15%` | router_head_summary minilm_head saving |
| web page | 131 | `4.58` | router_head_summary minilm_head quality |
| web page | 132 | `20%` | router_head_summary laya_head saving |
| web page | 132 | `4.54` | router_head_summary laya_head quality |
| web page | 133 | `38%` | router_head_summary hindsight ceiling saving; router_head_summary hindsight_ceiling saving |
| web page | 133 | `4.68` | router_head_summary hindsight_ceiling quality |
| web page | 134 | `50` | effort_summary sample size; effort sample size (config effort_eval.sample) |
| web page | 134 | `30` | effort sample: simple questions (config) |
| web page | 134 | `20` | per_answer_eval: answers improving >=2 v2_full -> cache_full_kb; judge_handcheck.md answers checked |
| web page | 139 | `50` | effort_summary sample size; effort sample size (config effort_eval.sample) |
| web page | 149 | `$0.264` | effort_summary always_strong total_cost_usd |
| web page | 150 | `0` | effort_summary thinking-off thinking_tokens |
| web page | 151 | `4.62` | effort_summary always_strong mean_quality; effort_summary sonnet_medium mean_quality |
| web page | 152 | `4.45` | effort_summary always_strong quality_complex |
| web page | 153 | `2.5` | effort_summary always_strong p50 latency (s) |
| web page | 157 | `$0.241` | effort_summary sonnet_low total_cost_usd |
| web page | 158 | `1,683` | effort_summary sonnet_low thinking_tokens |
| web page | 159 | `4.66` | effort_summary sonnet_low mean_quality; effort_summary sonnet_high mean_quality |
| web page | 160 | `4.60` | routing_summary laya mean_quality; effort_summary sonnet_low quality_complex |
| web page | 161 | `2.3` | effort_summary sonnet_low p50 latency (s) |
| web page | 165 | `$0.259` | effort_summary sonnet_medium total_cost_usd |
| web page | 166 | `3,433` | effort_summary sonnet_medium thinking_tokens |
| web page | 167 | `4.62` | effort_summary always_strong mean_quality; effort_summary sonnet_medium mean_quality |
| web page | 168 | `4.50` | effort_summary sonnet_medium quality_complex |
| web page | 169 | `2.6` | effort_summary sonnet_medium p50 latency (s) |
| web page | 173 | `$0.307` | effort_summary sonnet_high total_cost_usd |
| web page | 174 | `8,335` | effort_summary sonnet_high thinking_tokens |
| web page | 175 | `4.66` | effort_summary sonnet_low mean_quality; effort_summary sonnet_high mean_quality |
| web page | 176 | `4.65` | effort_summary sonnet_high quality_complex |
| web page | 177 | `3.5` | effort_summary sonnet_high p50 latency (s) |
| web page | 181 | `9%` | effort: low vs thinking off |
| web page | 181 | `28%` | effort: high vs low cost |
| web page | 182 | `26%` | effort_combo laya_head + sonnet_low saving |
| web page | 182 | `50` | effort_summary sample size; effort sample size (config effort_eval.sample) |
| web page | 183 | `$0.264` | effort_summary always_strong total_cost_usd |
| web page | 183 | `4.62` | effort_summary always_strong mean_quality; effort_summary sonnet_medium mean_quality |
| web page | 184 | `$0.241` | effort_summary sonnet_low total_cost_usd |
| web page | 184 | `4.66` | effort_summary sonnet_low mean_quality; effort_summary sonnet_high mean_quality |
| web page | 185 | `$0.259` | effort_summary sonnet_medium total_cost_usd |
| web page | 185 | `4.62` | effort_summary always_strong mean_quality; effort_summary sonnet_medium mean_quality |
| web page | 186 | `$0.307` | effort_summary sonnet_high total_cost_usd |
| web page | 186 | `4.66` | effort_summary sonnet_low mean_quality; effort_summary sonnet_high mean_quality |
| web page | 187 | `1,683` | effort_summary sonnet_low thinking_tokens |
| web page | 187 | `8,335` | effort_summary sonnet_high thinking_tokens |
| web page | 187 | `8%` | cache_full_kb vs v2_full cost |
| web page | 187 | `2` | config history.keep_last_turns |
| web page | 187 | `140` | 100 queries + conversation turns (data files) |
| web page | 187 | `1` | quality scale bottom (rubric) |
| web page | 187 | `$5,368` | cache_full_kb cost per answer x 1M |
| web page | 187 | `1` | quality scale bottom (rubric) |
| web page | 187 | `$13,946` | v1 cost per answer x 1M |
| web page | 199 | `78%` | variance.csv judge re-score identical share |
| web page | 199 | `17` | judge_handcheck.md AGREE count |
| web page | 199 | `20` | per_answer_eval: answers improving >=2 v2_full -> cache_full_kb; judge_handcheck.md answers checked |
| web page | 199 | `100` | test_queries.csv rows |
| web page | 199 | `0.1` | noise floor stated from judge variance (mean |diff| 0.23 per answer) |
| web page | 199 | `140` | 100 queries + conversation turns (data files) |
