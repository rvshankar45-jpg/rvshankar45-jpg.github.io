# QA gate 1 (data) - 2026-09-29 23:04

Backend: Claude Code CLI (headless), judge claude-sonnet-5-5 effort=medium, batches of 25.

12/12 checks passed. Usage this run: 25 new CLI calls (3 cached verdicts reused), 100,024 input / 13,203 output tokens, API-equivalent $0.312

- **PASS** queries.csv structure: 100 rows, unique ids=True, missing cols=[], empty fields=0
- **PASS** label values and mix: simple=62, complex=38 (target 60/40 +/-5); invalid=[]; tiers={'simple': 62, 'medium': 28, 'complex': 10}
- **PASS** no duplicate / near-duplicate queries: exact dupes=0, pairs over 0.95=0; max cosine=0.796 (q037 vs q068)
- **PASS** CLI token measurement valid (constant overhead, additive counts): overhead per model={'claude-sonnet-5-5': [455], 'claude-haiku-4-5-20251001': [380]} over 3 calls; tokens(A+B)-tokens(A)-tokens(B)={'claude-sonnet-5-5': 0, 'claude-haiku-4-5-20251001': 0} (tolerance 2)
- **PASS** kb.md token count (server-counted, overhead removed): 3636 tokens on claude-sonnet-5-5; 2662 on claude-haiku-4-5-20251001; target 3000-4000 on the strong model (v1 sends kb.md to it)
- **PASS** reference answers grounded in kb.md (judge): 140/140 supported and on-question
- **PASS** batched grading agrees with single-item grading (3 spot checks): ['q001', 'q065', 'q091'] identical verdicts batched vs single
- **PASS** blind re-label: every disagreement resolved: agreement 99% (1 disagreements, all kept with written reason: ['q088']); unresolved=[]; previously relabelled to match judge: ['q077', 'q078', 'q080', 'q081', 'q083', 'q084', 'q087']
- **PASS** conversations.json structure: 10 conversations, turns per conversation=[4, 4, 4, 4, 5, 3, 3, 4, 5, 4]
- **PASS** later conversation turns depend on earlier context (judge): 30/30 later turns need prior context
- **PASS** denylist scan for real brands / employers: denylist hits=[], other emails=[]
- **PASS** model scan for real brand / employer / person names: findings=[]
