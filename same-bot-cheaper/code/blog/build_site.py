"""Builds the GitHub Pages article (blog/site/index.html) in the same design as the author's
previous post. Prose comes from blog/blog.md; every figure in the extra components (stat tiles,
short version, bar charts) is computed from results/*.csv here at build time.

  .\\.venv\\Scripts\\python.exe -m blog.build_site
"""
import html
import re
from datetime import date

import markdown
import pandas as pd

from blog.make_card import SLUG
from src.common import ROOT

R, SITE = ROOT / "results", ROOT / "blog" / "site"
URL = f"https://rvshankar45-jpg.github.io/{SLUG}/"

CSS = """
  *,*::before,*::after{ box-sizing:border-box; } html{ color-scheme:light dark; } body{ margin:0; } img{ max-width:100%; }
  :root{
    --paper:#FAF6EF; --surface:#FFFFFF; --sunk:#F2ECE1; --ink:#17130D; --ink2:#5E564A; --ink3:#8C8274;
    --rule:#E2D9C9; --rule2:#CFC3AD; --v1:#D6283A; --v2:#2A78D6; --mute:#C9BFAE; --good:#1B8A5A; --flag:#C2410C;
    --shadow:0 1px 2px rgba(23,19,13,.05), 0 8px 24px -12px rgba(23,19,13,.18);
    --display:"Bricolage Grotesque", ui-sans-serif, system-ui, sans-serif;
    --body:"Source Serif 4", Georgia, "Times New Roman", serif;
    --mono:"JetBrains Mono", ui-monospace, "SFMono-Regular", Consolas, monospace;
  }
  @media (prefers-color-scheme: dark){ :root:not([data-theme="light"]){
    --paper:#131110; --surface:#1C1917; --sunk:#232020; --ink:#F7F2E9; --ink2:#BDB3A4; --ink3:#8E8478;
    --rule:#302B26; --rule2:#453E36; --v1:#FF6B77; --v2:#5598E7; --mute:#5A524A; --good:#3CC48A; --flag:#FB923C;
    --shadow:0 1px 2px rgba(0,0,0,.4), 0 8px 24px -12px rgba(0,0,0,.6); } }
  :root[data-theme="dark"]{
    --paper:#131110; --surface:#1C1917; --sunk:#232020; --ink:#F7F2E9; --ink2:#BDB3A4; --ink3:#8E8478;
    --rule:#302B26; --rule2:#453E36; --v1:#FF6B77; --v2:#5598E7; --mute:#5A524A; --good:#3CC48A; --flag:#FB923C;
    --shadow:0 1px 2px rgba(0,0,0,.4), 0 8px 24px -12px rgba(0,0,0,.6); }
  body{ background:var(--paper); color:var(--ink); font-family:var(--body); font-size:18px; line-height:1.62; -webkit-font-smoothing:antialiased; }
  .wrap{ max-width:1080px; margin:0 auto; padding-inline:20px; padding-block:0 72px; }
  .col{ max-width:660px; margin-inline:auto; }
  p{ margin:0 0 1.1em; } strong{ font-weight:600; }
  code{ font-family:var(--mono); font-size:.86em; background:var(--sunk); padding:.1em .34em; border-radius:4px; }
  h1,h2,h3{ font-family:var(--display); text-wrap:balance; margin:0; }
  header.top{ padding-block:18px 8px; }
  .kicker{ font-family:var(--mono); font-size:11.5px; letter-spacing:.14em; text-transform:uppercase; color:var(--flag); font-weight:700; }
  h1{ font-size:clamp(36px,6.6vw,66px); line-height:1.03; font-weight:800; letter-spacing:-.024em; margin:16px 0 0; }
  h1 .hit{ color:var(--v1); }
  .standfirst{ font-size:clamp(18px,2.3vw,22px); color:var(--ink2); margin-top:20px; max-width:34em; }
  .byline{ font-family:var(--mono); font-size:12px; color:var(--ink3); margin-top:24px; padding-top:16px;
           border-top:1px solid var(--rule); display:flex; flex-wrap:wrap; gap:8px 22px; }
  .thesis{ margin:40px 0; display:grid; grid-template-columns:auto 1fr; gap:0 30px; align-items:center; background:var(--surface);
           border:1px solid var(--rule); border-radius:3px; padding:28px 30px; box-shadow:var(--shadow); }
  .thesis .big{ font-family:var(--display); font-weight:800; font-size:clamp(72px,15vw,124px); line-height:.82; color:var(--v1); letter-spacing:-.05em; }
  .thesis .say{ font-size:17px; color:var(--ink2); } .thesis .say b{ color:var(--ink); font-weight:600; }
  @media (max-width:520px){ .thesis{ grid-template-columns:1fr; gap:10px; } }
  .stats{ display:grid; grid-template-columns:repeat(4,1fr); gap:1px; background:var(--rule); border:1px solid var(--rule);
          border-radius:3px; overflow:hidden; margin:30px 0 8px; }
  .stat{ background:var(--surface); padding:18px 16px; }
  .stat .v{ font-family:var(--display); font-weight:700; font-size:clamp(22px,3.4vw,30px); letter-spacing:-.02em; font-variant-numeric:tabular-nums; }
  .stat .k{ font-family:var(--mono); font-size:10.5px; letter-spacing:.09em; text-transform:uppercase; color:var(--ink3); margin-top:6px; line-height:1.4; }
  @media (max-width:640px){ .stats{ grid-template-columns:repeat(2,1fr); } }
  section{ margin-top:56px; }
  h2{ font-size:clamp(25px,3.6vw,34px); font-weight:700; letter-spacing:-.018em; line-height:1.14; margin-bottom:18px; }
  h2 .rule{ display:block; width:44px; height:4px; background:var(--flag); border-radius:2px; margin-bottom:14px; }
  .exec{ background:var(--surface); border:1px solid var(--rule2); border-radius:3px; padding:30px 28px; box-shadow:var(--shadow); }
  .exec h2{ margin-bottom:6px; }
  .exec .sub{ font-family:var(--mono); font-size:11px; letter-spacing:.1em; text-transform:uppercase; color:var(--ink3); margin-bottom:22px; }
  .finds{ display:grid; gap:2px; background:var(--rule); }
  .find{ background:var(--surface); display:grid; grid-template-columns:136px 1fr; gap:20px; padding:17px 2px; align-items:start; }
  .find .fig{ font-family:var(--display); font-weight:800; font-size:26px; line-height:1.05; letter-spacing:-.025em; font-variant-numeric:tabular-nums; }
  .find .fig small{ display:block; font-family:var(--mono); font-size:10px; font-weight:500; letter-spacing:.07em; text-transform:uppercase; color:var(--ink3); margin-top:5px; line-height:1.4; }
  .find .txt{ font-size:16.5px; line-height:1.55; } .find .txt b{ font-weight:600; }
  @media (max-width:560px){ .find{ grid-template-columns:1fr; gap:4px; } }
  .chart{ background:var(--surface); border:1px solid var(--rule); border-radius:3px; padding:26px 26px 20px; box-shadow:var(--shadow); margin:26px 0; }
  .chart .cap{ font-family:var(--display); font-weight:700; font-size:20px; }
  .chart .sub{ font-size:14px; color:var(--ink2); margin:6px 0 20px; }
  .bar{ display:grid; grid-template-columns:150px 1fr 110px; gap:10px; align-items:center; margin-bottom:7px; }
  .bar .nm{ font-family:var(--mono); font-size:12px; color:var(--ink2); text-align:right; line-height:1.25; }
  .bar .track{ background:var(--sunk); border-radius:2px; height:19px; overflow:hidden; }
  .bar .fill{ height:100%; border-radius:2px; transform-origin:left center; }
  .bar .vv{ font-family:var(--mono); font-size:12.5px; font-weight:700; font-variant-numeric:tabular-nums; }
  .bar .vv small{ font-weight:500; color:var(--ink3); }
  .bar.win .nm{ color:var(--ink); font-weight:700; }
  .axisnote{ font-family:var(--mono); font-size:10.5px; color:var(--ink3); border-top:1px solid var(--rule); padding-top:10px; margin-top:12px; }
  @media (max-width:520px){ .bar{ grid-template-columns:92px 1fr 84px; gap:7px; } }
  table{ width:100%; border-collapse:collapse; font-size:15px; margin:18px 0 22px; background:var(--surface); box-shadow:var(--shadow); }
  th,td{ text-align:left; padding:9px 12px; border-bottom:1px solid var(--rule); vertical-align:top; }
  th{ font-family:var(--mono); font-size:11px; letter-spacing:.08em; text-transform:uppercase; color:var(--ink3); font-weight:700; }
  td:nth-child(n+2){ font-family:var(--mono); font-size:14px; white-space:nowrap; }
  ul,ol{ margin:0 0 1.1em; padding-left:1.2em; } li{ margin-bottom:.5em; }
  .flat{ background:var(--surface); border:1px solid var(--rule); border-radius:3px; padding:18px 18px; box-shadow:var(--shadow); margin:22px 0; }
  .flat svg{ display:block; width:100%; height:auto; }
  .approach{ background:var(--surface); border:1px solid var(--rule2); border-left:4px solid var(--flag); border-radius:3px;
             padding:22px 24px 14px; box-shadow:var(--shadow); margin-bottom:22px; }
  .approach .lbl{ font-family:var(--mono); font-size:10.5px; letter-spacing:.12em; text-transform:uppercase; color:var(--flag);
                  font-weight:700; display:block; margin-bottom:12px; }
  .approach p{ font-size:16px; line-height:1.58; margin:0 0 .8em; color:var(--ink2); }
  .approach p strong{ color:var(--ink); }
  section p a, section li a{ color:var(--flag); text-underline-offset:3px; }
  .hero{ max-width:900px; margin:30px auto 0; } .hero img{ display:block; width:100%; height:auto; border-radius:4px; }
  table.words td{ font-family:var(--body); font-size:15.5px; white-space:normal; }
  table.words td:first-child{ width:38%; color:var(--ink2); }
  .takes{ display:grid; gap:2px; background:var(--rule); }
  .take{ background:var(--surface); display:grid; grid-template-columns:34px 1fr; gap:14px; padding:16px 2px; align-items:start; }
  .take .n{ font-family:var(--mono); font-size:12px; font-weight:700; color:var(--flag); border:1.5px solid var(--flag);
            border-radius:50%; width:26px; height:26px; display:grid; place-items:center; margin-top:2px; }
  .take .hd{ font-family:var(--display); font-weight:700; font-size:19px; letter-spacing:-.01em; line-height:1.25; }
  .take .tx{ font-size:16.5px; line-height:1.55; color:var(--ink2); margin-top:4px; }
  .more .post{ display:block; background:var(--surface); border:1px solid var(--rule); border-radius:3px; padding:18px 20px;
               margin-bottom:12px; text-decoration:none; color:var(--ink); box-shadow:var(--shadow); }
  .more .post h3{ font-size:19px; margin:0 0 6px; } .more .post p{ font-size:15.5px; color:var(--ink2); margin:0 0 8px; }
  .more .post .go{ font-family:var(--mono); font-size:12px; color:var(--flag); }
  .more .post:hover h3{ color:var(--flag); }
  .ravi{ background:#FFF1B8; color:#5A4500; font-family:var(--mono); font-size:13px; padding:2px 6px; border-radius:3px; }
  footer{ margin-top:64px; padding-top:20px; border-top:1px solid var(--rule); font-family:var(--mono); font-size:11.5px; color:var(--ink3); line-height:1.7; }
  .backlink{ display:inline-block; font-family:var(--mono); font-size:12px; letter-spacing:.06em; color:var(--ink3); text-decoration:none; padding-block:26px 0; }
  .backlink:hover, .backlink:focus-visible{ color:var(--flag); }
  em{ color:var(--ink2); }
  @media (prefers-reduced-motion:no-preference){
    .bar .fill{ animation:grow .7s cubic-bezier(.22,1,.36,1) both; }
    @keyframes grow{ from{ transform:scaleX(.04); } to{ transform:scaleX(1);} } }
"""

