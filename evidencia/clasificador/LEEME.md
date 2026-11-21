# Evidencia de la validación del clasificador

Copia local de lo que quedó en Google Drive (`fst/corridas/` y `fst/figuras/`), generado en Colab con
`fst_cnn_seg.validar` (validación cruzada por video, 5 partes, 11 videos, 7 987 segundos calificados).

- `corridas/*.npz`: predicciones por segundo de cada corrida (`P` = probabilidades de escalamiento, inmovilidad
  y nado; `conducta` = etiqueta del equipo). Es la evidencia primaria.
- `figuras/`: matriz de confusión y F1 (`confusion_y_f1.png`), métricas (`metricas_por_conducta.csv`), datos por
  conducta, curva de pérdida, líneas de tiempo humano vs. red y ejemplos de errores.
- `calcular_metricas.py` recalcula todo desde los `.npz`; su salida está en `salida_calcular_metricas.txt`.

Corrida `base` (validación estándar): exactitud 0.710, F1 0.646 / 0.712 / 0.732.
Las cifras del cap. 7 (exactitud 0.716, F1 0.663 / 0.719 / 0.732) no coinciden con ninguna de las seis corridas guardadas.
