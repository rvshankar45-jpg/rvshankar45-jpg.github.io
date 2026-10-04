I cut an AI support bot's cost by 64%. The famous model router did only a sixth of it.

I built the same support copilot twice, a naive version and an optimised one, and measured every token across 140 answers.

Three numbers:

- $1.95 to $0.69 for the same 140 answers. Quality moved from 4.63 to 4.49 out of 5.
- Retrieval delivered half of the saving, and most of the quality loss.
- An off-the-shelf routing model saved 12%. Trained on 270 labelled examples, it saved 20%.

The insight: "simple" to a human is not "safe for the cheap model". The small model scored 4.42 on simple questions where the strong one scored 4.79. A router is only as good as the outcome it learned to predict.

The surprise: the short prompt plus the full policy document, cached, scored 4.80, beating the original, at 62% below its cost. Sometimes the fix is sending more, cheaply.

Token cost is a product decision, not an infra bill.

Full write-up, charts and open code: https://rvshankar45-jpg.github.io/same-bot-cheaper/

What is your team's cost per answer?
