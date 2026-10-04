# I cut an AI support bot's cost by 64%. The famous router did a sixth of it.

*Same chatbot, built twice. 140 answers each, every token counted.*

Token cost is one of the biggest brakes on LLM adoption. Before accepting it as the price of AI, I wanted to see how much of it can be engineered away. So I built one small AI app twice, a quick version and a careful one, and measured what each costs to run.

## How this works, in one minute

**The app.** A customer-support chatbot for Leafy, a made-up online plant shop. A customer asks something like "What's your return window?" or "My plant arrived dead and I was charged twice", and the bot answers from Leafy's policy manual, a document of about 3,600 tokens in 9 sections. It runs on Anthropic's Claude models; everything is invented.

**Two versions.** Version 1 is built the quick way: every question goes to the strongest, most expensive model (Sonnet 5.5), with the whole manual and the whole chat attached. Version 2 adds six cost-saving fixes, one at a time.

**The test.** Both versions answer the same 100 customer questions (62 simple, 38 complex) and 10 back-and-forth conversations: 140 answers each.

**Counting tokens and cost.** AI models bill per token (about three-quarters of a word), for text sent and text written back. For every answer I recorded the token counts reported by the model provider, not estimates, and multiplied them by the published prices: Sonnet 5.5 costs $2 per million tokens sent and $10 per million written; the cheaper Haiku 4.5 costs $1 and $5. Adding up 140 answers gives each version's bill.

**Checking quality.** Cheaper is worthless if answers get worse. A separate AI grader scored every answer from 1 to 5 against a reference answer written from the manual: 5 means send it as is, 3 means acceptable but flawed.

## The short version

1. **64% cheaper.** Version 2 answered the same 140 questions for $0.69 instead of $1.95, with quality almost unchanged: 4.49 against 4.63 out of 5.
2. **Half the saving came from sending less.** Giving the model only the relevant part of the manual saved more than any other fix. It also caused most of the quality drop.
3. **The best build kept the whole manual.** Short instructions plus the full manual, stored in the provider's cache, were 62% cheaper than version 1 and scored highest of all: 4.80.
4. **The famous model router saved 12%.** After I trained it on 270 examples, it saved 20%.
5. **Thinking harder didn't pay.** Letting the expensive model think a little (low effort) was the cheapest setting at the same quality. High effort cost 28% more for no measurable gain.

## Why teams ship the expensive version

Version one of most AI features is built to ship: best model, whole manual, whole chat. It works, so nobody touches it. Shipping beats tuning, a quality drop nobody can measure feels risky, and nobody owns cost per answer. But token cost is a product decision, not an infra bill.

## The six fixes, explained

Each fix targets one way tokens leak:

| Where tokens leak | The fix in version 2 |
|---|---|
| Every question goes to the expensive model | **Routing:** a small local model, Laya, sends easy questions to the cheap model |
| The whole manual is sent with every question | **Retrieval:** send only the 3 manual sections most related to the question |
| The whole conversation is resent every turn | **History trimming:** keep the last 2 turns plus a short summary |
| 650 tokens of instructions where 170 do the job | **Short prompt:** a 170-token version |
| The same opening text is paid for at full price every time | **Prompt cache:** the provider stores repeated opening text and bills it at a tenth of the price |
| Answers run long; repeat questions start from scratch | **Concise answers + answer cache:** a "be concise" instruction and length cap, and reuse of answers to repeated questions |

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

## What each fix saved

Each row adds one fix and re-runs the whole test:

| Step | Cost (140 answers) | Quality |
|---|---|---|
| Version 1 | $1.95 | 4.63 |
| + routing | $1.75 | 4.56 |
| + retrieval | $1.12 | 4.34 |
| + history trimming | $1.12 | 4.39 |
| + short prompt and prompt cache | $0.91 | 4.40 |
| + concise answers and answer cache = version 2 | $0.69 | 4.49 |

**Retrieval did half the work.** Sending three sections instead of all nine saved $0.63 of the $1.26. It also cost the most quality: 14 answers dropped two points or more, usually because the right section was missed and the model honestly said it didn't know.

**Some fixes barely mattered.** Trimming history saved 0.5% of version 1's cost. The prompt cache saved nothing: the short prompt left only 203 repeatable tokens, under the 512 the cache needs. The answer cache never fired because no test question repeated. The last step's saving came from shorter answers.

