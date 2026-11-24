"""Primitivas de dibujo para el video didactico del clasificador (PIL, 1920x1080)."""
import math
import random
from PIL import Image, ImageDraw, ImageFont

W, H = 1920, 1080


def hx(s):
    s = s.lstrip('#')
    return tuple(int(s[i:i + 2], 16) for i in (0, 2, 4))


BG = (244, 244, 245)
INK = (35, 31, 32)
WHITE = (255, 255, 255)
GRIS = (118, 118, 128)
GRIS_C = (222, 222, 228)
LINEA = (200, 200, 208)
NADO = hx('2f80ed')
QUIETO = hx('e55b5b')
TREPA = hx('27ae60')
VIDEO = hx('8e44ad')
MED = hx('f2b01e')
FUS = hx('16a085')
AGUA = hx('cfe7f3')
AGUA2 = hx('8fc3e0')
CUERPO = (246, 242, 236)
CONDUCTA = {'nado': NADO, 'quieto': QUIETO, 'trepa': TREPA}


def mix(a, b, k):
    k = max(0.0, min(1.0, k))
    return tuple(int(round(a[i] * (1 - k) + b[i] * k)) for i in range(3))


def cl(x):
    return max(0.0, min(1.0, x))


def pr(t, a, b):
    return cl((t - a) / (b - a)) if b > a else (1.0 if t >= b else 0.0)


def ez(x):
    x = cl(x)
    return x * x * (3 - 2 * x)


def lerp(a, b, k):
    return a + (b - a) * k


_F = {}


def F(sz, b=False):
    k = (sz, b)
    if k not in _F:
        _F[k] = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf' if b else 'C:/Windows/Fonts/segoeui.ttf', sz)
    return _F[k]


_M = {}


def MO(sz, b=False):
    k = (sz, b)
    if k not in _M:
        _M[k] = ImageFont.truetype('C:/Windows/Fonts/consolab.ttf' if b else 'C:/Windows/Fonts/consola.ttf', sz)
    return _M[k]


def T(d, xy, s, sz=36, col=INK, b=False, anchor='la'):
    d.text((int(xy[0]), int(xy[1])), s, font=F(sz, b), fill=col, anchor=anchor)


def wrap(s, font, maxw):
    out = []
    for par in s.split('\n'):
        cur = ''
        for w in par.split(' '):
            tr = (cur + ' ' + w).strip()
            if font.getlength(tr) <= maxw or not cur:
                cur = tr
            else:
                out.append(cur)
                cur = w
        out.append(cur)
    return out


def TW(d, x, y, s, sz=34, col=INK, maxw=800, b=False, lh=1.28, center=False):
    """Texto con salto de linea automatico. Devuelve la y final."""
    f = F(sz, b)
    for ln in wrap(s, f, maxw):
        if center:
            d.text((int(x + maxw / 2), int(y)), ln, font=f, fill=col, anchor='ma')
        else:
            d.text((int(x), int(y)), ln, font=f, fill=col)
        y += sz * lh
    return y


def rr(d, box, r=18, fill=None, outline=None, w=3):
    d.rounded_rectangle([int(v) for v in box], radius=r, fill=fill, outline=outline, width=w)


def circ(d, c, r, fill=None, outline=None, w=3):
    d.ellipse([c[0] - r, c[1] - r, c[0] + r, c[1] + r], fill=fill, outline=outline, width=w)


def ln(d, p, q, col=INK, w=4):
    d.line([int(p[0]), int(p[1]), int(q[0]), int(q[1])], fill=col, width=int(w))


def head(d, tip, ang, col, size):
    l1 = (tip[0] - size * math.cos(ang - 0.45), tip[1] - size * math.sin(ang - 0.45))
    l2 = (tip[0] - size * math.cos(ang + 0.45), tip[1] - size * math.sin(ang + 0.45))
    d.polygon([tuple(tip), l1, l2], fill=col)


def arrow(d, p, q, col=INK, w=5, hd=20):
    ang = math.atan2(q[1] - p[1], q[0] - p[0])
    base = (q[0] - hd * 0.7 * math.cos(ang), q[1] - hd * 0.7 * math.sin(ang))
    ln(d, p, base, col, w)
    head(d, q, ang, col, hd)


def poly_arrow(d, pts, col=INK, w=5, hd=20, arrowhead=True):
    for a, b in zip(pts[:-2], pts[1:-1]):
        ln(d, a, b, col, w)
    if arrowhead:
        arrow(d, pts[-2], pts[-1], col, w, hd)
    else:
        ln(d, pts[-2], pts[-1], col, w)


