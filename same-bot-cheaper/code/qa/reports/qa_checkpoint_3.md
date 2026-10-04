# QA gate 3 (blog) - 2026-10-04 20:20

7/7 checks passed.

- **PASS** every number traces to results/ (or a stated design constant): 549 numbers across blog + LinkedIn post; unsourced=[]
- **PASS** word counts: blog 2408 words (900-2,500, raised from 1,200 at the author's request; tables, diagram code and placeholders excluded); LinkedIn 179 (150-200)
- **PASS** Laya described accurately (cost not tokens; limits stated): states 'Laya saves cost, not tokens', reports zero-shot vs trained honestly, and lists its new-domain limitation
- **PASS** claims match the data's direction (weak/mixed results stated as such): checked 11 directional claims; mismatched=[]
- **PASS** no invented quotes, stats or sources: links=['https://github.com/rvshankar45-jpg/Laya-model-router/blob/main/data/kb.md', 'https://github.com/rvshankar45-jpg/Laya-model-router/blob/main/data/kb.md', 'https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2', 'https://huggingface.co/convaiinnovations/laya', 'https://github.com/rvshankar45-jpg/Laya-model-router', 'https://rvshankar45-jpg.github.io/nothing-got-fixed/', 'https://rvshankar45-jpg.github.io/listing-ready-photos/', 'https://rvshankar45-jpg.github.io/same-bot-cheaper/'] (only the author's own repo and post); all statistics come from this repo's results
- **PASS** no real employer/customer/brand names; placeholders listed: denylist hits=[]; 0 placeholders: []
- **PASS** web page renders every table and has no stray control characters: tables in markdown=7, tables on page=7; control characters on page=0
