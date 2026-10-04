"""Probe: stdin prompt, --system-prompt-file, --json-schema, and caching of a large system prompt."""
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CLAUDE = shutil.which("claude.cmd") or shutil.which("claude")
STRIP = ["--strict-mcp-config", "--mcp-config", '{"mcpServers":{}}',
         "--setting-sources", "", "--exclude-dynamic-system-prompt-sections"]


def run(model, system, user, extra=()):
    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False, encoding="utf-8") as f:
        f.write(system)
    cmd = [CLAUDE, "-p", "--model", model, "--system-prompt-file", f.name, "--tools", "",
           "--output-format", "json", "--no-session-persistence", *STRIP, *extra]
    out = subprocess.run(cmd, input=user, capture_output=True, text=True, encoding="utf-8",
                         env={**os.environ, "MAX_THINKING_TOKENS": "0"})
    os.unlink(f.name)
    if out.returncode:
        print("ERR", out.stderr[:500], out.stdout[:500])
        return None
    return json.loads(out.stdout)


def show(tag, d):
    u = d["usage"]
    print(tag, {"in": u["input_tokens"], "cw": u["cache_creation_input_tokens"], "cr": u["cache_read_input_tokens"],
                "out": u["output_tokens"], "think": (u.get("output_tokens_details") or {}).get("thinking_tokens"),
                "ms": d["duration_api_ms"]}, "| result:", repr(d.get("result", "")[:80]),
          "| structured:", d.get("structured_output"), flush=True)


kb = (ROOT / "data" / "kb.md").read_text(encoding="utf-8")
H, S = "claude-haiku-4-5-20251001", "claude-sonnet-5-5"
long_user = "Summarise in 5 words: " + ("plants need light and water. " * 1500)  # ~45k chars via stdin
show("stdin-long haiku", run(H, "You are terse.", long_user))
schema = json.dumps({"type": "object", "additionalProperties": False, "required": ["answer"],
                     "properties": {"answer": {"type": "integer"}}})
show("json-schema haiku", run(H, "You are a calculator.", "What is 2+2?", ["--json-schema", schema]))
for i in range(2):
    show(f"KB system sonnet #{i+1}", run(S, kb, "What is the return window? One sentence."))
for i in range(2):
    show(f"KB system haiku #{i+1}", run(H, kb, "What is the return window? One sentence."))
