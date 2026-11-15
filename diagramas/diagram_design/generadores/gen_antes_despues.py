import html, os, sys

# Diagramas para la diapositiva «antes y después» (TT1 contra TT2): arquitectura y pipeline.
# Mismo lenguaje visual que contenedores.html y esquema_logico.html, pero con poco texto y letra grande, porque
# van dos por lámina. Uso: python gen_antes_despues.py CARPETA_SALIDA
esc = html.escape
W, H = 640, 600
INK, PAPEL, CREMA, ROJO, ROJO_F = '#1a1a1a', '#faf9f5', '#ece7d8', '#d9532c', '#fde8e1'
CSS = (".t{font:600 18px Geist,Arial,sans-serif;fill:#1a1a1a}"
       ".s{font:400 14px 'Geist Mono',monospace;fill:#1a1a1a}"
       ".k{font:400 12px 'Geist Mono',monospace;fill:#6b6b6b}"
       ".l{font:400 12.5px 'Geist Mono',monospace;fill:#444}"
       ".g{font:600 16px Geist,Arial,sans-serif;fill:#1a1a1a}")


def caja(o, x, y, w, h, titulo, lineas, estilo='', etiqueta=None):
    fondo = {'': '#ffffff', 'vol': CREMA, 'clave': ROJO_F, 'ext': '#ffffff'}[estilo]
    borde = ROJO if estilo == 'clave' else INK
    dash = ' stroke-dasharray="7,5"' if estilo == 'ext' else ''
    o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fondo}" stroke="{borde}" stroke-width="1.6"{dash}/>')
    if etiqueta:
        o.append(f'<text x="{x + 12}" y="{y + 16}" class="k">{esc(etiqueta)}</text>')
        ty = y + 38
    else:
        ty = y + 28
    o.append(f'<text x="{x + 12}" y="{ty}" class="t">{esc(titulo)}</text>')
    o.append(f'<line x1="{x}" y1="{ty + 9}" x2="{x + w}" y2="{ty + 9}" stroke="{borde}" stroke-width="1"/>')
    for i, l in enumerate(lineas):
        o.append(f'<text x="{x + 12}" y="{ty + 31 + i * 20}" class="s">{esc(l)}</text>')