def pt_on(pts, u):
    """Punto a la fraccion u (0-1) del largo de una poligonal."""
    ls = [math.hypot(b[0] - a[0], b[1] - a[1]) for a, b in zip(pts[:-1], pts[1:])]
    tot = sum(ls)
    r = cl(u) * tot
    for (a, b), L in zip(zip(pts[:-1], pts[1:]), ls):
        if r <= L or L == ls[-1]:
            k = r / L if L else 0
            return (lerp(a[0], b[0], k), lerp(a[1], b[1], k))
        r -= L
    return pts[-1]


def pulses(d, pts, t, col, n=3, speed=0.35, r=9):
    for i in range(n):
        u = (t * speed + i / n) % 1.0
        circ(d, pt_on(pts, u), r, fill=col, outline=WHITE, w=2)


def chip(d, x, y, s, col, sz=32, fg=WHITE, anchor='la', padx=22, pady=8):
    f = F(sz, True)
    w = f.getlength(s) + 2 * padx
    h = sz * 1.25 + 2 * pady - 8
    if anchor[0] == 'm':
        x -= w / 2
    elif anchor[0] == 'r':
        x -= w
    rr(d, (x, y, x + w, y + h), r=int(h / 2), fill=col)
    d.text((int(x + w / 2), int(y + h / 2)), s, font=f, fill=fg, anchor='mm')
    return w, h


def caja(d, box, fill=WHITE, outline=LINEA, r=22, w=3):
    rr(d, box, r, fill, outline, w)


def knob(d, cx, cy, r, ang, col=INK):
    circ(d, (cx, cy), r, fill=WHITE, outline=col, w=4)
    for k in range(0, 360, 45):
        a = math.radians(k)
        ln(d, (cx + (r + 5) * math.cos(a), cy + (r + 5) * math.sin(a)), (cx + (r + 11) * math.cos(a), cy + (r + 11) * math.sin(a)), GRIS, 2)
    a = math.radians(ang)
    ln(d, (cx, cy), (cx + (r - 4) * math.cos(a), cy + (r - 4) * math.sin(a)), col, 5)


# ------------------------------------------------------------------ espécimen
def _ell_rot(d, c, rx, ry, ang, fill, outline, w):
    pts = []
    ca, sa = math.cos(ang), math.sin(ang)
    for k in range(40):
        a = 2 * math.pi * k / 40
        x, y = rx * math.cos(a), ry * math.sin(a)
        pts.append((c[0] + x * ca - y * sa, c[1] + x * sa + y * ca))
    d.polygon(pts, fill=fill, outline=outline, width=w)


def rata(d, x, y, s, f, t, pose='nado', wall=None):
    """Espécimen de caricatura. (x, y) = centro del cuerpo; f = vector hacia donde mira."""
    fl = math.hypot(*f)
    f = (f[0] / fl, f[1] / fl)
    pp = (-f[1], f[0])
    if pp[1] < 0:
        pp = (-pp[0], -pp[1])
    ang = math.atan2(f[1], f[0])
    o = (70, 64, 66)
    lw = max(2, int(3 * s))
    # cola
    pts = []
    for i in range(7):
        a = 60 + i * 8.5
        wv = math.sin(t * 4 + i * 0.9) * (3 + i) * s * (1.0 if pose != 'quieto' else 0.35)
        pts.append((x - f[0] * a * s + pp[0] * wv, y - f[1] * a * s + pp[1] * wv))
    d.line([(int(a), int(b)) for a, b in pts], fill=(214, 168, 160), width=max(3, int(6 * s)), joint='curve')
    # patas
    if pose == 'nado':
        for k, off in enumerate((-22, 26)):
            m = math.sin(t * 9 + k * 2.2) * 12 * s
            p0 = (x + f[0] * off * s + pp[0] * 20 * s, y + f[1] * off * s + pp[1] * 20 * s)
            p1 = (p0[0] + pp[0] * 16 * s - f[0] * m, p0[1] + pp[1] * 16 * s - f[1] * m)
            ln(d, p0, p1, o, max(3, int(6 * s)))
    elif pose == 'quieto':
        for k, off in enumerate((-22, 24)):
            p0 = (x + f[0] * off * s + pp[0] * 18 * s, y + f[1] * off * s + pp[1] * 18 * s)
            p1 = (p0[0] + pp[0] * 14 * s, p0[1] + pp[1] * 14 * s + 2 * s)
            ln(d, p0, p1, o, max(3, int(6 * s)))
    elif pose == 'trepa' and wall is not None:
        for k in range(2):
            m = math.sin(t * 5 + k * 1.6) * 14 * s
            p0 = (x + f[0] * (38 + 12 * k) * s, y + f[1] * (38 + 12 * k) * s)
            p1 = (wall, p0[1] + m - 6 * s)
            ln(d, p0, p1, o, max(3, int(6 * s)))
            circ(d, p1, 5 * s, fill=o)
    # cuerpo y cabeza
    _ell_rot(d, (x, y), 60 * s, 30 * s, ang, CUERPO, o, lw)
    hc = (x + f[0] * 70 * s, y + f[1] * 70 * s)
    circ(d, hc, 25 * s, fill=CUERPO, outline=o, w=lw)
    ear = (hc[0] - f[0] * 8 * s - pp[0] * 14 * s, hc[1] - f[1] * 8 * s - pp[1] * 14 * s)
    circ(d, ear, 10 * s, fill=(236, 190, 184), outline=o, w=max(2, int(2 * s)))
    eye = (hc[0] + f[0] * 6 * s - pp[0] * 8 * s, hc[1] + f[1] * 6 * s - pp[1] * 8 * s)
    circ(d, eye, 4 * s, fill=INK)
    nose = (hc[0] + f[0] * 24 * s, hc[1] + f[1] * 24 * s)
    circ(d, nose, 6 * s, fill=(190, 110, 110))


