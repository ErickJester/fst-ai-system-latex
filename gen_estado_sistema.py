"""
Maquina de Estados Global - Ciclo de Vida del Experimento FST
Salida: diagramas/estado_sistema.png
"""
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

# ---------- paleta -----------------------------------------------------------
TC   = "#1A1A1A"   # texto principal
SC   = "#555555"   # texto secundario
AC   = "#3A3A3A"   # flechas
LC   = "#222222"   # labels de transicion

# estados simples
SBG, SBD = "#DAE8FC", "#6C8EBF"   # azul
# estado error
EBG, EBD = "#F8CECC", "#B85450"   # rojo
# estado terminal-ish (archivado)
ABG, ABD = "#E1D5E7", "#9673A6"   # lila
# composite estados
C1BG, C1BD = "#F5F5F5", "#999999"   # gris generico
C2BG, C2BD = "#E8F5E9", "#82B366"   # verde (procesamiento)
C3BG, C3BD = "#F0F4FF", "#6C8EBF"   # azul suave (completado)

# ---------- helpers ----------------------------------------------------------
def state(ax, x, y, w, h, label, bg=SBG, bd=SBD, fs=8.5):
    r = FancyBboxPatch((x - w/2, y - h/2), w, h,
                       boxstyle="round,pad=0.08",
                       facecolor=bg, edgecolor=bd, linewidth=1.5, zorder=5)
    ax.add_patch(r)
    ax.text(x, y, label, ha="center", va="center",
            fontsize=fs, fontweight="bold", color=TC, zorder=6,
            multialignment="center")


def composite(ax, x, y, w, h, title, bg=C1BG, bd=C1BD):
    """caja de estado compuesto con header."""
    # marco principal
    r = FancyBboxPatch((x - w/2, y - h/2), w, h,
                       boxstyle="round,pad=0.12",
                       facecolor=bg, edgecolor=bd,
                       linewidth=1.6, zorder=2)
    ax.add_patch(r)
    # header (franja superior)
    header_h = 0.42
    hr = FancyBboxPatch((x - w/2 + 0.02, y + h/2 - header_h),
                        w - 0.04, header_h - 0.02,
                        boxstyle="round,pad=0.02",
                        facecolor=bd, edgecolor=bd, linewidth=0,
                        zorder=3, alpha=0.65)
    ax.add_patch(hr)
    ax.text(x, y + h/2 - header_h/2 - 0.03, title,
            ha="center", va="center", fontsize=9.5, fontweight="bold",
            color="white", zorder=4)


def initial(ax, x, y, r=0.16):
    ax.add_patch(plt.Circle((x, y), r, color="black", zorder=6))


def final(ax, x, y, r=0.18):
    ax.add_patch(plt.Circle((x, y), r, color="black", zorder=6))
    ax.add_patch(plt.Circle((x, y), r + 0.1, color="black",
                            fill=False, linewidth=1.8, zorder=6))


def arrow(ax, x1, y1, x2, y2, label="", lx=None, ly=None,
          cs="arc3,rad=0.", fs=7.0, color=AC, lw=1.2,
          style="->"):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle=style, color=color, lw=lw,
                                connectionstyle=cs),
                zorder=7)
    if label:
        mx = lx if lx is not None else (x1 + x2) / 2
        my = ly if ly is not None else (y1 + y2) / 2
        ax.text(mx, my, label, ha="center", va="center", fontsize=fs,
                color=LC,
                bbox=dict(boxstyle="round,pad=0.18", facecolor="white",
                          edgecolor="#CCCCCC", linewidth=0.6, alpha=0.95),
                zorder=8)


# ---------- figura -----------------------------------------------------------
W, H = 13, 18
fig, ax = plt.subplots(figsize=(W, H))
ax.set_xlim(0, 13)
ax.set_ylim(0, 18)
ax.axis("off")
fig.patch.set_facecolor("white")
ax.set_facecolor("white")

# titulo
ax.text(6.5, 17.5,
        "M\u00e1quina de Estados Global \u2014 Ciclo de Vida del Experimento FST",
        ha="center", va="center", fontsize=13, fontweight="bold", color=TC)
ax.text(6.5, 17.1, "Plataforma Web FST  \u00b7  TT 2026-B066",
        ha="center", va="center", fontsize=9, color=SC, style="italic")

# ---------- inicial ----------------------------------------------------------
initial(ax, 4.0, 16.3)

# ---------- composite: Incompleto -------------------------------------------
composite(ax, 4.0, 13.55, 6.4, 3.2, "Incompleto")
# sub-inicial
initial(ax, 2.0, 14.45, r=0.12)
# sub-estados
state(ax, 4.0, 14.45, 3.2, 0.6, "SinSujetos")
state(ax, 4.0, 13.50, 3.9, 0.6, "EsperandoVideos")
state(ax, 4.0, 12.55, 4.4, 0.6, "ListoParaEjecuci\u00f3n")

# sub-transiciones internas
arrow(ax, 2.15, 14.45, 2.4, 14.45)   # inicial -> SinSujetos
arrow(ax, 4.0, 14.15, 4.0, 13.80,
      "sujetos registrados\n(etiquetas / \u00edndices)",
      lx=5.9, ly=13.98, fs=6.5)
arrow(ax, 4.0, 13.20, 4.0, 12.85,
      "videos validados\ny subidos",
      lx=5.95, ly=13.03, fs=6.5)

# Inicial global -> Incompleto
arrow(ax, 4.0, 16.14, 4.0, 15.18,
      "Investigador crea\nnuevo experimento",
      lx=5.9, ly=15.65, fs=7.0)

# ---------- composite: Motor de Analisis ------------------------------------
composite(ax, 4.0, 8.45, 6.4, 5.2, "Motor de An\u00e1lisis  (Worker As\u00edncrono)",
          bg=C2BG, bd=C2BD)