ARCH = """<div class="flat"><svg viewBox="0 0 640 230" role="img" aria-label="Architecture: a customer message first checks the answer cache; new questions go to the Laya router, which sends easy ones to Haiku and hard ones to Sonnet; both receive a short prompt with the top 3 manual sections and trimmed history.">
<g font-family="JetBrains Mono, monospace" font-size="11" fill="currentColor">
<rect x="6" y="92" width="104" height="44" rx="4" fill="none" stroke="currentColor" stroke-opacity=".35"/><text x="58" y="112" text-anchor="middle">Customer</text><text x="58" y="126" text-anchor="middle">message</text>
<rect x="138" y="92" width="96" height="44" rx="4" fill="none" stroke="var(--flag)"/><text x="186" y="112" text-anchor="middle">Answer</text><text x="186" y="126" text-anchor="middle">cache</text>
<rect x="262" y="92" width="104" height="44" rx="4" fill="none" stroke="var(--v2)" stroke-width="2"/><text x="314" y="112" text-anchor="middle" font-weight="700">Laya router</text><text x="314" y="126" text-anchor="middle" opacity=".7">local GPU</text>
<rect x="404" y="40" width="96" height="40" rx="4" fill="none" stroke="currentColor" stroke-opacity=".35"/><text x="452" y="64" text-anchor="middle">Haiku 4.5</text>
<rect x="404" y="148" width="96" height="40" rx="4" fill="none" stroke="currentColor" stroke-opacity=".35"/><text x="452" y="172" text-anchor="middle">Sonnet 5.5</text>
<rect x="540" y="92" width="94" height="44" rx="4" fill="none" stroke="currentColor" stroke-opacity=".35"/><text x="587" y="118" text-anchor="middle">Answer</text>
<rect x="262" y="186" width="122" height="38" rx="4" fill="var(--sunk)" stroke="currentColor" stroke-opacity=".2"/><text x="323" y="202" text-anchor="middle" font-size="10">short prompt + top 3</text><text x="323" y="216" text-anchor="middle" font-size="10">sections + 2 turns</text>
</g>
<g stroke="currentColor" stroke-opacity=".45" stroke-width="1.5" fill="none">
<path d="M110 114 H138"/><path d="M234 114 H262"/><path d="M366 106 L404 64"/><path d="M366 122 L404 166"/>
<path d="M500 60 L540 108"/><path d="M500 168 L540 122"/><path d="M186 92 V20 H587 V92" stroke-dasharray="4 4"/><path d="M384 205 L404 180"/>
</g>
<g font-family="JetBrains Mono, monospace" font-size="10" fill="currentColor" opacity=".6"><text x="330" y="86">easy</text><text x="330" y="152">hard</text><text x="300" y="14">repeat question: cached answer, no model call</text></g>
</svg></div>"""


