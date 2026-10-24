# Preguntas pendientes

> Una por punto. Al responder, se borra de aquí. Si la respuesta debe persistir, se deja
> el tiempo necesario y luego se mueve al `.md` que corresponda.

Salen de la reauditoría del 11-oct (`hallazgosAgentes11oct-reauditoria/`). Cada punto dice
qué pasa hoy en el documento, qué opciones hay y cuál recomiendo. Si contestas «recomendado»,
aplico esa opción. Los marcados **(equipo)** también los resuelve Erick o los directores;
puedes contestar con tu mejor criterio y yo lo dejo registrado como tuyo, o me dices que lo
anote como pendiente para ellos.

Las preguntas para el laboratorio (Q-A a Q-H, incluidos el volumen de trabajo y cuántas
personas usan el sistema a la vez) están en `errores/preguntas-doctor.md`, no aquí.

---

Salen de las respuestas del orquestador web del 23-oct (E3, E9, E11 de `angel.md` §E).

- **P-2 · Salidas de la red: el documento contra `fst_auto` (E7 y E12).** Evidencia del orquestador web, HEAD
  9844e57: la red `Fusion` tiene **3** neuronas de salida (`fst_cnn.py:66` y `:243`: escalamiento, inmovilidad,
  nado). «Activa» no es salida: la calcula `segundos.py:54-66` con una regla de tres pasos y umbral 0.80, y el
  worker la guarda como «conducta activa» (el dominio de `SEGUNDO.conducta` ya la admite). Ninguna nota de
  `fst_auto` habla de pasar a cuatro salidas. El documento dice lo contrario: **4** salidas y sin umbral (D-78
  y D-94 en los caps. 2, 3 y 5). Opciones: (a) el documento se queda con cuatro salidas sin umbral, el cap. 6
  también, y el código se alinea después; no se mencionan plazos (D-117). (b) El documento pasa a tres salidas
  más la regla de umbral 0.80, lo que obliga a reescribir los caps. 2, 3 y 5 y a revertir D-78 y D-94.
  Recomendado: (a), porque dijiste que el documento es definitivo y sin plazos. Riesgo de (a): el jurado verá un
  código con tres salidas. (Cambio mi recomendación anterior, que era (b)-tres: no tenía esta evidencia.)
