"""Backend that calls Claude through the Claude Code CLI in headless mode (`claude -p`).

Why: this project runs on a Claude Code subscription instead of an API key.
The CLI returns the API's real `usage` block, but every call also carries a
small fixed harness overhead (instructions Claude Code always sends). We strip
it as far as the CLI allows (no tools, no MCP servers, no settings, no dynamic
prompt sections, thinking off) and measure what remains per model with
`calibrate()`, so payload tokens = reported total input - overhead.
"""
import json
import os
import shutil
import subprocess
import tempfile
import time
from functools import lru_cache

def _claude() -> str | None:
    # resolved per call: Claude Code can auto-update itself mid-run and briefly remove its launcher
    return shutil.which("claude.cmd") or shutil.which("claude")


CLAUDE = _claude()


def version() -> str:
    out = subprocess.run([_claude(), "--version"], capture_output=True, text=True, encoding="utf-8",
                         env={**os.environ, "DISABLE_AUTOUPDATER": "1"})
    return out.stdout.strip()
STRIP = ["--tools", "", "--strict-mcp-config", "--mcp-config", '{"mcpServers":{}}',
         "--setting-sources", "", "--exclude-dynamic-system-prompt-sections", "--no-session-persistence"]


PROBE_USER = "Reply with the single word OK."


class CLIError(RuntimeError):
    pass


def call(model: str, system: str, user: str, *, schema: dict | None = None, effort: str | None = None,
         thinking: bool = False, max_output_tokens: int | None = None, timeout: int = 600) -> dict:
    """One headless call. Returns text, structured output, raw usage and latency."""

    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False, encoding="utf-8") as f:
        f.write(system)
    cmd = ["<claude>", "-p", "--model", model, "--system-prompt-file", f.name, "--output-format", "json", *STRIP]
    if schema:
        cmd += ["--json-schema", json.dumps(schema)]
    if effort:
        cmd += ["--effort", effort]
    env = {**os.environ, "DISABLE_AUTOUPDATER": "1"}  # never self-update mid-experiment
    if not thinking:
        env["MAX_THINKING_TOKENS"] = "0"
    if max_output_tokens:
        env["CLAUDE_CODE_MAX_OUTPUT_TOKENS"] = str(max_output_tokens)
    t0 = time.perf_counter()
    try:
        for attempt in range(6):
            exe = _claude()
            try:
                if not exe:
                    raise FileNotFoundError("claude launcher not on PATH")
                out = subprocess.run([exe, *cmd[1:]], input=user, capture_output=True, text=True, encoding="utf-8",
                                     env=env, timeout=timeout)
                break
            except FileNotFoundError:
                if attempt == 5:
                    raise CLIError("claude CLI not found after retries (update in progress?)")
                time.sleep(20)
    finally:
        os.unlink(f.name)
    wall_ms = (time.perf_counter() - t0) * 1000
    try:
        d = json.loads(out.stdout)
    except json.JSONDecodeError:
        raise CLIError(f"non-JSON output (rc={out.returncode}): {out.stdout[:300]} {out.stderr[:300]}")
    # When the output cap is hit the CLI reports an error and drops the partial text, but the
    # usage block is still real. Return it flagged as capped instead of raising.
    capped = bool(d.get("is_error")) and "output token maximum" in str(d.get("result", ""))
    if (d.get("is_error") or d.get("subtype") != "success") and not capped:
        raise CLIError(f"CLI error: {d.get('subtype')} {d.get('result', '')[:300]} api_status={d.get('api_error_status')}")
    u = d["usage"]
    return {
        "model": model,
        "capped": capped,
        "text": "" if capped else d.get("result", ""),
        "structured": d.get("structured_output"),
        "stop_reason": d.get("stop_reason"),
        "input_tokens": u["input_tokens"],
        "cache_write_tokens": u.get("cache_creation_input_tokens") or 0,
        "cache_read_tokens": u.get("cache_read_input_tokens") or 0,
        "output_tokens": u["output_tokens"],
        "thinking_tokens": (u.get("output_tokens_details") or {}).get("thinking_tokens") or 0,
        "total_input_tokens": u["input_tokens"] + (u.get("cache_creation_input_tokens") or 0)
        + (u.get("cache_read_input_tokens") or 0),
        "api_ms": d.get("duration_api_ms"),
        "wall_ms": round(wall_ms),
        "raw_usage": u,
    }


@lru_cache(maxsize=None)
def overhead(model: str, schema_json: str | None = None) -> int:
    """Total input tokens of a call with system='.' and the fixed probe user message.
    Everything above this in a real call is our payload (to within a few tokens)."""
    schema = json.loads(schema_json) if schema_json else None
    return call(model, ".", PROBE_USER, schema=schema)["total_input_tokens"]


def system_tokens(model: str, system: str) -> int:
    """Server-counted tokens of a system prompt, harness overhead removed (CLI stand-in for count_tokens).
    Uses the same probe user message as overhead(), so it cancels out."""
    return call(model, system, PROBE_USER)["total_input_tokens"] - overhead(model)
