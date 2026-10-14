import html, sys

# Vision general de los casos de uso (diagramas/puml/cu_vision_general.puml y cu_paquete1..5.puml):
# los tres actores, los cinco paquetes y los casos de uso que contiene cada uno.
esc = html.escape

PAQUETES = [
    ('PAQUETE 1', 'Autenticación y gestión de usuarios', [
        ('CU-01', 'Iniciar sesión'), ('CU-02', 'Cerrar sesión'), ('CU-03', 'Recuperar contraseña'),
        ('CU-16', 'Cambiar contraseña al primer acceso'), ('CU-18', 'Actualizar perfil propio'),
        ('CU-11', 'Gestionar cuenta de usuario'), ('CU-12', 'Crear cuenta de usuario'),
        ('CU-17', 'Desactivar cuenta de usuario')]),
    ('PAQUETE 2', 'Gestión de experimentos y carga de video', [
        ('CU-04', 'Registrar experimento'), ('CU-05', 'Subir video'),
        ('CU-19', 'Encolar análisis automático'), ('CU-20', 'Notificar rechazo de video')]),
    ('PAQUETE 3', 'Pipeline de análisis conductual', [
        ('', 'Ejecutar pipeline de análisis'), ('', 'Reportar error de pipeline'),
        ('', 'Pausar el análisis'), ('', 'Ajustar el recuadro y continuar'),
        ('', 'Cancelar el análisis en pausa'), ('CU-07', 'Monitorear progreso'),
        ('CU-08', 'Descargar reporte de diagnóstico')]),
    ('PAQUETE 4', 'Resultados y reportes', [
        ('CU-09', 'Consultar resultados'), ('CU-10', 'Descargar reporte (PDF, CSV, XLSX)'),
        ('CU-25', 'Revisar segundo a segundo'), ('CU-26', 'Corregir etiqueta de un segundo'),
        ('CU-27', 'Consultar estadísticas de grupo o tanda'), ('', 'Reiniciar el análisis')]),
    ('PAQUETE 5', 'Dashboard, notificaciones y administración', [
        ('CU-22', 'Consultar dashboard'), ('CU-23', 'Eliminar experimento'),
        ('CU-14', 'Borrar video automáticamente'), ('CU-13', 'Monitorear estado del sistema'),
        ('CU-24', 'Gestionar experimentos globales'), ('', 'Listar usuarios'),
        ('', 'Notificar uso de disco'), ('', 'Avisar expiración de video')]),
]
# quien usa cada paquete: (investigador, administrador, worker)
USA = [(1, 1, 0), (1, 0, 0), (1, 0, 1), (1, 0, 0), (1, 1, 1)]
ROL = {  # texto junto a la flecha, si el diagrama lo trae
    (2, 'inv'): 'observa', (2, 'wrk'): 'ejecuta el pipeline'}

CHW, CHH, GAPC = 200, 36, 12
POR_FILA = 4
PX, PW = 330, POR_FILA * CHW + (POR_FILA - 1) * GAPC + 28   # paquete: x y ancho
out = []

# --- paquetes ---
y = 40
cajas = []
for i, (num, nombre, cus) in enumerate(PAQUETES):
    filas = (len(cus) + POR_FILA - 1) // POR_FILA
    h = 36 + filas * (CHH + 10) + 8
    out.append(f'<rect x="{PX}" y="{y}" width="{PW}" height="{h}" rx="8" fill="#f1eee5" stroke="#6b6b6b" stroke-dasharray="6,4"/>')
    out.append(f'<text x="{PX+14}" y="{y+16}" class="st">{num}</text>')
    out.append(f'<text x="{PX+14}" y="{y+31}" class="nm">{esc(nombre)}</text>')
    for k, (cu, txt) in enumerate(cus):
        r, c = divmod(k, POR_FILA)
        cx = PX + 14 + c * (CHW + GAPC)
        cy = y + 40 + r * (CHH + 10)
        out.append(f'<rect x="{cx}" y="{cy}" width="{CHW}" height="{CHH}" rx="{CHH//2}" fill="#faf9f5" stroke="#1a1a1a"/>')
        if cu:
            out.append(f'<text x="{cx+CHW/2}" y="{cy+14}" text-anchor="middle" class="st">{cu}</text>')
            out.append(f'<text x="{cx+CHW/2}" y="{cy+27}" text-anchor="middle" class="a">{esc(txt)}</text>')
        else:
            out.append(f'<text x="{cx+CHW/2}" y="{cy+CHH/2+3}" text-anchor="middle" class="a">{esc(txt)}</text>')
    cajas.append((y, h))
    y += h + 22
