"""Procedural, original silhouette-documentary artwork for the Eilean Mor demo.

Every scene returns (background RGB image, overlays dict). Overlays are RGBA
layers that render.py animates with ffmpeg (fog drift, rain, rotating beam,
bobbing boat, rising wave, flicker...).
"""
import math
import random

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1920, 1080
FONT_SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
FONT_MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
SIL = (6, 9, 13)


# ---------------------------------------------------------------- helpers
def vgrad(top, bottom, w=W, h=H):
    t = np.linspace(0, 1, h)[:, None, None]
    a = np.array(top, float)[None, None, :]
    b = np.array(bottom, float)[None, None, :]
    return np.repeat(a * (1 - t) + b * t, w, axis=1)


def fnoise(w, h, seed, octaves=(4, 8, 16, 32, 64), stretch=1.0, sy=None):
    """Fractal noise. stretch scales x-cells; sy scales y-cells (default keeps aspect)."""
    rng = np.random.default_rng(seed)
    acc = np.zeros((h, w))
    amp, total = 1.0, 0.0
    for o in octaves:
        gw = max(2, int(o * stretch))
        gh = max(2, int(o * sy)) if sy else max(2, o * h // w + 2)
        g = Image.fromarray((rng.random((gh, gw)) * 255).astype(np.uint8))
        acc += amp * np.asarray(g.resize((w, h), Image.BICUBIC), float) / 255
        total += amp
        amp *= 0.55
    acc /= total
    return (acc - acc.min()) / (np.ptp(acc) + 1e-9)


def blend(base, color, mask):
    m = np.clip(mask, 0, 1)[..., None]
    return base * (1 - m) + np.array(color, float) * m


def add_glow(arr, x, y, r, color, strength=1.0):
    yy, xx = np.mgrid[0:arr.shape[0], 0:arr.shape[1]]
    d = np.sqrt((xx - x) ** 2 + (yy - y) ** 2) / r
    g = np.clip(1 - d, 0, 1) ** 2.2 * strength
    return np.clip(arr + g[..., None] * np.array(color, float), 0, 255)


def clouds(arr, seed, color, density=0.55, top=0, bottom=None):
    bottom = bottom or arr.shape[0]
    n = fnoise(arr.shape[1], arr.shape[0], seed, stretch=0.7, sy=1.1)
    m = np.clip((n - (1 - density)) * 2.2, 0, 1)
    fade = np.zeros(arr.shape[0])
    fade[top:bottom] = np.linspace(1, 0.15, bottom - top)
    return blend(arr, color, m * fade[:, None])


def sea(arr, horizon, seed, base=(9, 16, 24), hl=(70, 92, 110)):
    h = arr.shape[0] - horizon
    s = vgrad(base, (4, 7, 11), arr.shape[1], h)
    n = fnoise(arr.shape[1], h, seed, octaves=(6, 12, 24, 48), stretch=0.35, sy=2.2)
    streak = np.clip((n - 0.62) * 3.0, 0, 1) * np.linspace(0.9, 0.25, h)[:, None]
    s = blend(s, hl, streak * 0.55)
    arr[horizon:] = s
    return arr


def ridge(x0, x1, ybase, amp, seed, step=14):
    rnd = random.Random(seed)
    pts, y = [], ybase
    for x in range(x0, x1 + step, step):
        y += rnd.uniform(-amp, amp)
        y = min(max(y, ybase - amp * 6), ybase + amp * 2)
        pts.append((x, y))
    return pts


def to_img(arr):
    return Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8), "RGB")


def font(path, size):
    return ImageFont.truetype(path, size)


def text_layer(lines, pos="bottom", size=46, mono=True, color=(225, 215, 195)):
    """Transparent overlay with documentary-style captions (date stamps etc.)."""
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    f = font(FONT_MONO if mono else FONT_SERIF, size)
    y = H - 170 - (len(lines) - 1) * (size + 14) if pos == "bottom" else 120
    for ln in lines:
        tw = d.textlength(ln, font=f)
        x = (W - tw) / 2
        d.text((x + 3, y + 3), ln, font=f, fill=(0, 0, 0, 200))
        d.text((x, y), ln, font=f, fill=color + (255,))
        y += size + 14
    return lay


