#!/usr/bin/env python3
"""Strata cover art: layered strata, branching fracture, converging
streamlines, mesh warped toward the fracture — after the user's cover.
Generates the homepage banner and the og:image."""
import math
from PIL import Image, ImageDraw, ImageFont

PAPER = (243, 238, 226)
SAGE = (185, 195, 177)
STONE = (215, 210, 194)
CREAM2 = (238, 232, 216)
RUST = (179, 79, 40)
PINE = (47, 75, 63)
INK = (35, 38, 31)
PALE = (233, 228, 210)

# deterministic jitter
J = [0.31, -0.62, 0.18, 0.77, -0.35, 0.52, -0.81, 0.09, 0.44, -0.27,
     0.66, -0.48, 0.23, -0.72, 0.58, -0.14, 0.39, -0.55, 0.71, -0.08]


def smooth(x, terms):
    return sum(a * math.sin(f * x + p) for a, f, p in terms)


def boundary(W, H, base_frac, amp, seed):
    terms = [(amp, 2.2 / W, seed), (amp * 0.5, 5.1 / W, seed * 2.3)]
    pts = []
    for i in range(121):
        x = i / 120 * W
        slope = (1 - x / W) * 0.30 * H
        pts.append((x, base_frac * H + slope + smooth(x, terms)))
    return pts


