# Number-to-source table (blog + LinkedIn post)

| file | line | number | source |
|---|---|---|---|
| blog | 1 | `64%` | 1 - v2_full/v1_naive total_cost_usd |
| blog | 3 | `140` | 100 queries + conversation turns (data files) |
| blog | 9 | `3,600` | kb.md tokens on strong model = 3636 (QA gate 1), rounded to 100 |
| blog | 9 | `9` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank; kb.md sections (retriever chunks) |
| blog | 11 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 11 | `5.5` | model name: Claude Sonnet 5.5 |
| blog | 11 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
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
| blog | 17 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 17 | `5` | quality scale top (rubric); config cache.ttl_seconds in minutes; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 17 | `5` | quality scale top (rubric); config cache.ttl_seconds in minutes; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 17 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 21 | `64%` | 1 - v2_full/v1_naive total_cost_usd |
| blog | 21 | `140` | 100 queries + conversation turns (data files) |
| blog | 21 | `$0.69` | summary.csv v2_full total_cost_usd |
| blog | 21 | `$1.95` | summary.csv v1_naive total_cost_usd |
| blog | 21 | `4.49` | summary.csv v2_full mean_quality |
| blog | 21 | `5` | quality scale top (rubric); config cache.ttl_seconds in minutes; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 21 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| blog | 22 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 23 | `62%` | 1 - cache_full_kb/v1 cost |
| blog | 23 | `4.80` | summary.csv cache_full_kb mean_quality |
| blog | 24 | `12%` | routing_summary laya vs always_strong cost; router_head_summary zero-shot saving |
| blog | 24 | `270` | data/router_train.csv rows |
| blog | 24 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
| blog | 25 | `28%` | effort: high vs low cost |
| blog | 35 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 38 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 39 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 40 | `650` | persona tokens on strong model = 652 (rounded to 10) |
| blog | 40 | `170` | tight prompt tokens on strong model = 170 (rounded to 10) |
| blog | 40 | `170` | tight prompt tokens on strong model = 170 (rounded to 10) |
| blog | 49 | `4.5` | model name: Claude Haiku 4.5 |
| blog | 50 | `5.5` | model name: Claude Sonnet 5.5 |
| blog | 51 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 51 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 60 | `140` | 100 queries + conversation turns (data files) |
| blog | 60 | `140` | 100 queries + conversation turns (data files) |
| blog | 62 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 62 | `$1.95` | summary.csv v1_naive total_cost_usd |
| blog | 62 | `700,263` | summary v1_naive total_input_tokens + output_tokens |
| blog | 62 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| blog | 63 | `$1.75` | summary.csv plus_route total_cost_usd |
| blog | 63 | `666,257` | summary plus_route total_input_tokens + output_tokens |
| blog | 63 | `4.56` | summary.csv plus_route mean_quality; summary.csv plus_route mean_quality |
| blog | 64 | `$1.12` | summary.csv plus_retrieve total_cost_usd; summary.csv plus_trim total_cost_usd |
| blog | 64 | `340,018` | summary plus_retrieve total_input_tokens + output_tokens |
| blog | 64 | `4.34` | summary.csv plus_retrieve mean_quality; summary.csv plus_retrieve mean_quality |
| blog | 65 | `$1.12` | summary.csv plus_retrieve total_cost_usd; summary.csv plus_trim total_cost_usd |
| blog | 65 | `340,217` | summary plus_trim total_input_tokens + output_tokens |
| blog | 65 | `4.39` | summary.csv plus_trim mean_quality |
| blog | 66 | `$0.91` | summary.csv plus_tight_cache total_cost_usd |
| blog | 66 | `264,266` | summary plus_tight_cache total_input_tokens + output_tokens |
| blog | 66 | `4.40` | summary.csv plus_tight_cache mean_quality |
| blog | 67 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 67 | `$0.69` | summary.csv v2_full total_cost_usd |
| blog | 67 | `239,713` | summary v2_full total_input_tokens + output_tokens |
| blog | 67 | `4.49` | summary.csv v2_full mean_quality |
| blog | 71 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 71 | `9` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank; kb.md sections (retriever chunks) |
| blog | 71 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 71 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 73 | `$0.63` | retrieval step: plus_route - plus_retrieve cost |
| blog | 73 | `$1.26` | total saving v1 - v2 |
| blog | 75 | `5` | quality scale top (rubric); config cache.ttl_seconds in minutes; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 75 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 75 | `14` | per_answer_eval: answers dropping >=2 from plus_route to plus_retrieve |
| blog | 75 | `140` | 100 queries + conversation turns (data files) |
| blog | 77 | `0.5%` | trim step / v1 cost |
| blog | 77 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 77 | `203` | calls_eval v2_full Sonnet static_prefix_tokens |
| blog | 77 | `512` | config cache.min_tokens strong |
| blog | 79 | `66%` | 1 - v2/v1 (total_input_tokens + output_tokens) |
| blog | 79 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 79 | `5%` | routing step token reduction (plus_route vs v1_naive) |
| blog | 79 | `199` | tokens added by history trimming (plus_trim - plus_retrieve) |
| blog | 81 | `4.80` | summary.csv cache_full_kb mean_quality |
| blog | 81 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 81 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| blog | 81 | `62%` | 1 - cache_full_kb/v1 cost |
| blog | 81 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 83 | `140` | 100 queries + conversation turns (data files) |
| blog | 83 | `140` | 100 queries + conversation turns (data files) |
| blog | 85 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 85 | `$0.91` | summary.csv plus_tight_cache total_cost_usd |
| blog | 85 | `264,266` | summary plus_tight_cache total_input_tokens + output_tokens |
| blog | 85 | `4.40` | summary.csv plus_tight_cache mean_quality |
| blog | 86 | `$0.75` | summary.csv cache_full_kb total_cost_usd |
| blog | 86 | `588,461` | summary cache_full_kb total_input_tokens + output_tokens |
| blog | 86 | `4.80` | summary.csv cache_full_kb mean_quality |
| blog | 88 | `17%` | cache_full_kb vs plus_tight_cache cost (same setup, RAG vs cache) |
| blog | 88 | `20` | per_answer_eval: answers improving >=2 v2_full -> cache_full_kb; judge_handcheck.md answers checked |
| blog | 90 | `5` | quality scale top (rubric); config cache.ttl_seconds in minutes; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 96 | `9` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank; kb.md sections (retriever chunks) |
| blog | 98 | `384` | MiniLM embedding dimensions |
| blog | 99 | `9` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank; kb.md sections (retriever chunks) |
| blog | 99 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 99 | `60` | config retrieval.rrf_k (fusion constant) |
| blog | 99 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 99 | `60` | config retrieval.rrf_k (fusion constant) |
| blog | 100 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 102 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 106 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 106 | `74%` | retrieval_recall right section found at k=1 |
| blog | 106 | `11%` | retrieval_recall share of manual sent at k=1 |
| blog | 107 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 107 | `89%` | retrieval_recall right section found at k=2 |
| blog | 107 | `22%` | retrieval_recall share of manual sent at k=2 |
| blog | 108 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 108 | `95%` | retrieval_recall right section found at k=3 |
| blog | 108 | `33%` | retrieval_recall share of manual sent at k=3 |
| blog | 109 | `4` | retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 109 | `96%` | retrieval_recall right section found at k=4 |
| blog | 109 | `44%` | retrieval_recall share of manual sent at k=4 |
| blog | 110 | `5` | quality scale top (rubric); config cache.ttl_seconds in minutes; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 110 | `97%` | retrieval_recall right section found at k=5 |
| blog | 110 | `56%` | retrieval_recall share of manual sent at k=5 |
| blog | 112 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 112 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 112 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 118 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 118 | `4` | retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 118 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 119 | `4` | retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 119 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 119 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 120 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 120 | `5` | quality scale top (rubric); config cache.ttl_seconds in minutes; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 120 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 121 | `5` | quality scale top (rubric); config cache.ttl_seconds in minutes; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 121 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 121 | `4` | retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 122 | `8` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 122 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 122 | `5` | quality scale top (rubric); config cache.ttl_seconds in minutes; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 123 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 123 | `7` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 123 | `6` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 125 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 125 | `7` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 125 | `6` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 133 | `12%` | routing_summary laya vs always_strong cost; router_head_summary zero-shot saving |
| blog | 133 | `4.60` | routing_summary laya mean_quality; effort_summary sonnet_low quality_complex |
| blog | 133 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| blog | 133 | `45` | routing_confusion laya simple->strong |
| blog | 133 | `62` | test_queries.csv label=simple |
| blog | 135 | `136` | llm_router tokens per query |
| blog | 135 | `1,176` | routing_summary llm_router p50_router_ms |
| blog | 135 | `194` | routing_summary laya p50_router_ms |
| blog | 137 | `0.2` | rule fixed in eval/run_routing_eval.py (complex gap <= 0.2) |
| blog | 137 | `0.50` | threshold_sweep recommended |
| blog | 137 | `4.32` | threshold_sweep quality_complex at recommended |
| blog | 137 | `4.00` | threshold_sweep quality_complex at next threshold |
| blog | 141 | `0.63` | router_head_summary laya_zero_shot@0.50 auc_haiku_ok |
| blog | 141 | `0.5` | AUC of a coin flip (definition) |
| blog | 141 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 145 | `270` | data/router_train.csv rows |
| blog | 146 | `37%` | router_head_qa train_haiku_ok_rate |
| blog | 148 | `100` | test_queries.csv rows |
| blog | 150 | `5` | quality scale top (rubric); config cache.ttl_seconds in minutes; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 150 | `100` | test_queries.csv rows |
| blog | 154 | `12%` | routing_summary laya vs always_strong cost; router_head_summary zero-shot saving |
| blog | 154 | `4.60` | routing_summary laya mean_quality; effort_summary sonnet_low quality_complex |
| blog | 154 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
| blog | 155 | `13%` | router_head_summary length_rule saving |
| blog | 155 | `4.59` | router_head_summary length_rule quality |
| blog | 155 | `23%` | router_head_summary length_rule share_to_haiku |
| blog | 156 | `15%` | router_head_summary minilm_head saving |
| blog | 156 | `4.58` | router_head_summary minilm_head quality |
| blog | 156 | `27%` | router_head_summary minilm_head share_to_haiku |
| blog | 157 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
| blog | 157 | `4.54` | router_head_summary laya_head quality |
| blog | 157 | `36%` | router_head_summary laya_head share_to_haiku |
| blog | 158 | `38%` | router_head_summary hindsight ceiling saving; router_head_summary hindsight_ceiling saving |
| blog | 158 | `4.68` | router_head_summary hindsight_ceiling quality |
| blog | 158 | `60%` | router_head_summary hindsight_ceiling share_to_haiku |
| blog | 160 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
| blog | 160 | `100` | test_queries.csv rows |
| blog | 160 | `$0.517` | router_head_summary always_sonnet cost_usd (100 test questions) |
| blog | 160 | `$0.415` | router_head_summary laya_head cost_usd (100 test questions) |
| blog | 160 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
| blog | 160 | `36%` | router_head_summary laya_head share_to_haiku |
| blog | 160 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
| blog | 160 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| blog | 160 | `4.54` | router_head_summary laya_head quality |
| blog | 160 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 162 | `60%` | router_head_summary hindsight_ceiling share_to_haiku |
| blog | 162 | `38%` | router_head_summary hindsight ceiling saving; router_head_summary hindsight_ceiling saving |
| blog | 162 | `4.68` | router_head_summary hindsight_ceiling quality |
| blog | 164 | `0.63` | router_head_summary laya_zero_shot@0.50 auc_haiku_ok |
| blog | 164 | `0.75` | router_head_summary laya_head auc_haiku_ok |
| blog | 164 | `2,000` | router_head_bootstrap resamples |
| blog | 164 | `1,991` | router_head_bootstrap resamples with extra saving > 0 |
| blog | 164 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 164 | `15` | router_head_bootstrap extra saving 95% CI high (points) |
| blog | 164 | `0.76` | router_head_summary length_rule auc_haiku_ok |
| blog | 164 | `13%` | router_head_summary length_rule saving |
| blog | 166 | `4.42` | routing_summary always_cheap quality_simple |
| blog | 166 | `4.79` | routing_summary always_strong quality_simple |
| blog | 166 | `38%` | router_head_summary hindsight ceiling saving; router_head_summary hindsight_ceiling saving |
| blog | 170 | `5.5` | model name: Claude Sonnet 5.5 |
| blog | 170 | `4.5` | model name: Claude Haiku 4.5 |
| blog | 170 | `50` | effort_summary sample size; effort sample size (config effort_eval.sample) |
| blog | 170 | `30` | effort sample: simple questions (config) |
| blog | 170 | `20` | per_answer_eval: answers improving >=2 v2_full -> cache_full_kb; judge_handcheck.md answers checked |
| blog | 172 | `5.5` | model name: Claude Sonnet 5.5 |
| blog | 172 | `50` | effort_summary sample size; effort sample size (config effort_eval.sample) |
| blog | 174 | `$0.264` | effort_summary always_strong total_cost_usd |
| blog | 174 | `0` | effort_summary thinking-off thinking_tokens |
| blog | 174 | `4.62` | effort_summary always_strong mean_quality; effort_summary sonnet_medium mean_quality |
| blog | 174 | `4.45` | effort_summary always_strong quality_complex |
| blog | 174 | `2.5` | effort_summary always_strong p50 latency (s) |
| blog | 175 | `$0.241` | effort_summary sonnet_low total_cost_usd |
| blog | 175 | `1,683` | effort_summary sonnet_low thinking_tokens |
| blog | 175 | `4.66` | effort_summary sonnet_low mean_quality; effort_summary sonnet_high mean_quality |
| blog | 175 | `4.60` | routing_summary laya mean_quality; effort_summary sonnet_low quality_complex |
| blog | 175 | `2.3` | effort_summary sonnet_low p50 latency (s) |
| blog | 176 | `$0.259` | effort_summary sonnet_medium total_cost_usd |
| blog | 176 | `3,433` | effort_summary sonnet_medium thinking_tokens |
| blog | 176 | `4.62` | effort_summary always_strong mean_quality; effort_summary sonnet_medium mean_quality |
| blog | 176 | `4.50` | effort_summary sonnet_medium quality_complex |
| blog | 176 | `2.6` | effort_summary sonnet_medium p50 latency (s) |
| blog | 177 | `$0.307` | effort_summary sonnet_high total_cost_usd |
| blog | 177 | `8,335` | effort_summary sonnet_high thinking_tokens |
| blog | 177 | `4.66` | effort_summary sonnet_low mean_quality; effort_summary sonnet_high mean_quality |
| blog | 177 | `4.65` | effort_summary sonnet_high quality_complex |
| blog | 177 | `3.5` | effort_summary sonnet_high p50 latency (s) |
| blog | 179 | `9%` | effort: low vs thinking off |
| blog | 179 | `28%` | effort: high vs low cost |
| blog | 181 | `26%` | effort_combo laya_head + sonnet_low saving |
| blog | 185 | `8%` | cache_full_kb vs v2_full cost |
| blog | 185 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 185 | `140` | 100 queries + conversation turns (data files) |
| blog | 185 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 185 | `$5,368` | cache_full_kb cost per answer x 1M |
| blog | 185 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 185 | `$13,946` | v1 cost per answer x 1M |
| blog | 203 | `78%` | variance.csv judge re-score identical share |
| blog | 203 | `17` | judge_handcheck.md AGREE count |
| blog | 203 | `20` | per_answer_eval: answers improving >=2 v2_full -> cache_full_kb; judge_handcheck.md answers checked |
| blog | 203 | `100` | test_queries.csv rows |
| blog | 203 | `0.1` | noise floor stated from judge variance (mean |diff| 0.23 per answer) |
| blog | 203 | `140` | 100 queries + conversation turns (data files) |
| linkedin | 5 | `140` | 100 queries + conversation turns (data files) |
| linkedin | 9 | `$1.95` | summary.csv v1_naive total_cost_usd |
| linkedin | 9 | `$0.69` | summary.csv v2_full total_cost_usd |
| linkedin | 9 | `64%` | 1 - v2_full/v1_naive total_cost_usd |
| linkedin | 9 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| linkedin | 9 | `4.49` | summary.csv v2_full mean_quality |
| linkedin | 9 | `5` | quality scale top (rubric); config cache.ttl_seconds in minutes; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| linkedin | 11 | `12%` | routing_summary laya vs always_strong cost; router_head_summary zero-shot saving |
| linkedin | 11 | `270` | data/router_train.csv rows |
| linkedin | 11 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
| linkedin | 13 | `62%` | 1 - cache_full_kb/v1 cost |
| web page | 5 | `140` | 100 queries + conversation turns (data files) |
| web page | 6 | `64%` | 1 - v2_full/v1_naive total_cost_usd |
| web page | 9 | `5.5` | model name: Claude Sonnet 5.5 |
| web page | 9 | `4.5` | model name: Claude Haiku 4.5 |
| web page | 10 | `2026` | publication year (byline) |
| web page | 13 | `3,600` | kb.md tokens on strong model = 3636 (QA gate 1), rounded to 100 |
| web page | 13 | `9` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank; kb.md sections (retriever chunks) |
| web page | 13 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 13 | `5.5` | model name: Claude Sonnet 5.5 |
| web page | 13 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 13 | `100` | test_queries.csv rows |
| web page | 13 | `62` | test_queries.csv label=simple |
| web page | 13 | `38` | test_queries.csv label=complex |
| web page | 13 | `10` | conversations.json |
| web page | 13 | `140` | 100 queries + conversation turns (data files) |
| web page | 13 | `5.5` | model name: Claude Sonnet 5.5 |
| web page | 13 | `$2` | config pricing claude-sonnet-5-5 input per MTok |
| web page | 13 | `$10` | config pricing claude-sonnet-5-5 output per MTok |
| web page | 13 | `4.5` | model name: Claude Haiku 4.5 |
| web page | 13 | `$1` | config pricing claude-haiku-4-5-20251001 input per MTok |
| web page | 13 | `$5` | config pricing claude-haiku-4-5-20251001 output per MTok |
| web page | 13 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 13 | `5` | quality scale top (rubric); config cache.ttl_seconds in minutes; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 13 | `5` | quality scale top (rubric); config cache.ttl_seconds in minutes; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 13 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 15 | `64%` | 1 - v2_full/v1_naive total_cost_usd |
| web page | 15 | `140` | 100 queries + conversation turns (data files) |
| web page | 16 | `$1.95` | summary.csv v1_naive total_cost_usd |
| web page | 16 | `$0.69` | summary.csv v2_full total_cost_usd |
| web page | 16 | `66%` | 1 - v2/v1 (total_input_tokens + output_tokens) |
| web page | 17 | `$0.69` | summary.csv v2_full total_cost_usd |
| web page | 17 | `140` | 100 queries + conversation turns (data files) |
| web page | 17 | `$1.95` | summary.csv v1_naive total_cost_usd |
| web page | 18 | `66%` | 1 - v2/v1 (total_input_tokens + output_tokens) |
| web page | 19 | `4.49` | summary.csv v2_full mean_quality |
| web page | 19 | `5` | quality scale top (rubric); config cache.ttl_seconds in minutes; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 19 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| web page | 20 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
| web page | 21 | `64%` | 1 - v2_full/v1_naive total_cost_usd |
| web page | 21 | `140` | 100 queries + conversation turns (data files) |
| web page | 21 | `$0.69` | summary.csv v2_full total_cost_usd |
| web page | 21 | `$1.95` | summary.csv v1_naive total_cost_usd |
| web page | 21 | `4.49` | summary.csv v2_full mean_quality |
| web page | 21 | `5` | quality scale top (rubric); config cache.ttl_seconds in minutes; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 21 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| web page | 21 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 21 | `62%` | 1 - cache_full_kb/v1 cost |
| web page | 21 | `4.80` | summary.csv cache_full_kb mean_quality |
| web page | 21 | `12%` | routing_summary laya vs always_strong cost; router_head_summary zero-shot saving |
| web page | 21 | `270` | data/router_train.csv rows |
| web page | 21 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
| web page | 21 | `28%` | effort: high vs low cost |
| web page | 27 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 37 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 41 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 44 | `650` | persona tokens on strong model = 652 (rounded to 10) |
| web page | 44 | `170` | tight prompt tokens on strong model = 170 (rounded to 10) |
| web page | 45 | `170` | tight prompt tokens on strong model = 170 (rounded to 10) |
| web page | 62 | `4.5` | model name: Claude Haiku 4.5 |
| web page | 63 | `5.5` | model name: Claude Sonnet 5.5 |
| web page | 65 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 65 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 77 | `140` | 100 queries + conversation turns (data files) |
| web page | 78 | `140` | 100 queries + conversation turns (data files) |
| web page | 84 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 85 | `$1.95` | summary.csv v1_naive total_cost_usd |
| web page | 86 | `700,263` | summary v1_naive total_input_tokens + output_tokens |
| web page | 87 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| web page | 91 | `$1.75` | summary.csv plus_route total_cost_usd |
| web page | 92 | `666,257` | summary plus_route total_input_tokens + output_tokens |
| web page | 93 | `4.56` | summary.csv plus_route mean_quality; summary.csv plus_route mean_quality |
| web page | 97 | `$1.12` | summary.csv plus_retrieve total_cost_usd; summary.csv plus_trim total_cost_usd |
| web page | 98 | `340,018` | summary plus_retrieve total_input_tokens + output_tokens |
| web page | 99 | `4.34` | summary.csv plus_retrieve mean_quality; summary.csv plus_retrieve mean_quality |
| web page | 103 | `$1.12` | summary.csv plus_retrieve total_cost_usd; summary.csv plus_trim total_cost_usd |
| web page | 104 | `340,217` | summary plus_trim total_input_tokens + output_tokens |
| web page | 105 | `4.39` | summary.csv plus_trim mean_quality |
| web page | 109 | `$0.91` | summary.csv plus_tight_cache total_cost_usd |
| web page | 110 | `264,266` | summary plus_tight_cache total_input_tokens + output_tokens |
| web page | 111 | `4.40` | summary.csv plus_tight_cache mean_quality |
| web page | 114 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 115 | `$0.69` | summary.csv v2_full total_cost_usd |
| web page | 116 | `239,713` | summary v2_full total_input_tokens + output_tokens |
| web page | 117 | `4.49` | summary.csv v2_full mean_quality |
| web page | 122 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 122 | `9` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank; kb.md sections (retriever chunks) |
| web page | 122 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 122 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 123 | `$0.63` | retrieval step: plus_route - plus_retrieve cost |
| web page | 123 | `$1.26` | total saving v1 - v2 |
| web page | 124 | `5` | quality scale top (rubric); config cache.ttl_seconds in minutes; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 124 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 124 | `14` | per_answer_eval: answers dropping >=2 from plus_route to plus_retrieve |
| web page | 124 | `140` | 100 queries + conversation turns (data files) |
| web page | 125 | `0.5%` | trim step / v1 cost |
| web page | 125 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 125 | `203` | calls_eval v2_full Sonnet static_prefix_tokens |
| web page | 125 | `512` | config cache.min_tokens strong |
| web page | 126 | `66%` | 1 - v2/v1 (total_input_tokens + output_tokens) |
| web page | 126 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 126 | `5%` | routing step token reduction (plus_route vs v1_naive) |
| web page | 126 | `199` | tokens added by history trimming (plus_trim - plus_retrieve) |
| web page | 127 | `4.80` | summary.csv cache_full_kb mean_quality |
| web page | 127 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 127 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| web page | 127 | `62%` | 1 - cache_full_kb/v1 cost |
| web page | 127 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 132 | `140` | 100 queries + conversation turns (data files) |
| web page | 133 | `140` | 100 queries + conversation turns (data files) |
| web page | 139 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 140 | `$0.91` | summary.csv plus_tight_cache total_cost_usd |
| web page | 141 | `264,266` | summary plus_tight_cache total_input_tokens + output_tokens |
| web page | 142 | `4.40` | summary.csv plus_tight_cache mean_quality |
| web page | 146 | `$0.75` | summary.csv cache_full_kb total_cost_usd |
| web page | 147 | `588,461` | summary cache_full_kb total_input_tokens + output_tokens |
| web page | 148 | `4.80` | summary.csv cache_full_kb mean_quality |
| web page | 152 | `17%` | cache_full_kb vs plus_tight_cache cost (same setup, RAG vs cache) |
| web page | 152 | `20` | per_answer_eval: answers improving >=2 v2_full -> cache_full_kb; judge_handcheck.md answers checked |
| web page | 153 | `5` | quality scale top (rubric); config cache.ttl_seconds in minutes; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 153 | `140` | 100 queries + conversation turns (data files) |
| web page | 153 | `5` | quality scale top (rubric); config cache.ttl_seconds in minutes; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 154 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 154 | `$1.95` | summary.csv v1_naive total_cost_usd |
| web page | 154 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| web page | 155 | `$1.75` | summary.csv plus_route total_cost_usd |
| web page | 155 | `4.56` | summary.csv plus_route mean_quality; summary.csv plus_route mean_quality |
| web page | 156 | `$1.12` | summary.csv plus_retrieve total_cost_usd; summary.csv plus_trim total_cost_usd |
| web page | 156 | `4.34` | summary.csv plus_retrieve mean_quality; summary.csv plus_retrieve mean_quality |
| web page | 157 | `$1.12` | summary.csv plus_retrieve total_cost_usd; summary.csv plus_trim total_cost_usd |
| web page | 157 | `4.39` | summary.csv plus_trim mean_quality |
| web page | 158 | `$0.91` | summary.csv plus_tight_cache total_cost_usd |
| web page | 158 | `4.40` | summary.csv plus_tight_cache mean_quality |
| web page | 159 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 159 | `$0.69` | summary.csv v2_full total_cost_usd |
| web page | 159 | `4.49` | summary.csv v2_full mean_quality |
| web page | 160 | `$0.75` | summary.csv cache_full_kb total_cost_usd |
| web page | 160 | `4.80` | summary.csv cache_full_kb mean_quality |
| web page | 163 | `9` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank; kb.md sections (retriever chunks) |
| web page | 165 | `384` | MiniLM embedding dimensions |
| web page | 166 | `9` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank; kb.md sections (retriever chunks) |
| web page | 166 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 166 | `60` | config retrieval.rrf_k (fusion constant) |
| web page | 166 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 166 | `60` | config retrieval.rrf_k (fusion constant) |
| web page | 167 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 169 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 180 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 181 | `74%` | retrieval_recall right section found at k=1 |
| web page | 182 | `11%` | retrieval_recall share of manual sent at k=1 |
| web page | 185 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 186 | `89%` | retrieval_recall right section found at k=2 |
| web page | 187 | `22%` | retrieval_recall share of manual sent at k=2 |
| web page | 190 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 191 | `95%` | retrieval_recall right section found at k=3 |
| web page | 192 | `33%` | retrieval_recall share of manual sent at k=3 |
| web page | 195 | `4` | retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 196 | `96%` | retrieval_recall right section found at k=4 |
| web page | 197 | `44%` | retrieval_recall share of manual sent at k=4 |
| web page | 200 | `5` | quality scale top (rubric); config cache.ttl_seconds in minutes; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 201 | `97%` | retrieval_recall right section found at k=5 |
| web page | 202 | `56%` | retrieval_recall share of manual sent at k=5 |
| web page | 206 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 206 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 206 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 220 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 221 | `4` | retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 222 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 226 | `4` | retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 227 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 228 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 232 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 233 | `5` | quality scale top (rubric); config cache.ttl_seconds in minutes; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 234 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 238 | `5` | quality scale top (rubric); config cache.ttl_seconds in minutes; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 239 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 240 | `4` | retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 244 | `8` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 245 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 246 | `5` | quality scale top (rubric); config cache.ttl_seconds in minutes; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 250 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 251 | `7` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 252 | `6` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 256 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 256 | `7` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 256 | `6` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 258 | `12%` | routing_summary laya vs always_strong cost; router_head_summary zero-shot saving |
| web page | 258 | `4.60` | routing_summary laya mean_quality; effort_summary sonnet_low quality_complex |
| web page | 258 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| web page | 258 | `45` | routing_confusion laya simple->strong |
| web page | 258 | `62` | test_queries.csv label=simple |
| web page | 259 | `136` | llm_router tokens per query |
| web page | 259 | `1,176` | routing_summary llm_router p50_router_ms |
| web page | 259 | `194` | routing_summary laya p50_router_ms |
| web page | 260 | `0.2` | rule fixed in eval/run_routing_eval.py (complex gap <= 0.2) |
| web page | 260 | `0.50` | threshold_sweep recommended |
| web page | 260 | `4.32` | threshold_sweep quality_complex at recommended |
| web page | 260 | `4.00` | threshold_sweep quality_complex at next threshold |
| web page | 260 | `0.63` | router_head_summary laya_zero_shot@0.50 auc_haiku_ok |
| web page | 260 | `0.5` | AUC of a coin flip (definition) |
| web page | 260 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 263 | `270` | data/router_train.csv rows |
| web page | 264 | `37%` | router_head_qa train_haiku_ok_rate |
| web page | 266 | `100` | test_queries.csv rows |
| web page | 268 | `5` | quality scale top (rubric); config cache.ttl_seconds in minutes; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 268 | `100` | test_queries.csv rows |
| web page | 281 | `12%` | routing_summary laya vs always_strong cost; router_head_summary zero-shot saving |
| web page | 282 | `4.60` | routing_summary laya mean_quality; effort_summary sonnet_low quality_complex |
| web page | 283 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
| web page | 287 | `13%` | router_head_summary length_rule saving |
| web page | 288 | `4.59` | router_head_summary length_rule quality |
| web page | 289 | `23%` | router_head_summary length_rule share_to_haiku |
| web page | 293 | `15%` | router_head_summary minilm_head saving |
| web page | 294 | `4.58` | router_head_summary minilm_head quality |
| web page | 295 | `27%` | router_head_summary minilm_head share_to_haiku |
| web page | 299 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
| web page | 300 | `4.54` | router_head_summary laya_head quality |
| web page | 301 | `36%` | router_head_summary laya_head share_to_haiku |
| web page | 305 | `38%` | router_head_summary hindsight ceiling saving; router_head_summary hindsight_ceiling saving |
| web page | 306 | `4.68` | router_head_summary hindsight_ceiling quality |
| web page | 307 | `60%` | router_head_summary hindsight_ceiling share_to_haiku |
| web page | 311 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
| web page | 311 | `100` | test_queries.csv rows |
| web page | 311 | `$0.517` | router_head_summary always_sonnet cost_usd (100 test questions) |
| web page | 311 | `$0.415` | router_head_summary laya_head cost_usd (100 test questions) |
| web page | 311 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
| web page | 311 | `36%` | router_head_summary laya_head share_to_haiku |
| web page | 311 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
| web page | 311 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| web page | 311 | `4.54` | router_head_summary laya_head quality |
| web page | 311 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 312 | `60%` | router_head_summary hindsight_ceiling share_to_haiku |
| web page | 312 | `38%` | router_head_summary hindsight ceiling saving; router_head_summary hindsight_ceiling saving |
| web page | 312 | `4.68` | router_head_summary hindsight_ceiling quality |
| web page | 313 | `0.63` | router_head_summary laya_zero_shot@0.50 auc_haiku_ok |
| web page | 313 | `0.75` | router_head_summary laya_head auc_haiku_ok |
| web page | 313 | `2,000` | router_head_bootstrap resamples |
| web page | 313 | `1,991` | router_head_bootstrap resamples with extra saving > 0 |
| web page | 313 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 313 | `15` | router_head_bootstrap extra saving 95% CI high (points) |
| web page | 313 | `0.76` | router_head_summary length_rule auc_haiku_ok |
| web page | 313 | `13%` | router_head_summary length_rule saving |
| web page | 314 | `4.42` | routing_summary always_cheap quality_simple |
| web page | 314 | `4.79` | routing_summary always_strong quality_simple |
| web page | 314 | `38%` | router_head_summary hindsight ceiling saving; router_head_summary hindsight_ceiling saving |
| web page | 314 | `100` | test_queries.csv rows |
| web page | 315 | `12%` | routing_summary laya vs always_strong cost; router_head_summary zero-shot saving |
| web page | 315 | `4.60` | routing_summary laya mean_quality; effort_summary sonnet_low quality_complex |
| web page | 316 | `13%` | router_head_summary length_rule saving |
| web page | 316 | `4.59` | router_head_summary length_rule quality |
| web page | 317 | `15%` | router_head_summary minilm_head saving |
| web page | 317 | `4.58` | router_head_summary minilm_head quality |
| web page | 318 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
| web page | 318 | `4.54` | router_head_summary laya_head quality |
| web page | 319 | `38%` | router_head_summary hindsight ceiling saving; router_head_summary hindsight_ceiling saving |
| web page | 319 | `4.68` | router_head_summary hindsight_ceiling quality |
| web page | 320 | `5.5` | model name: Claude Sonnet 5.5 |
| web page | 320 | `4.5` | model name: Claude Haiku 4.5 |
| web page | 320 | `50` | effort_summary sample size; effort sample size (config effort_eval.sample) |
| web page | 320 | `30` | effort sample: simple questions (config) |
| web page | 320 | `20` | per_answer_eval: answers improving >=2 v2_full -> cache_full_kb; judge_handcheck.md answers checked |
| web page | 324 | `5.5` | model name: Claude Sonnet 5.5 |
| web page | 325 | `50` | effort_summary sample size; effort sample size (config effort_eval.sample) |
| web page | 335 | `$0.264` | effort_summary always_strong total_cost_usd |
| web page | 336 | `0` | effort_summary thinking-off thinking_tokens |
| web page | 337 | `4.62` | effort_summary always_strong mean_quality; effort_summary sonnet_medium mean_quality |
| web page | 338 | `4.45` | effort_summary always_strong quality_complex |
| web page | 339 | `2.5` | effort_summary always_strong p50 latency (s) |
| web page | 343 | `$0.241` | effort_summary sonnet_low total_cost_usd |
| web page | 344 | `1,683` | effort_summary sonnet_low thinking_tokens |
| web page | 345 | `4.66` | effort_summary sonnet_low mean_quality; effort_summary sonnet_high mean_quality |
| web page | 346 | `4.60` | routing_summary laya mean_quality; effort_summary sonnet_low quality_complex |
| web page | 347 | `2.3` | effort_summary sonnet_low p50 latency (s) |
| web page | 351 | `$0.259` | effort_summary sonnet_medium total_cost_usd |
| web page | 352 | `3,433` | effort_summary sonnet_medium thinking_tokens |
| web page | 353 | `4.62` | effort_summary always_strong mean_quality; effort_summary sonnet_medium mean_quality |
| web page | 354 | `4.50` | effort_summary sonnet_medium quality_complex |
| web page | 355 | `2.6` | effort_summary sonnet_medium p50 latency (s) |
| web page | 359 | `$0.307` | effort_summary sonnet_high total_cost_usd |
| web page | 360 | `8,335` | effort_summary sonnet_high thinking_tokens |
| web page | 361 | `4.66` | effort_summary sonnet_low mean_quality; effort_summary sonnet_high mean_quality |
| web page | 362 | `4.65` | effort_summary sonnet_high quality_complex |
| web page | 363 | `3.5` | effort_summary sonnet_high p50 latency (s) |
| web page | 367 | `9%` | effort: low vs thinking off |
| web page | 367 | `28%` | effort: high vs low cost |
| web page | 368 | `26%` | effort_combo laya_head + sonnet_low saving |
| web page | 368 | `50` | effort_summary sample size; effort sample size (config effort_eval.sample) |
| web page | 369 | `$0.264` | effort_summary always_strong total_cost_usd |
| web page | 369 | `4.62` | effort_summary always_strong mean_quality; effort_summary sonnet_medium mean_quality |
| web page | 370 | `$0.241` | effort_summary sonnet_low total_cost_usd |
| web page | 370 | `4.66` | effort_summary sonnet_low mean_quality; effort_summary sonnet_high mean_quality |
| web page | 371 | `$0.259` | effort_summary sonnet_medium total_cost_usd |
| web page | 371 | `4.62` | effort_summary always_strong mean_quality; effort_summary sonnet_medium mean_quality |
| web page | 372 | `$0.307` | effort_summary sonnet_high total_cost_usd |
| web page | 372 | `4.66` | effort_summary sonnet_low mean_quality; effort_summary sonnet_high mean_quality |
| web page | 373 | `1,683` | effort_summary sonnet_low thinking_tokens |
| web page | 373 | `8,335` | effort_summary sonnet_high thinking_tokens |
| web page | 373 | `8%` | cache_full_kb vs v2_full cost |
| web page | 373 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 373 | `140` | 100 queries + conversation turns (data files) |
| web page | 373 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 373 | `$5,368` | cache_full_kb cost per answer x 1M |
| web page | 373 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 373 | `$13,946` | v1 cost per answer x 1M |
| web page | 384 | `78%` | variance.csv judge re-score identical share |
| web page | 384 | `17` | judge_handcheck.md AGREE count |
| web page | 384 | `20` | per_answer_eval: answers improving >=2 v2_full -> cache_full_kb; judge_handcheck.md answers checked |
| web page | 384 | `100` | test_queries.csv rows |
| web page | 384 | `0.1` | noise floor stated from judge variance (mean |diff| 0.23 per answer) |
| web page | 384 | `140` | 100 queries + conversation turns (data files) |