def cilindro(d, cx, top, w, h, water=0.30):
    x0, x1, y0, y1 = cx - w // 2, cx + w // 2, top, top + h
    yw = top + int(h * water)
    d.rectangle([x0 + 3, yw, x1 - 3, y1 - 4], fill=AGUA)
    d.line([x0 + 3, yw, x1 - 3, yw], fill=AGUA2, width=5)
    rr(d, (x0, y0, x1, y1), r=26, outline=INK, w=6)
    return x0, x1, y0, y1, yw


def cil(d, cx, top, pose, t, w=230, h=430, s=None, ph=0.0):
    x0, x1, y0, y1, yw = cilindro(d, cx, top, w, h)
    s = s or w / 320.0
    if pose == 'nado':
        c = math.cos(t * 0.8 + ph)
        x = cx + 0.13 * w * math.sin(t * 0.8 + ph)
        y = yw + 0.30 * h + 22 * s * math.sin(t * 1.7 + ph)
        face = 1 if c > 0 else -1
        rata(d, x, y, s, (face, -0.18), t, 'nado')
    elif pose == 'quieto':
        rata(d, cx, yw + 95 * s + 3 * s * math.sin(t * 1.3 + ph), s, (0, -1), t, 'quieto')
    elif pose == 'trepa':
        wall = x1 - 3
        rata(d, x1 - 70 * s, yw - 10 * s + 22 * s * math.sin(t * 2.4 + ph), s, (0.12, -1), t, 'trepa', wall=wall)
    return x0, x1, y0, y1, yw


def miniframe(d, x, y, w, h, ph, bright=1.0, flip=False, shift=0):
    base = tuple(int(c * bright) if bright < 1 else int(c + (255 - c) * (bright - 1)) for c in AGUA)
    rr(d, (x, y, x + w, y + h), r=10, fill=base, outline=INK, w=3)
    bx = x + w / 2 + (w * 0.22) * math.sin(ph) + shift
    by = y + h * 0.62 + (h * 0.07) * math.cos(ph * 1.3)
    col = tuple(int(c * bright) if bright < 1 else int(c + (255 - c) * (bright - 1)) for c in CUERPO)
    d.ellipse([bx - w * 0.17, by - h * 0.10, bx + w * 0.17, by + h * 0.10], fill=col, outline=INK, width=2)
    sg = -1 if flip else 1
    circ(d, (bx + sg * w * 0.19, by - h * 0.01), h * 0.07, fill=col, outline=INK, w=2)


# ------------------------------------------------------------------ frutas y palitos
def fruta(d, cx, cy, kind, s=1.0):
    if kind == 'manzana':
        circ(d, (cx, cy + 4 * s), 62 * s, fill=hx('e0463b'), outline=hx('9c2a22'), w=4)
        d.ellipse([cx + 2 * s, cy - 78 * s, cx + 44 * s, cy - 52 * s], fill=hx('5fb85b'), outline=hx('3a7a37'), width=3)
        ln(d, (cx, cy - 56 * s), (cx - 4 * s, cy - 80 * s), hx('6b4a2a'), int(6 * s))
    else:
        d.arc([cx - 78 * s, cy - 96 * s, cx + 78 * s, cy + 62 * s], 20, 160, fill=hx('f4cf3a'), width=int(34 * s))
        d.arc([cx - 78 * s, cy - 96 * s, cx + 78 * s, cy + 62 * s], 20, 160, fill=hx('c9a21a'), width=int(5 * s))
        circ(d, (cx - 72 * s, cy - 10 * s), 7 * s, fill=hx('6b4a2a'))


