# Number-to-source table (blog + LinkedIn post)

| file | line | number | source |
|---|---|---|---|
| blog | 1 | `64%` | 1 - v2_full/v1_naive total_cost_usd |
| blog | 3 | `140` | 100 queries + conversation turns (data files) |
| blog | 9 | `3,600` | kb.md tokens on strong model = 3636 (QA gate 1), rounded to 100 |
| blog | 9 | `9` | kb.md sections (retriever chunks) |
| blog | 11 | `1` | quality scale bottom (rubric) |
| blog | 11 | `5.5` | model name: Claude Sonnet 5.5 |
| blog | 11 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points) |
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
| blog | 24 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
| blog | 25 | `28%` | effort: high vs low cost |
| blog | 35 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points) |
| blog | 38 | `3` | config retrieval.top_k |
| blog | 39 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points) |
| blog | 40 | `650` | persona tokens on strong model = 652 (rounded to 10) |
| blog | 40 | `170` | tight prompt tokens on strong model = 170 (rounded to 10) |
| blog | 40 | `170` | tight prompt tokens on strong model = 170 (rounded to 10) |
| blog | 49 | `4.5` | model name: Claude Haiku 4.5 |
| blog | 50 | `5.5` | model name: Claude Sonnet 5.5 |
| blog | 51 | `3` | config retrieval.top_k |
| blog | 51 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points) |
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
| blog | 67 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points) |
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
| blog | 83 | `0.2` | rule fixed in eval/run_routing_eval.py (complex gap <= 0.2) |
| blog | 83 | `0.50` | threshold_sweep recommended |
| blog | 83 | `4.32` | threshold_sweep quality_complex at recommended |
| blog | 83 | `4.00` | threshold_sweep quality_complex at next threshold |
| blog | 87 | `0.63` | router_head_summary laya_zero_shot@0.50 auc_haiku_ok |
| blog | 87 | `0.5` | AUC of a coin flip (definition) |
| blog | 87 | `1` | quality scale bottom (rubric) |
| blog | 91 | `270` | data/router_train.csv rows |
| blog | 92 | `37%` | router_head_qa train_haiku_ok_rate |
| blog | 94 | `100` | test_queries.csv rows |
| blog | 98 | `12%` | routing_summary laya vs always_strong cost; router_head_summary zero-shot saving |
| blog | 98 | `4.60` | routing_summary laya mean_quality; effort_summary sonnet_low quality_complex |
| blog | 98 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
| blog | 99 | `13%` | router_head_summary length_rule saving |
| blog | 99 | `4.59` | router_head_summary length_rule quality |
| blog | 99 | `23%` | router_head_summary length_rule share_to_haiku |
| blog | 100 | `15%` | router_head_summary minilm_head saving |
| blog | 100 | `4.58` | router_head_summary minilm_head quality |
| blog | 100 | `27%` | router_head_summary minilm_head share_to_haiku |
| blog | 101 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
| blog | 101 | `4.54` | router_head_summary laya_head quality |
| blog | 101 | `36%` | router_head_summary laya_head share_to_haiku |
| blog | 102 | `38%` | router_head_summary hindsight ceiling saving; router_head_summary hindsight_ceiling saving |
| blog | 102 | `4.68` | router_head_summary hindsight_ceiling quality |
| blog | 102 | `60%` | router_head_summary hindsight_ceiling share_to_haiku |
| blog | 104 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
| blog | 104 | `12%` | routing_summary laya vs always_strong cost; router_head_summary zero-shot saving |
| blog | 104 | `0.63` | router_head_summary laya_zero_shot@0.50 auc_haiku_ok |
| blog | 104 | `0.75` | router_head_summary laya_head auc_haiku_ok |
| blog | 104 | `2,000` | router_head_bootstrap resamples |
| blog | 104 | `1,991` | router_head_bootstrap resamples with extra saving > 0 |
| blog | 104 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points) |
| blog | 104 | `15` | router_head_bootstrap extra saving 95% CI high (points) |
| blog | 104 | `0.76` | router_head_summary length_rule auc_haiku_ok |
| blog | 104 | `13%` | router_head_summary length_rule saving |
| blog | 106 | `4.42` | routing_summary always_cheap quality_simple |
| blog | 106 | `4.79` | routing_summary always_strong quality_simple |
| blog | 106 | `38%` | router_head_summary hindsight ceiling saving; router_head_summary hindsight_ceiling saving |
| blog | 110 | `50` | effort_summary sample size; effort sample size (config effort_eval.sample) |
| blog | 110 | `30` | effort sample: simple questions (config) |
| blog | 110 | `20` | per_answer_eval: answers improving >=2 v2_full -> cache_full_kb; judge_handcheck.md answers checked |
| blog | 112 | `50` | effort_summary sample size; effort sample size (config effort_eval.sample) |
| blog | 114 | `$0.264` | effort_summary always_strong total_cost_usd |
| blog | 114 | `0` | effort_summary thinking-off thinking_tokens |
| blog | 114 | `4.62` | effort_summary always_strong mean_quality; effort_summary sonnet_medium mean_quality |
| blog | 114 | `4.45` | effort_summary always_strong quality_complex |
| blog | 114 | `2.5` | effort_summary always_strong p50 latency (s) |
| blog | 115 | `$0.241` | effort_summary sonnet_low total_cost_usd |
| blog | 115 | `1,683` | effort_summary sonnet_low thinking_tokens |
| blog | 115 | `4.66` | effort_summary sonnet_low mean_quality; effort_summary sonnet_high mean_quality |
| blog | 115 | `4.60` | routing_summary laya mean_quality; effort_summary sonnet_low quality_complex |
| blog | 115 | `2.3` | effort_summary sonnet_low p50 latency (s) |
| blog | 116 | `$0.259` | effort_summary sonnet_medium total_cost_usd |
| blog | 116 | `3,433` | effort_summary sonnet_medium thinking_tokens |
| blog | 116 | `4.62` | effort_summary always_strong mean_quality; effort_summary sonnet_medium mean_quality |
| blog | 116 | `4.50` | effort_summary sonnet_medium quality_complex |
| blog | 116 | `2.6` | effort_summary sonnet_medium p50 latency (s) |
| blog | 117 | `$0.307` | effort_summary sonnet_high total_cost_usd |
| blog | 117 | `8,335` | effort_summary sonnet_high thinking_tokens |
| blog | 117 | `4.66` | effort_summary sonnet_low mean_quality; effort_summary sonnet_high mean_quality |
| blog | 117 | `4.65` | effort_summary sonnet_high quality_complex |
| blog | 117 | `3.5` | effort_summary sonnet_high p50 latency (s) |
| blog | 119 | `9%` | effort: low vs thinking off |
| blog | 119 | `28%` | effort: high vs low cost |
| blog | 121 | `26%` | effort_combo laya_head + sonnet_low saving |
| blog | 125 | `8%` | cache_full_kb vs v2_full cost |
| blog | 125 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points) |
| blog | 125 | `140` | 100 queries + conversation turns (data files) |
| blog | 125 | `1` | quality scale bottom (rubric) |
| blog | 125 | `$5,368` | cache_full_kb cost per answer x 1M |
| blog | 125 | `1` | quality scale bottom (rubric) |
| blog | 125 | `$13,946` | v1 cost per answer x 1M |
| blog | 144 | `78%` | variance.csv judge re-score identical share |
| blog | 144 | `17` | judge_handcheck.md AGREE count |
| blog | 144 | `20` | per_answer_eval: answers improving >=2 v2_full -> cache_full_kb; judge_handcheck.md answers checked |
| blog | 144 | `100` | test_queries.csv rows |
| blog | 144 | `0.1` | noise floor stated from judge variance (mean |diff| 0.23 per answer) |
| blog | 144 | `140` | 100 queries + conversation turns (data files) |
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
| linkedin | 9 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
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
| web page | 12 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points) |
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
| web page | 19 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
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
| web page | 20 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
| web page | 20 | `28%` | effort: high vs low cost |
| web page | 26 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points) |
| web page | 36 | `3` | config retrieval.top_k |
| web page | 40 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points) |
| web page | 43 | `650` | persona tokens on strong model = 652 (rounded to 10) |
| web page | 43 | `170` | tight prompt tokens on strong model = 170 (rounded to 10) |
| web page | 44 | `170` | tight prompt tokens on strong model = 170 (rounded to 10) |
| web page | 61 | `4.5` | model name: Claude Haiku 4.5 |
| web page | 62 | `5.5` | model name: Claude Sonnet 5.5 |
| web page | 64 | `3` | config retrieval.top_k |
| web page | 64 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points) |
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
| web page | 107 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points) |
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
| web page | 121 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points) |
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
| web page | 126 | `0.2` | rule fixed in eval/run_routing_eval.py (complex gap <= 0.2) |
| web page | 126 | `0.50` | threshold_sweep recommended |
| web page | 126 | `4.32` | threshold_sweep quality_complex at recommended |
| web page | 126 | `4.00` | threshold_sweep quality_complex at next threshold |
| web page | 126 | `0.63` | router_head_summary laya_zero_shot@0.50 auc_haiku_ok |
| web page | 126 | `0.5` | AUC of a coin flip (definition) |
| web page | 126 | `1` | quality scale bottom (rubric) |
| web page | 129 | `270` | data/router_train.csv rows |
| web page | 130 | `37%` | router_head_qa train_haiku_ok_rate |
| web page | 132 | `100` | test_queries.csv rows |
| web page | 146 | `12%` | routing_summary laya vs always_strong cost; router_head_summary zero-shot saving |
| web page | 147 | `4.60` | routing_summary laya mean_quality; effort_summary sonnet_low quality_complex |
| web page | 148 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
| web page | 152 | `13%` | router_head_summary length_rule saving |
| web page | 153 | `4.59` | router_head_summary length_rule quality |
| web page | 154 | `23%` | router_head_summary length_rule share_to_haiku |
| web page | 158 | `15%` | router_head_summary minilm_head saving |
| web page | 159 | `4.58` | router_head_summary minilm_head quality |
| web page | 160 | `27%` | router_head_summary minilm_head share_to_haiku |
| web page | 164 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
| web page | 165 | `4.54` | router_head_summary laya_head quality |
| web page | 166 | `36%` | router_head_summary laya_head share_to_haiku |
| web page | 170 | `38%` | router_head_summary hindsight ceiling saving; router_head_summary hindsight_ceiling saving |
| web page | 171 | `4.68` | router_head_summary hindsight_ceiling quality |
| web page | 172 | `60%` | router_head_summary hindsight_ceiling share_to_haiku |
| web page | 176 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
| web page | 176 | `12%` | routing_summary laya vs always_strong cost; router_head_summary zero-shot saving |
| web page | 176 | `0.63` | router_head_summary laya_zero_shot@0.50 auc_haiku_ok |
| web page | 176 | `0.75` | router_head_summary laya_head auc_haiku_ok |
| web page | 176 | `2,000` | router_head_bootstrap resamples |
| web page | 176 | `1,991` | router_head_bootstrap resamples with extra saving > 0 |
| web page | 176 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points) |
| web page | 176 | `15` | router_head_bootstrap extra saving 95% CI high (points) |
| web page | 176 | `0.76` | router_head_summary length_rule auc_haiku_ok |
| web page | 176 | `13%` | router_head_summary length_rule saving |
| web page | 177 | `4.42` | routing_summary always_cheap quality_simple |
| web page | 177 | `4.79` | routing_summary always_strong quality_simple |
| web page | 177 | `38%` | router_head_summary hindsight ceiling saving; router_head_summary hindsight_ceiling saving |
| web page | 177 | `100` | test_queries.csv rows |
| web page | 178 | `12%` | routing_summary laya vs always_strong cost; router_head_summary zero-shot saving |
| web page | 178 | `4.60` | routing_summary laya mean_quality; effort_summary sonnet_low quality_complex |
| web page | 179 | `13%` | router_head_summary length_rule saving |
| web page | 179 | `4.59` | router_head_summary length_rule quality |
| web page | 180 | `15%` | router_head_summary minilm_head saving |
| web page | 180 | `4.58` | router_head_summary minilm_head quality |
| web page | 181 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
| web page | 181 | `4.54` | router_head_summary laya_head quality |
| web page | 182 | `38%` | router_head_summary hindsight ceiling saving; router_head_summary hindsight_ceiling saving |
| web page | 182 | `4.68` | router_head_summary hindsight_ceiling quality |
| web page | 183 | `50` | effort_summary sample size; effort sample size (config effort_eval.sample) |
| web page | 183 | `30` | effort sample: simple questions (config) |
| web page | 183 | `20` | per_answer_eval: answers improving >=2 v2_full -> cache_full_kb; judge_handcheck.md answers checked |
| web page | 188 | `50` | effort_summary sample size; effort sample size (config effort_eval.sample) |
| web page | 198 | `$0.264` | effort_summary always_strong total_cost_usd |
| web page | 199 | `0` | effort_summary thinking-off thinking_tokens |
| web page | 200 | `4.62` | effort_summary always_strong mean_quality; effort_summary sonnet_medium mean_quality |
| web page | 201 | `4.45` | effort_summary always_strong quality_complex |
| web page | 202 | `2.5` | effort_summary always_strong p50 latency (s) |
| web page | 206 | `$0.241` | effort_summary sonnet_low total_cost_usd |
| web page | 207 | `1,683` | effort_summary sonnet_low thinking_tokens |
| web page | 208 | `4.66` | effort_summary sonnet_low mean_quality; effort_summary sonnet_high mean_quality |
| web page | 209 | `4.60` | routing_summary laya mean_quality; effort_summary sonnet_low quality_complex |
| web page | 210 | `2.3` | effort_summary sonnet_low p50 latency (s) |
| web page | 214 | `$0.259` | effort_summary sonnet_medium total_cost_usd |
| web page | 215 | `3,433` | effort_summary sonnet_medium thinking_tokens |
| web page | 216 | `4.62` | effort_summary always_strong mean_quality; effort_summary sonnet_medium mean_quality |
| web page | 217 | `4.50` | effort_summary sonnet_medium quality_complex |
| web page | 218 | `2.6` | effort_summary sonnet_medium p50 latency (s) |
| web page | 222 | `$0.307` | effort_summary sonnet_high total_cost_usd |
| web page | 223 | `8,335` | effort_summary sonnet_high thinking_tokens |
| web page | 224 | `4.66` | effort_summary sonnet_low mean_quality; effort_summary sonnet_high mean_quality |
| web page | 225 | `4.65` | effort_summary sonnet_high quality_complex |
| web page | 226 | `3.5` | effort_summary sonnet_high p50 latency (s) |
| web page | 230 | `9%` | effort: low vs thinking off |
| web page | 230 | `28%` | effort: high vs low cost |
| web page | 231 | `26%` | effort_combo laya_head + sonnet_low saving |
| web page | 231 | `50` | effort_summary sample size; effort sample size (config effort_eval.sample) |
| web page | 232 | `$0.264` | effort_summary always_strong total_cost_usd |
| web page | 232 | `4.62` | effort_summary always_strong mean_quality; effort_summary sonnet_medium mean_quality |
| web page | 233 | `$0.241` | effort_summary sonnet_low total_cost_usd |
| web page | 233 | `4.66` | effort_summary sonnet_low mean_quality; effort_summary sonnet_high mean_quality |
| web page | 234 | `$0.259` | effort_summary sonnet_medium total_cost_usd |
| web page | 234 | `4.62` | effort_summary always_strong mean_quality; effort_summary sonnet_medium mean_quality |
| web page | 235 | `$0.307` | effort_summary sonnet_high total_cost_usd |
| web page | 235 | `4.66` | effort_summary sonnet_low mean_quality; effort_summary sonnet_high mean_quality |
| web page | 236 | `1,683` | effort_summary sonnet_low thinking_tokens |
| web page | 236 | `8,335` | effort_summary sonnet_high thinking_tokens |
| web page | 236 | `8%` | cache_full_kb vs v2_full cost |
| web page | 236 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points) |
| web page | 236 | `140` | 100 queries + conversation turns (data files) |
| web page | 236 | `1` | quality scale bottom (rubric) |
| web page | 236 | `$5,368` | cache_full_kb cost per answer x 1M |
| web page | 236 | `1` | quality scale bottom (rubric) |
| web page | 236 | `$13,946` | v1 cost per answer x 1M |
| web page | 248 | `78%` | variance.csv judge re-score identical share |
| web page | 248 | `17` | judge_handcheck.md AGREE count |
| web page | 248 | `20` | per_answer_eval: answers improving >=2 v2_full -> cache_full_kb; judge_handcheck.md answers checked |
| web page | 248 | `100` | test_queries.csv rows |
| web page | 248 | `0.1` | noise floor stated from judge variance (mean |diff| 0.23 per answer) |
| web page | 248 | `140` | 100 queries + conversation turns (data files) |
