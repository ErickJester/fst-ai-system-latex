# Diagrama de clases en dos hojas carta horizontales

Es el mismo diagrama de clases (`../clases.puml`), partido en dos figuras para que cada una
quepa en una hoja carta horizontal del documento con su pie de figura.

| Hoja | Contenido | Archivo |
|------|-----------|---------|
| 1 | Usuarios, experimentos, grupos, tandas, espécimen, video y análisis | [clases_hoja1.html](clases_hoja1.html) / [clases_hoja1.png](clases_hoja1.png) |
| 2 | Observaciones, resultados y análisis automático (worker, pipeline, conducta, segundo, ROI) | [clases_hoja2.html](clases_hoja2.html) / [clases_hoja2.png](clases_hoja2.png) |

`Video`, `Analisis` y `Especimen` aparecen en las dos hojas, porque son los puntos donde se
unen.

## Tamaño

Con los márgenes del documento (3 cm a los lados y 2 cm arriba y abajo) y una figura de hasta
el 90 % de la altura del texto, la hoja 1 (1400 × 1170 px) y la hoja 2 (1740 × 1113 px) caben
con su pie de figura. Con eso, la letra de las clases queda en unos 4 pt en papel. Es
legible, pero chica: para ganar tamaño habría que partir el diagrama en tres hojas.

## Fuente y generador

`../clases.puml`. Los datos de las clases y las relaciones están escritos dentro de
`generadores/gen_clases_hojas.py`: si cambia el diagrama de clases, hay que actualizarlo.

```bash
python diagramas/diagram_design/generadores/gen_clases_hojas.py 1 diagramas/diagram_design/clases_hoja1.html
python diagramas/diagram_design/generadores/gen_clases_hojas.py 2 diagramas/diagram_design/clases_hoja2.html
```
