"""Graficas de la validacion del clasificador (cap. 7).

Los valores son los de las tablas del cap. 7 (validacion por video, 7 987 segundos):
  - Tabla de precision, recall y F1 por conducta.
  - Matriz de confusion en segundos (filas: conducta marcada por el equipo; columnas: la decidida
    por el clasificador).
Uso:  python gen_graficas_clasificador.py CARPETA_SALIDA
Colores: las primeras tres posiciones de la paleta categorica validada (azul, naranja, aqua) y una
rampa de un solo tono azul para la matriz.
"""
import os
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

SALIDA = sys.argv[1] if len(sys.argv) > 1 else '.'
os.makedirs(SALIDA, exist_ok=True)

TINTA, TINTA2, REJILLA = '#0b0b0b', '#52514e', '#e3e2dd'
AZUL, NARANJA, AQUA = '#2a78d6', '#eb6834', '#1baf7a'
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11, 'axes.edgecolor': REJILLA,
                     'axes.labelcolor': TINTA2, 'xtick.color': TINTA2, 'ytick.color': TINTA2,
                     'text.color': TINTA})

CONDUCTAS = ['Escalamiento', 'Inmovilidad', 'Nado']
PRECISION = [0.646, 0.727, 0.732]
RECALL = [0.682, 0.710, 0.732]
F1 = [0.663, 0.719, 0.732]
SEGUNDOS = [1244, 2924, 3819]
MATRIZ = [[848, 89, 307],
          [132, 2077, 715],
          [333, 690, 2796]]


def metricas():
    fig, ax = plt.subplots(figsize=(8.2, 4.6), dpi=220)
    ancho, sep = 0.25, 0.02
    series = [('Precisión', PRECISION, AZUL), ('Recall', RECALL, NARANJA), ('F1', F1, AQUA)]
    for k, (nombre, vals, color) in enumerate(series):
        xs = [i + (k - 1) * (ancho + sep) for i in range(3)]
        barras = ax.bar(xs, vals, ancho, color=color, label=nombre, zorder=3)
        for x, v in zip(xs, vals):
            ax.text(x, v + 0.012, '%.3f' % v, ha='center', va='bottom', fontsize=9.5, color=TINTA)
    ax.set_xticks(range(3))
    ax.set_xticklabels(['%s\n(%s segundos)' % (c, format(s, ',').replace(',', ' '))
                        for c, s in zip(CONDUCTAS, SEGUNDOS)])
    ax.set_ylim(0, 1.0)
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
    ax.yaxis.grid(True, color=REJILLA, linewidth=1, zorder=0)
    ax.set_axisbelow(True)
    for lado in ('top', 'right', 'left'):
        ax.spines[lado].set_visible(False)
    ax.tick_params(length=0)
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.12), ncol=3, frameon=False)
    fig.tight_layout()
    fig.savefig(os.path.join(SALIDA, 'clasificador_metricas.png'), facecolor='white')
    plt.close(fig)


def confusion():
    rampa = LinearSegmentedColormap.from_list('azul', ['#eef4fc', '#2a78d6', '#0b3a78'])
    fig, ax = plt.subplots(figsize=(6.6, 5.2), dpi=220)
    pct = [[v / sum(f) for v in f] for f in MATRIZ]
    ax.imshow(pct, cmap=rampa, vmin=0, vmax=0.85, aspect='auto')
    for i in range(3):
        for j in range(3):
            claro = pct[i][j] > 0.45
            ax.text(j, i, '%s\n(%.1f %%)' % (format(MATRIZ[i][j], ',').replace(',', ' '), pct[i][j] * 100),
                    ha='center', va='center', fontsize=12, color='white' if claro else TINTA,
                    fontweight='bold' if i == j else 'normal')
    ax.set_xticks(range(3))
    ax.set_xticklabels(CONDUCTAS)
    ax.set_yticks(range(3))
    ax.set_yticklabels(CONDUCTAS)
    ax.set_xlabel('Conducta decidida por el clasificador')
    ax.set_ylabel('Conducta marcada por el equipo')
    ax.xaxis.set_label_position('bottom')
    ax.set_xticks([x - 0.5 for x in range(1, 3)], minor=True)
    ax.set_yticks([y - 0.5 for y in range(1, 3)], minor=True)
    ax.grid(which='minor', color='white', linewidth=3)
    ax.tick_params(which='both', length=0)
    for lado in ax.spines.values():
        lado.set_visible(False)
    fig.tight_layout()
    fig.savefig(os.path.join(SALIDA, 'clasificador_matriz_confusion.png'), facecolor='white')
    plt.close(fig)


metricas()
confusion()
print('ok', SALIDA)