def draw_art(img, band_starts=None, fade_w_frac=0.05):
    """band_starts: per-band left cutoff fraction (None = full width)."""
    W, H = img.size
    fracs = [0.28, 0.40, 0.50, 0.58, 0.68]
    colors = [STONE, SAGE, CREAM2, RUST, PINE]
    amps = [H * 0.045, H * 0.04, H * 0.035, H * 0.028, H * 0.028]
    seeds = [1.3, 2.9, 4.2, 5.7, 7.1]
    bounds = [boundary(W, H, f, a, s) for f, a, s in zip(fracs, amps, seeds)]
    pine_top = bounds[-1]

    art = Image.new("RGBA", (W, H), (0, 0, 0, 0))

    # --- strata bands, each on its own layer with a soft left fade ------
    for i, pts in enumerate(bounds):
        layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ld = ImageDraw.Draw(layer)
        lower = bounds[i + 1] if i + 1 < len(bounds) else None
        poly = list(pts) + (list(reversed(lower)) if lower else [(W, H * 2), (0, H * 2)])
        ld.polygon(poly, fill=colors[i] + (255,))
        if band_starts is not None:
            x1 = int(band_starts[i] * W)
            x0 = max(0, x1 - int(fade_w_frac * W))
            mask = Image.new("L", (W, H), 255)
            mdr = ImageDraw.Draw(mask)
            mdr.rectangle([0, 0, x0, H], fill=0)
            for x in range(x0, x1):
                mdr.line([(x, 0), (x, H)], fill=int(255 * (x - x0) / max(1, x1 - x0)))
            layer.putalpha(Image.composite(layer.getchannel("A"), Image.new("L", (W, H), 0), mask))
        art.alpha_composite(layer)

    d = ImageDraw.Draw(art)

    # --- mesh in the pine band, warped toward a focus -------------------
    fx, fy = 0.735 * W, 0.92 * H

    def warp(x, y):
        r = math.hypot(x - fx, y - fy) + 1e-6
        p = 0.42 * math.exp(-(r / (0.20 * W)) ** 2)
        return (x + (fx - x) * p, y + (fy - y) * p)

    mesh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    md = ImageDraw.Draw(mesh)
    x_mesh0 = 0.0 if band_starts is None else max(0.0, band_starts[4] - 0.06)
    nv = int((1 - x_mesh0) * 46)
    for k in range(nv + 1):
        bx = (x_mesh0 + k * (1 - x_mesh0) / nv) * W
        pts = [warp(bx, 0.40 * H + j / 40 * 0.65 * H) for j in range(41)]
        md.line(pts, fill=PALE + (95,), width=max(1, W // 1300))
    for k in range(15):
        by = (0.44 + k * 0.04) * H
        pts = [warp((x_mesh0 + j / 80 * (1 - x_mesh0)) * W, by) for j in range(81)]
        md.line(pts, fill=PALE + (95,), width=max(1, W // 1300))
    pine_mask = Image.new("L", (W, H), 0)
    pm = ImageDraw.Draw(pine_mask)
    pm.polygon(list(pine_top) + [(W, H * 2), (0, H * 2)], fill=255)
    if band_starts is not None:
        pm.rectangle([0, 0, int((band_starts[4] - 0.04) * W), H], fill=0)
    art.paste(mesh, (0, 0), Image.composite(mesh.getchannel("A"), Image.new("L", (W, H), 0), pine_mask))
    d = ImageDraw.Draw(art)

    # --- branching fracture: clean kinked segments ----------------------
    lw = max(1.5, W / 900)

    def crack(x0, y0, y1, drift_per_seg, n, w0, w1, joff=0):
        pts = [(x0, y0)]
        for i in range(1, n + 1):
            y = y0 + (y1 - y0) * i / n
            x = pts[-1][0] + drift_per_seg + J[(i + joff) % 20] * 0.010 * W * 0.6
            pts.append((x, y))
        for i in range(n):
            w = w0 + (w1 - w0) * i / n
            d.line([pts[i], pts[i + 1]], fill=INK + (255,), width=max(1, round(w)))
        return pts

    ybase = H * 1.02
    tip_y = 0.26 * H
    main = crack(0.75 * W, ybase, tip_y, -0.004 * W, 12, 3.2 * lw, 1.0, 0)
    n3, n6, n8 = main[4], main[7], main[9]
    crack(n3[0], n3[1], n3[1] - 0.30 * H, +0.010 * W, 5, 1.8 * lw, 0.8, 5)
    crack(n6[0], n6[1], n6[1] - 0.22 * H, -0.012 * W, 4, 1.6 * lw, 0.8, 9)
    crack(n8[0], n8[1], n8[1] - 0.16 * H, +0.013 * W, 4, 1.4 * lw, 0.8, 13)
    tipx = main[-1][0]

    # --- streamlines drifting into the fracture tip ---------------------
    top0 = bounds[0]

    def top_y_at(x):
        return top0[min(120, max(0, int(x / W * 120)))][1]

    art_left = 0.0 if band_starts is None else min(band_starts) - 0.02
    for k in range(11):
        sx = (max(art_left + 0.06, 0.42) + 0.05 * k) * W
        x, y = sx, -0.05 * H
        pts = []
        step = 0.02 * H
        while y < H:
            if y > top_y_at(x) - 0.02 * H and y > tip_y:
                break
            x += (tipx - x) * 0.014
            y += step
            pts.append((x, y))
        if len(pts) < 6:
            continue
        wline = max(1, round(W / 1300))
        if k % 3 == 1:
            for i in range(0, len(pts) - 3, 7):
                d.line(pts[i:i + 5], fill=RUST + (225,), width=wline)
        else:
            d.line(pts, fill=RUST + (225,), width=wline)
        if k % 3 == 0 and len(pts) > 20:
            i = int(len(pts) * 0.55)
            (ax, ay), (bx2, by2) = pts[i - 1], pts[i]
            ang = math.atan2(by2 - ay, bx2 - ax)
            L = 0.018 * H
            for da in (2.65, -2.65):
                d.line([(bx2, by2), (bx2 + L * math.cos(ang + da), by2 + L * math.sin(ang + da))],
                       fill=RUST + (245,), width=wline)

    img.alpha_composite(art)
    return img


def make_banner():
    W, H = 2580, 660
    img = Image.new("RGBA", (W, H), PAPER + (255,))
    draw_art(img, band_starts=None)
    img.convert("RGB").save("yulong_website/assets/img/cover-strata.png", optimize=True)
    print("banner ok")


def font(path, size, axes=None):
    f = ImageFont.truetype(path, size)
    if axes:
        try:
            f.set_variation_by_axes(axes)
        except Exception:
            pass
    return f


def make_og():
    W, H = 1200, 630
    img = Image.new("RGBA", (W, H), PAPER + (255,))
    draw_art(img, band_starts=[0.56, 0.53, 0.58, 0.50, 0.46], fade_w_frac=0.035)
    d = ImageDraw.Draw(img)
    FD = "fonts/BodoniModa.ttf"
    FM = "fonts/SplineSansMono.ttf"
    name = font(FD, 126, [600, 96])
    mono = font(FM, 25, [500])
    d.text((72, 92), "YULONG", font=name, fill=INK)
    d.text((72, 230), "LIU", font=name, fill=INK)
    d.line([(76, 424), (452, 424)], fill=RUST, width=3)
    d.ellipse([(460, 418), (473, 431)], fill=RUST)
    d.text((76, 458), "COMPUTATIONAL GEOMECHANICS +", font=mono, fill=INK)
    d.text((76, 494), "SCIENTIFIC MACHINE LEARNING", font=mono, fill=INK)
    d.text((76, 552), "PH.D. CANDIDATE · CORNELL UNIVERSITY", font=font(FM, 19, [400]), fill=(107, 109, 96))
    img.convert("RGB").save("yulong_website/assets/img/og-yulong-liu.png", optimize=True)
    print("og ok")


make_banner()
make_og()
