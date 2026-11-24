"""Director del video: voz, tiempos, render por escena y mezcla.

    py vid_main.py tts             escribe textos.json y sintetiza la voz (PowerShell)
    py vid_main.py still N T       guarda PNG de la escena N (1..) en el segundo T
    py vid_main.py render          renderiza todas las escenas en paralelo y arma el MP4
"""
import json
import math
import os
import subprocess
import sys
import wave
from multiprocessing import Pool

import numpy as np
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vid_lib import *
from scenes_a import S1, S2, S3, S4, S5, Ctx
from scenes_b import S7, S8, S9, S10, S11
from scenes_c import SP, SF

HERE = os.path.dirname(os.path.abspath(__file__))
VOZ = os.path.join(HERE, 'voz')
OUT = (1280, 720)
FPS = 24
PRE, GAP, POST = 0.7, 0.55, 1.3
ESCENAS = [S1, S2, S3, S4, SP, S5, SF, S7, S8, S9, S10, S11]
FFMPEG = r'C:\Users\ID634\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.0.2-full_build\bin\ffmpeg.exe'


def durs_beats(i):
    """Duracion (s) de la voz de cada beat de la escena i (0-index)."""
    out = []
    for j, (disp, spk) in enumerate(ESCENAS[i]['beats']):
        f = os.path.join(VOZ, 's%02d_b%02d.wav' % (i + 1, j))
        if os.path.exists(f):
            with wave.open(f) as w:
                out.append(w.getnframes() / w.getframerate())
        else:
            out.append(len(spk) * 0.065)
    return out


def tiempos(i):
    ds = durs_beats(i)
    B, t = [], PRE
    for dd in ds:
        B.append(t)
        t += dd + GAP
    total = t - GAP + POST
    total = math.ceil(total * FPS) / FPS
    B.append(total)  # centinela
    return B, ds, total


def caption(c, i):
    t, B = c.t, c.B
    n = len(ESCENAS[i]['beats'])
    cur = -1
    for j in range(n):
        if t >= B[j]:
            cur = j
    if cur < 0:
        return
    txt = ESCENAS[i]['beats'][cur][0]
    d = c.d
    rr(d, (110, 880, 1810, 1064), r=26, fill=WHITE, outline=LINEA, w=3)
    f = F(38, False)
    lines = wrap(txt, f, 1620)
    y = 972 - len(lines) * 24
    for l in lines:
        d.text((960, y), l, font=f, fill=INK, anchor='ma')
        y += 48


def frame(i, t):
    img = Image.new('RGB', (W, H), BG)
    d = ImageDraw.Draw(img)
    B, ds, total = tiempos(i)
    sc = ESCENAS[i]
    c = Ctx(img, d, t, B)
    T(d, (96, 40), sc['title'], 62, INK, True)
    d.rounded_rectangle([96, 124, 96 + 150, 131], radius=3, fill=FUS)
    chip(d, 1824, 52, '%d / %d' % (i + 1, len(ESCENAS)), GRIS, 28, anchor='ra')
    sc['draw'](c)
    caption(c, i)
    return img


def render_escena(i):
    B, ds, total = tiempos(i)
    n = int(round(total * FPS))
    out = os.path.join(HERE, 'seg_%02d.mp4' % (i + 1))
    cmd = [FFMPEG, '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', '%dx%d' % OUT,
           '-r', str(FPS), '-i', '-', '-c:v', 'libx264', '-preset', 'medium', '-crf', '20', '-pix_fmt', 'yuv420p', out]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for k in range(n):
        img = frame(i, k / FPS).resize(OUT, Image.LANCZOS)
        p.stdin.write(img.tobytes())
    p.stdin.close()
    p.wait()
    return i, n


def pista_audio():
    """Une todas las frases en una sola pista de audio, alineada con las escenas."""
    partes = []
    sr = None
    for i in range(len(ESCENAS)):
        B, ds, total = tiempos(i)
        n = int(round(total * 48000))
        buf = np.zeros(n, dtype=np.float32)
        for j, dd in enumerate(ds):
            f = os.path.join(VOZ, 's%02d_b%02d.wav' % (i + 1, j))
            with wave.open(f) as w:
                fr = w.getframerate()
                x = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768.0
                if w.getnchannels() == 2:
                    x = x.reshape(-1, 2).mean(1)
            m = int(len(x) * 48000 / fr)
            x = np.interp(np.linspace(0, len(x) - 1, m), np.arange(len(x)), x)
            a = int(B[j] * 48000)
            buf[a:a + m] += x[:max(0, min(m, n - a))]
        partes.append(buf)
    y = np.concatenate(partes)
    pk = max(1e-6, np.abs(y).max())
    y = y / pk * 0.9
    with wave.open(os.path.join(HERE, 'pista.wav'), 'w') as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(48000)
        w.writeframes((y * 32767).astype(np.int16).tobytes())


def tts():
    os.makedirs(VOZ, exist_ok=True)
    items = []
    for i, sc in enumerate(ESCENAS):
        for j, (disp, spk) in enumerate(sc['beats']):
            items.append({'id': 's%02d_b%02d' % (i + 1, j), 'texto': spk})
    with open(os.path.join(HERE, 'textos.json'), 'w', encoding='utf-8') as f:
        json.dump(items, f, ensure_ascii=False, indent=1)
    print(len(items), 'frases')


if __name__ == '__main__':
    a = sys.argv[1]
    if a == 'tts':
        tts()
    elif a == 'still':
        i, t = int(sys.argv[2]) - 1, float(sys.argv[3])
        fr = frame(i, t)
        fr.save(os.path.join(HERE, 'still_%02d_%05.1f.png' % (i + 1, t)))
        B, ds, total = tiempos(i)
        print('escena', i + 1, 'dur %.1f' % total, 'beats', [round(x, 1) for x in B])
    elif a == 'info':
        tot = 0
        for i in range(len(ESCENAS)):
            B, ds, total = tiempos(i)
            tot += total
            print(i + 1, round(total, 1), [round(x, 1) for x in B[:-1]])
        print('TOTAL %.1f s = %.1f min' % (tot, tot / 60))
    elif a == 'render':
        sel = [int(x) - 1 for x in sys.argv[2:]] or list(range(len(ESCENAS)))
        with Pool(min(14, len(sel))) as pool:
            for i, n in pool.imap_unordered(render_escena, sel):
                print('escena', i + 1, n, 'cuadros', flush=True)
        if len(sel) == len(ESCENAS):
            pista_audio()