def palito(d, cx, cy, s, kind, t=0.0):
    col = INK
    w = max(3, int(5 * s))
    circ(d, (cx, cy - 62 * s), 15 * s, outline=col, w=w)
    sw = math.sin(t * 6)
    if kind == 'correr':
        ln(d, (cx, cy - 46 * s), (cx + 6 * s, cy + 6 * s), col, w)
        ln(d, (cx + 2 * s, cy - 34 * s), (cx + 26 * s, cy - 16 * s + 6 * s * sw), col, w)
        ln(d, (cx + 2 * s, cy - 34 * s), (cx - 24 * s, cy - 18 * s - 6 * s * sw), col, w)
        ln(d, (cx + 6 * s, cy + 6 * s), (cx + 30 * s, cy + 40 * s + 6 * s * sw), col, w)
        ln(d, (cx + 6 * s, cy + 6 * s), (cx - 24 * s, cy + 36 * s - 6 * s * sw), col, w)
    elif kind == 'saltar':
        cy -= abs(sw) * 14 * s
        ln(d, (cx, cy - 46 * s), (cx, cy + 6 * s), col, w)
        ln(d, (cx, cy - 34 * s), (cx + 30 * s, cy - 56 * s), col, w)
        ln(d, (cx, cy - 34 * s), (cx - 30 * s, cy - 56 * s), col, w)
        ln(d, (cx, cy + 6 * s), (cx + 22 * s, cy + 36 * s), col, w)
        ln(d, (cx, cy + 6 * s), (cx - 22 * s, cy + 36 * s), col, w)
    elif kind == 'nadar':
        d.arc([cx - 70 * s, cy + 6 * s, cx + 70 * s, cy + 70 * s], 200, 340, fill=NADO, width=w)
        ln(d, (cx - 30 * s, cy - 40 * s + 4 * s * sw), (cx + 10 * s, cy - 50 * s), col, w)
        ln(d, (cx + 10 * s, cy - 50 * s), (cx + 44 * s, cy - 36 * s - 6 * s * sw), col, w)
        ln(d, (cx - 30 * s, cy - 40 * s), (cx - 60 * s, cy - 20 * s + 8 * s * sw), col, w)
    else:  # bailar
        ln(d, (cx, cy - 46 * s), (cx + 8 * s * sw, cy + 6 * s), col, w)
        ln(d, (cx, cy - 34 * s), (cx + 34 * s, cy - 60 * s + 8 * s * sw), col, w)
        ln(d, (cx, cy - 34 * s), (cx - 34 * s, cy - 60 * s - 8 * s * sw), col, w)
        ln(d, (cx + 8 * s * sw, cy + 6 * s), (cx + 22 * s, cy + 38 * s), col, w)
        ln(d, (cx + 8 * s * sw, cy + 6 * s), (cx - 22 * s, cy + 38 * s), col, w)


def cam(d, x, y, t):
    rr(d, (x, y, x + 120, y + 78), r=12, fill=hx('3a3a44'))
    circ(d, (x + 50, y + 39), 24, fill=hx('1c1c24'), outline=hx('8a8a96'), w=4)
    circ(d, (x + 50, y + 39), 9, fill=hx('4a90d9'))
    d.polygon([(x + 120, y + 26), (x + 150, y + 10), (x + 150, y + 68), (x + 120, y + 52)], fill=hx('3a3a44'))
    if int(t * 2) % 2 == 0:
        circ(d, (x + 100, y + 14), 6, fill=QUIETO)


def tick(d, cx, cy, r, col, w=10):
    ln(d, (cx - r * 0.55, cy + r * 0.05), (cx - r * 0.12, cy + r * 0.50), col, w)
    ln(d, (cx - r * 0.12, cy + r * 0.50), (cx + r * 0.62, cy - r * 0.50), col, w)


def cruz(d, cx, cy, r, col, w=10):
    ln(d, (cx - r * 0.5, cy - r * 0.5), (cx + r * 0.5, cy + r * 0.5), col, w)
    ln(d, (cx - r * 0.5, cy + r * 0.5), (cx + r * 0.5, cy - r * 0.5), col, w)