**The surprise was a build I added myself:** the short prompt plus the *whole* manual, cached. It scored 4.80, against version 1's 4.63, at 62% below version 1's cost. It fixed 20 answers by two points or more and made none worse. On this model, caching the manual beat searching it.

## Does a smarter router help?

Laya is a small open-source decision model that runs on a laptop GPU. It scores each question for difficulty; above a cut-off, the question goes to the expensive model.

Out of the box, it saved **12%** against always using the expensive model, at the same quality (4.60 vs 4.63): about a sixth of the total saving. It still sent 45 of the 62 simple questions to the expensive model.

It beat asking the cheap model to classify each question first, which cost 136 extra tokens and 1,176 ms per question; Laya took 194 ms and no API tokens. Laya saves cost, not tokens: the same prompt simply goes to a cheaper model.

Then I trained it on 270 new questions, each labelled by whether the cheap model's answer held up. Its saving rose from **12% to 20%** at 4.54 quality. A router with perfect hindsight would save 38%.

The lesson: "simple" to a human isn't "safe for the cheap model". The cheap model scored 4.42 on simple questions where the expensive model scored 4.79. A router is only as good as the outcome it learned to predict.

The cut-off is a product call. I fixed the rule before looking: the cheapest setting where quality on complex questions stays within 0.2 of always-expensive. That picked 0.50. One notch higher, complex quality fell from 4.32 to 4.00.

## Should the expensive model think harder?

Newer models can reason privately before answering. You choose how much with an "effort" setting, and you pay for that hidden thinking as output tokens without ever seeing them. I ran the expensive model at each setting on 50 of the questions (30 simple, 20 complex):

| Thinking setting | Cost (50 questions) | Hidden thinking tokens | Quality | Complex questions | Typical wait |
|---|---|---|---|---|---|
| Off | $0.264 | 0 | 4.62 | 4.45 | 2.5 s |
| Low | $0.241 | 1,683 | 4.66 | 4.60 | 2.3 s |
| Medium | $0.259 | 3,433 | 4.62 | 4.50 | 2.6 s |
| High | $0.307 | 8,335 | 4.66 | 4.65 | 3.5 s |

**Low effort was the cheapest and fastest setting**, 9% below thinking off at the same quality, because its visible answers were shorter. High effort used five times the hidden tokens of low and cost 28% more for no measurable gain; its small edge on complex questions is within noise on 20 questions.

Routing and effort stack: the trained Laya router plus low-effort thinking saved 26% at equal quality on these 50 questions.

## What I'd ship

I'd ship the cached whole-manual build, and test it with low-effort thinking, a pairing I haven't measured yet. It cost 8% more than version 2 and scored best, though on 140 synthetic answers read that as "at least as good as version 1". At a million answers a month: about $5,368 against version 1's $13,946.

Around it:

- **A quality guardrail**: score a sample of real answers every week.
- **Escalation**: when the router is unsure, pay for the expensive model.
- **Per-intent rules**: billing disputes and safety questions never go to the cheap model.
- **Cost per resolved ticket** as the north-star metric, not cost per call.
- **Drift monitoring**: re-label traffic monthly and retrain the router.

Not worth optimising here: history trimming and high effort.

## A reusable checklist

Before any LLM call, ask:

1. **Does this need the smartest model?** Measure it; "simple" fooled me.
2. **Does it need all this context?** Cutting it was the biggest saving and the biggest risk.
3. **Have we answered this before?** Cache the repeated part, prompt or answer.

## Limitations

The data is synthetic, and one AI wrote both test and training questions, which flatters the trained router. An AI judge scored quality: re-scoring the same answers gave the identical score 78% of the time, and I agreed with 17 of 20 hand-checked scores. With 100 questions, gaps under 0.1 in average quality are noise. Laya ran off the shelf on a new domain, where its scores bunch together. Million-answer figures scale up 140 synthetic answers. I ran the models through Claude Code's command line and subtracted the fixed overhead it adds to every call.

## Try it

Code, data and every result: [rvshankar45-jpg/Laya-model-router](https://github.com/rvshankar45-jpg/Laya-model-router).

What's your team's cost per answer? If you don't know, that's the first number to find.

## More writing

- [They answered 99% of the angry reviews. Nothing got fixed.](https://rvshankar45-jpg.github.io/nothing-got-fixed/) Do delivery apps fix what users complain about in their reviews?
- [Better listing photos, without asking sellers for more.](https://rvshankar45-jpg.github.io/listing-ready-photos/) Can open image models clean up second-hand listing photos as well as GPT?
