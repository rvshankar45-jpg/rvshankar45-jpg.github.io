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
| blog | 62 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
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
| blog | 67 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 67 | `$0.69` | summary.csv v2_full total_cost_usd |
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
| blog | 79 | `4.80` | summary.csv cache_full_kb mean_quality |
| blog | 79 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 79 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| blog | 79 | `62%` | 1 - cache_full_kb/v1 cost |
| blog | 79 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 81 | `140` | 100 queries + conversation turns (data files) |
| blog | 83 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 83 | `$0.91` | summary.csv plus_tight_cache total_cost_usd |
| blog | 83 | `4.40` | summary.csv plus_tight_cache mean_quality |
| blog | 84 | `$0.75` | summary.csv cache_full_kb total_cost_usd |
| blog | 84 | `4.80` | summary.csv cache_full_kb mean_quality |
| blog | 86 | `17%` | cache_full_kb vs plus_tight_cache cost (same setup, RAG vs cache) |
| blog | 86 | `20` | per_answer_eval: answers improving >=2 v2_full -> cache_full_kb; judge_handcheck.md answers checked |
| blog | 88 | `5` | quality scale top (rubric); config cache.ttl_seconds in minutes; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 94 | `9` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank; kb.md sections (retriever chunks) |
| blog | 96 | `384` | MiniLM embedding dimensions |
| blog | 97 | `9` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank; kb.md sections (retriever chunks) |
| blog | 97 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 97 | `60` | config retrieval.rrf_k (fusion constant) |
| blog | 97 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 97 | `60` | config retrieval.rrf_k (fusion constant) |
| blog | 98 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 100 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 104 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 104 | `74%` | retrieval_recall right section found at k=1 |
| blog | 104 | `11%` | retrieval_recall share of manual sent at k=1 |
| blog | 105 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 105 | `89%` | retrieval_recall right section found at k=2 |
| blog | 105 | `22%` | retrieval_recall share of manual sent at k=2 |
| blog | 106 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 106 | `95%` | retrieval_recall right section found at k=3 |
| blog | 106 | `33%` | retrieval_recall share of manual sent at k=3 |
| blog | 107 | `4` | retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 107 | `96%` | retrieval_recall right section found at k=4 |
| blog | 107 | `44%` | retrieval_recall share of manual sent at k=4 |
| blog | 108 | `5` | quality scale top (rubric); config cache.ttl_seconds in minutes; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 108 | `97%` | retrieval_recall right section found at k=5 |
| blog | 108 | `56%` | retrieval_recall share of manual sent at k=5 |
| blog | 110 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 110 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 110 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 116 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 116 | `4` | retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 116 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 117 | `4` | retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 117 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 117 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 118 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 118 | `5` | quality scale top (rubric); config cache.ttl_seconds in minutes; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 118 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 119 | `5` | quality scale top (rubric); config cache.ttl_seconds in minutes; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 119 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 119 | `4` | retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 120 | `8` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 120 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 120 | `5` | quality scale top (rubric); config cache.ttl_seconds in minutes; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 121 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 121 | `7` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 121 | `6` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 123 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 123 | `7` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 123 | `6` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 131 | `12%` | routing_summary laya vs always_strong cost; router_head_summary zero-shot saving |
| blog | 131 | `4.60` | routing_summary laya mean_quality; effort_summary sonnet_low quality_complex |
| blog | 131 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| blog | 131 | `45` | routing_confusion laya simple->strong |
| blog | 131 | `62` | test_queries.csv label=simple |
| blog | 133 | `136` | llm_router tokens per query |
| blog | 133 | `1,176` | routing_summary llm_router p50_router_ms |
| blog | 133 | `194` | routing_summary laya p50_router_ms |
| blog | 135 | `0.2` | rule fixed in eval/run_routing_eval.py (complex gap <= 0.2) |
| blog | 135 | `0.50` | threshold_sweep recommended |
| blog | 135 | `4.32` | threshold_sweep quality_complex at recommended |
| blog | 135 | `4.00` | threshold_sweep quality_complex at next threshold |
| blog | 139 | `0.63` | router_head_summary laya_zero_shot@0.50 auc_haiku_ok |
| blog | 139 | `0.5` | AUC of a coin flip (definition) |
| blog | 139 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 143 | `270` | data/router_train.csv rows |
| blog | 144 | `37%` | router_head_qa train_haiku_ok_rate |
| blog | 146 | `100` | test_queries.csv rows |
| blog | 148 | `5` | quality scale top (rubric); config cache.ttl_seconds in minutes; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 148 | `100` | test_queries.csv rows |
| blog | 152 | `12%` | routing_summary laya vs always_strong cost; router_head_summary zero-shot saving |
| blog | 152 | `4.60` | routing_summary laya mean_quality; effort_summary sonnet_low quality_complex |
| blog | 152 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
| blog | 153 | `13%` | router_head_summary length_rule saving |
| blog | 153 | `4.59` | router_head_summary length_rule quality |
| blog | 153 | `23%` | router_head_summary length_rule share_to_haiku |
| blog | 154 | `15%` | router_head_summary minilm_head saving |
| blog | 154 | `4.58` | router_head_summary minilm_head quality |
| blog | 154 | `27%` | router_head_summary minilm_head share_to_haiku |
| blog | 155 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
| blog | 155 | `4.54` | router_head_summary laya_head quality |
| blog | 155 | `36%` | router_head_summary laya_head share_to_haiku |
| blog | 156 | `38%` | router_head_summary hindsight ceiling saving; router_head_summary hindsight_ceiling saving |
| blog | 156 | `4.68` | router_head_summary hindsight_ceiling quality |
| blog | 156 | `60%` | router_head_summary hindsight_ceiling share_to_haiku |
| blog | 158 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
| blog | 158 | `100` | test_queries.csv rows |
| blog | 158 | `$0.517` | router_head_summary always_sonnet cost_usd (100 test questions) |
| blog | 158 | `$0.415` | router_head_summary laya_head cost_usd (100 test questions) |
| blog | 158 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
| blog | 158 | `36%` | router_head_summary laya_head share_to_haiku |
| blog | 158 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
| blog | 158 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| blog | 158 | `4.54` | router_head_summary laya_head quality |
| blog | 158 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 160 | `60%` | router_head_summary hindsight_ceiling share_to_haiku |
| blog | 160 | `38%` | router_head_summary hindsight ceiling saving; router_head_summary hindsight_ceiling saving |
| blog | 160 | `4.68` | router_head_summary hindsight_ceiling quality |
| blog | 162 | `0.63` | router_head_summary laya_zero_shot@0.50 auc_haiku_ok |
| blog | 162 | `0.75` | router_head_summary laya_head auc_haiku_ok |
| blog | 162 | `2,000` | router_head_bootstrap resamples |
| blog | 162 | `1,991` | router_head_bootstrap resamples with extra saving > 0 |
| blog | 162 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 162 | `15` | router_head_bootstrap extra saving 95% CI high (points) |
| blog | 162 | `0.76` | router_head_summary length_rule auc_haiku_ok |
| blog | 162 | `13%` | router_head_summary length_rule saving |
| blog | 164 | `4.42` | routing_summary always_cheap quality_simple |
| blog | 164 | `4.79` | routing_summary always_strong quality_simple |
| blog | 164 | `38%` | router_head_summary hindsight ceiling saving; router_head_summary hindsight_ceiling saving |
| blog | 168 | `5.5` | model name: Claude Sonnet 5.5 |
| blog | 168 | `4.5` | model name: Claude Haiku 4.5 |
| blog | 168 | `50` | effort_summary sample size; effort sample size (config effort_eval.sample) |
| blog | 168 | `30` | effort sample: simple questions (config) |
| blog | 168 | `20` | per_answer_eval: answers improving >=2 v2_full -> cache_full_kb; judge_handcheck.md answers checked |
| blog | 170 | `5.5` | model name: Claude Sonnet 5.5 |
| blog | 170 | `50` | effort_summary sample size; effort sample size (config effort_eval.sample) |
| blog | 172 | `$0.264` | effort_summary always_strong total_cost_usd |
| blog | 172 | `0` | effort_summary thinking-off thinking_tokens |
| blog | 172 | `4.62` | effort_summary always_strong mean_quality; effort_summary sonnet_medium mean_quality |
| blog | 172 | `4.45` | effort_summary always_strong quality_complex |
| blog | 172 | `2.5` | effort_summary always_strong p50 latency (s) |
| blog | 173 | `$0.241` | effort_summary sonnet_low total_cost_usd |
| blog | 173 | `1,683` | effort_summary sonnet_low thinking_tokens |
| blog | 173 | `4.66` | effort_summary sonnet_low mean_quality; effort_summary sonnet_high mean_quality |
| blog | 173 | `4.60` | routing_summary laya mean_quality; effort_summary sonnet_low quality_complex |
| blog | 173 | `2.3` | effort_summary sonnet_low p50 latency (s) |
| blog | 174 | `$0.259` | effort_summary sonnet_medium total_cost_usd |
| blog | 174 | `3,433` | effort_summary sonnet_medium thinking_tokens |
| blog | 174 | `4.62` | effort_summary always_strong mean_quality; effort_summary sonnet_medium mean_quality |
| blog | 174 | `4.50` | effort_summary sonnet_medium quality_complex |
| blog | 174 | `2.6` | effort_summary sonnet_medium p50 latency (s) |
| blog | 175 | `$0.307` | effort_summary sonnet_high total_cost_usd |
| blog | 175 | `8,335` | effort_summary sonnet_high thinking_tokens |
| blog | 175 | `4.66` | effort_summary sonnet_low mean_quality; effort_summary sonnet_high mean_quality |
| blog | 175 | `4.65` | effort_summary sonnet_high quality_complex |
| blog | 175 | `3.5` | effort_summary sonnet_high p50 latency (s) |
| blog | 177 | `9%` | effort: low vs thinking off |
| blog | 177 | `28%` | effort: high vs low cost |
| blog | 179 | `26%` | effort_combo laya_head + sonnet_low saving |
| blog | 183 | `8%` | cache_full_kb vs v2_full cost |
| blog | 183 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 183 | `140` | 100 queries + conversation turns (data files) |
| blog | 183 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 183 | `$5,368` | cache_full_kb cost per answer x 1M |
| blog | 183 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 183 | `$13,946` | v1 cost per answer x 1M |
| blog | 201 | `78%` | variance.csv judge re-score identical share |
| blog | 201 | `17` | judge_handcheck.md AGREE count |
| blog | 201 | `20` | per_answer_eval: answers improving >=2 v2_full -> cache_full_kb; judge_handcheck.md answers checked |
| blog | 201 | `100` | test_queries.csv rows |
| blog | 201 | `0.1` | noise floor stated from judge variance (mean |diff| 0.23 per answer) |
| blog | 201 | `140` | 100 queries + conversation turns (data files) |
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
| web page | 83 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 84 | `$1.95` | summary.csv v1_naive total_cost_usd |
| web page | 85 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| web page | 89 | `$1.75` | summary.csv plus_route total_cost_usd |
| web page | 90 | `4.56` | summary.csv plus_route mean_quality; summary.csv plus_route mean_quality |
| web page | 94 | `$1.12` | summary.csv plus_retrieve total_cost_usd; summary.csv plus_trim total_cost_usd |
| web page | 95 | `4.34` | summary.csv plus_retrieve mean_quality; summary.csv plus_retrieve mean_quality |
| web page | 99 | `$1.12` | summary.csv plus_retrieve total_cost_usd; summary.csv plus_trim total_cost_usd |
| web page | 100 | `4.39` | summary.csv plus_trim mean_quality |
| web page | 104 | `$0.91` | summary.csv plus_tight_cache total_cost_usd |
| web page | 105 | `4.40` | summary.csv plus_tight_cache mean_quality |
| web page | 108 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 109 | `$0.69` | summary.csv v2_full total_cost_usd |
| web page | 110 | `4.49` | summary.csv v2_full mean_quality |
| web page | 115 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 115 | `9` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank; kb.md sections (retriever chunks) |
| web page | 115 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 115 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 116 | `$0.63` | retrieval step: plus_route - plus_retrieve cost |
| web page | 116 | `$1.26` | total saving v1 - v2 |
| web page | 117 | `5` | quality scale top (rubric); config cache.ttl_seconds in minutes; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 117 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 117 | `14` | per_answer_eval: answers dropping >=2 from plus_route to plus_retrieve |
| web page | 117 | `140` | 100 queries + conversation turns (data files) |
| web page | 118 | `0.5%` | trim step / v1 cost |
| web page | 118 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 118 | `203` | calls_eval v2_full Sonnet static_prefix_tokens |
| web page | 118 | `512` | config cache.min_tokens strong |
| web page | 119 | `4.80` | summary.csv cache_full_kb mean_quality |
| web page | 119 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 119 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| web page | 119 | `62%` | 1 - cache_full_kb/v1 cost |
| web page | 119 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 124 | `140` | 100 queries + conversation turns (data files) |
| web page | 130 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 131 | `$0.91` | summary.csv plus_tight_cache total_cost_usd |
| web page | 132 | `4.40` | summary.csv plus_tight_cache mean_quality |
| web page | 136 | `$0.75` | summary.csv cache_full_kb total_cost_usd |
| web page | 137 | `4.80` | summary.csv cache_full_kb mean_quality |
| web page | 141 | `17%` | cache_full_kb vs plus_tight_cache cost (same setup, RAG vs cache) |
| web page | 141 | `20` | per_answer_eval: answers improving >=2 v2_full -> cache_full_kb; judge_handcheck.md answers checked |
| web page | 142 | `5` | quality scale top (rubric); config cache.ttl_seconds in minutes; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 142 | `140` | 100 queries + conversation turns (data files) |
| web page | 142 | `5` | quality scale top (rubric); config cache.ttl_seconds in minutes; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 143 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 143 | `$1.95` | summary.csv v1_naive total_cost_usd |
| web page | 143 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| web page | 144 | `$1.75` | summary.csv plus_route total_cost_usd |
| web page | 144 | `4.56` | summary.csv plus_route mean_quality; summary.csv plus_route mean_quality |
| web page | 145 | `$1.12` | summary.csv plus_retrieve total_cost_usd; summary.csv plus_trim total_cost_usd |
| web page | 145 | `4.34` | summary.csv plus_retrieve mean_quality; summary.csv plus_retrieve mean_quality |
| web page | 146 | `$1.12` | summary.csv plus_retrieve total_cost_usd; summary.csv plus_trim total_cost_usd |
| web page | 146 | `4.39` | summary.csv plus_trim mean_quality |
| web page | 147 | `$0.91` | summary.csv plus_tight_cache total_cost_usd |
| web page | 147 | `4.40` | summary.csv plus_tight_cache mean_quality |
| web page | 148 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 148 | `$0.69` | summary.csv v2_full total_cost_usd |
| web page | 148 | `4.49` | summary.csv v2_full mean_quality |
| web page | 149 | `$0.75` | summary.csv cache_full_kb total_cost_usd |
| web page | 149 | `4.80` | summary.csv cache_full_kb mean_quality |
| web page | 152 | `9` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank; kb.md sections (retriever chunks) |
| web page | 154 | `384` | MiniLM embedding dimensions |
| web page | 155 | `9` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank; kb.md sections (retriever chunks) |
| web page | 155 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 155 | `60` | config retrieval.rrf_k (fusion constant) |
| web page | 155 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 155 | `60` | config retrieval.rrf_k (fusion constant) |
| web page | 156 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 158 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 169 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 170 | `74%` | retrieval_recall right section found at k=1 |
| web page | 171 | `11%` | retrieval_recall share of manual sent at k=1 |
| web page | 174 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 175 | `89%` | retrieval_recall right section found at k=2 |
| web page | 176 | `22%` | retrieval_recall share of manual sent at k=2 |
| web page | 179 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 180 | `95%` | retrieval_recall right section found at k=3 |
| web page | 181 | `33%` | retrieval_recall share of manual sent at k=3 |
| web page | 184 | `4` | retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 185 | `96%` | retrieval_recall right section found at k=4 |
| web page | 186 | `44%` | retrieval_recall share of manual sent at k=4 |
| web page | 189 | `5` | quality scale top (rubric); config cache.ttl_seconds in minutes; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 190 | `97%` | retrieval_recall right section found at k=5 |
| web page | 191 | `56%` | retrieval_recall share of manual sent at k=5 |
| web page | 195 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 195 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 195 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 209 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 210 | `4` | retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 211 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 215 | `4` | retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 216 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 217 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 221 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 222 | `5` | quality scale top (rubric); config cache.ttl_seconds in minutes; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 223 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 227 | `5` | quality scale top (rubric); config cache.ttl_seconds in minutes; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 228 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 229 | `4` | retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 233 | `8` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 234 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 235 | `5` | quality scale top (rubric); config cache.ttl_seconds in minutes; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 239 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 240 | `7` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 241 | `6` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 245 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 245 | `7` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 245 | `6` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 247 | `12%` | routing_summary laya vs always_strong cost; router_head_summary zero-shot saving |
| web page | 247 | `4.60` | routing_summary laya mean_quality; effort_summary sonnet_low quality_complex |
| web page | 247 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| web page | 247 | `45` | routing_confusion laya simple->strong |
| web page | 247 | `62` | test_queries.csv label=simple |
| web page | 248 | `136` | llm_router tokens per query |
| web page | 248 | `1,176` | routing_summary llm_router p50_router_ms |
| web page | 248 | `194` | routing_summary laya p50_router_ms |
| web page | 249 | `0.2` | rule fixed in eval/run_routing_eval.py (complex gap <= 0.2) |
| web page | 249 | `0.50` | threshold_sweep recommended |
| web page | 249 | `4.32` | threshold_sweep quality_complex at recommended |
| web page | 249 | `4.00` | threshold_sweep quality_complex at next threshold |
| web page | 249 | `0.63` | router_head_summary laya_zero_shot@0.50 auc_haiku_ok |
| web page | 249 | `0.5` | AUC of a coin flip (definition) |
| web page | 249 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 252 | `270` | data/router_train.csv rows |
| web page | 253 | `37%` | router_head_qa train_haiku_ok_rate |
| web page | 255 | `100` | test_queries.csv rows |
| web page | 257 | `5` | quality scale top (rubric); config cache.ttl_seconds in minutes; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 257 | `100` | test_queries.csv rows |
| web page | 270 | `12%` | routing_summary laya vs always_strong cost; router_head_summary zero-shot saving |
| web page | 271 | `4.60` | routing_summary laya mean_quality; effort_summary sonnet_low quality_complex |
| web page | 272 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
| web page | 276 | `13%` | router_head_summary length_rule saving |
| web page | 277 | `4.59` | router_head_summary length_rule quality |
| web page | 278 | `23%` | router_head_summary length_rule share_to_haiku |
| web page | 282 | `15%` | router_head_summary minilm_head saving |
| web page | 283 | `4.58` | router_head_summary minilm_head quality |
| web page | 284 | `27%` | router_head_summary minilm_head share_to_haiku |
| web page | 288 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
| web page | 289 | `4.54` | router_head_summary laya_head quality |
| web page | 290 | `36%` | router_head_summary laya_head share_to_haiku |
| web page | 294 | `38%` | router_head_summary hindsight ceiling saving; router_head_summary hindsight_ceiling saving |
| web page | 295 | `4.68` | router_head_summary hindsight_ceiling quality |
| web page | 296 | `60%` | router_head_summary hindsight_ceiling share_to_haiku |
| web page | 300 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
| web page | 300 | `100` | test_queries.csv rows |
| web page | 300 | `$0.517` | router_head_summary always_sonnet cost_usd (100 test questions) |
| web page | 300 | `$0.415` | router_head_summary laya_head cost_usd (100 test questions) |
| web page | 300 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
| web page | 300 | `36%` | router_head_summary laya_head share_to_haiku |
| web page | 300 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
| web page | 300 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| web page | 300 | `4.54` | router_head_summary laya_head quality |
| web page | 300 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 301 | `60%` | router_head_summary hindsight_ceiling share_to_haiku |
| web page | 301 | `38%` | router_head_summary hindsight ceiling saving; router_head_summary hindsight_ceiling saving |
| web page | 301 | `4.68` | router_head_summary hindsight_ceiling quality |
| web page | 302 | `0.63` | router_head_summary laya_zero_shot@0.50 auc_haiku_ok |
| web page | 302 | `0.75` | router_head_summary laya_head auc_haiku_ok |
| web page | 302 | `2,000` | router_head_bootstrap resamples |
| web page | 302 | `1,991` | router_head_bootstrap resamples with extra saving > 0 |
| web page | 302 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 302 | `15` | router_head_bootstrap extra saving 95% CI high (points) |
| web page | 302 | `0.76` | router_head_summary length_rule auc_haiku_ok |
| web page | 302 | `13%` | router_head_summary length_rule saving |
| web page | 303 | `4.42` | routing_summary always_cheap quality_simple |
| web page | 303 | `4.79` | routing_summary always_strong quality_simple |
| web page | 303 | `38%` | router_head_summary hindsight ceiling saving; router_head_summary hindsight_ceiling saving |
| web page | 303 | `100` | test_queries.csv rows |
| web page | 304 | `12%` | routing_summary laya vs always_strong cost; router_head_summary zero-shot saving |
| web page | 304 | `4.60` | routing_summary laya mean_quality; effort_summary sonnet_low quality_complex |
| web page | 305 | `13%` | router_head_summary length_rule saving |
| web page | 305 | `4.59` | router_head_summary length_rule quality |
| web page | 306 | `15%` | router_head_summary minilm_head saving |
| web page | 306 | `4.58` | router_head_summary minilm_head quality |
| web page | 307 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
| web page | 307 | `4.54` | router_head_summary laya_head quality |
| web page | 308 | `38%` | router_head_summary hindsight ceiling saving; router_head_summary hindsight_ceiling saving |
| web page | 308 | `4.68` | router_head_summary hindsight_ceiling quality |
| web page | 309 | `5.5` | model name: Claude Sonnet 5.5 |
| web page | 309 | `4.5` | model name: Claude Haiku 4.5 |
| web page | 309 | `50` | effort_summary sample size; effort sample size (config effort_eval.sample) |
| web page | 309 | `30` | effort sample: simple questions (config) |
| web page | 309 | `20` | per_answer_eval: answers improving >=2 v2_full -> cache_full_kb; judge_handcheck.md answers checked |
| web page | 313 | `5.5` | model name: Claude Sonnet 5.5 |
| web page | 314 | `50` | effort_summary sample size; effort sample size (config effort_eval.sample) |
| web page | 324 | `$0.264` | effort_summary always_strong total_cost_usd |
| web page | 325 | `0` | effort_summary thinking-off thinking_tokens |
| web page | 326 | `4.62` | effort_summary always_strong mean_quality; effort_summary sonnet_medium mean_quality |
| web page | 327 | `4.45` | effort_summary always_strong quality_complex |
| web page | 328 | `2.5` | effort_summary always_strong p50 latency (s) |
| web page | 332 | `$0.241` | effort_summary sonnet_low total_cost_usd |
| web page | 333 | `1,683` | effort_summary sonnet_low thinking_tokens |
| web page | 334 | `4.66` | effort_summary sonnet_low mean_quality; effort_summary sonnet_high mean_quality |
| web page | 335 | `4.60` | routing_summary laya mean_quality; effort_summary sonnet_low quality_complex |
| web page | 336 | `2.3` | effort_summary sonnet_low p50 latency (s) |
| web page | 340 | `$0.259` | effort_summary sonnet_medium total_cost_usd |
| web page | 341 | `3,433` | effort_summary sonnet_medium thinking_tokens |
| web page | 342 | `4.62` | effort_summary always_strong mean_quality; effort_summary sonnet_medium mean_quality |
| web page | 343 | `4.50` | effort_summary sonnet_medium quality_complex |
| web page | 344 | `2.6` | effort_summary sonnet_medium p50 latency (s) |
| web page | 348 | `$0.307` | effort_summary sonnet_high total_cost_usd |
| web page | 349 | `8,335` | effort_summary sonnet_high thinking_tokens |
| web page | 350 | `4.66` | effort_summary sonnet_low mean_quality; effort_summary sonnet_high mean_quality |
| web page | 351 | `4.65` | effort_summary sonnet_high quality_complex |
| web page | 352 | `3.5` | effort_summary sonnet_high p50 latency (s) |
| web page | 356 | `9%` | effort: low vs thinking off |
| web page | 356 | `28%` | effort: high vs low cost |
| web page | 357 | `26%` | effort_combo laya_head + sonnet_low saving |
| web page | 357 | `50` | effort_summary sample size; effort sample size (config effort_eval.sample) |
| web page | 358 | `$0.264` | effort_summary always_strong total_cost_usd |
| web page | 358 | `4.62` | effort_summary always_strong mean_quality; effort_summary sonnet_medium mean_quality |
| web page | 359 | `$0.241` | effort_summary sonnet_low total_cost_usd |
| web page | 359 | `4.66` | effort_summary sonnet_low mean_quality; effort_summary sonnet_high mean_quality |
| web page | 360 | `$0.259` | effort_summary sonnet_medium total_cost_usd |
| web page | 360 | `4.62` | effort_summary always_strong mean_quality; effort_summary sonnet_medium mean_quality |
| web page | 361 | `$0.307` | effort_summary sonnet_high total_cost_usd |
| web page | 361 | `4.66` | effort_summary sonnet_low mean_quality; effort_summary sonnet_high mean_quality |
| web page | 362 | `1,683` | effort_summary sonnet_low thinking_tokens |
| web page | 362 | `8,335` | effort_summary sonnet_high thinking_tokens |
| web page | 362 | `8%` | cache_full_kb vs v2_full cost |
| web page | 362 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 362 | `140` | 100 queries + conversation turns (data files) |
| web page | 362 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 362 | `$5,368` | cache_full_kb cost per answer x 1M |
| web page | 362 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 362 | `$13,946` | v1 cost per answer x 1M |
| web page | 373 | `78%` | variance.csv judge re-score identical share |
| web page | 373 | `17` | judge_handcheck.md AGREE count |
| web page | 373 | `20` | per_answer_eval: answers improving >=2 v2_full -> cache_full_kb; judge_handcheck.md answers checked |
| web page | 373 | `100` | test_queries.csv rows |
| web page | 373 | `0.1` | noise floor stated from judge variance (mean |diff| 0.23 per answer) |
| web page | 373 | `140` | 100 queries + conversation turns (data files) |
