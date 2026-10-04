"""v1 - the naive baseline, built the way many teams actually ship a first version:

- every query goes to the strong model
- the full kb.md is pasted into the system prompt on every call
- conversations resend the full history every turn
- a long, friendly ~600-token persona prompt with repeated instructions
- no output cap (only a generous safety ceiling) and no caching

It is the shared pipeline with every optimization flag off, so v1 and each v2 variant
differ only in the flags being compared.
"""
from src.llm import LLM
from src.v2_optimized import Pipeline

VARIANT = "v1_naive"


def build(llm: LLM) -> Pipeline:
    return Pipeline(flags=[], variant=VARIANT, llm=llm)
