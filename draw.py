#!/usr/bin/env python3
"""Generator for news-image-20261125 entry.png (build-time only; grader runs main.py).

Draws a 1024x1024 news front page for Wednesday 25 November 2026 with Pillow.
Written from scratch for this competition.
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
INK = (11, 18, 32)
PAPER = (247, 244, 238)
CARD = (255, 255, 255)
MUTED = (92, 102, 120)
RED = (196, 30, 42)
GOLD = (214, 154, 32)
TEAL = (0, 128, 128)
BLUE = (24, 78, 160)
GREEN = (28, 122, 74)
PURPLE = (96, 62, 150)
DARK = (22, 30, 48)

BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SERIFB = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_icon(d, kind, cx, cy, r, color):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color)
    wht = (255, 255, 255)
    if kind == "pct":
        f = font(BOLD, 34)
        d.text((cx, cy - 2), "%", font=f, fill=wht, anchor="mm")
    elif kind == "city":
        for dx, hh in ((-16, 22), (-5, 32), (7, 26)):
            d.rectangle([cx + dx, cy + 16 - hh, cx + dx + 9, cy + 16], fill=wht)
        d.line([cx - 22, cy + 16, cx + 22, cy + 16], fill=wht, width=3)
    elif kind == "shield":
        d.polygon([(cx, cy - 20), (cx + 16, cy - 12), (cx + 16, cy + 4),
                   (cx, cy + 20), (cx - 16, cy + 4), (cx - 16, cy - 12)], fill=wht)
        d.line([cx - 7, cy, cx - 2, cy + 6], fill=color, width=4)
        d.line([cx - 2, cy + 6, cx + 8, cy - 6], fill=color, width=4)
    elif kind == "cross":
        d.rectangle([cx - 5, cy - 17, cx + 5, cy + 17], fill=wht)
        d.rectangle([cx - 17, cy - 5, cx + 17, cy + 5], fill=wht)
    elif kind == "isles":
        for dx, dy, rr in ((-14, 6, 7), (2, -8, 9), (15, 8, 6)):
            d.ellipse([cx + dx - rr, cy + dy - rr, cx + dx + rr, cy + dy + rr], fill=wht)
        d.arc([cx - 22, cy - 20, cx + 22, cy + 20], 200, 340, fill=wht, width=3)
    elif kind == "ball":
        d.ellipse([cx - 18, cy - 18, cx + 18, cy + 18], outline=wht, width=3)
        d.polygon([(cx, cy - 8), (cx + 8, cy - 2), (cx + 5, cy + 7),
                   (cx - 5, cy + 7), (cx - 8, cy - 2)], fill=wht)
        for a in (0, 72, 144, 216, 288):
            import math
            x = cx + 17 * math.cos(math.radians(a - 90))
            y = cy + 17 * math.sin(math.radians(a - 90))
            d.line([cx, cy, x, y], fill=wht, width=2)


CARDS = [
    ("TRADE", "Washington", RED, "pct", "US proposes tariffs\non 14 partners",
     "Washington targets “excess factory capacity”; China faces the highest rates. Stocks slide.", "14"),
    ("GAZA", "Middle East", DARK, "city", "Strike kills Hamas\nsecurity official",
     "Gaza City airstrike kills Mohammad Abuelouf, his wife and two children, officials say.", "4"),
    ("UKRAINE", "Europe", BLUE, "shield", "War toll estimate\npasses 720,000",
     "New analysis estimates Russian military deaths since 2022; Moscow rejects a Western force.", "720K+"),
    ("CONGO", "Africa", TEAL, "cross", "UN evacuates\nEbola workers",
     "Peacekeepers move 10 trapped health staff as fighting disrupts the response in the east.", "10"),
    ("PACIFIC", "Security", GREEN, "isles", "Solomons sign\nAustralia treaty",
     "Solomon Islands names Australia its primary security partner; foreign bases ruled out.", "PACT"),
    ("SPORT", "Champions League", PURPLE, "ball", "Liverpool & Barça\nwin big",
     "Liverpool 3–0 at Brugge, Barça 4–1; PSG held 2–2 by Roma, Bayern beaten at Lille.", "3–0"),
]


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # header band
    d.rectangle([0, 0, W, 158], fill=INK)
    d.rectangle([0, 158, W, 166], fill=RED)
    d.text((36, 26), "WORLD NEWS  •  ONE DAY, ONE PAGE", font=font(BOLD, 21), fill=GOLD)
    d.text((36, 54), "Wednesday 25 November 2026", font=font(SERIFB, 42), fill=(255, 255, 255))
    d.text((36, 112), "The day’s most consequential stories — trade, war, health, the Pacific and sport.",
           font=font(REG, 20), fill=(196, 205, 220))
    # date badge
    d.rounded_rectangle([852, 30, 988, 128], radius=12, fill=RED)
    d.text((920, 52), "25", font=font(BOLD, 52), fill=(255, 255, 255), anchor="mm")
    d.text((920, 96), "NOV 2026", font=font(BOLD, 19), fill=(255, 255, 255), anchor="mm")

    # cards grid 2 x 3
    x0, y0, cw, ch, gap = 32, 184, 472, 218, 16
    for i, (tag, region, color, icon, head, body, stat) in enumerate(CARDS):
        col, row = i % 2, i // 2
        x = x0 + col * (cw + gap)
        y = y0 + row * (ch + gap)
        d.rounded_rectangle([x, y, x + cw, y + ch], radius=14, fill=CARD, outline=(216, 210, 198), width=2)
        d.rounded_rectangle([x + 3, y + 14, x + 11, y + ch - 14], radius=4, fill=color)
        draw_icon(d, icon, x + 52, y + 52, 30, color)
        d.text((x + 96, y + 26), tag, font=font(BOLD, 20), fill=color)
        d.text((x + 96, y + 50), region, font=font(REG, 17), fill=MUTED)
        # stat chip right
        tw = d.textlength(stat, font=font(BOLD, 30))
        d.rounded_rectangle([x + cw - tw - 36, y + 20, x + cw - 16, y + 62], radius=10, fill=(240, 236, 226))
        d.text((x + cw - 26, y + 41), stat, font=font(BOLD, 30), fill=DARK, anchor="rm")
        hy = y + 92
        for line in head.split("\n"):
            d.text((x + 28, hy), line, font=font(BOLD, 31), fill=DARK)
            hy += 36
        by = hy + 6
        for line in wrap(d, body, font(REG, 19), cw - 56)[:3]:
            d.text((x + 28, by), line, font=font(REG, 19), fill=(52, 60, 76))
            by += 24

    # ticker
    ty = y0 + 3 * ch + 2 * gap + 14
    d.rounded_rectangle([32, ty, 992, ty + 92], radius=12, fill=INK)
    d.text((52, ty + 14), "ALSO ON 25 NOV", font=font(BOLD, 19), fill=GOLD)
    ticker = ("US inflation 3.8% y/y  •  Iowa detonates 9,500 lb of lead azide  •  "
              "Bangladesh garment wage +36%  •  Colombia frees ~30 hostages  •  UK energy cap +26%")
    lines = wrap(d, ticker, font(REG, 19), 920)
    ly = ty + 42
    for line in lines[:2]:
        d.text((52, ly), line, font=font(REG, 19), fill=(235, 238, 245))
        ly += 24

    d.text((36, 990), "Sources: Reuters • AP • UEFA • Daily Brief (25 Nov 2026). Events dated 25 Nov 2026.",
           font=font(REG, 15), fill=MUTED)

    img.save("assets/entry.png", optimize=True)
    print("wrote assets/entry.png")


if __name__ == "__main__":
    main()
