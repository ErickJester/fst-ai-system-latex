# Flujo general del sistema

![Flujo del sistema](../../figures/diagramas/flujo_sistema.png)

Archivo interactivo: [flujo_sistema.html](flujo_sistema.html).
Versión en PlantUML del documento: [`../flujo_general.puml`](../flujo_general.puml).

## Qué muestra

El camino de un video desde que el investigador lo sube hasta que descarga los reportes
(abajo), y, aparte, cómo se entrena el modelo que usa la clasificación (arriba).

## Flujo por video (de izquierda a derecha)

1. **El investigador sube el video del experimento.**
2. **El backend** valida formato y orientación (`.mp4` o `.mov`, en horizontal) y guarda el
   video en el volumen compartido.
3. **Se encola el análisis:** se crea un registro con estado «en cola» en la tabla
   `ANALISIS`.
4. **El worker toma la tarea** consultando periódicamente esa tabla.
5. **Pipeline de análisis,** tres etapas:
   - *Preprocesamiento:* registro de cámara y modelo de fondo.
   - *Cilindros:* localiza de 2 a 4 tubos por video.
   - *Clasificación:* decide la conducta de cada segundo con el modelo entrenado. Es la
     única etapa que usa el modelo.
6. **Si todo sale bien** se guardan los resultados: conducta de cada segundo, tiempos por
   minuto y la copia del video para revisión (H.264).
7. **Si falla** (el video no se abre o no se encuentran los cilindros), el análisis pasa a
   «error», se genera el reporte de diagnóstico y se avisa al investigador (RN-11).
8. **El investigador consulta y revisa** segundo a segundo; al guardar, los totales por
   minuto se recalculan (RN-14).
9. **Descarga los reportes** en PDF, CSV o XLSX.

## Entrenamiento y evaluación (fuera de línea)

Ocurre antes de desplegar y no forma parte del flujo por video: videos del laboratorio,
etiquetado por el equipo (el etiquetador propone la conducta y el equipo revisa y corrige),
entrenamiento, modelo entrenado (queda en el volumen de modelos) y evaluación con
precisión, *recall* y F1 por conducta. **Sin las anotaciones manuales del laboratorio**,
ni para entrenar ni para probar. La evaluación está marcada como provisional porque sigue
abierta la pregunta de si basta con F1 sobre un conjunto de prueba propio.

## Fuentes

Cap. 5: «Arquitectura general», «Diseño del pipeline de análisis conductual» (módulos 1 a
4, entrenamiento en bola de nieve) y «Ciclo de vida del análisis»; cap. 4: RN-11, RN-14.

## Diferencias con `flujo_general.puml` y con el texto

- El `.puml` agrupa todo en «Sistema web», «Análisis de conducta» y «Almacenamiento»; aquí
  se muestra el recorrido paso a paso, con el camino de falla.
- El `.puml` dice «Preprocesamiento (cuadros y limpieza)»; aquí dice lo que describe el
  cap. 5: registro de cámara y modelo de fondo.
- **El texto del cap. 5 (párrafo antes de la figura del flujo)** dice que el ciclo de
  entrenamiento es «anotación experta, dataset y entrenamiento». Eso contradice la
  estrategia vigente (se entrena sin las anotaciones del laboratorio) y este diagrama.
  En la rama `decisiones-11oct` ya está corregido: el párrafo dice ahora «clips etiquetados por
  el equipo, entrenamiento y evaluación».

## Cómo regenerarlo

```bash
python diagramas/diagram_design/generadores/gen_flujo.py diagramas/diagram_design/flujo_sistema.html
```

## Actualización del 12-oct (rama `decisiones-11oct`)

- **Día 1:** se sube y se guarda, pero no se encola ni se analiza (D-71). Está en el cuadro
  «Se encola el análisis».
- **Pausa:** si durante la clasificación pasan 3 s seguidos sin ver al espécimen, el análisis
  pasa a «en pausa» y se avisa al usuario; si ajusta el recuadro, continúa, y si no responde
  en 5 minutos, se cancela (RN-17, D-67). Aparece como un cuadro punteado a la derecha de la
  clasificación.
- **Reinicio:** el investigador puede reiniciar el análisis desde la pantalla de revisión; el
  resultado anterior se borra al empezar el nuevo (RN-04, D-68). Está en el cuadro final del
  investigador.

## Actualización del 12-oct (D-84 a D-89)

- **Worker:** toma la tarea más antigua y procesa un video a la vez (D-85).
- **Pausa:** guarda una imagen fija, avisa, y el usuario ajusta el recuadro o cancela; el
  análisis continúa desde ahí, y sin respuesta en 5 minutos se cancela (D-89).
- **Falla:** cualquier fallo imprevisto termina igual, con «error» y reporte de diagnóstico, y
  el worker sigue con el siguiente video (D-88).