def flecha(o, pts, etiqueta=None, lado='der'):
    d = 'M' + ' L'.join(f'{x},{y}' for x, y in pts[:-1]) + f' L{pts[-1][0]},{pts[-1][1]}'
    o.append(f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="1.6"/>')
    (x1, y1), (x2, y2) = pts[-2], pts[-1]
    if abs(y2 - y1) >= abs(x2 - x1):
        s = 1 if y2 > y1 else -1
        o.append(f'<path d="M{x2 - 5},{y2 - 9 * s} L{x2},{y2} L{x2 + 5},{y2 - 9 * s}" fill="none" stroke="{INK}" stroke-width="1.6"/>')
    else:
        s = 1 if x2 > x1 else -1
        o.append(f'<path d="M{x2 - 9 * s},{y2 - 5} L{x2},{y2} L{x2 - 9 * s},{y2 + 5}" fill="none" stroke="{INK}" stroke-width="1.6"/>')
    if etiqueta:
        mx, my = (pts[0][0] + pts[1][0]) / 2, (pts[0][1] + pts[1][1]) / 2
        w = len(etiqueta) * 7.6 + 8
        x0 = mx + 8 if lado == 'der' else mx - 8 - w
        o.append(f'<rect x="{x0:.0f}" y="{my - 9:.0f}" width="{w:.0f}" height="17" fill="{PAPEL}"/>')
        o.append(f'<text x="{x0 + 4:.0f}" y="{my + 4:.0f}" class="l">{esc(etiqueta)}</text>')


def pagina(nombre, cuerpo):
    svg = (f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{esc(nombre)}" '
           f'xmlns="http://www.w3.org/2000/svg"><style>{CSS}</style>' + '\n'.join(cuerpo) + '</svg>')
    return ('<!doctype html>\n<html lang="es"><head><meta charset="utf-8"><title>' + esc(nombre) + '</title>\n'
            '<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;600&family=Geist+Mono:wght@400;600&display=swap" rel="stylesheet">\n'
            f'<style>html,body{{margin:0;background:{PAPEL}}}svg{{display:block}}</style></head><body>{svg}</body></html>')


def arquitectura(tt2):
    o = [f'<rect width="{W}" height="{H}" fill="{PAPEL}"/>']
    caja(o, 20, 14, 280, 52, 'Navegador del investigador', [], 'ext')
    if tt2:
        caja(o, 20, 100, 280, 106, 'web', ['React.js + Vite · nginx', 'Interfaz del investigador'], '', '«contenedor»')
        caja(o, 20, 236, 280, 128, 'api', ['Spring Boot · Java 21', 'API REST con JWT', 'Encola los análisis'], '', '«contenedor»')
        caja(o, 340, 100, 280, 264, 'worker', ['Python · PyTorch · OpenCV', 'Pipeline de 3 etapas', 'Red R(2+1)D-18', 'Un video a la vez'], 'clave', '«contenedor»')
    else:
        caja(o, 20, 100, 280, 106, 'frontend', ['React.js + Vite', 'Interfaz del investigador'], '', '«contenedor»')
        caja(o, 20, 236, 280, 128, 'backend', ['Flask + Gunicorn', 'API REST con JWT', 'Encola los análisis'], '', '«contenedor»')
        caja(o, 340, 100, 280, 264, 'worker', ['Python · OpenCV · PyTorch', 'Pipeline de 5 módulos', 'YOLOv8 + ByteTrack', 'ResNet-18 y ResNet-50'], 'clave', '«contenedor»')
    flecha(o, [(160, 66), (160, 100)], 'navegador')
    flecha(o, [(160, 206), (160, 236)], 'API REST + JWT')
    # capa de datos
    o.append(f'<rect x="20" y="412" width="600" height="178" rx="8" fill="#f3f1ea" stroke="{INK}" stroke-width="1.4" stroke-dasharray="7,5"/>')
    o.append(f'<text x="34" y="436" class="g">Capa de datos</text>')
    if tt2:
        caja(o, 34, 448, 180, 128, 'db', ['PostgreSQL', 'Cuentas, resultados', 'y cola de análisis'], '', '«contenedor»')
        caja(o, 228, 448, 190, 128, 'Volumen', ['Videos y reportes', 'compartido'], 'vol')
        caja(o, 432, 448, 174, 128, 'Modelos', ['Clasificador', 'entrenado', '(solo lectura)'], 'vol')
    else:
        caja(o, 34, 448, 280, 128, 'db', ['PostgreSQL', 'Cuentas, resultados', 'y cola de análisis'], '', '«contenedor»')
        caja(o, 328, 448, 278, 128, 'Archivos', ['Videos originales', 'y reportes'], 'vol')
    flecha(o, [(110, 364), (110, 448)], 'encola y sirve', 'der')
    flecha(o, [(480, 364), (480, 448)], 'toma la cola y guarda', 'izq')
    return pagina('Arquitectura del TT2' if tt2 else 'Arquitectura del TT1', o)


def tarjeta(o, y, h, num, titulo, lineas, estilo=''):
    fondo = ROJO_F if estilo == 'clave' else ('#f3f1ea' if estilo == 'baja' else '#ffffff')
    borde = ROJO if estilo in ('clave', 'baja') else INK
    dash = ' stroke-dasharray="7,5"' if estilo == 'baja' else ''
    o.append(f'<rect x="20" y="{y}" width="600" height="{h}" rx="8" fill="{fondo}" stroke="{borde}" stroke-width="1.6"{dash}/>')
    o.append(f'<circle cx="46" cy="{y + 28}" r="14" fill="{INK}"/>')
    o.append(f'<text x="46" y="{y + 34}" text-anchor="middle" class="t" fill="#fff" style="fill:#fff;font-size:16px">{num}</text>')
    o.append(f'<text x="72" y="{y + 34}" class="t">{esc(titulo)}</text>')
    for i, l in enumerate(lineas):
        o.append(f'<text x="38" y="{y + 62 + i * 21}" class="s">{esc(l)}</text>')


def pipeline(tt2):
    o = [f'<rect width="{W}" height="{H}" fill="{PAPEL}"/>']
    if tt2:
        tars = [('1', 'Preprocesamiento', ['Comprueba que el video abra,', 'corrige su rotación y confirma', 'que el modelo esté disponible'], ''),
                ('2', 'Localización de cilindros', ['Modelo de fondo y línea de agua;', 'separa los cilindros y calcula la', 'región de cada uno (de 2 a 4)'], ''),
                ('3', 'Clasificación de conducta', ['15 rasgos y 7 reglas; clip de 16 cuadros', 'Red R(2+1)D-18 con 22 medidas:', 'una conducta por segundo'], 'clave'),
                ('4', 'Resultados', ['Conducta de cada segundo, tiempos', 'por minuto y copia del video', 'para revisión'], '')]
        h = 120
    else:
        tars = [('1', 'Preprocesamiento', ['Lectura de cuadros, ecualización adaptativa (CLAHE)', 'y estabilización de la cámara (ECC + ORB)'], ''),
                ('2', 'Detección de regiones', ['Distribución de los cilindros (1×4, 2×2 o 1×3),', 'región de cada cilindro y línea de agua'], ''),
                ('3', 'Seguimiento', ['YOLOv8 + ByteTrack: asignación por IoU,', 'validación física y recuperación de estado'], 'baja'),
                ('4', 'Clasificación', ['ResNet-18, con ResNet-50 y heurística de respaldo;', 'voto mayoritario por ventana de un segundo'], ''),
                ('5', 'Resultados', ['Tiempos por conducta y desglose por minuto,', 'video anotado y datos de seguimiento'], '')]
        h = 100
    n = len(tars)
    gap = 22 if tt2 else 20
    total = n * h + (n - 1) * gap
    y = 14 + (H - 28 - total) // 2
    for i, (num, t, ls, est) in enumerate(tars):
        if tt2 and h == 120:
            lines = ls
        else:
            lines = ls[:3]
        tarjeta(o, y, h, num, t, lines, est)
        if i < n - 1:
            flecha(o, [(320, y + h), (320, y + h + gap)])
        y += h + gap
    if not tt2:
        y3 = 14 + (H - 28 - total) // 2 + 2 * (h + gap)
        o.append(f'<text x="606" y="{y3 + 34}" text-anchor="end" class="l" style="fill:{ROJO}">se eliminó en el TT2</text>')
    return pagina('Pipeline del TT2' if tt2 else 'Pipeline del TT1', o)


if __name__ == '__main__':
    d = sys.argv[1] if len(sys.argv) > 1 else '.'
    os.makedirs(d, exist_ok=True)
    for nombre, f in (('arquitectura_tt1', lambda: arquitectura(False)), ('arquitectura_tt2', lambda: arquitectura(True)),
                      ('pipeline_tt1', lambda: pipeline(False)), ('pipeline_tt2', lambda: pipeline(True))):
        open(os.path.join(d, nombre + '.html'), 'w', encoding='utf-8').write(f())
        print(nombre, W, H)
