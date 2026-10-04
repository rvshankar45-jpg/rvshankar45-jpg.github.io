"""Cost from token counts x the per-model prices in config.yaml (USD per million tokens)."""
from src.common import config


def rates(model: str) -> dict:
    return config()["pricing"][model]


def cost_usd(model: str, input_tokens: int = 0, output_tokens: int = 0,
             cache_read_tokens: int = 0, cache_write_tokens: int = 0) -> float:
    p = rates(model)
    return (input_tokens * p["input"] + output_tokens * p["output"]
            + cache_read_tokens * p["cache_read"] + cache_write_tokens * p["cache_write"]) / 1_000_000
