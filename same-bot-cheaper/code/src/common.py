"""Shared config / env loading. Paths are resolved relative to the repo root."""
from functools import lru_cache
from pathlib import Path

import yaml
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")


@lru_cache(maxsize=1)
def config() -> dict:
    with open(ROOT / "config.yaml", encoding="utf-8") as f:
        return yaml.safe_load(f)


def path(key: str) -> Path:
    return ROOT / config()["paths"][key]


def price(model: str) -> dict:
    return config()["pricing"][model]


def cost_usd(model: str, input_tokens=0, output_tokens=0, cache_read=0, cache_write=0) -> float:
    p = price(model)
    return (input_tokens * p["input"] + output_tokens * p["output"]
            + cache_read * p["cache_read"] + cache_write * p["cache_write"]) / 1_000_000
