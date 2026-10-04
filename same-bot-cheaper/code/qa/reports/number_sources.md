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
| blog | 168 | `50` | effort_summary sample size; effort sample size (config effort_eval.sample) |
| blog | 168 | `30` | effort sample: simple questions (config) |
| blog | 168 | `20` | per_answer_eval: answers improving >=2 v2_full -> cache_full_kb; judge_handcheck.md answers checked |
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
| linkedin | 1 | `64%` | 1 - v2_full/v1_naive total_cost_usd |
| linkedin | 3 | `140` | 100 queries + conversation turns (data files) |
| linkedin | 7 | `$1.95` | summary.csv v1_naive total_cost_usd |
| linkedin | 7 | `$0.69` | summary.csv v2_full total_cost_usd |
| linkedin | 7 | `140` | 100 queries + conversation turns (data files) |
| linkedin | 7 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| linkedin | 7 | `4.49` | summary.csv v2_full mean_quality |
| linkedin | 7 | `5` | quality scale top (rubric); config cache.ttl_seconds in minutes; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
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
| web page | 12 | `9` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank; kb.md sections (retriever chunks) |
| web page | 12 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 12 | `5.5` | model name: Claude Sonnet 5.5 |
| web page | 12 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
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
| web page | 12 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 12 | `5` | quality scale top (rubric); config cache.ttl_seconds in minutes; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 12 | `5` | quality scale top (rubric); config cache.ttl_seconds in minutes; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 12 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
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
| web page | 18 | `5` | quality scale top (rubric); config cache.ttl_seconds in minutes; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 18 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| web page | 19 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
| web page | 20 | `64%` | 1 - v2_full/v1_naive total_cost_usd |
| web page | 20 | `140` | 100 queries + conversation turns (data files) |
| web page | 20 | `$0.69` | summary.csv v2_full total_cost_usd |
| web page | 20 | `$1.95` | summary.csv v1_naive total_cost_usd |
| web page | 20 | `4.49` | summary.csv v2_full mean_quality |
| web page | 20 | `5` | quality scale top (rubric); config cache.ttl_seconds in minutes; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 20 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| web page | 20 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 20 | `62%` | 1 - cache_full_kb/v1 cost |
| web page | 20 | `4.80` | summary.csv cache_full_kb mean_quality |
| web page | 20 | `12%` | routing_summary laya vs always_strong cost; router_head_summary zero-shot saving |
| web page | 20 | `270` | data/router_train.csv rows |
| web page | 20 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
| web page | 20 | `28%` | effort: high vs low cost |
| web page | 26 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 36 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 40 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 43 | `650` | persona tokens on strong model = 652 (rounded to 10) |
| web page | 43 | `170` | tight prompt tokens on strong model = 170 (rounded to 10) |
| web page | 44 | `170` | tight prompt tokens on strong model = 170 (rounded to 10) |
| web page | 61 | `4.5` | model name: Claude Haiku 4.5 |
| web page | 62 | `5.5` | model name: Claude Sonnet 5.5 |
| web page | 64 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 64 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 76 | `140` | 100 queries + conversation turns (data files) |
| web page | 82 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
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
| web page | 107 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 108 | `$0.69` | summary.csv v2_full total_cost_usd |
| web page | 109 | `4.49` | summary.csv v2_full mean_quality |
| web page | 114 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 114 | `9` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank; kb.md sections (retriever chunks) |
| web page | 114 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 114 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 115 | `$0.63` | retrieval step: plus_route - plus_retrieve cost |
| web page | 115 | `$1.26` | total saving v1 - v2 |
| web page | 116 | `5` | quality scale top (rubric); config cache.ttl_seconds in minutes; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 116 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 116 | `14` | per_answer_eval: answers dropping >=2 from plus_route to plus_retrieve |
| web page | 116 | `140` | 100 queries + conversation turns (data files) |
| web page | 117 | `0.5%` | trim step / v1 cost |
| web page | 117 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 117 | `203` | calls_eval v2_full Sonnet static_prefix_tokens |
| web page | 117 | `512` | config cache.min_tokens strong |
| web page | 118 | `4.80` | summary.csv cache_full_kb mean_quality |
| web page | 118 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 118 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| web page | 118 | `62%` | 1 - cache_full_kb/v1 cost |
| web page | 118 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 123 | `140` | 100 queries + conversation turns (data files) |
| web page | 129 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 130 | `$0.91` | summary.csv plus_tight_cache total_cost_usd |
| web page | 131 | `4.40` | summary.csv plus_tight_cache mean_quality |
| web page | 135 | `$0.75` | summary.csv cache_full_kb total_cost_usd |
| web page | 136 | `4.80` | summary.csv cache_full_kb mean_quality |
| web page | 140 | `17%` | cache_full_kb vs plus_tight_cache cost (same setup, RAG vs cache) |
| web page | 140 | `20` | per_answer_eval: answers improving >=2 v2_full -> cache_full_kb; judge_handcheck.md answers checked |
| web page | 141 | `5` | quality scale top (rubric); config cache.ttl_seconds in minutes; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 141 | `140` | 100 queries + conversation turns (data files) |
| web page | 141 | `5` | quality scale top (rubric); config cache.ttl_seconds in minutes; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 142 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 142 | `$1.95` | summary.csv v1_naive total_cost_usd |
| web page | 142 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| web page | 143 | `$1.75` | summary.csv plus_route total_cost_usd |
| web page | 143 | `4.56` | summary.csv plus_route mean_quality; summary.csv plus_route mean_quality |
| web page | 144 | `$1.12` | summary.csv plus_retrieve total_cost_usd; summary.csv plus_trim total_cost_usd |
| web page | 144 | `4.34` | summary.csv plus_retrieve mean_quality; summary.csv plus_retrieve mean_quality |
| web page | 145 | `$1.12` | summary.csv plus_retrieve total_cost_usd; summary.csv plus_trim total_cost_usd |
| web page | 145 | `4.39` | summary.csv plus_trim mean_quality |
| web page | 146 | `$0.91` | summary.csv plus_tight_cache total_cost_usd |
| web page | 146 | `4.40` | summary.csv plus_tight_cache mean_quality |
| web page | 147 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 147 | `$0.69` | summary.csv v2_full total_cost_usd |
| web page | 147 | `4.49` | summary.csv v2_full mean_quality |
| web page | 148 | `$0.75` | summary.csv cache_full_kb total_cost_usd |
| web page | 148 | `4.80` | summary.csv cache_full_kb mean_quality |
| web page | 151 | `9` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank; kb.md sections (retriever chunks) |
| web page | 153 | `384` | MiniLM embedding dimensions |
| web page | 154 | `9` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank; kb.md sections (retriever chunks) |
| web page | 154 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 154 | `60` | config retrieval.rrf_k (fusion constant) |
| web page | 154 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 154 | `60` | config retrieval.rrf_k (fusion constant) |
| web page | 155 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 157 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 168 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 169 | `74%` | retrieval_recall right section found at k=1 |
| web page | 170 | `11%` | retrieval_recall share of manual sent at k=1 |
| web page | 173 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 174 | `89%` | retrieval_recall right section found at k=2 |
| web page | 175 | `22%` | retrieval_recall share of manual sent at k=2 |
| web page | 178 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 179 | `95%` | retrieval_recall right section found at k=3 |
| web page | 180 | `33%` | retrieval_recall share of manual sent at k=3 |
| web page | 183 | `4` | retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 184 | `96%` | retrieval_recall right section found at k=4 |
| web page | 185 | `44%` | retrieval_recall share of manual sent at k=4 |
| web page | 188 | `5` | quality scale top (rubric); config cache.ttl_seconds in minutes; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 189 | `97%` | retrieval_recall right section found at k=5 |
| web page | 190 | `56%` | retrieval_recall share of manual sent at k=5 |
| web page | 194 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 194 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 194 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 208 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 209 | `4` | retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 210 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 214 | `4` | retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 215 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 216 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 220 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 221 | `5` | quality scale top (rubric); config cache.ttl_seconds in minutes; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 222 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 226 | `5` | quality scale top (rubric); config cache.ttl_seconds in minutes; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 227 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 228 | `4` | retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 232 | `8` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 233 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 234 | `5` | quality scale top (rubric); config cache.ttl_seconds in minutes; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 238 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 239 | `7` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 240 | `6` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 244 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 244 | `7` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 244 | `6` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 246 | `12%` | routing_summary laya vs always_strong cost; router_head_summary zero-shot saving |
| web page | 246 | `4.60` | routing_summary laya mean_quality; effort_summary sonnet_low quality_complex |
| web page | 246 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| web page | 246 | `45` | routing_confusion laya simple->strong |
| web page | 246 | `62` | test_queries.csv label=simple |
| web page | 247 | `136` | llm_router tokens per query |
| web page | 247 | `1,176` | routing_summary llm_router p50_router_ms |
| web page | 247 | `194` | routing_summary laya p50_router_ms |
| web page | 248 | `0.2` | rule fixed in eval/run_routing_eval.py (complex gap <= 0.2) |
| web page | 248 | `0.50` | threshold_sweep recommended |
| web page | 248 | `4.32` | threshold_sweep quality_complex at recommended |
| web page | 248 | `4.00` | threshold_sweep quality_complex at next threshold |
| web page | 248 | `0.63` | router_head_summary laya_zero_shot@0.50 auc_haiku_ok |
| web page | 248 | `0.5` | AUC of a coin flip (definition) |
| web page | 248 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 251 | `270` | data/router_train.csv rows |
| web page | 252 | `37%` | router_head_qa train_haiku_ok_rate |
| web page | 254 | `100` | test_queries.csv rows |
| web page | 256 | `5` | quality scale top (rubric); config cache.ttl_seconds in minutes; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 256 | `100` | test_queries.csv rows |
| web page | 269 | `12%` | routing_summary laya vs always_strong cost; router_head_summary zero-shot saving |
| web page | 270 | `4.60` | routing_summary laya mean_quality; effort_summary sonnet_low quality_complex |
| web page | 271 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
| web page | 275 | `13%` | router_head_summary length_rule saving |
| web page | 276 | `4.59` | router_head_summary length_rule quality |
| web page | 277 | `23%` | router_head_summary length_rule share_to_haiku |
| web page | 281 | `15%` | router_head_summary minilm_head saving |
| web page | 282 | `4.58` | router_head_summary minilm_head quality |
| web page | 283 | `27%` | router_head_summary minilm_head share_to_haiku |
| web page | 287 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
| web page | 288 | `4.54` | router_head_summary laya_head quality |
| web page | 289 | `36%` | router_head_summary laya_head share_to_haiku |
| web page | 293 | `38%` | router_head_summary hindsight ceiling saving; router_head_summary hindsight_ceiling saving |
| web page | 294 | `4.68` | router_head_summary hindsight_ceiling quality |
| web page | 295 | `60%` | router_head_summary hindsight_ceiling share_to_haiku |
| web page | 299 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
| web page | 299 | `100` | test_queries.csv rows |
| web page | 299 | `$0.517` | router_head_summary always_sonnet cost_usd (100 test questions) |
| web page | 299 | `$0.415` | router_head_summary laya_head cost_usd (100 test questions) |
| web page | 299 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
| web page | 299 | `36%` | router_head_summary laya_head share_to_haiku |
| web page | 299 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
| web page | 299 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| web page | 299 | `4.54` | router_head_summary laya_head quality |
| web page | 299 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 300 | `60%` | router_head_summary hindsight_ceiling share_to_haiku |
| web page | 300 | `38%` | router_head_summary hindsight ceiling saving; router_head_summary hindsight_ceiling saving |
| web page | 300 | `4.68` | router_head_summary hindsight_ceiling quality |
| web page | 301 | `0.63` | router_head_summary laya_zero_shot@0.50 auc_haiku_ok |
| web page | 301 | `0.75` | router_head_summary laya_head auc_haiku_ok |
| web page | 301 | `2,000` | router_head_bootstrap resamples |
| web page | 301 | `1,991` | router_head_bootstrap resamples with extra saving > 0 |
| web page | 301 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 301 | `15` | router_head_bootstrap extra saving 95% CI high (points) |
| web page | 301 | `0.76` | router_head_summary length_rule auc_haiku_ok |
| web page | 301 | `13%` | router_head_summary length_rule saving |
| web page | 302 | `4.42` | routing_summary always_cheap quality_simple |
| web page | 302 | `4.79` | routing_summary always_strong quality_simple |
| web page | 302 | `38%` | router_head_summary hindsight ceiling saving; router_head_summary hindsight_ceiling saving |
| web page | 302 | `100` | test_queries.csv rows |
| web page | 303 | `12%` | routing_summary laya vs always_strong cost; router_head_summary zero-shot saving |
| web page | 303 | `4.60` | routing_summary laya mean_quality; effort_summary sonnet_low quality_complex |
| web page | 304 | `13%` | router_head_summary length_rule saving |
| web page | 304 | `4.59` | router_head_summary length_rule quality |
| web page | 305 | `15%` | router_head_summary minilm_head saving |
| web page | 305 | `4.58` | router_head_summary minilm_head quality |
| web page | 306 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
| web page | 306 | `4.54` | router_head_summary laya_head quality |
| web page | 307 | `38%` | router_head_summary hindsight ceiling saving; router_head_summary hindsight_ceiling saving |
| web page | 307 | `4.68` | router_head_summary hindsight_ceiling quality |
| web page | 308 | `50` | effort_summary sample size; effort sample size (config effort_eval.sample) |
| web page | 308 | `30` | effort sample: simple questions (config) |
| web page | 308 | `20` | per_answer_eval: answers improving >=2 v2_full -> cache_full_kb; judge_handcheck.md answers checked |
| web page | 313 | `50` | effort_summary sample size; effort sample size (config effort_eval.sample) |
| web page | 323 | `$0.264` | effort_summary always_strong total_cost_usd |
| web page | 324 | `0` | effort_summary thinking-off thinking_tokens |
| web page | 325 | `4.62` | effort_summary always_strong mean_quality; effort_summary sonnet_medium mean_quality |
| web page | 326 | `4.45` | effort_summary always_strong quality_complex |
| web page | 327 | `2.5` | effort_summary always_strong p50 latency (s) |
| web page | 331 | `$0.241` | effort_summary sonnet_low total_cost_usd |
| web page | 332 | `1,683` | effort_summary sonnet_low thinking_tokens |
| web page | 333 | `4.66` | effort_summary sonnet_low mean_quality; effort_summary sonnet_high mean_quality |
| web page | 334 | `4.60` | routing_summary laya mean_quality; effort_summary sonnet_low quality_complex |
| web page | 335 | `2.3` | effort_summary sonnet_low p50 latency (s) |
| web page | 339 | `$0.259` | effort_summary sonnet_medium total_cost_usd |
| web page | 340 | `3,433` | effort_summary sonnet_medium thinking_tokens |
| web page | 341 | `4.62` | effort_summary always_strong mean_quality; effort_summary sonnet_medium mean_quality |
| web page | 342 | `4.50` | effort_summary sonnet_medium quality_complex |
| web page | 343 | `2.6` | effort_summary sonnet_medium p50 latency (s) |
| web page | 347 | `$0.307` | effort_summary sonnet_high total_cost_usd |
| web page | 348 | `8,335` | effort_summary sonnet_high thinking_tokens |
| web page | 349 | `4.66` | effort_summary sonnet_low mean_quality; effort_summary sonnet_high mean_quality |
| web page | 350 | `4.65` | effort_summary sonnet_high quality_complex |
| web page | 351 | `3.5` | effort_summary sonnet_high p50 latency (s) |
| web page | 355 | `9%` | effort: low vs thinking off |
| web page | 355 | `28%` | effort: high vs low cost |
| web page | 356 | `26%` | effort_combo laya_head + sonnet_low saving |
| web page | 356 | `50` | effort_summary sample size; effort sample size (config effort_eval.sample) |
| web page | 357 | `$0.264` | effort_summary always_strong total_cost_usd |
| web page | 357 | `4.62` | effort_summary always_strong mean_quality; effort_summary sonnet_medium mean_quality |
| web page | 358 | `$0.241` | effort_summary sonnet_low total_cost_usd |
| web page | 358 | `4.66` | effort_summary sonnet_low mean_quality; effort_summary sonnet_high mean_quality |
| web page | 359 | `$0.259` | effort_summary sonnet_medium total_cost_usd |
| web page | 359 | `4.62` | effort_summary always_strong mean_quality; effort_summary sonnet_medium mean_quality |
| web page | 360 | `$0.307` | effort_summary sonnet_high total_cost_usd |
| web page | 360 | `4.66` | effort_summary sonnet_low mean_quality; effort_summary sonnet_high mean_quality |
| web page | 361 | `1,683` | effort_summary sonnet_low thinking_tokens |
| web page | 361 | `8,335` | effort_summary sonnet_high thinking_tokens |
| web page | 361 | `8%` | cache_full_kb vs v2_full cost |
| web page | 361 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 361 | `140` | 100 queries + conversation turns (data files) |
| web page | 361 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 361 | `$5,368` | cache_full_kb cost per answer x 1M |
| web page | 361 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 361 | `$13,946` | v1 cost per answer x 1M |
| web page | 372 | `78%` | variance.csv judge re-score identical share |
| web page | 372 | `17` | judge_handcheck.md AGREE count |
| web page | 372 | `20` | per_answer_eval: answers improving >=2 v2_full -> cache_full_kb; judge_handcheck.md answers checked |
| web page | 372 | `100` | test_queries.csv rows |
| web page | 372 | `0.1` | noise floor stated from judge variance (mean |diff| 0.23 per answer) |
| web page | 372 | `140` | 100 queries + conversation turns (data files) |
