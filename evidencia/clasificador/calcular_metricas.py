"""Recalcula precisión, recall, F1, exactitud y matriz de confusión a partir de las predicciones
guardadas por la validación por video (corridas/*.npz, salida de fst_cnn_seg.validar).
Uso: python calcular_metricas.py [corridas/base.npz ...]   (sin argumentos, todas las corridas)"""
import sys, glob, numpy as np
C = ['escalamiento', 'inmovilidad', 'nado']
for f in (sys.argv[1:] or sorted(glob.glob('corridas/*.npz'))):
    z = np.load(f, allow_pickle=True)
    y, P = z['conducta'], z['P']
    m = np.isin(y, C)
    yi = np.array([C.index(v) for v in y[m]]); pr = P[m].argmax(1)
    cm = np.zeros((3, 3), int)
    for a, b in zip(yi, pr):
        cm[a, b] += 1
    pre, rec = cm.diagonal() / cm.sum(0), cm.diagonal() / cm.sum(1)
    f1 = 2 * pre * rec / (pre + rec)
    print(f'== {f}: {m.sum()} segundos, exactitud {cm.trace()/cm.sum():.3f}, F1 promedio {f1.mean():.3f}')
    for i, c in enumerate(C):
        print(f'   {c:13s} precisión {pre[i]:.3f}  recall {rec[i]:.3f}  F1 {f1[i]:.3f}  segundos {cm[i].sum()}')
    print('   matriz (filas: humano; columnas: red):', cm.tolist())
