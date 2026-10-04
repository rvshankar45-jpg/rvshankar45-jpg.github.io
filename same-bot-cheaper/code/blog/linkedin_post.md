Token cost is one of the quiet reasons AI features never leave the pilot stage.

So instead of accepting it as the price of AI, I tested how much of it can be engineered away.

I took one AI support bot and ran it two ways: the quick build most teams ship first, and a careful one. Same 140 answers, every token counted.

What I found:

- $1.95 became $0.69. That's 64% cheaper. Quality moved from 4.63 to 4.49 out of 5.
- Sending less context (RAG) did half the work.
- The famous model router (Laya) saved 12% off the shelf. Trained on 270 labelled examples, it saved 20%.

The lesson for product teams: "simple" to a human is not "safe for the cheap model". On simple questions the small model scored 4.42; the strong one scored 4.79.

The surprise: caching the whole policy manual scored 4.80, better than the original, at 62% below its cost. Sometimes the fix is sending more, cheaply.

Token cost is a product decision, not an infra bill.

Full write-up, charts and open code: https://rvshankar45-jpg.github.io/same-bot-cheaper/

What does one answer cost your team?
