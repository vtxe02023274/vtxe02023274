"""Builds banner.svg, the pixel style header of the profile README.

Text is rasterized without anti-aliasing and written out as rects, so it
stays crisp at any size. The avatar is reduced to a 64x64, 24 color image
and embedded as a PNG.

    python tools/banner.py
"""

import base64
import io
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
FONTS = Path("C:/Windows/Fonts")

WIDTH, HEIGHT = 960, 240
NAVY = "#002263"
DEEP = "#00163f"
GRID = "#0a2f7a"
CREAM = "#fbf4e2"
ORANGE = "#ff8a2b"
TEAL = "#2fd3c0"
DIM = "#5f7fc4"


def glyph_rects(text, font_path, size, cell, x0, y0, color, bold=False):
    """Draws text one pixel at a time, each pixel a cell x cell square.

    bold widens every stroke by one pixel to the right, for small CJK sizes
    whose strokes are a single pixel.
    """
    font = ImageFont.truetype(str(font_path), size)
    left, top, right, bottom = font.getbbox(text)
    img = Image.new("1", (right - left + 2, bottom - top + 2), 0)
    draw = ImageDraw.Draw(img)
    draw.fontmode = "1"
    draw.text((-left + 1, -top + 1), text, font=font, fill=1)
    if bold:
        draw.text((-left + 2, -top + 1), text, font=font, fill=1)
    rects = []
    for y in range(img.height):
        x = 0
        while x < img.width:
            if img.getpixel((x, y)):
                start = x
                while x < img.width and img.getpixel((x, y)):
                    x += 1
                rects.append(
                    f'<rect x="{x0 + start * cell}" y="{y0 + y * cell}" '
                    f'width="{(x - start) * cell}" height="{cell}"/>'
                )
            x += 1
    return f'<g fill="{color}">{"".join(rects)}</g>', img.width * cell, img.height * cell


def avatar_png():
    img = Image.open(ROOT / "avatar" / "current.png").convert("RGB")
    small = img.resize((64, 64), Image.BOX).quantize(colors=24, dither=Image.Dither.NONE)
    out = io.BytesIO()
    small.convert("RGB").save(out, "PNG", optimize=True)
    return base64.b64encode(out.getvalue()).decode("ascii")


def main():
    parts = []

    # Background, a faint 8 px grid and scanlines.
    parts.append(f'<rect width="{WIDTH}" height="{HEIGHT}" fill="{DEEP}"/>')
    parts.append(
        '<defs>'
        f'<pattern id="grid" width="8" height="8" patternUnits="userSpaceOnUse">'
        f'<rect width="8" height="8" fill="none" stroke="{GRID}" stroke-width="1"/></pattern>'
        '<pattern id="scan" width="4" height="4" patternUnits="userSpaceOnUse">'
        '<rect width="4" height="2" fill="#000" opacity="0.18"/></pattern>'
        '</defs>'
    )
    parts.append(f'<rect width="{WIDTH}" height="{HEIGHT}" fill="url(#grid)" opacity="0.5"/>')

    # Avatar in a stepped pixel frame.
    ax, ay, size = 40, 24, 192
    parts.append(f'<rect x="{ax - 8}" y="{ay + 8}" width="{size + 16}" height="{size - 16}" fill="{CREAM}"/>')
    parts.append(f'<rect x="{ax + 8}" y="{ay - 8}" width="{size - 16}" height="{size + 16}" fill="{CREAM}"/>')
    parts.append(f'<rect x="{ax}" y="{ay}" width="{size}" height="{size}" fill="{CREAM}"/>')
    parts.append(
        f'<image x="{ax + 8}" y="{ay + 8}" width="{size - 16}" height="{size - 16}" '
        f'style="image-rendering:pixelated" href="data:image/png;base64,{avatar_png()}"/>'
    )

    # Name, title and a terminal line with a blinking cursor.
    tx = 280
    name, _, name_h = glyph_rects("冷牛", FONTS / "msjhbd.ttc", 16, 6, tx, 24, CREAM, bold=True)
    parts.append(name)
    title, _, title_h = glyph_rects(
        "GAME SERVER DEVELOPER", FONTS / "consolab.ttf", 13, 3, tx, 34 + name_h, ORANGE
    )
    parts.append(title)
    line_y = 48 + name_h + title_h
    line, line_w, _ = glyph_rects(
        "> netcode / protocols / 2d game tools", FONTS / "consola.ttf", 11, 2, tx, line_y, TEAL
    )
    parts.append(line)
    parts.append(
        f'<rect x="{tx + line_w + 6}" y="{line_y + 2}" width="12" height="20" fill="{TEAL}">'
        '<animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.5;0.5;1" dur="1s" repeatCount="indefinite"/>'
        '</rect>'
    )

    # Twinkling pixel stars in the empty corner.
    for i, (sx, sy) in enumerate([(820, 40), (880, 92), (760, 120), (900, 180), (840, 200)]):
        parts.append(
            f'<rect x="{sx}" y="{sy}" width="6" height="6" fill="{CREAM}">'
            f'<animate attributeName="opacity" values="0.2;1;0.2" dur="{2 + i * 0.6:.1f}s" repeatCount="indefinite"/>'
            '</rect>'
        )

    # Bottom bar: a loading meter made of blocks.
    for i in range(24):
        color = ORANGE if i < 17 else DIM
        parts.append(f'<rect x="{tx + i * 14}" y="{HEIGHT - 20}" width="10" height="8" fill="{color}"/>')

    parts.append(f'<rect width="{WIDTH}" height="{HEIGHT}" fill="url(#scan)"/>')
    parts.append(f'<rect x="2" y="2" width="{WIDTH - 4}" height="{HEIGHT - 4}" fill="none" stroke="{NAVY}" stroke-width="4"/>')

    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" '
        f'viewBox="0 0 {WIDTH} {HEIGHT}" shape-rendering="crispEdges">'
        + "".join(parts)
        + "</svg>\n"
    )
    (ROOT / "banner.svg").write_text(svg, encoding="utf-8", newline="\n")
    print(f"banner.svg {len(svg) // 1024} KiB")


if __name__ == "__main__":
    main()