state(ax, 4.0, 10.30, 3.2, 0.55, "Encolado")
state(ax, 4.0, 9.45,  4.4, 0.55, "Preprocesamiento")
state(ax, 4.0, 8.60,  4.4, 0.55, "Detecci\u00f3n de ROIs")
state(ax, 4.0, 7.75,  5.2, 0.55, "Rastreo  (YOLOv8 + ByteTrack)")
state(ax, 4.0, 6.90,  5.0, 0.55, "Clasificaci\u00f3n de Conducta")

# sub-transiciones internas del motor
arrow(ax, 4.0, 10.02, 4.0, 9.73, "worker toma el trabajo",
      lx=6.35, ly=9.88, fs=6.5)
arrow(ax, 4.0, 9.17, 4.0, 8.88, "CLAHE aplicado",
      lx=5.9, ly=9.03, fs=6.5)
arrow(ax, 4.0, 8.32, 4.0, 8.03, "cilindros detectados",
      lx=6.25, ly=8.17, fs=6.5)
arrow(ax, 4.0, 7.47, 4.0, 7.18, "tracks y coordenadas listas",
      lx=6.55, ly=7.32, fs=6.5)

# ListoParaEjecucion -> Encolado (Motor)
arrow(ax, 4.0, 12.25, 4.0, 11.02,
      'Investigador presiona\n"Iniciar An\u00e1lisis"',
      lx=6.15, ly=11.63, fs=7.0)

# ---------- estado simple: FalloAnalisis ------------------------------------
state(ax, 10.8, 8.45, 3.4, 0.95,
      "FalloAn\u00e1lisis\n(video corrupto, error modelo,\nfalta de RAM)",
      bg=EBG, bd=EBD, fs=7.2)

# Motor -> Fallo
arrow(ax, 6.6, 8.45, 9.1, 8.45,
      "error durante el pipeline",
      lx=7.85, ly=8.62, fs=7.0,
      cs="arc3,rad=0.")

# Fallo -> Encolado (reintento) - curva por arriba
arrow(ax, 10.8, 8.92, 5.6, 10.30,
      "Investigador solicita reintento",
      cs="arc3,rad=-0.35", lx=9.2, ly=10.55, fs=7.0)

# ---------- composite: Completado -------------------------------------------
composite(ax, 4.0, 3.85, 6.4, 2.7, "Completado",
          bg=C3BG, bd=C3BD)
initial(ax, 2.0, 4.55, r=0.12)
state(ax, 4.0, 4.55, 3.8, 0.55, "ResultadosDisponibles")
state(ax, 4.0, 3.55, 3.6, 0.55, "ReporteGenerado")

arrow(ax, 2.15, 4.55, 2.4, 4.55)   # inicial -> ResultadosDisponibles
arrow(ax, 4.0, 4.27, 4.0, 3.83,
      "Investigador solicita\nexportaci\u00f3n (CSV / PDF)",
      lx=6.15, ly=4.05, fs=6.5)

# Motor -> Completado
arrow(ax, 4.0, 5.85, 4.0, 5.22,
      "pipeline finaliza con \u00e9xito  (100%)",
      lx=6.35, ly=5.53, fs=7.0)

# ---------- Archivado --------------------------------------------------------
state(ax, 10.8, 3.85, 3.2, 0.85,
      "Archivado\n(archivos .mp4 eliminados\ntras N d\u00edas)",
      bg=ABG, bd=ABD, fs=7.2)

# Completado -> Archivado
arrow(ax, 7.22, 3.85, 9.2, 3.85,
      "cronjob de limpieza\n(N d\u00edas)",
      lx=8.2, ly=4.15, fs=7.0)

# ---------- final global -----------------------------------------------------
final(ax, 6.5, 1.2)

# Archivado -> final
arrow(ax, 10.8, 3.42, 6.82, 1.35,
      "Investigador elimina\nexperimento",
      cs="arc3,rad=-0.25", lx=10.3, ly=1.7, fs=7.0)

# FalloAnalisis -> final
arrow(ax, 10.8, 7.97, 6.82, 1.45,
      "Investigador elimina\nexperimento",
      cs="arc3,rad=0.45", lx=12.3, ly=4.8, fs=7.0)

# Incompleto -> final (cancelar)
arrow(ax, 0.82, 13.55, 6.18, 1.35,
      "Investigador cancela /\nelimina experimento",
      cs="arc3,rad=0.55", lx=0.6, ly=7.5, fs=7.0)

# ---------- leyenda ----------------------------------------------------------
lx0, ly0 = 0.3, 0.2
ax.text(lx0, ly0 + 0.45, "Leyenda", fontsize=8, fontweight="bold", color=TC)
items = [
    (SBG, SBD, "Estado simple"),
    (EBG, EBD, "Estado de error"),
    (ABG, ABD, "Estado de archivo"),
    (C2BG, C2BD, "Estado compuesto"),
]
for i, (fc, ec, lbl) in enumerate(items):
    rx = lx0 + i * 3.1
    r = FancyBboxPatch((rx, ly0 - 0.05), 0.4, 0.22,
                       boxstyle="round,pad=0.03",
                       facecolor=fc, edgecolor=ec, linewidth=1.2, zorder=4)
    ax.add_patch(r)
    ax.text(rx + 0.5, ly0 + 0.06, lbl, fontsize=7.5, va="center", color=TC)

# ---------- guardar ----------------------------------------------------------
OUT = (r"C:\Users\ID634\Desktop\proyectos\latexFST"
       r"\fst-ai-system-latex\diagramas\estado_sistema.png")
plt.savefig(OUT, dpi=180, bbox_inches="tight", facecolor="white")
plt.close()
print("Guardado:", OUT)
