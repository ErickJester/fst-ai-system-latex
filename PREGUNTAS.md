# Preguntas pendientes

> Una por punto. Al responder, se borra de aquí. Si la respuesta debe persistir, se deja
> el tiempo necesario y luego se mueve al `.md` que corresponda.

## Revisión segundo a segundo (decisiones D-34 y D-35)

Ya decidido y registrado: el análisis corre en segundo plano a su ritmo; solo al final el
usuario ve la pantalla de revisión segundo a segundo; las correcciones se guardan en una
tabla nueva por segundo.

1. **Quién corrige y cómo cuenta.** ¿Cualquier investigador puede corregir un análisis o
   solo quien lo creó (y el administrador)? ¿Los reportes usan las correcciones y marcan
   que fueron revisadas?
2. **Video para reproducir en el navegador.** Los `.mov` del iPhone suelen venir en un
   códec (HEVC) que Chrome y Firefox no reproducen. Para la pantalla de revisión hay que
   generar una copia en formato compatible (H.264) de los primeros 300 s. ¿La genera el
   worker al terminar el análisis? Es trabajo extra de procesamiento por video.

## Diferido: intervención humana cuando se pierde el tubo

Quedó fuera de esta versión porque no habrá vista en vivo. Si se retoma:

3. **¿Y si el usuario no está mirando cuando el sistema pierde el tubo?** ¿El análisis
   queda en pausa esperando, se le avisa con una notificación, y cuánto tiempo espera?
4. **¿Cómo decide el sistema que «el video se movió»?** Por ejemplo: el alineado de la
   cámara falla, o no se ve al espécimen durante N segundos. ¿Quién fija ese criterio?
5. **¿Se guarda el recuadro que dibuja el usuario?** Habría que guardar segundo, tubo y
   coordenadas: sería un cambio más al modelo de datos.
6. **¿Cambian las reglas de pausar y cancelar?** Hoy el investigador no puede pausar,
   cancelar ni reiniciar un análisis.
7. **¿Se permiten varios análisis en pantalla a la vez?** Hoy se procesan uno por uno en
   cola.

## Auditoría del 11-oct: decisiones para cerrar los pendientes de Vanesa

Cada punto trae mi recomendación. Los marcados **(equipo)** también los resuelve Erick o los
directores; los demás son solo tuyos. IDs de `hallazgosAgentes11oct/`.

### A. Verificar contra un artículo (los abres tú, yo corrijo)

8. **DSAAN (Meng et al. 2024): ¿separa tres conductas o una?** Hoy el cap. 1 dice que sí y la
   tabla del cap. 2 dice que no. Si no las separa, dejo solo `della_valle2025` en el cap. 1 y
   en la frase del cap. 2. (C1-03, C2-05)
9. **YOLO-Behaviour (Chan et al. 2025): ¿detecta y luego clasifica, o detecta la conducta
   directamente?** Si es lo segundo, reescribo el párrafo y la frase «este proyecto conserva
   la separación». (C2-04)
10. **`cryan2005` es sobre la suspensión de la cola, no el nado forzado.** Recomiendo quitarlo
    de los caps. 1 y 3 (la afirmación sobre antidepresivos ya la cubre `slattery2012`) y
    dejar las tres conductas solo con `armario2021`. ¿Lo quito, o tienes la referencia
    correcta de Cryan? (C3-03)
11. **ResNet: el artículo habla de «degradación», no de gradiente que se desvanece.**
    Recomiendo reescribir con «problema de degradación» y conservar la idea de que la
    conexión directa ayuda al gradiente. ¿Lo hago? (C3-04)
12. **`armario2021` para el descriptor de «área de movimiento / posición vertical».**
    Recomiendo quitar la cita y describir los rasgos como en el cap. 5 (verticalidad,
    posición del centroide respecto de la línea de agua). (C2-13)
13. **Atributo de la ISO 25010 para la robustez frente a iluminación (cap. 1).** Recomiendo
    quitar la cláusula de la norma: «se documentarán los requisitos mínimos de calidad de
    los videos». (C1-16)
14. **ANY-maze: ¿agrego una entrada `@online` de Stoelting o bajo la afirmación «más
    usadas»?** Recomiendo agregar la entrada. (C1-19, C2-12)

### B. Decisión de contenido tuya

15. **F1 «por clase» o «por conducta».** `CLAUDE.md` dice «por clase». Recomiendo
    «por conducta» en todo el documento (D-53 pide «conducta») y actualizar `CLAUDE.md`.
    Afecta resumen, cap. 1, cap. 2 y OE-5. (TT-06) **(equipo)**
16. **Título de la portada con «IA» y «RATA».** ¿Es el título registrado ante la escuela? Si
    se puede cambiar: «…ANÁLISIS CONDUCTUAL CON VISIÓN POR COMPUTADORA… EN ESPÉCIMEN…».
    Si no, lo dejo como excepción anotada en `PENDIENTES.md`. (TT-03) **(equipo y directores)**
17. **«En minutos genera un reporte».** No hay medición. Recomiendo «genera un reporte cuando
    termina, sin que el investigador tenga que estar presente» en cap. 1 y resumen. (C1-12)
18. **Gráficas de barras de la comparación entre grupos.** Ni RF-21 ni el cap. 5 las piden.
    Recomiendo quitarlas del cap. 1: «muestra el tiempo promedio por conducta de cada
    grupo». (C1-08)
19. **«Sprint 6» (cap. 3) y «flujo óptico» (cronograma del cap. 1).** Recomiendo
    «durante la fase de pruebas y validación (TT-II)» y quitar «flujo óptico».
    (C1-22, C3-08, C1-14) **(equipo)**
20. **Despliegue en la ESCOM.** Recomiendo que el alcance diga «una prueba de despliegue en el
    servidor de la ESCOM sí se hace; la operación permanente queda fuera», y alinear con
    RNF-10. (C1-05) **(equipo)**
21. **Unidad del tiempo de análisis.** Recomiendo «minutos de procesamiento por minuto de
    video» en el cap. 3 (como el cap. 2), sin fijar el umbral. (C3-06, C2-14) **(equipo)**
22. **Sturman/DeepLabCut descritos dos veces en el cap. 2.** Recomiendo dejar el resultado de
    Sturman en «Trabajos similares» y la técnica de DeepLabCut en la otra sección. (C2-10)

### C. Casos de uso

23. **CU-11 y CU-12: ¿van en el Paquete 1 (como el diagrama) o en el 5 (como las fichas)?**
    Recomiendo moverlos al Paquete 1 en las fichas y reescribir la introducción del 5 sin
    «exclusivo del Administrador». (DF-09)
24. **Eliminar un experimento: ¿desde el dashboard o desde su detalle, y pide nombre y
    contraseña?** Si vale el mockup v2: en el detalle, con nombre y contraseña, y RN-09 con
    la misma confirmación. (C5-08) **(equipo)**
25. **Formato del video: ¿se valida en el navegador y la orientación/reproducibilidad en el
    servidor?** Es lo más plausible; así quedaría `seq_carga_video` y CU-05. (DF-11, C4-10)
    **(equipo)**
26. **Regla «siempre al menos un Administrador activo».** ¿La registramos como RN nueva o la
    quitamos de CU-17, CU-11 y la pantalla? (C5-17) **(equipo)**