# ------------------------------------------------------------- set pieces
def lighthouse(d, cx, base_y, height, lit, scale=1.0):
    bw, tw = 70 * scale, 44 * scale
    top = base_y - height
    d.polygon([(cx - bw, base_y), (cx + bw, base_y), (cx + tw, top), (cx - tw, top)], fill=SIL)
    for i in range(1, 4):  # faint bands
        yb = base_y - height * i / 4
        wb = bw - (bw - tw) * i / 4
        d.line([(cx - wb, yb), (cx + wb, yb)], fill=(14, 19, 26), width=max(2, int(5 * scale)))
    g = 18 * scale
    d.rectangle([cx - tw - g, top - 10 * scale, cx + tw + g, top], fill=SIL)
    lw = tw * 0.8
    lamp = (235, 200, 140) if lit else (20, 28, 36)
    d.rectangle([cx - lw, top - 70 * scale, cx + lw, top - 10 * scale], fill=lamp)
    for k in (-0.4, 0.0, 0.4):
        d.line([(cx + lw * k, top - 70 * scale), (cx + lw * k, top - 10 * scale)], fill=SIL, width=max(2, int(4 * scale)))
    d.polygon([(cx - lw - 8 * scale, top - 70 * scale), (cx + lw + 8 * scale, top - 70 * scale), (cx, top - 115 * scale)], fill=SIL)
    return (cx, top - 40 * scale)


def island(d, x0, x1, top_y, seed, cliff_drop=260):
    pts = ridge(x0 + 90, x1 - 90, top_y, 9, seed)
    left = [(x0, top_y + cliff_drop), (x0 + 30, top_y + cliff_drop * 0.45), (x0 + 70, top_y + 25)]
    right = [(x1 - 70, top_y + 30), (x1 - 25, top_y + cliff_drop * 0.5), (x1, top_y + cliff_drop)]
    poly = left + pts + right
    d.polygon(poly, fill=SIL)
    return pts


def figure(d, x, y, h, lean=0.0):
    hw = h * 0.16
    d.ellipse([x - h * 0.07, y - h, x + h * 0.07, y - h * 0.86], fill=SIL)
    d.polygon([(x - hw * 0.9, y - h * 0.86), (x + hw * 0.9, y - h * 0.86),
               (x + hw + lean * h, y - h * 0.18), (x - hw + lean * h, y - h * 0.18)], fill=SIL)
    d.polygon([(x - hw * 0.8 + lean * h, y - h * 0.2), (x - hw * 0.15 + lean * h, y - h * 0.2), (x - hw * 0.3, y), (x - hw * 0.7, y)], fill=SIL)
    d.polygon([(x + hw * 0.15 + lean * h, y - h * 0.2), (x + hw * 0.8 + lean * h, y - h * 0.2), (x + hw * 0.7, y), (x + hw * 0.3, y)], fill=SIL)
    d.rectangle([x - h * 0.09, y - h * 1.02, x + h * 0.09, y - h * 0.97], fill=SIL)  # cap