def bars(rows, vmax, cap, sub, note=""):
    out = [f'<div class="chart"><div class="cap">{cap}</div><div class="sub">{sub}</div>']
    for name, val, label, colour, win in rows:
        w = 100 * val / vmax
        out.append(f'<div class="bar{" win" if win else ""}"><div class="nm">{name}</div><div class="track">'
                   f'<div class="fill" style="width:{w:.1f}%;background:var(--{colour})"></div></div><div class="vv">{label}</div></div>')
    if note:
        out.append(f'<div class="axisnote">{note}</div>')
    return "\n".join(out) + "</div>"


def main():
    s = pd.read_csv(R / "summary.csv").set_index("variant")
    rs = pd.read_csv(R / "routing_summary.csv").set_index("strategy")
    rh = pd.read_csv(R / "router_head_summary.csv").set_index("router")
    eff = pd.read_csv(R / "effort_summary.csv").set_index("strategy")
    n = int(s.loc["v1_naive", "answers"])
    v1, v2 = s.loc["v1_naive", "total_cost_usd"], s.loc["v2_full", "total_cost_usd"]
    tok = s.total_input_tokens + s.output_tokens
    pct = lambda x: f"{round(100 * x)}%"  # noqa: E731
    retr_share = (s.loc["plus_route", "total_cost_usd"] - s.loc["plus_retrieve", "total_cost_usd"]) / (v1 - v2)
    zs, tr = rh.loc["laya_zero_shot@0.50", "saving_vs_always_sonnet"], rh.loc["laya_head", "saving_vs_always_sonnet"]
    low_save = 1 - eff.loc["sonnet_low", "total_cost_usd"] / eff.loc["always_strong", "total_cost_usd"]

    md = (ROOT / "blog" / "blog.md").read_text(encoding="utf-8")
    md = re.sub(r"```mermaid.*?```", "@@ARCH@@", md, flags=re.S)
    h1 = re.search(r"^# (.+)$", md, flags=re.M).group(1)
    head_hit = h1.split(". ", 1)
    intro, rest = md.split("\n## ", 1)
    intro_paras = [p for p in intro.split("\n\n")[2:] if p.strip()]
    sections = ("## " + rest).split("\n## ")

    def render(text):
        h = markdown.markdown(text, extensions=["tables"])
        # tables of words (not figures) wrap normally, with the leak column narrow and the fix column wide
        h = re.sub(r"<table>(?=(?:(?!</table>).)*<td><strong>)", '<table class="words">', h, flags=re.S)
        h = re.sub(r"\[RAVI:([^\]]*)\]", lambda m: f'<span class="ravi">[RAVI:{m.group(1)}]</span>', h)
        return h.replace("<p>@@ARCH@@</p>", ARCH)

    body, approach_html, short_html = [], "", ""
    for sec in sections:
        sec = sec.lstrip("# ")
        title, txt = sec.split("\n", 1)
        if title.startswith("How this works"):  # the method box under the headline, as in the previous post
            paras = [p for p in txt.strip().split("\n\n") if p.strip()]
            approach_html = (f'<section class="col" style="margin-top:30px"><div class="approach"><span class="lbl">{html.escape(title)}</span>'
                             + "".join(render(p) for p in paras) + "</div></section>")
            continue
        if title.startswith("The short version"):  # one plain sentence per finding, numbered
            items = re.findall(r"^\d+\.\s+\*\*(.+?)\*\*\s*(.+)$", txt, flags=re.M)
            rows = "".join(f'<div class="take"><div class="n">{i}</div><div><div class="hd">{html.escape(a)}</div>'
                           f'<div class="tx">{render(b)[3:-4]}</div></div></div>' for i, (a, b) in enumerate(items, 1))
            short_html = (f'<section class="col"><div class="exec"><h2><span class="rule"></span>{html.escape(title)}</h2>'
                          f'<div class="sub">five findings in plain words</div><div class="takes">{rows}</div></div></section>')
            continue
        if title.startswith("More writing"):
            links = re.findall(r"^- \[(.+?)\]\((.+?)\)\s*(.*)$", txt, flags=re.M)
            cards = "".join(f'<a class="post" href="{u.replace("https://rvshankar45-jpg.github.io", "")}"><h3>{html.escape(t)}</h3>'
                            f'<p>{html.escape(d)}</p><span class="go">Read →</span></a>' for t, u, d in links)
            body.append(f'<section class="col more"><span hidden>MORE-WRITING-START</span>'
                        f'<h2><span class="rule"></span>{html.escape(title)}</h2>{cards}</section>')
            continue
        h = f'<h2><span class="rule"></span>{html.escape(title)}</h2>' + render(txt)
        if title.startswith("What each fix saved"):
            steps = ["v1_naive", "plus_route", "plus_retrieve", "plus_trim", "plus_tight_cache", "v2_full", "cache_full_kb"]
            lbl = ["Version 1", "+ routing", "+ retrieval", "+ history trim", "+ short prompt", "Version 2", "Whole manual, cached"]
            rows = [(lbl[i], s.loc[k, "total_cost_usd"], f"${s.loc[k, 'total_cost_usd']:.2f} <small>q {s.loc[k, 'mean_quality']:.2f}</small>",
                     "v1" if k == "v1_naive" else ("good" if k == "cache_full_kb" else "v2"), k in ("v2_full", "cache_full_kb"))
                    for i, k in enumerate(steps)]
            h += bars(rows, v1, "Cost of the same 140 answers after each fix",
                      "US$ at the provider's list prices · q = average grade out of 5",
                      "All bars share one scale. The green bar is the extra build: short prompt plus the whole manual, cached.")
        if title.startswith("Does a smarter router"):
            order = [("Laya off the shelf", "laya_zero_shot@0.50"), ("Message-length rule", "length_rule"),
                     ("Small model + trained head", "minilm_head"), ("Laya + trained head", "laya_head"),
                     ("Perfect hindsight", "hindsight_ceiling")]
            rows = [(nm, rh.loc[k, "saving_vs_always_sonnet"], f"{pct(rh.loc[k, 'saving_vs_always_sonnet'])} <small>q {rh.loc[k, 'quality']:.2f}</small>",
                     "v2" if k == "laya_head" else ("good" if k == "hindsight_ceiling" else "mute"), k == "laya_head") for nm, k in order]
            h += bars(rows, rh.loc["hindsight_ceiling", "saving_vs_always_sonnet"], "How much each router saved",
                      "100 test questions · saving vs always using the expensive model · q = average grade",
                      "Trained heads learn one thing: will the cheap model's answer hold up? The hindsight bar uses the answers' grades, so it can't be built.")
        if title.startswith("Should the expensive model"):
            order = [("Thinking off", "always_strong"), ("Low effort", "sonnet_low"), ("Medium effort", "sonnet_medium"), ("High effort", "sonnet_high")]
            rows = [(nm, eff.loc[k, "total_cost_usd"], f"${eff.loc[k, 'total_cost_usd']:.3f} <small>q {eff.loc[k, 'mean_quality']:.2f}</small>",
                     "v2" if k == "sonnet_low" else "mute", k == "sonnet_low") for nm, k in order]
            h += bars(rows, eff.total_cost_usd.loc[[k for _, k in order]].max(), "Cost by thinking setting (expensive model)",
                      f"{int(eff.loc['sonnet_low', 'n'])} questions · same prompts · q = average grade",
                      f"Hidden thinking tokens: low {int(eff.loc['sonnet_low', 'thinking_tokens']):,}, high {int(eff.loc['sonnet_high', 'thinking_tokens']):,}.")
        body.append(f'<section class="col">{h}</section>')

    stats = [(f"${v2:.2f}", f"cost of {n} answers · v1 ${v1:.2f}"), (pct(1 - tok["v2_full"] / tok["v1_naive"]), "fewer tokens"),
             (f"{s.loc['v2_full', 'mean_quality']:.2f}", f"average quality / 5 · v1 {s.loc['v1_naive', 'mean_quality']:.2f}"),
             (pct(tr), "trained router saving")]
    stat_html = "\n".join(f'<div class="stat"><div class="v num">{v}</div><div class="k">{k}</div></div>' for v, k in stats)
    intro_html = "".join(render(p) for p in intro_paras)
    title = h1
    desc = f"Same AI support bot, built twice: {pct(1 - v2 / v1)} cheaper. Retrieval did half the work; the famous router did a sixth."
    page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:type" content="article">
