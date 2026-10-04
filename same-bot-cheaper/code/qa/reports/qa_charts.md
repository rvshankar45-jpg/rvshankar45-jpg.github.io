# QA gate - charts - 2026-10-04 14:47

6/6 checks passed.

- **PASS** plotted numbers match the CSVs (recomputed independently): 12 charts checked; mismatches=[]
- **PASS** every title's claim is true: all 12 titles re-derived from the CSVs and equal
- **PASS** waterfall bars sum to v1 - v2: sum of steps -1.257748 vs v2-v1 -1.257748
- **PASS** axes labelled with units; no misleading truncation: unlabelled=[]; bar axes not starting at 0 (or 1 = bottom of the 1-5 quality scale)=[]; chart 10 uses unit-bearing panel titles, 05 is a matrix; 07 is log-scale and says so
- **PASS** text readable and inside the image: smallest text 10.5pt (footer credit; data labels >= 12pt) on a 1800x1012 image; clipped=[]
- **PASS** every exported PNG opened and inspected: 12 PNGs inspected; 8 needed layout fixes, all re-inspected

## Visual inspection log

- 01_cost_waterfall: ok
- 02_tokens_per_answer: ok
- 03_quality_by_variant: fixed: title clipped; value labels collided with baseline -> moved inside bars
- 04_threshold_sweep: fixed: annotation collided with guard line and curve -> placed in empty area
- 05_routing_confusion: fixed: footer crowded x labels -> bottom margin
- 06_latency: fixed: legend covered a bar
- 07_projected_monthly_cost: fixed: '$' parsed as maths (garbled subtitle), log ticks, y label clipped
- 08_routing_scatter: fixed: two labels overlapped / truncated -> leader line
- 09_quality_simple_vs_complex: ok
- 10_router_overhead: fixed: title clipped
- 11_trained_router_head: ok
- 12_effort_levels: fixed: title clipped