H = y + 40

# --- actores ---
def actor(cx, cy, nombre, sub='', fill='#faf9f5'):
    out.append(f'<circle cx="{cx}" cy="{cy-26}" r="9" fill="{fill}" stroke="#1a1a1a"/>')
    out.append(f'<line x1="{cx}" y1="{cy-17}" x2="{cx}" y2="{cy+8}" stroke="#1a1a1a"/>')
    out.append(f'<line x1="{cx-14}" y1="{cy-10}" x2="{cx+14}" y2="{cy-10}" stroke="#1a1a1a"/>')
    out.append(f'<line x1="{cx}" y1="{cy+8}" x2="{cx-12}" y2="{cy+26}" stroke="#1a1a1a"/>')
    out.append(f'<line x1="{cx}" y1="{cy+8}" x2="{cx+12}" y2="{cy+26}" stroke="#1a1a1a"/>')
    out.append(f'<text x="{cx}" y="{cy+42}" text-anchor="middle" class="nm">{esc(nombre)}</text>')
    if sub:
        out.append(f'<text x="{cx}" y="{cy+55}" text-anchor="middle" class="st">{esc(sub)}</text>')

def flecha(pts, color='#1a1a1a', dash=False):
    d = 'M' + ' L'.join(f'{x},{y}' for x, y in pts)
    out.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="1.1"' + (' stroke-dasharray="4,3"' if dash else '') + ' marker-end="url(#cu-arr)"/>')

def etiqueta(x, y, t, ancla='middle'):
    w = len(t) * 5.2 + 8
    x0 = x - w / 2 if ancla == 'middle' else (x - 4 if ancla == 'start' else x - w + 4)
    out.append(f'<rect x="{x0:.0f}" y="{y-9}" width="{w:.0f}" height="12" fill="#faf9f5"/><text x="{x}" y="{y}" text-anchor="{ancla}" class="r">{esc(t)}</text>')

centros = [by + bh / 2 for by, bh in cajas]
AX_INV, AX_ADM, AX_WRK = 150, 95, PX + PW + 140
# bus del investigador (entre su actor y los paquetes), uno del administrador y uno del worker
BUS_INV, BUS_ADM, BUS_WRK = 250, 200, PX + PW + 60
inv_y = (centros[0] + centros[4]) / 2
adm_y = centros[0] - 10
wrk_y = (centros[2] + centros[4]) / 2

# investigador: desde el actor al bus, y del bus a cada paquete que usa
out.append(f'<line x1="{BUS_INV}" y1="{centros[0]}" x2="{BUS_INV}" y2="{centros[4]}" stroke="#1a1a1a"/>')
flecha([(AX_INV + 22, inv_y), (BUS_INV, inv_y)])
for i, (inv, adm, wrk) in enumerate(USA):
    if inv:
        flecha([(BUS_INV, centros[i]), (PX, centros[i])])
etiqueta(BUS_INV + 40, centros[2] - 6, 'observa', 'start')
# administrador: solo paquetes 1 y 5
out.append(f'<line x1="{BUS_ADM}" y1="{centros[0] + 14}" x2="{BUS_ADM}" y2="{centros[4] + 14}" stroke="#d9532c"/>')
flecha([(AX_ADM + 22, adm_y + 40), (BUS_ADM, adm_y + 40)], '#d9532c')
for i, (inv, adm, wrk) in enumerate(USA):
    if adm:
        yy = centros[i] + 14
        out.append(f'<path d="M{BUS_ADM},{yy} L{PX-6},{yy}" fill="none" stroke="#d9532c" stroke-width="1.1"/>')
        out.append(f'<path d="M{PX-12},{yy-4} L{PX-6},{yy} L{PX-12},{yy+4}" fill="none" stroke="#d9532c"/>')
