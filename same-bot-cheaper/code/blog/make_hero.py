"""Hero image for the top of the article: two receipts - version 1's bill and version 2's itemised
savings - with a "64% cheaper" stamp. Every figure is read from results/*.csv at build time.

  .\\.venv\\Scripts\\python.exe -m blog.make_hero     -> blog/site/hero.png
"""
from pathlib import Path

import pandas as pd
from PIL import Image, ImageDraw, ImageFilter, ImageFont

from src.common import ROOT

F = Path("C:/Windows/Fonts")
W, H = 1600, 780
PAPER, INK, INK2, INK3, RULE = "#FAF6EF", "#17130D", "#5E564A", "#8C8274", "#E2D9C9"
RED, FLAG, BLUE, GREEN = "#D6283A", "#C2410C", "#2A78D6", "#1B8A5A"
MONO, MONOB = (lambda s: ImageFont.truetype(str(F / "consola.ttf"), s)), (lambda s: ImageFont.truetype(str(F / "consolab.ttf"), s))
BOLD, BLACK = (lambda s: ImageFont.truetype(str(F / "segoeuib.ttf"), s)), (lambda s: ImageFont.truetype(str(F / "seguibl.ttf"), s))


def receipt(width, lines, title, total_label, total, total_col):
    """Renders one receipt (with a torn zig-zag bottom) on a transparent canvas."""
    pad, lh = 36, 40
    height = 150 + lh * len(lines) + 100
    im = Image.new("RGBA", (width, height + 24), (0, 0, 0, 0))
    g = ImageDraw.Draw(im)
    g.rectangle([0, 0, width, height], fill="white")
    zig = [(x, height + (12 if (x // 18) % 2 else 0)) for x in range(0, width + 18, 18)]
    g.polygon([(0, height)] + zig + [(width, height)], fill="white")
    g.text((pad, 34), title, font=MONOB(26), fill=INK)
    g.text((pad, 74), "140 customer answers", font=MONO(21), fill=INK3)
    g.line([(pad, 118), (width - pad, 118)], fill=INK3, width=2)
    y = 138
    for left, right, col in lines:
        g.text((pad, y), left, font=MONO(24), fill=INK2)
        if right:
            w = g.textlength(right, font=MONOB(24))
            dots_x0 = pad + g.textlength(left, font=MONO(24)) + 10
            for x in range(int(dots_x0), int(width - pad - w - 10), 12):
                g.text((x, y), ".", font=MONO(24), fill=RULE)
            g.text((width - pad - w, y), right, font=MONOB(24), fill=col)
        y += lh
    y += 16
    for k in range(pad, width - pad, 14):
        g.line([(k, y), (k + 7, y)], fill=INK3, width=2)
    y += 22
    g.text((pad, y), total_label, font=MONOB(30), fill=INK)
    w = g.textlength(total, font=MONOB(44))
    g.text((width - pad - w, y - 8), total, font=MONOB(44), fill=total_col)
    return im


def paste_with_shadow(base, im, xy, angle):
    im = im.rotate(angle, expand=True, resample=Image.BICUBIC)
    shadow = Image.new("RGBA", im.size, (0, 0, 0, 0))
    shadow.paste((23, 19, 13, 60), mask=im.split()[3])
    shadow = shadow.filter(ImageFilter.GaussianBlur(14))
    base.alpha_composite(shadow, (xy[0] + 10, xy[1] + 16))
    base.alpha_composite(im, xy)


def main():
    s = pd.read_csv(ROOT / "results" / "summary.csv").set_index("variant")
    v1, v2 = s.loc["v1_naive", "total_cost_usd"], s.loc["v2_full", "total_cost_usd"]
    steps = ["v1_naive", "plus_route", "plus_retrieve", "plus_trim", "plus_tight_cache", "v2_full"]
    d = -s.loc[steps, "total_cost_usd"].diff().iloc[1:]
    pct = round(100 * (1 - v2 / v1))

    base = Image.new("RGBA", (W, H), PAPER)
    v1_lines = [("Strongest model, always", "", INK2), ("Whole manual, every call", "", INK2),
                ("Whole chat, every turn", "", INK2), ("650-token prompt", "", INK2), ("Long answers", "", INK2)]
    r1 = receipt(470, v1_lines, "VERSION 1  ·  QUICK BUILD", "TOTAL", f"${v1:.2f}", RED)
    names = {"plus_route": "Router (Laya)", "plus_retrieve": "Retrieval (RAG)", "plus_trim": "History trim",
             "plus_tight_cache": "Short prompt", "v2_full": "Concise answers"}
    v2_lines = [("Starting bill", f"${v1:.2f}", INK2)] + [(names[k], f"-${d[k]:.2f}", BLUE if d[k] < d.max() else FLAG) for k in steps[1:]]
    r2 = receipt(520, v2_lines, "VERSION 2  ·  OPTIMISED", "TOTAL", f"${v2:.2f}", GREEN)
    paste_with_shadow(base, r1, (60, 150), 3)
    paste_with_shadow(base, r2, (570, 70), -2)

    # stamp
    st = Image.new("RGBA", (360, 360), (0, 0, 0, 0))
    g = ImageDraw.Draw(st)
    g.ellipse([10, 10, 350, 350], outline=RED, width=10)
    g.ellipse([34, 34, 326, 326], outline=RED, width=3)
    for txt, font, y in [(f"{pct}%", BLACK(118), 88), ("CHEAPER", BOLD(42), 222)]:
        w = g.textlength(txt, font=font)
        g.text(((360 - w) / 2, y), txt, font=font, fill=RED)
    st = st.rotate(-14, expand=True, resample=Image.BICUBIC)
    a = st.split()[3].point(lambda v: int(v * 0.88))
    st.putalpha(a)
    base.alpha_composite(st, (1010, 330))

    g = ImageDraw.Draw(base)
    g.text((1170, 110), "Same chatbot.", font=BOLD(46), fill=INK)
    g.text((1170, 168), "Same questions.", font=BOLD(46), fill=INK)
    g.text((1170, 226), "Smaller bill.", font=BOLD(46), fill=RED)
    pill, pf = "Routing by Laya AI", BOLD(30)
    pw = g.textlength(pill, font=pf) + 56
    g.rounded_rectangle([1170, 298, 1170 + pw, 352], radius=27, fill=FLAG)
    g.text((1198, 305), pill, font=pf, fill="white")
    out = ROOT / "blog" / "site"
    out.mkdir(parents=True, exist_ok=True)
    base.convert("RGB").save(out / "hero.png", optimize=True)
    print("hero.png written")


if __name__ == "__main__":
    main()
