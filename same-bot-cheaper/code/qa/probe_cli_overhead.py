"""Probe how many hidden tokens the Claude Code CLI adds to a headless call,
and which flags strip them. Prints usage per flag set."""
import json
import os
import subprocess
import sys

STRIP = ["--strict-mcp-config", "--mcp-config", '{"mcpServers":{}}',
         "--setting-sources", "", "--exclude-dynamic-system-prompt-sections"]


def run(model, extra=(), env_extra=None, prompt="What is 2+2? Answer with just the number.", system="You are a calculator."):
    cmd = ["claude", "-p", prompt, "--model", model, "--system-prompt", system, "--tools", "",
           "--output-format", "json", "--no-session-persistence", *extra]
    env = {**os.environ, **(env_extra or {})}
    out = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", env=env, shell=(os.name == "nt"))
    d = json.loads(out.stdout)
    u = d["usage"]
    return {"in": u["input_tokens"], "cw": u["cache_creation_input_tokens"], "cr": u["cache_read_input_tokens"],
            "out": u["output_tokens"], "think": (u.get("output_tokens_details") or {}).get("thinking_tokens"),
            "ms": d["duration_api_ms"], "result": d["result"][:40]}


if __name__ == "__main__":
    model = sys.argv[1] if len(sys.argv) > 1 else "claude-haiku-4-5-20251001"
    cases = {
        "A plain": ([], None),
        "B no-mcp+no-settings+no-dyn": (STRIP, None),
        "C B + MAX_THINKING_TOKENS=0": (STRIP, {"MAX_THINKING_TOKENS": "0"}),
        "D repeat C": (STRIP, {"MAX_THINKING_TOKENS": "0"}),
    }
    for name, (extra, env) in cases.items():
        print(name, run(model, extra, env), flush=True)