# worker: paquetes 3 y 5
out.append(f'<line x1="{BUS_WRK}" y1="{centros[2]}" x2="{BUS_WRK}" y2="{centros[4]}" stroke="#6b6b6b" stroke-dasharray="4,3"/>')
flecha([(AX_WRK - 22, wrk_y), (BUS_WRK, wrk_y)], '#6b6b6b', True)
for i, (inv, adm, wrk) in enumerate(USA):
    if wrk:
        yy = centros[i]
        out.append(f'<path d="M{BUS_WRK},{yy} L{PX+PW+6},{yy}" fill="none" stroke="#6b6b6b" stroke-width="1.1" stroke-dasharray="4,3"/>')
        out.append(f'<path d="M{PX+PW+12},{yy-4} L{PX+PW+6},{yy} L{PX+PW+12},{yy+4}" fill="none" stroke="#6b6b6b"/>')
etiqueta(BUS_WRK + 6, centros[2] - 6, 'ejecuta el pipeline', 'start')

actor(AX_INV, inv_y, 'Investigador')
actor(AX_ADM, adm_y + 40, 'Administrador', 'con permisos extra', '#fbe9e2')
actor(AX_WRK, wrk_y, ':Worker:', '«system»', '#fdf6d8')

W = AX_WRK + 110
leg = f'''<g transform="translate(40,{H-22})" class="lg">
<line x1="0" y1="0" x2="28" y2="0" stroke="#1a1a1a"/><path d="M22,-4 L28,0 L22,4" fill="none" stroke="#1a1a1a"/><text x="38" y="3">INVESTIGADOR</text>
<line x1="170" y1="0" x2="198" y2="0" stroke="#d9532c"/><path d="M192,-4 L198,0 L192,4" fill="none" stroke="#d9532c"/><text x="208" y="3">ADMINISTRADOR (ADEMÁS DE LO DEL INVESTIGADOR)</text>
<line x1="540" y1="0" x2="568" y2="0" stroke="#6b6b6b" stroke-dasharray="4,3"/><path d="M562,-4 L568,0 L562,4" fill="none" stroke="#6b6b6b"/><text x="578" y="3">WORKER (SISTEMA)</text>
</g>'''
svg = f'''<svg viewBox="0 0 {W} {H}" role="img" aria-labelledby="cu-title cu-desc" xmlns="http://www.w3.org/2000/svg">
<title id="cu-title">Casos de uso: visión general</title>
<desc id="cu-desc">Los tres actores del sistema (investigador, administrador y worker) y los cinco paquetes de casos de uso con los casos de uso de cada uno.</desc>
<defs><marker id="cu-arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="10" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1,1 L9,5 L1,9" fill="none" stroke="#444" stroke-width="1.2"/></marker></defs>
<style>
.a{{font:400 9px 'Geist Mono',monospace;fill:#1a1a1a}}
.nm{{font:600 12px Geist,sans-serif;fill:#1a1a1a}}
.st{{font:400 8px 'Geist Mono',monospace;fill:#6b6b6b;letter-spacing:.06em}}
.r{{font:400 8px 'Geist Mono',monospace;fill:#6b6b6b;letter-spacing:.06em}}
.lg text{{font:400 9px 'Geist Mono',monospace;fill:#6b6b6b}}
</style>
{chr(10).join(out)}
{leg}
</svg>'''
page = f'''<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Casos de uso: visión general</title>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;600&family=Geist+Mono:wght@400&display=swap" rel="stylesheet">
<style>
html,body{{margin:0;background:#faf9f5}}
svg{{display:block;width:{W}px;height:{H}px}}
</style></head><body>{svg}</body></html>'''
open(sys.argv[1], 'w', encoding='utf-8').write(page)
print('ok', W, 'x', H)