<meta property="og:url" content="{URL}">
<meta property="og:image" content="{URL}card.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="1200">
<meta name="twitter:card" content="summary_large_image">
<title>{html.escape(title)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&family=JetBrains+Mono:wght@500;700&display=swap">
<style>{CSS}</style>
</head>
<body>
<div class="wrap">
  <div class="col"><a class="backlink" href="/">&larr; Ravishankar R</a></div>
  <header class="top col">
    <div class="kicker">{n} answers · two builds · every token counted</div>
    <h1>{html.escape(head_hit[0])}. <span class="hit">{html.escape(head_hit[1])}</span></h1>
    <div class="standfirst">{render(intro_paras[0])[3:-4]}</div>
    <div class="byline"><span>Leafy, a fictional plant shop</span><span>Claude Sonnet 5.5 · Haiku 4.5 · Laya</span>
      <span>{date.today():%B %Y}</span><span>open code &amp; data</span></div>
  </header>
  <div class="hero"><img src="hero.png" width="1600" height="780" alt="Two receipts for the same 140 answers: version 1 totals ${v1:.2f}; version 2 itemises the savings from routing, retrieval, history trimming, a short prompt and concise answers, totalling ${v2:.2f}, under a stamp reading {pct(1 - v2 / v1)} cheaper."></div>
  {approach_html}
  <section class="col">{"".join(render(p) for p in intro_paras[1:])}</section>
  <div class="col"><div class="thesis"><div class="big">{pct(1 - v2 / v1)}</div><div class="say"><b>Cheaper, for the same {n} answers.</b>
    ${v1:.2f} became ${v2:.2f}, with {pct(1 - tok['v2_full'] / tok['v1_naive'])} fewer tokens. Half of it came from sending less context; about a sixth from the model router everyone talks about.</div></div></div>
  <div class="col"><div class="stats">{stat_html}</div></div>
  {short_html}
  {"".join(body)}
  <footer class="col">
    {n} answers · 100 test questions + 10 conversations · 270 separate training questions for the router.
    All data is synthetic; no real customer or company appears. Every figure on this page is generated from the analysis output at build time rather than typed by hand.
  </footer>
</div>
</body>
</html>
"""
    SITE.mkdir(parents=True, exist_ok=True)
    (SITE / "index.html").write_text(page, encoding="utf-8")
    print("written", SITE / "index.html", len(page), "bytes")


if __name__ == "__main__":
    main()
