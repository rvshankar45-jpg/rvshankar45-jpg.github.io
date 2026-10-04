# I cut an AI support bot's cost by 64%. The famous router did a sixth of it.

*Same chatbot, built twice. 100 questions, 10 conversations, 140 answers, every token counted.*

Token cost is a product decision, not an infra bill. To see how much of it is waste, I built the same support copilot twice and measured both.

The optimised build answered the same 140 questions for **$0.69 instead of $1.95**: 64% cheaper, with 66% fewer tokens. Average quality moved from 4.63 to 4.49 out of 5. What surprised me was where the savings came from, and what the most talked-about technique actually delivered.

Token cost is one of the biggest brakes on LLM adoption. Before accepting it as the price of AI, I wanted to see how much of it can be engineered away.

## Why teams ship the expensive version

Version one of most AI features is built to ship. Send everything to the best model, paste in the whole manual, resend the whole chat. It works, so nobody touches it. Shipping beats tuning, everyone fears a quality drop they can't measure, and nobody owns cost per answer.

## Where tokens leak

1. **The wrong model**: every question goes to the strongest one.
2. **The whole manual**: the full policy document rides along on every call.
3. **The whole conversation**: history is resent in full every turn.
4. **The essay prompt**: 650 tokens of instructions where 170 do the job.
5. **The long answer**: no length guidance.
6. **The repeat question**: the same FAQ answered from scratch.

## What I built

A support copilot for Leafy, a fictional plant shop: a realistic policy document, 100 test questions (62 simple, 38 complex) and 10 multi-turn conversations. Version one has every leak. Version two fixes them one at a time, so each fix is its own measured step. A separate model graded every answer from 1 to 5 against a reference answer: 5 means send it as is, 3 means acceptable but flawed.

| Step added | Cost (140 answers) | Quality |
|---|---|---|
| v1: strongest model, full manual, full history | $1.95 | 4.63 |
| + routing: Laya sends easy questions to the cheap model | $1.75 | 4.56 |
| + retrieval: send only the 3 most relevant manual sections | $1.12 | 4.34 |
| + history: last 2 turns plus a summary | $1.12 | 4.39 |
| + short prompt, cached | $0.91 | 4.40 |
| + "be concise" and an answer cache = v2 | $0.69 | 4.49 |

```mermaid
flowchart LR
  Q[Customer message] --> C{Answer cache}
  C -- repeat --> A[Answer]
  C -- new --> L[Laya router<br/>local GPU]
  L -- easy --> H[Haiku 4.5]
  L -- hard --> S[Sonnet 5.5]
  K[(Policy manual)] -- top 3 sections --> P[Short prompt<br/>+ last 2 turns + summary]
  P --> H & S
  H & S --> A
```

## What happened

**Retrieval did half the work.** Sending three manual sections instead of the whole thing saved $0.63 of the $1.26. It also caused most of the quality loss: 14 answers dropped two points or more, usually because the right section wasn't retrieved and the model said, honestly, that it didn't know.

**Some fixes barely mattered.** Trimming history saved 0.5% of v1's cost. The prompt cache, which bills a repeated opening of the prompt at a tenth of the price, saved nothing in v2: the short prompt left only 203 repeatable tokens, under the 512 the cache needs. The answer cache never fired because no test question repeated; real FAQ traffic would differ.

**The surprise was a build I added myself.** The short prompt plus the *whole* manual, cached, scored 4.80, against v1's 4.63, at 62% below v1's cost. It fixed 20 answers by two points or more and made none worse. On this model, caching the manual beat searching it.

## Did Laya earn its place?

Laya is a small open-source decision model that runs on a laptop GPU. For each question it estimates whether the cheap model can handle it; above a cut-off score, the question goes to the strong model.

Out of the box, it saved **12%** against always using the strong model, at the same quality (4.60 vs 4.63). In the step-by-step build, routing delivered about a sixth of the total saving. It still sent 45 of the 62 simple questions to the expensive model.

It did beat the obvious alternative: asking the cheap model to classify each question first cost 136 extra tokens and 1,176 ms per question. Laya took 194 ms and no API tokens. Laya saves cost, not tokens; the same prompt simply goes to a cheaper model.

Then I trained it on 270 new questions, each labelled by whether the cheap model's answer held up. Laya's saving rose from **12% to 20%** at 4.54 quality. A router with perfect hindsight would save 38%.

"Simple" to a human isn't "safe for the cheap model": the cheap model scored 4.42 on simple questions where the strong model scored 4.79. A router is only as good as the outcome it learned to predict.

## The trade-off I had to make

The cut-off is a product call. I fixed the rule before looking: the cheapest setting where complex-question quality stays within 0.2 of always-strong. That picked 0.50. One notch higher, complex quality fell from 4.32 to 4.00.

The second dial is effort: how much hidden reasoning the strong model does before answering. On 50 questions, low effort was 9% cheaper than reasoning switched off, with no measurable quality difference. High effort spent 8,335 hidden reasoning tokens against 1,683 and cost 28% more for no measurable gain. Trained Laya plus low effort saved 26% at equal quality on the same 50.

## What I'd ship

I'd ship the cached whole-manual build, not v2. It cost 8% more than v2 and scored best of all builds, though on 140 synthetic answers read that as "at least as good as v1", not proof. Scaled to a million answers a month, that is about $5,368 against v1's $13,946.

Around it:

- **A quality guardrail**: score a sample of real answers every week.
- **Confidence-based escalation**: when the router is unsure, pay for the strong model.
- **Per-intent rules**: billing disputes and safety questions never go to the cheap model.
- **Cost per resolved ticket** as the north-star metric, not cost per call.
- **Drift monitoring**: re-label a slice of traffic monthly and retrain the router.

What I chose not to optimise: history trimming and high effort. The data says they aren't worth the complexity here.

## A reusable framework

Before any LLM call, ask:

1. **Does this need the smartest model?** Measure it; "simple" fooled me.
2. **Does it need all this context?** Cutting it was the biggest saving and the biggest risk.
3. **Have we answered this before?** Cache the repeated part, prompt or answer.

## Limitations

The data is synthetic, and one AI wrote both test and training questions, which flatters the trained router. An AI judge scored quality: re-scoring the same answers gave the identical score 78% of the time, and I agreed with 17 of 20 hand-checked scores. With 100 questions, gaps under 0.1 in average quality are noise. Laya ran off the shelf on a new domain, where its scores bunch together. Costs are list API prices; the million-answer figures scale up 140 synthetic answers. I measured through Claude Code's command line, subtracting the fixed overhead it adds to every call.

## Try it

Code, data and every result: [rvshankar45-jpg/Laya-model-router](https://github.com/rvshankar45-jpg/Laya-model-router).

What's your team's cost per answer? If you don't know, that's the first number to find.
