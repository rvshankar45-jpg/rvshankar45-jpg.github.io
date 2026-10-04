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
| blog | 17 | `5` | quality scale top (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 17 | `5` | quality scale top (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 17 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 21 | `64%` | 1 - v2_full/v1_naive total_cost_usd |
| blog | 21 | `140` | 100 queries + conversation turns (data files) |
| blog | 21 | `$0.69` | summary.csv v2_full total_cost_usd |
| blog | 21 | `$1.95` | summary.csv v1_naive total_cost_usd |
| blog | 21 | `4.49` | summary.csv v2_full mean_quality |
| blog | 21 | `5` | quality scale top (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
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
| blog | 75 | `5` | quality scale top (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
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
| blog | 79 | `20` | per_answer_eval: answers improving >=2 v2_full -> cache_full_kb; judge_handcheck.md answers checked |
| blog | 85 | `9` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank; kb.md sections (retriever chunks) |
| blog | 87 | `384` | MiniLM embedding dimensions |
| blog | 88 | `9` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank; kb.md sections (retriever chunks) |
| blog | 88 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 88 | `60` | config retrieval.rrf_k (fusion constant) |
| blog | 88 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 88 | `60` | config retrieval.rrf_k (fusion constant) |
| blog | 89 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 91 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 95 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 95 | `74%` | retrieval_recall right section found at k=1 |
| blog | 95 | `11%` | retrieval_recall share of manual sent at k=1 |
| blog | 96 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 96 | `89%` | retrieval_recall right section found at k=2 |
| blog | 96 | `22%` | retrieval_recall share of manual sent at k=2 |
| blog | 97 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 97 | `95%` | retrieval_recall right section found at k=3 |
| blog | 97 | `33%` | retrieval_recall share of manual sent at k=3 |
| blog | 98 | `4` | retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 98 | `96%` | retrieval_recall right section found at k=4 |
| blog | 98 | `44%` | retrieval_recall share of manual sent at k=4 |
| blog | 99 | `5` | quality scale top (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 99 | `97%` | retrieval_recall right section found at k=5 |
| blog | 99 | `56%` | retrieval_recall share of manual sent at k=5 |
| blog | 101 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 101 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 101 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 107 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 107 | `4` | retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 107 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 108 | `4` | retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 108 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 108 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 109 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 109 | `5` | quality scale top (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 109 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 110 | `5` | quality scale top (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 110 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 110 | `4` | retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 111 | `8` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 111 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 111 | `5` | quality scale top (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 112 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 112 | `7` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 112 | `6` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 114 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 114 | `7` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 114 | `6` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 122 | `12%` | routing_summary laya vs always_strong cost; router_head_summary zero-shot saving |
| blog | 122 | `4.60` | routing_summary laya mean_quality; effort_summary sonnet_low quality_complex |
| blog | 122 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| blog | 122 | `45` | routing_confusion laya simple->strong |
| blog | 122 | `62` | test_queries.csv label=simple |
| blog | 124 | `136` | llm_router tokens per query |
| blog | 124 | `1,176` | routing_summary llm_router p50_router_ms |
| blog | 124 | `194` | routing_summary laya p50_router_ms |
| blog | 126 | `0.2` | rule fixed in eval/run_routing_eval.py (complex gap <= 0.2) |
| blog | 126 | `0.50` | threshold_sweep recommended |
| blog | 126 | `4.32` | threshold_sweep quality_complex at recommended |
| blog | 126 | `4.00` | threshold_sweep quality_complex at next threshold |
| blog | 130 | `0.63` | router_head_summary laya_zero_shot@0.50 auc_haiku_ok |
| blog | 130 | `0.5` | AUC of a coin flip (definition) |
| blog | 130 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 134 | `270` | data/router_train.csv rows |
| blog | 135 | `37%` | router_head_qa train_haiku_ok_rate |
| blog | 137 | `100` | test_queries.csv rows |
| blog | 139 | `5` | quality scale top (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 139 | `100` | test_queries.csv rows |
| blog | 143 | `12%` | routing_summary laya vs always_strong cost; router_head_summary zero-shot saving |
| blog | 143 | `4.60` | routing_summary laya mean_quality; effort_summary sonnet_low quality_complex |
| blog | 143 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
| blog | 144 | `13%` | router_head_summary length_rule saving |
| blog | 144 | `4.59` | router_head_summary length_rule quality |
| blog | 144 | `23%` | router_head_summary length_rule share_to_haiku |
| blog | 145 | `15%` | router_head_summary minilm_head saving |
| blog | 145 | `4.58` | router_head_summary minilm_head quality |
| blog | 145 | `27%` | router_head_summary minilm_head share_to_haiku |
| blog | 146 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
| blog | 146 | `4.54` | router_head_summary laya_head quality |
| blog | 146 | `36%` | router_head_summary laya_head share_to_haiku |
| blog | 147 | `38%` | router_head_summary hindsight ceiling saving; router_head_summary hindsight_ceiling saving |
| blog | 147 | `4.68` | router_head_summary hindsight_ceiling quality |
| blog | 147 | `60%` | router_head_summary hindsight_ceiling share_to_haiku |
| blog | 149 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
| blog | 149 | `12%` | routing_summary laya vs always_strong cost; router_head_summary zero-shot saving |
| blog | 149 | `0.63` | router_head_summary laya_zero_shot@0.50 auc_haiku_ok |
| blog | 149 | `0.75` | router_head_summary laya_head auc_haiku_ok |
| blog | 149 | `2,000` | router_head_bootstrap resamples |
| blog | 149 | `1,991` | router_head_bootstrap resamples with extra saving > 0 |
| blog | 149 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 149 | `15` | router_head_bootstrap extra saving 95% CI high (points) |
| blog | 149 | `0.76` | router_head_summary length_rule auc_haiku_ok |
| blog | 149 | `13%` | router_head_summary length_rule saving |
| blog | 151 | `4.42` | routing_summary always_cheap quality_simple |
| blog | 151 | `4.79` | routing_summary always_strong quality_simple |
| blog | 151 | `38%` | router_head_summary hindsight ceiling saving; router_head_summary hindsight_ceiling saving |
| blog | 155 | `50` | effort_summary sample size; effort sample size (config effort_eval.sample) |
| blog | 155 | `30` | effort sample: simple questions (config) |
| blog | 155 | `20` | per_answer_eval: answers improving >=2 v2_full -> cache_full_kb; judge_handcheck.md answers checked |
| blog | 157 | `50` | effort_summary sample size; effort sample size (config effort_eval.sample) |
| blog | 159 | `$0.264` | effort_summary always_strong total_cost_usd |
| blog | 159 | `0` | effort_summary thinking-off thinking_tokens |
| blog | 159 | `4.62` | effort_summary always_strong mean_quality; effort_summary sonnet_medium mean_quality |
| blog | 159 | `4.45` | effort_summary always_strong quality_complex |
| blog | 159 | `2.5` | effort_summary always_strong p50 latency (s) |
| blog | 160 | `$0.241` | effort_summary sonnet_low total_cost_usd |
| blog | 160 | `1,683` | effort_summary sonnet_low thinking_tokens |
| blog | 160 | `4.66` | effort_summary sonnet_low mean_quality; effort_summary sonnet_high mean_quality |
| blog | 160 | `4.60` | routing_summary laya mean_quality; effort_summary sonnet_low quality_complex |
| blog | 160 | `2.3` | effort_summary sonnet_low p50 latency (s) |
| blog | 161 | `$0.259` | effort_summary sonnet_medium total_cost_usd |
| blog | 161 | `3,433` | effort_summary sonnet_medium thinking_tokens |
| blog | 161 | `4.62` | effort_summary always_strong mean_quality; effort_summary sonnet_medium mean_quality |
| blog | 161 | `4.50` | effort_summary sonnet_medium quality_complex |
| blog | 161 | `2.6` | effort_summary sonnet_medium p50 latency (s) |
| blog | 162 | `$0.307` | effort_summary sonnet_high total_cost_usd |
| blog | 162 | `8,335` | effort_summary sonnet_high thinking_tokens |
| blog | 162 | `4.66` | effort_summary sonnet_low mean_quality; effort_summary sonnet_high mean_quality |
| blog | 162 | `4.65` | effort_summary sonnet_high quality_complex |
| blog | 162 | `3.5` | effort_summary sonnet_high p50 latency (s) |
| blog | 164 | `9%` | effort: low vs thinking off |
| blog | 164 | `28%` | effort: high vs low cost |
| blog | 166 | `26%` | effort_combo laya_head + sonnet_low saving |
| blog | 170 | `8%` | cache_full_kb vs v2_full cost |
| blog | 170 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 170 | `140` | 100 queries + conversation turns (data files) |
| blog | 170 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 170 | `$5,368` | cache_full_kb cost per answer x 1M |
| blog | 170 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| blog | 170 | `$13,946` | v1 cost per answer x 1M |
| blog | 188 | `78%` | variance.csv judge re-score identical share |
| blog | 188 | `17` | judge_handcheck.md AGREE count |
| blog | 188 | `20` | per_answer_eval: answers improving >=2 v2_full -> cache_full_kb; judge_handcheck.md answers checked |
| blog | 188 | `100` | test_queries.csv rows |
| blog | 188 | `0.1` | noise floor stated from judge variance (mean |diff| 0.23 per answer) |
| blog | 188 | `140` | 100 queries + conversation turns (data files) |
| linkedin | 1 | `64%` | 1 - v2_full/v1_naive total_cost_usd |
| linkedin | 3 | `140` | 100 queries + conversation turns (data files) |
| linkedin | 7 | `$1.95` | summary.csv v1_naive total_cost_usd |
| linkedin | 7 | `$0.69` | summary.csv v2_full total_cost_usd |
| linkedin | 7 | `140` | 100 queries + conversation turns (data files) |
| linkedin | 7 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| linkedin | 7 | `4.49` | summary.csv v2_full mean_quality |
| linkedin | 7 | `5` | quality scale top (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
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
| web page | 12 | `5` | quality scale top (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 12 | `5` | quality scale top (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
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
| web page | 18 | `5` | quality scale top (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 18 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| web page | 19 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
| web page | 20 | `64%` | 1 - v2_full/v1_naive total_cost_usd |
| web page | 20 | `140` | 100 queries + conversation turns (data files) |
| web page | 20 | `$0.69` | summary.csv v2_full total_cost_usd |
| web page | 20 | `$1.95` | summary.csv v1_naive total_cost_usd |
| web page | 20 | `4.49` | summary.csv v2_full mean_quality |
| web page | 20 | `5` | quality scale top (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
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
| web page | 116 | `5` | quality scale top (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
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
| web page | 118 | `20` | per_answer_eval: answers improving >=2 v2_full -> cache_full_kb; judge_handcheck.md answers checked |
| web page | 118 | `140` | 100 queries + conversation turns (data files) |
| web page | 118 | `5` | quality scale top (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 119 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 119 | `$1.95` | summary.csv v1_naive total_cost_usd |
| web page | 119 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| web page | 120 | `$1.75` | summary.csv plus_route total_cost_usd |
| web page | 120 | `4.56` | summary.csv plus_route mean_quality; summary.csv plus_route mean_quality |
| web page | 121 | `$1.12` | summary.csv plus_retrieve total_cost_usd; summary.csv plus_trim total_cost_usd |
| web page | 121 | `4.34` | summary.csv plus_retrieve mean_quality; summary.csv plus_retrieve mean_quality |
| web page | 122 | `$1.12` | summary.csv plus_retrieve total_cost_usd; summary.csv plus_trim total_cost_usd |
| web page | 122 | `4.39` | summary.csv plus_trim mean_quality |
| web page | 123 | `$0.91` | summary.csv plus_tight_cache total_cost_usd |
| web page | 123 | `4.40` | summary.csv plus_tight_cache mean_quality |
| web page | 124 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 124 | `$0.69` | summary.csv v2_full total_cost_usd |
| web page | 124 | `4.49` | summary.csv v2_full mean_quality |
| web page | 125 | `$0.75` | summary.csv cache_full_kb total_cost_usd |
| web page | 125 | `4.80` | summary.csv cache_full_kb mean_quality |
| web page | 128 | `9` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank; kb.md sections (retriever chunks) |
| web page | 130 | `384` | MiniLM embedding dimensions |
| web page | 131 | `9` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank; kb.md sections (retriever chunks) |
| web page | 131 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 131 | `60` | config retrieval.rrf_k (fusion constant) |
| web page | 131 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 131 | `60` | config retrieval.rrf_k (fusion constant) |
| web page | 132 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 134 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 145 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 146 | `74%` | retrieval_recall right section found at k=1 |
| web page | 147 | `11%` | retrieval_recall share of manual sent at k=1 |
| web page | 150 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 151 | `89%` | retrieval_recall right section found at k=2 |
| web page | 152 | `22%` | retrieval_recall share of manual sent at k=2 |
| web page | 155 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 156 | `95%` | retrieval_recall right section found at k=3 |
| web page | 157 | `33%` | retrieval_recall share of manual sent at k=3 |
| web page | 160 | `4` | retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 161 | `96%` | retrieval_recall right section found at k=4 |
| web page | 162 | `44%` | retrieval_recall share of manual sent at k=4 |
| web page | 165 | `5` | quality scale top (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 166 | `97%` | retrieval_recall right section found at k=5 |
| web page | 167 | `56%` | retrieval_recall share of manual sent at k=5 |
| web page | 171 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 171 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 171 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 185 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 186 | `4` | retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 187 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 191 | `4` | retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 192 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 193 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 197 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 198 | `5` | quality scale top (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 199 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 203 | `5` | quality scale top (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 204 | `3` | config retrieval.top_k; retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 205 | `4` | retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 209 | `8` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 210 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 211 | `5` | quality scale top (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 215 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 216 | `7` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 217 | `6` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 221 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 221 | `7` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 221 | `6` | retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 223 | `12%` | routing_summary laya vs always_strong cost; router_head_summary zero-shot saving |
| web page | 223 | `4.60` | routing_summary laya mean_quality; effort_summary sonnet_low quality_complex |
| web page | 223 | `4.63` | summary.csv v1_naive mean_quality; routing_summary always_strong mean_quality |
| web page | 223 | `45` | routing_confusion laya simple->strong |
| web page | 223 | `62` | test_queries.csv label=simple |
| web page | 224 | `136` | llm_router tokens per query |
| web page | 224 | `1,176` | routing_summary llm_router p50_router_ms |
| web page | 224 | `194` | routing_summary laya p50_router_ms |
| web page | 225 | `0.2` | rule fixed in eval/run_routing_eval.py (complex gap <= 0.2) |
| web page | 225 | `0.50` | threshold_sweep recommended |
| web page | 225 | `4.32` | threshold_sweep quality_complex at recommended |
| web page | 225 | `4.00` | threshold_sweep quality_complex at next threshold |
| web page | 225 | `0.63` | router_head_summary laya_zero_shot@0.50 auc_haiku_ok |
| web page | 225 | `0.5` | AUC of a coin flip (definition) |
| web page | 225 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 228 | `270` | data/router_train.csv rows |
| web page | 229 | `37%` | router_head_qa train_haiku_ok_rate |
| web page | 231 | `100` | test_queries.csv rows |
| web page | 233 | `5` | quality scale top (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 233 | `100` | test_queries.csv rows |
| web page | 246 | `12%` | routing_summary laya vs always_strong cost; router_head_summary zero-shot saving |
| web page | 247 | `4.60` | routing_summary laya mean_quality; effort_summary sonnet_low quality_complex |
| web page | 248 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
| web page | 252 | `13%` | router_head_summary length_rule saving |
| web page | 253 | `4.59` | router_head_summary length_rule quality |
| web page | 254 | `23%` | router_head_summary length_rule share_to_haiku |
| web page | 258 | `15%` | router_head_summary minilm_head saving |
| web page | 259 | `4.58` | router_head_summary minilm_head quality |
| web page | 260 | `27%` | router_head_summary minilm_head share_to_haiku |
| web page | 264 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
| web page | 265 | `4.54` | router_head_summary laya_head quality |
| web page | 266 | `36%` | router_head_summary laya_head share_to_haiku |
| web page | 270 | `38%` | router_head_summary hindsight ceiling saving; router_head_summary hindsight_ceiling saving |
| web page | 271 | `4.68` | router_head_summary hindsight_ceiling quality |
| web page | 272 | `60%` | router_head_summary hindsight_ceiling share_to_haiku |
| web page | 276 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
| web page | 276 | `12%` | routing_summary laya vs always_strong cost; router_head_summary zero-shot saving |
| web page | 276 | `0.63` | router_head_summary laya_zero_shot@0.50 auc_haiku_ok |
| web page | 276 | `0.75` | router_head_summary laya_head auc_haiku_ok |
| web page | 276 | `2,000` | router_head_bootstrap resamples |
| web page | 276 | `1,991` | router_head_bootstrap resamples with extra saving > 0 |
| web page | 276 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 276 | `15` | router_head_bootstrap extra saving 95% CI high (points) |
| web page | 276 | `0.76` | router_head_summary length_rule auc_haiku_ok |
| web page | 276 | `13%` | router_head_summary length_rule saving |
| web page | 277 | `4.42` | routing_summary always_cheap quality_simple |
| web page | 277 | `4.79` | routing_summary always_strong quality_simple |
| web page | 277 | `38%` | router_head_summary hindsight ceiling saving; router_head_summary hindsight_ceiling saving |
| web page | 277 | `100` | test_queries.csv rows |
| web page | 278 | `12%` | routing_summary laya vs always_strong cost; router_head_summary zero-shot saving |
| web page | 278 | `4.60` | routing_summary laya mean_quality; effort_summary sonnet_low quality_complex |
| web page | 279 | `13%` | router_head_summary length_rule saving |
| web page | 279 | `4.59` | router_head_summary length_rule quality |
| web page | 280 | `15%` | router_head_summary minilm_head saving |
| web page | 280 | `4.58` | router_head_summary minilm_head quality |
| web page | 281 | `20%` | router_head_summary laya_head saving; router_head_summary laya_zero_shot@0.50 share_to_haiku |
| web page | 281 | `4.54` | router_head_summary laya_head quality |
| web page | 282 | `38%` | router_head_summary hindsight ceiling saving; router_head_summary hindsight_ceiling saving |
| web page | 282 | `4.68` | router_head_summary hindsight_ceiling quality |
| web page | 283 | `50` | effort_summary sample size; effort sample size (config effort_eval.sample) |
| web page | 283 | `30` | effort sample: simple questions (config) |
| web page | 283 | `20` | per_answer_eval: answers improving >=2 v2_full -> cache_full_kb; judge_handcheck.md answers checked |
| web page | 288 | `50` | effort_summary sample size; effort sample size (config effort_eval.sample) |
| web page | 298 | `$0.264` | effort_summary always_strong total_cost_usd |
| web page | 299 | `0` | effort_summary thinking-off thinking_tokens |
| web page | 300 | `4.62` | effort_summary always_strong mean_quality; effort_summary sonnet_medium mean_quality |
| web page | 301 | `4.45` | effort_summary always_strong quality_complex |
| web page | 302 | `2.5` | effort_summary always_strong p50 latency (s) |
| web page | 306 | `$0.241` | effort_summary sonnet_low total_cost_usd |
| web page | 307 | `1,683` | effort_summary sonnet_low thinking_tokens |
| web page | 308 | `4.66` | effort_summary sonnet_low mean_quality; effort_summary sonnet_high mean_quality |
| web page | 309 | `4.60` | routing_summary laya mean_quality; effort_summary sonnet_low quality_complex |
| web page | 310 | `2.3` | effort_summary sonnet_low p50 latency (s) |
| web page | 314 | `$0.259` | effort_summary sonnet_medium total_cost_usd |
| web page | 315 | `3,433` | effort_summary sonnet_medium thinking_tokens |
| web page | 316 | `4.62` | effort_summary always_strong mean_quality; effort_summary sonnet_medium mean_quality |
| web page | 317 | `4.50` | effort_summary sonnet_medium quality_complex |
| web page | 318 | `2.6` | effort_summary sonnet_medium p50 latency (s) |
| web page | 322 | `$0.307` | effort_summary sonnet_high total_cost_usd |
| web page | 323 | `8,335` | effort_summary sonnet_high thinking_tokens |
| web page | 324 | `4.66` | effort_summary sonnet_low mean_quality; effort_summary sonnet_high mean_quality |
| web page | 325 | `4.65` | effort_summary sonnet_high quality_complex |
| web page | 326 | `3.5` | effort_summary sonnet_high p50 latency (s) |
| web page | 330 | `9%` | effort: low vs thinking off |
| web page | 330 | `28%` | effort: high vs low cost |
| web page | 331 | `26%` | effort_combo laya_head + sonnet_low saving |
| web page | 331 | `50` | effort_summary sample size; effort sample size (config effort_eval.sample) |
| web page | 332 | `$0.264` | effort_summary always_strong total_cost_usd |
| web page | 332 | `4.62` | effort_summary always_strong mean_quality; effort_summary sonnet_medium mean_quality |
| web page | 333 | `$0.241` | effort_summary sonnet_low total_cost_usd |
| web page | 333 | `4.66` | effort_summary sonnet_low mean_quality; effort_summary sonnet_high mean_quality |
| web page | 334 | `$0.259` | effort_summary sonnet_medium total_cost_usd |
| web page | 334 | `4.62` | effort_summary always_strong mean_quality; effort_summary sonnet_medium mean_quality |
| web page | 335 | `$0.307` | effort_summary sonnet_high total_cost_usd |
| web page | 335 | `4.66` | effort_summary sonnet_low mean_quality; effort_summary sonnet_high mean_quality |
| web page | 336 | `1,683` | effort_summary sonnet_low thinking_tokens |
| web page | 336 | `8,335` | effort_summary sonnet_high thinking_tokens |
| web page | 336 | `8%` | cache_full_kb vs v2_full cost |
| web page | 336 | `2` | config history.keep_last_turns; router_head_bootstrap extra saving 95% CI low (points); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 336 | `140` | 100 queries + conversation turns (data files) |
| web page | 336 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 336 | `$5,368` | cache_full_kb cost per answer x 1M |
| web page | 336 | `1` | quality scale bottom (rubric); retrieval_recall k; retrieval_example keyword_rank; retrieval_example meaning_rank; retrieval_example combined_rank |
| web page | 336 | `$13,946` | v1 cost per answer x 1M |
| web page | 347 | `78%` | variance.csv judge re-score identical share |
| web page | 347 | `17` | judge_handcheck.md AGREE count |
| web page | 347 | `20` | per_answer_eval: answers improving >=2 v2_full -> cache_full_kb; judge_handcheck.md answers checked |
| web page | 347 | `100` | test_queries.csv rows |
| web page | 347 | `0.1` | noise floor stated from judge variance (mean |diff| 0.23 per answer) |
| web page | 347 | `140` | 100 queries + conversation turns (data files) |