def boat_layer(scale=1.0, lights=False):
    lay = Image.new("RGBA", (int(520 * scale), int(300 * scale)), (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    s = scale
    d.polygon([(20 * s, 200 * s), (500 * s, 200 * s), (440 * s, 260 * s), (70 * s, 260 * s)], fill=SIL + (255,))
    d.rectangle([180 * s, 130 * s, 330 * s, 200 * s], fill=SIL + (255,))
    d.rectangle([240 * s, 40 * s, 262 * s, 130 * s], fill=SIL + (255,))
    d.line([(251 * s, 40 * s), (60 * s, 200 * s)], fill=SIL + (255,), width=max(1, int(3 * s)))
    if lights:
        for lx in (205, 240, 275, 305):
            d.rectangle([lx * s, 150 * s, (lx + 12) * s, 162 * s], fill=(240, 200, 120, 255))
    return lay


def stone_wall(seed, warm=(46, 36, 28)):
    arr = vgrad((34, 27, 22), (16, 13, 11))
    n = fnoise(W, H, seed, octaves=(16, 32, 64, 128))
    arr = blend(arr, warm, n * 0.5)
    img = to_img(arr)
    d = ImageDraw.Draw(img)
    rnd = random.Random(seed)
    y, row = 0, 0
    while y < H * 0.72:
        bh = rnd.randint(70, 100)
        x = -rnd.randint(0, 120) if row % 2 else 0
        while x < W:
            bw = rnd.randint(140, 230)
            d.rectangle([x, y, x + bw, y + bh], outline=(12, 10, 8), width=4)
            x += bw
        y += bh
        row += 1
    d.rectangle([0, int(H * 0.72), W, H], fill=(14, 11, 9))
    return img


def fog_layer(seed, alpha=95, width=W * 2, color=(150, 165, 175)):
    n = fnoise(width, H, seed, octaves=(3, 6, 12, 24), stretch=1.0)
    a = (np.clip((n - 0.35) * 1.6, 0, 1) * alpha).astype(np.uint8)
    rgb = np.zeros((H, width, 3), np.uint8) + np.array(color, np.uint8)
    lay = Image.fromarray(np.dstack([rgb, a]), "RGBA")
    # seamless horizontal wrap: mirror second half
    half = lay.crop((0, 0, width // 2, H))
    lay.paste(half.transpose(Image.FLIP_LEFT_RIGHT), (width // 2, 0))
    return lay.filter(ImageFilter.GaussianBlur(6))


def rain_layer(seed, n=1400, alpha=70):
    lay = Image.new("RGBA", (W, H * 2), (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    rnd = random.Random(seed)
    for _ in range(n):
        x, y = rnd.randint(0, W), rnd.randint(0, H)
        ln = rnd.randint(25, 60)
        a = rnd.randint(alpha // 3, alpha)
        for yy in (y, y + H):  # tile vertically for seamless scroll
            d.line([(x, yy), (x - 8, yy + ln)], fill=(190, 205, 215, a), width=2)
    return lay


def beam_layer(size=2600, half_angle=9, length=1300, color=(255, 232, 190)):
    lay = np.zeros((size, size, 4), np.float32)
    c = size / 2
    yy, xx = np.mgrid[0:size, 0:size]
    dx, dy = xx - c, yy - c
    r = np.sqrt(dx * dx + dy * dy)
    ang = np.degrees(np.abs(np.arctan2(dy, dx)))
    core = np.clip(1 - ang / half_angle, 0, 1) ** 1.6
    fall = np.clip(1 - r / length, 0, 1) ** 0.8
    a = core * fall * 150
    for i, v in enumerate(color):
        lay[..., i] = v
    lay[..., 3] = a
    img = Image.fromarray(lay.astype(np.uint8), "RGBA").filter(ImageFilter.GaussianBlur(10))
    return img


# ------------------------------------------------------------------ scenes
def night_sky(seed, moon=None):
    arr = vgrad((6, 11, 18), (26, 40, 52))
    arr = clouds(arr, seed, (40, 52, 62), density=0.6, bottom=int(H * 0.6))
    if moon:
        arr = add_glow(arr, moon[0], moon[1], 260, (60, 70, 78), 0.8)
    return arr


def s_lighthouse_dark(seed=1):
    arr = night_sky(seed)
    arr = sea(arr, 700, seed + 1)
    img = to_img(arr)
    d = ImageDraw.Draw(img)
    island(d, 980, 1650, 610, seed, 500)
    lighthouse(d, 1330, 612, 330, lit=False, scale=1.05)
    return img, {"rain": True, "fog": True, "lightning": True}


def s_sea_waves(seed=2):
    arr = night_sky(seed, moon=(1500, 230))
    arr = sea(arr, 520, seed + 1, hl=(95, 115, 130))
    return to_img(arr), {"fog": True, "waves": True}


def s_boat_approach(seed=3):
    arr = night_sky(seed)
    arr = sea(arr, 640, seed + 1)
    img = to_img(arr)
    d = ImageDraw.Draw(img)
    island(d, 1250, 1920, 560, seed, 600)
    lighthouse(d, 1600, 562, 260, lit=False, scale=0.85)
    return img, {"boat": True, "fog": True, "rain": True}


def s_look_up(seed=4):
    arr = vgrad((5, 9, 15), (30, 44, 56))
    arr = clouds(arr, seed, (44, 56, 66), density=0.65)
    img = to_img(arr)
    d = ImageDraw.Draw(img)
    pts = ridge(0, W, 760, 9, seed)
    d.polygon([(0, H)] + pts + [(W, H)], fill=SIL)
    lighthouse(d, 960, 770, 620, lit=False, scale=1.9)
    return img, {"fog": True}


def s_map(seed=5):
    arr = vgrad((168, 146, 108), (126, 104, 74))
    n = fnoise(W, H, seed, octaves=(8, 16, 32, 64, 128))
    arr = blend(arr, (92, 72, 48), n * 0.6)
    img = to_img(arr)
    d = ImageDraw.Draw(img)
    rnd = random.Random(seed)
    ink = (52, 38, 26)
    # Scotland-ish coastline blob (stylised, original)
    coast = [(1200, 120), (1340, 220), (1300, 360), (1420, 470), (1380, 620), (1500, 760),
             (1450, 900), (1560, 1060), (1920, 1080), (1920, 0), (1250, 0)]
    d.polygon(coast, fill=(140, 116, 80), outline=ink, width=5)
    for (cx, cy, r) in ((1060, 300, 60), (990, 430, 40), (1110, 520, 30), (1020, 640, 45)):  # Hebrides
        d.ellipse([cx - r * 1.6, cy - r, cx + r * 1.6, cy + r], fill=(140, 116, 80), outline=ink, width=4)
    for (cx, cy) in ((640, 330), (668, 352), (622, 362), (690, 318), (654, 300), (705, 345), (615, 335)):
        r = rnd.randint(9, 16)
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(120, 96, 64), outline=ink, width=3)
    d.ellipse([600, 270, 735, 400], outline=(140, 30, 24), width=6)
    for i in range(0, 34):  # dotted route
        t = i / 34
        x, y = 980 - 300 * t, 430 - 90 * t
        if i % 2 == 0:
            d.ellipse([x - 4, y - 4, x + 4, y + 4], fill=ink)
    f1, f2 = font(FONT_SERIF, 54), font(FONT_SERIF, 38)
    d.text((470, 430), "ISLAS FLANNAN", font=f1, fill=ink)
    d.text((515, 495), "Eilean Mòr", font=f2, fill=(110, 30, 24))
    d.text((1480, 520), "ESCOCIA", font=f1, fill=ink)
    d.text((140, 860), "OCÉANO ATLÁNTICO", font=f2, fill=ink)
    d.text((140, 120), "1900", font=font(FONT_SERIF, 70), fill=ink)
    img = img.filter(ImageFilter.GaussianBlur(0.8))
    return img, {}


def s_keepers(seed=6):
    arr = vgrad((40, 34, 28), (12, 10, 9))
    arr = add_glow(arr, 960, 470, 520, (90, 70, 40), 0.9)
    img = to_img(arr)
    d = ImageDraw.Draw(img)
    for x, h in ((640, 600), (960, 640), (1280, 590)):
        figure(d, x, 960, h)
    d.rectangle([0, 950, W, H], fill=SIL)
    return img, {"fog": True, "flicker": True,
                 "caption": ["JAMES DUCAT  ·  THOMAS MARSHALL  ·  DONALD MACARTHUR"]}


def s_waves_crash(seed=7):
    arr = night_sky(seed)
    arr = sea(arr, 600, seed + 1, hl=(110, 128, 140))
    img = to_img(arr)
    d = ImageDraw.Draw(img)
    pts = ridge(0, 820, 520, 10, seed)
    d.polygon([(0, H)] + pts + [(820, 640), (900, H)], fill=SIL)
    foam = fnoise(900, 420, seed, octaves=(8, 16, 32, 64))
    yy, xx = np.mgrid[0:420, 0:900]
    rad = np.clip(1 - np.sqrt(((xx - 450) / 450) ** 2 + ((yy - 260) / 260) ** 2), 0, 1)
    a = (np.clip((foam - 0.45) * 2.5, 0, 1) * rad * 220).astype(np.uint8)
    spray = Image.fromarray(np.dstack([np.full((420, 900, 3), 205, np.uint8), a]), "RGBA")
    spray = spray.filter(ImageFilter.GaussianBlur(5))
    img.paste(spray, (620, 420), spray)
    return img, {"fog": True, "waves": True, "rain": True}


def s_interior_lamp(seed=8):
    img = stone_wall(seed)
    d = ImageDraw.Draw(img)
    d.rectangle([1250, 160, 1600, 520], fill=(18, 30, 44), outline=(10, 8, 6), width=14)  # window
    d.line([(1425, 160), (1425, 520)], fill=(10, 8, 6), width=10)
    d.rectangle([520, 700, 1300, 740], fill=(28, 20, 14))  # table
    for x in (560, 1250):
        d.rectangle([x, 740, x + 22, 1000], fill=(22, 16, 11))
    d.ellipse([820, 610, 940, 700], fill=(30, 26, 22))  # lamp base (cold)
    d.rectangle([862, 470, 898, 615], fill=(34, 38, 40))
    d.ellipse([840, 420, 920, 490], outline=(60, 64, 66), width=5)
    return img, {}


def s_ship_passing(seed=9):
    arr = night_sky(seed)
    arr = sea(arr, 680, seed + 1)
    img = to_img(arr)
    d = ImageDraw.Draw(img)
    island(d, 1400, 1920, 600, seed, 500)
    lighthouse(d, 1700, 602, 300, lit=False, scale=0.95)
    return img, {"ship": True, "fog": True,
                 "caption": ["15 · DICIEMBRE · 1900"]}


def s_empty_bed(seed=10):
    img = stone_wall(seed, warm=(40, 32, 26))
    d = ImageDraw.Draw(img)
    d.rectangle([420, 640, 1500, 700], fill=(26, 20, 15))
    d.rectangle([440, 560, 1480, 650], fill=(70, 66, 60))  # blanket (flat, unused)
    d.rectangle([440, 545, 640, 600], fill=(96, 92, 86))  # pillow
    for x in (420, 1480):
        d.rectangle([x, 480, x + 30, 1000], fill=(22, 16, 11))
    return img, {}


def s_table_clock(seed=11):
    img = stone_wall(seed)
    d = ImageDraw.Draw(img)
    d.rectangle([380, 720, 1540, 760], fill=(30, 22, 15))
    for x in (420, 1480):
        d.rectangle([x, 760, x + 24, 1020], fill=(22, 16, 11))
    for cx in (640, 960, 1280):  # plates with untouched food
        d.ellipse([cx - 130, 660, cx + 130, 730], fill=(150, 146, 136))
        d.ellipse([cx - 70, 670, cx + 70, 715], fill=(96, 70, 44))
    cx, cy, r = 960, 300, 130  # wall clock, stopped
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(176, 166, 146), outline=(24, 18, 12), width=12)
    for k in range(12):
        a = math.radians(k * 30)
        d.line([(cx + math.sin(a) * r * 0.78, cy - math.cos(a) * r * 0.78),
                (cx + math.sin(a) * r * 0.9, cy - math.cos(a) * r * 0.9)], fill=(24, 18, 12), width=6)
    d.line([(cx, cy), (cx + 60, cy - 40)], fill=(20, 14, 10), width=10)
    d.line([(cx, cy), (cx - 10, cy - 100)], fill=(20, 14, 10), width=6)
    return img, {"flicker": True, "fog": True, "candle": (1500, 560)}


def s_chair(seed=12):
    img = stone_wall(seed)
    d = ImageDraw.Draw(img)
    d.rectangle([300, 640, 1100, 680], fill=(30, 22, 15))
    d.rectangle([330, 680, 352, 950], fill=(22, 16, 11))
    d.rectangle([1050, 680, 1072, 950], fill=(22, 16, 11))
    # overturned chair lying on the floor
    c = (26, 19, 13)
    d.polygon([(1180, 930), (1560, 900), (1566, 940), (1186, 970)], fill=c)  # seat
    d.polygon([(1540, 900), (1760, 720), (1790, 745), (1566, 930)], fill=c)  # backrest
    d.line([(1220, 960), (1180, 1040)], fill=c, width=16)
    d.line([(1500, 935), (1470, 1035)], fill=c, width=16)
    return img, {"spot": (1450, 900)}


def s_coat(seed=13):
    img = stone_wall(seed, warm=(38, 30, 24))
    d = ImageDraw.Draw(img)
    d.rectangle([560, 300, 1360, 322], fill=(20, 15, 10))  # rack
    for x in (700, 960, 1220):
        d.line([(x, 322), (x, 360)], fill=(60, 56, 50), width=8)
        d.arc([x - 18, 345, x + 18, 380], 0, 180, fill=(60, 56, 50), width=6)
    # single oilskin coat on the right hook; the other two hooks are empty
    x = 1220
    d.polygon([(x - 25, 375), (x + 25, 375), (x + 120, 470), (x + 140, 900),
               (x - 140, 900), (x - 120, 470)], fill=(62, 58, 30))
    d.line([(x, 390), (x, 900)], fill=(30, 28, 14), width=6)
    return img, {"spot": (1220, 620)}


def s_logbook(seed=14):
    arr = vgrad((26, 20, 15), (8, 6, 5))
    arr = add_glow(arr, 1300, 430, 700, (120, 80, 36), 1.0)
    img = to_img(arr)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 640, W, H], fill=(30, 21, 14))
    d.polygon([(420, 700), (950, 660), (950, 980), (420, 1010)], fill=(196, 182, 150))
    d.polygon([(950, 660), (1480, 700), (1480, 1010), (950, 980)], fill=(186, 172, 140))
    rnd = random.Random(seed)
    for page in ((470, 940), (1000, 1430)):
        for i in range(10):
            y = 700 + i * 26
            x0 = page[0]
            x1 = page[0] + rnd.randint(260, page[1] - page[0] - 20)
            d.line([(x0, y + (10 if page[0] < 900 else 0)), (x1, y)], fill=(70, 56, 40), width=3)
    d.rectangle([1530, 470, 1580, 660], fill=(210, 196, 168))  # candle
    d.ellipse([1540, 425, 1570, 478], fill=(255, 210, 140))
    return img, {"flicker": True, "candle": (1555, 440)}


def s_giant_wave(seed=15):
    arr = night_sky(seed)
    arr = sea(arr, 760, seed + 1)
    img = to_img(arr)
    d = ImageDraw.Draw(img)
    pts = ridge(900, W, 700, 6, seed)
    d.polygon([(900, H)] + pts + [(W, H)], fill=SIL)
    for x in (1500, 1560, 1615):
        figure(d, x, 700, 90)
    return img, {"giant_wave": True, "rain": True, "lightning": True}


def s_cliff_silhouettes(seed=16):
    arr = vgrad((40, 50, 58), (12, 16, 20))
    arr = clouds(arr, seed, (70, 80, 88), density=0.6, bottom=700)
    img = to_img(arr)
    d = ImageDraw.Draw(img)
    pts = ridge(0, W, 820, 5, seed)
    d.polygon([(0, H)] + pts + [(W, H)], fill=SIL)
    for x, h in ((820, 300), (960, 320), (1100, 295)):
        figure(d, x, 830, h, lean=-0.05)
    return img, {"fog": True, "rain": True}


def s_modern_beam(seed=17):
    arr = night_sky(seed)
    arr = sea(arr, 700, seed + 1)
    img = to_img(arr)
    d = ImageDraw.Draw(img)
    island(d, 520, 1400, 600, seed, 500)
    lamp = lighthouse(d, 960, 602, 330, lit=True, scale=1.05)
    arr2 = add_glow(np.asarray(img, float), lamp[0], lamp[1], 180, (180, 150, 100), 1.0)
    return to_img(arr2), {"beam": lamp, "fog": True, "caption": ["HOY"]}


def s_dusk(seed=18):
    arr = vgrad((52, 56, 62), (120, 104, 92))
    arr = clouds(arr, seed, (70, 72, 78), density=0.55, bottom=560)
    arr = add_glow(arr, 1250, 640, 500, (90, 60, 30), 0.7)
    arr = sea(arr, 640, seed + 1, base=(40, 44, 50), hl=(130, 120, 110))
    return to_img(arr), {"fog": True, "waves": True}


def title_card(seed=0):
    arr = vgrad((4, 7, 11), (18, 26, 34))
    arr = clouds(arr, seed, (30, 40, 48), density=0.5)
    img = to_img(arr)
    d = ImageDraw.Draw(img)
    island(d, 1300, 1920, 820, seed, 300)
    lighthouse(d, 1640, 822, 250, lit=False, scale=0.8)
    f1, f2 = font(FONT_SERIF, 92), font(FONT_MONO, 40)
    for txt, f, y, col in (("EL MISTERIO", f1, 360, (225, 214, 190)),
                           ("DEL FARO DE EILEAN MÒR", f1, 470, (225, 214, 190)),
                           ("ESCOCIA  ·  DICIEMBRE DE 1900", f2, 610, (175, 40, 36))):
        x = 140
        d.text((x + 4, y + 4), txt, font=f, fill=(0, 0, 0))
        d.text((x, y), txt, font=f, fill=col)
    return img, {"fog": True}


SCENES = {
    "title": title_card, "lighthouse_dark": s_lighthouse_dark, "sea_waves": s_sea_waves,
    "boat": s_boat_approach, "look_up": s_look_up, "map": s_map, "keepers": s_keepers,
    "waves_crash": s_waves_crash, "interior_lamp": s_interior_lamp, "ship": s_ship_passing,
    "empty_bed": s_empty_bed, "table_clock": s_table_clock, "chair": s_chair, "coat": s_coat,
    "logbook": s_logbook, "giant_wave": s_giant_wave, "cliff": s_cliff_silhouettes,
    "modern_beam": s_modern_beam, "dusk": s_dusk,
}
