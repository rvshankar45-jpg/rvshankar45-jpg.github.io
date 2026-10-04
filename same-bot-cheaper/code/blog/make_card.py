"""Social card / thumbnail (1200x1200) in the same layout as the author's previous post card.
Every number is read from results/*.csv at build time.

  .\\.venv\\Scripts\\python.exe -m blog.make_card     -> blog/site/card.png
"""
from pathlib import Path

import pandas as pd
from PIL import Image, ImageDraw, ImageFont

from src.common import ROOT

SLUG = "same-bot-cheaper"
OUT = ROOT / "blog" / "site"
F = Path("C:/Windows/Fonts")
PAPER, INK, INK2, INK3, RULE = "#FAF6EF", "#17130D", "#5E564A", "#8C8274", "#E2D9C9"
FLAG, HIT, TRACK, BLUE, SURF = "#C2410C", "#D6283A", "#F2ECE1", "#2a78d6", "#FFFFFF"


def font(name, size):
    return ImageFont.truetype(str(F / name), size)


BLACK, BOLD, SEMI, REG = (lambda s: font("seguibl.ttf", s)), (lambda s: font("segoeuib.ttf", s)), \
    (lambda s: font("seguisb.ttf", s)), (lambda s: font("segoeui.ttf", s))


def main():
    s = pd.read_csv(ROOT / "results" / "summary.csv").set_index("variant")
    rh = pd.read_csv(ROOT / "results" / "router_head_summary.csv").set_index("router")
    v1, v2 = s.loc["v1_naive", "total_cost_usd"], s.loc["v2_full", "total_cost_usd"]
    steps = ["v1_naive", "plus_route", "plus_retrieve", "plus_trim", "plus_tight_cache", "v2_full"]
    d = -s.loc[steps, "total_cost_usd"].diff().iloc[1:]
    names = {"plus_route": "Laya routing", "plus_retrieve": "Retrieval", "plus_trim": "Trim history",
             "plus_tight_cache": "Tight prompt", "v2_full": "Concise answers"}
    d = d.sort_values(ascending=False)
    n_units = int(s.loc["v1_naive", "answers"])
    pct = round(100 * (1 - v2 / v1))
    zs, tr = 100 * rh.loc["laya_zero_shot@0.50", "saving_vs_always_sonnet"], 100 * rh.loc["laya_head", "saving_vs_always_sonnet"]
    q1, qc = s.loc["v1_naive", "mean_quality"], s.loc["cache_full_kb", "mean_quality"]

    im = Image.new("RGB", (1200, 1200), PAPER)
    g = ImageDraw.Draw(im)
    X = 80
    g.text((X, 72), f"{n_units} ANSWERS  ·  2 BUILDS  ·  EVERY TOKEN COUNTED", font=BOLD(25), fill=FLAG)
    g.text((X, 112), "Same AI support bot,", font=BOLD(92), fill=INK)
    g.text((X, 212), "built twice.", font=BOLD(92), fill=INK)
    g.text((X, 312), f"{pct}% cheaper.", font=BOLD(92), fill=HIT)
    g.line([(X, 430), (1120, 430)], fill=RULE, width=3)

    # left: cost of the same answers
    g.text((X, 452), f"COST OF THE SAME {n_units} ANSWERS", font=SEMI(21), fill=INK3)
    for i, (lbl, val, col) in enumerate([("v1 naive", v1, HIT), ("v2 optimised", v2, BLUE)]):
        y = 510 + i * 112
        g.text((X, y), lbl, font=BOLD(34), fill=col)
        g.text((X, y + 44), f"${val:.2f}", font=BLACK(44), fill=INK)
        w = int(220 * val / v1)
        g.rectangle([X + 170, y + 62, X + 170 + 220, y + 84], fill=TRACK)
        g.rectangle([X + 170, y + 62, X + 170 + w, y + 84], fill=col)

    # right: where the saving came from
    RX = 610
    g.text((RX, 452), "WHERE THE SAVING CAME FROM", font=SEMI(21), fill=INK3)
    top = d.iloc[0]
    for i, (k, val) in enumerate(d.items()):
        y = 500 + i * 56
        bold = i == 0
        g.text((RX, y), names[k], font=(BOLD if bold else SEMI)(27), fill=INK if bold else INK2)
        bx = RX + 250
        g.rectangle([bx, y + 10, bx + 170, y + 32], fill=TRACK)
        g.rectangle([bx, y + 10, bx + max(3, int(170 * val / top)), y + 32], fill=FLAG if bold else "#C9BFAE")
        g.text((bx + 180, y), f"-${val:.2f}", font=BOLD(26), fill=FLAG if bold else INK2)
    g.line([(X, 800), (1120, 800)], fill=RULE, width=3)

    # quote box
    g.rectangle([X, 828, 1120, 1004], fill=SURF, outline=RULE, width=3)
    g.rectangle([X, 828, X + 8, 1004], fill=FLAG)
    g.text((X + 42, 852), "The famous router did a sixth of it:", font=BOLD(37), fill=INK)
    g.text((X + 42, 898), f"{zs:.0f}% off the shelf, {tr:.0f}% once trained.", font=BOLD(37), fill=INK)
    g.text((X + 42, 952), f"Caching the whole manual scored best: {qc:.2f} vs v1's {q1:.2f}.", font=REG(29), fill=INK2)

    g.text((X, 1052), f"rvshankar45-jpg.github.io/{SLUG}", font=BOLD(27), fill=INK2)
    pill = "Routing by Laya AI · runs on a laptop"
    pw = g.textlength(pill, font=BOLD(22)) + 56
    g.rounded_rectangle([1120 - pw, 1040, 1120, 1094], radius=27, fill=FLAG)
    g.text((1120 - pw + 28, 1052), pill, font=BOLD(22), fill="white")
    OUT.mkdir(parents=True, exist_ok=True)
    im.save(OUT / "card.png", optimize=True)
    print("card.png written:", OUT / "card.png")


if __name__ == "__main__":
    main()
