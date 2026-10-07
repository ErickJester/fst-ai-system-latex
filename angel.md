# Para Ángel y su Claude: qué revisar de los cambios de Vanesa

**Rama:** `accesos-login` (salió de `main` en `2fbd456`). **No se ha unido a `main`.**
**Estado:** el documento compila sin errores ni avisos.

**Actualización del 6-oct:** se incorporaron a esta rama los 5 commits nuevos de `main`
(hasta `cd10710`: D-53, D-54, D-55, CLA-04). Hubo un solo conflicto, en el diagrama del
paquete 4 (`cu_paquete4.puml` y su PNG). Se resolvió quedándose con los cambios de esta rama
y con la frase de Ángel «[la conducta del sistema no es la correcta]». Los demás cambios se
unieron solos. Los números de línea de este archivo ya están corregidos para esa versión.

Este archivo dice qué cambió, qué quedó en la zona de Ángel y qué tiene que verificar
antes de dar por buenos los cambios. Va en orden de importancia: primero lo que hay que
**hacer**, luego lo que hay que **revisar**.

---

## 1. Lo que Ángel tiene que hacer (zona suya, no se tocó)

| # | Dónde | Qué hacer |
|---|-------|-----------|
| 1 | `chapters/05_diseno.tex:313` | Dice «(ver CU-21, RF-23)». **CU-21 ya no existe** (se fusionó en CU-22). Cambiar a «(ver CU-22, RF-23)». |
| 2 | `front/glosario.tex` | Faltan dos entradas: **tanda** (de 2 a 4 especímenes de un mismo grupo que se graban juntos; un grupo tiene una o más tandas; cada tanda produce hasta dos videos) y **repetibilidad** (el mismo video analizado varias veces da el mismo resultado, con variabilidad máxima de 5 a 10 %). |
| 3 | `chapters/04_analisis.tex` | Falta el requisito de **repetibilidad**. Los caps. 1 y 2 ya dicen que es el criterio principal del laboratorio (entrevista P13 y P8). Si el cap. 4 no lo recoge, el documento se contradice. |
| 4 | `02_estado_arte.tex`, `01_introduccion.tex` | Siglas y términos que **no se definieron** porque están en párrafos de Ángel (clasificador): **SVM** (cap. 2, clasificadores clásicos), **TT-II** (cap. 2, redes 3D), ***transfer learning*** (título de subsección del cap. 2) y **BORIS** (tabla de cronograma del cap. 1). **ROI** ya no hace falta: el cap. 3 se reescribió y desapareció. |
| 5 | caps. 3, 4 y 5 | **Portabilidad e ISO.** El cap. 3 (`03_marco_teorico.tex`) atribuye la portabilidad a la ISO/IEC/IEEE 12207, y los caps. 4 (~línea 734) y 5 (~línea 93) lo repiten. Vanesa cree que la ISO/IEC 25010:2023 ya no usa «portabilidad» sino «flexibilidad», pero **no está verificado**. Revisar la norma antes de cambiar. No se modificó nada en este punto. |
| 6 | `chapters/04_analisis.tex:455` | Dice «dos evaluadores humanos». Es una cita de la literatura y se dejó como está, pero conviene leerla por si choca con «tres analistas». |

---

## 2. Cambios que hizo Vanesa (en palabras simples)

### Capítulo 1 y resumen
- **Tres analistas, no dos.** El tiempo de anotación manual «se triplica». La entrevista (P12) lo dice así: con tres analistas se multiplica el tiempo.
- **El desglose por minuto ya no es opcional.** El laboratorio lo pidió como necesidad (P9).
- **Cuarta conducta.** La *conducta activa* ahora aparece en la propuesta y en los objetivos.
- **Grupos.** Hay tres *tipos* de grupo (control, referencia, tratamiento experimental). Un experimento tiene tres o más grupos, en promedio cuatro, porque un tipo puede repetirse. Los 6 a 8 especímenes por grupo son lo habitual, no una regla.
- **Tanda.** Se define el término y se aclara que «experimento» siempre significa el estudio completo.
- **Repetibilidad.** Se agrega como criterio principal del laboratorio, por encima de la velocidad.
- **Acervo histórico.** Nuevo punto en «Fuera del alcance»: los 80 a 100 videos históricos no se cargan al sistema.
- **Siglas y normas.** Se definen OMS, IPN/ENMyH, TT1/TT2, ISO/IEC/IEEE, ISO/IEC 25010 y *Forced Swim Test*.
- **Resumen.** Mismo cambio de «tres analistas», «una hora y media a dos horas» y siglas.

### Capítulo 2
- Se quitó la sección de DeepLabCut que estaba **duplicada**; se conservó una y se le pasó la cita que le faltaba.
- Se agregó la **repetibilidad** como criterio de calidad propio del laboratorio.
- Se definieron ML y DL.
- No se agregó columna de repetibilidad a la tabla comparativa: habría que afirmar algo de cada herramienta y no hay fuente.

### Capítulo 3
- El criterio de escalamiento ahora habla de **vista lateral** (antes decía cenital).
- Se quitó «los antidepresivos tipo antidepresivos como la fluoxetina».
- Se quitó la lista de tablas del modelo viejo y se dejó la idea de base de datos relacional con ORM.
- Protocolo del laboratorio: se agregó la **estructura del experimento** (grupos, tandas, cifras de la entrevista) y la **iluminación de referencia** (unos 2,500 lúmenes, sin garantía formal).
- Se definió FPS.

### Bibliografía
- Se quitaron 6 entradas que nadie cita: `abadi2016`, `henriques2015`, `lauer2022_madlc`, `lukezic2017`, `bewley2016_sort`, `wojke2017_deepsort`, y el comentario sobrante «INSTRUCCIONES».
- **No se quitó** `zhang2022_bytetrack`: lo cita `06_desarrollo.tex` (capítulo comentado en `main.tex`).

### Casos de uso (diagramas y fichas del cap. 5)
- Los seis diagramas se rehicieron y ahora **cada caso de uso lleva el mismo CU-xx que su ficha**.
- Se quitó «:Sistema:» como actor, y el Administrador hereda del Investigador también en la visión general y en el paquete 5.
- CU-16 (cambiar contraseña al primer acceso) ahora **extiende** a CU-01, y CU-17 (desactivar cuenta) **extiende** a CU-11. Antes eran `include` mal puestos.
- Paquete 2: se quitó la cadena falsa de `include`; CU-19 se incluye en CU-05, y CU-20 y CU-07 la extienden.
- Paquete 3: CU-08 (diagnóstico) ahora se dibuja y extiende a CU-07. Se quitaron las etapas del pipeline.
- Paquete 4: CU-10 extiende a CU-09 (antes se contradecían) y dice PDF, CSV o XLSX.
- Paquete 5: la alerta de disco es independiente y llega al Administrador. Se quitó «Conservar resultados» (es una regla, no un caso de uso).
- **CU-15** («Verificar pertenencia a Administrador») **se queda como ficha de regla de acceso**, fuera del dibujo.
- **CU-21 se fusionó en CU-22**: el dashboard ahora explica el estado agregado del experimento.
- Se actualizó la fila «Referencias» de 18 fichas, en las dos puntas de cada relación, y se quitaron las 4 citas internas «D-XX».
- `gen_pngs.sh` ya no usa rutas absolutas de otra computadora.

### Otras correcciones en las fichas (no estaban en la lista de pendientes)
Contradecían decisiones ya tomadas, por eso se corrigieron: se quitó la comparación Día 1 vs. Día 2 del texto del paquete 4 y de CU-09 (D-44); se quitó «código de error» en CU-07 y CU-20 (D-47); se cambió «en tiempo real» por «por etapas» o «periódicamente»; se completó la conducta activa en CU-07; y se reescribieron las introducciones de los paquetes 1, 2, 3, 4 y 5 para que describan lo que dibujan los diagramas.

### `PENDIENTES-VANESA.md`
Se llenó la sección «Para Erick» con los puntos 1, 4, 5 de la tabla de arriba y dos observaciones de casos de uso.

---

## 3. Qué debe verificar Ángel (y su Claude), archivo por archivo

1. **`chapters/01_introduccion.tex`**: leer los párrafos nuevos de «tipos de grupo», «tanda» y «repetibilidad». ¿Coinciden con cómo describe el cap. 4 los grupos y las tandas? ¿«Hasta dos videos por tanda» concuerda con RF-09?
2. **`chapters/03_marco_teorico.tex`, protocolo**: la estructura del experimento (3 o más grupos, 6 a 8 especímenes, tandas de 2 a 4, 3 a 4 experimentos por semestre, unos 8 videos por experimento) debe concordar con `PENDIENTES.md` («Lo que ya está decidido») y con el cap. 4.
3. **Iluminación de 2,500 lúmenes**: la cifra viene de una respuesta directa del equipo (30-ago), no de la entrevista. Los lúmenes miden flujo de luz, no iluminación sobre una superficie (eso son lux). Conviene confirmar con el laboratorio cuál es.
4. **`chapters/05_diseno.tex`, sección de casos de uso** (de `\section{Diseño de casos de uso}` a antes de `\section{Diagramas de secuencia}`): comprobar que cada `include` o `extend` del diagrama aparece en la fila «Referencias» de **las dos fichas**.
5. **Referencias a fichas fuera de esa sección**: buscar «CU-» en el resto del cap. 5 y en el cap. 4, por si algo apunta a un CU eliminado o cambiado.
6. **Secuencias** (`seq_*.puml`): revisar si mencionan CU-21, CU-15 o el viejo «Gestionar cuenta de investigador» (ahora «Gestionar cuenta de usuario»).
7. **Diagramas**: abrir `figures/mermaid/cu_*.png` y confirmar que se leen bien. Se generaron con PlantUML 1.2026.8 y `!pragma layout smetana`.
8. **Casos de uso sin ficha propia** (su contenido está dentro de otra ficha): «Ejecutar pipeline de análisis» y «Reportar error de pipeline» (CU-07), «Desglosar por minuto» y «Comparar grupos en Día 2» (CU-09), «Generar archivo de reporte» (CU-10). Decidir si basta o si cada uno necesita ficha.
9. **Decisión abierta:** CU-06 «Consultar historial de experimentos» repite lo que hace CU-22, y CU-24 «Gestionar experimentos globales» se solapa con los dos, porque todos ven todos los experimentos (RN-08). No se tocaron.
10. **`bib/referencias.bib`**: compilar y confirmar que no aparece ninguna cita rota. Si algún capítulo comentado se reactiva, revisar las 6 entradas eliminadas.

---

## 4. Riesgos y cosas que no son seguras

- **«Tres analistas» y «se triplica»** salen de la entrevista (P12). La nota de `errores/` dice que la cuenta de «más de 200 horas-persona» solo cuadra con tres analistas.
- **La repetibilidad (5 a 10 %)** se escribe como lo que el laboratorio señaló (P13). Es un criterio del laboratorio, **no** un atributo de la ISO/IEC 25010, y así quedó dicho en el cap. 2.
- **Acervo histórico:** se dijo solo que no se carga al sistema. No se afirmó cómo se usa, porque `CLAUDE.md` y D-26 prohíben entrenar con las anotaciones del laboratorio.
- **ISO/IEC 25010 y «portabilidad»:** sin verificar (punto 5 de la primera tabla).
- **`04_analisis.tex:446`** menciona el umbral 0.70 como historia. Es de Ángel; conviene confirmar que se entiende como algo descartado.

---

## 5. Respuestas sugeridas para el frontend (no están decididas)

Estas tres preguntas se contestaron como **recomendación**, a partir de `INSTRUCCIONES-WEB.md`. Las decide Vanesa con el equipo.

1. **Contraseña temporal:** sí mostrarla una sola vez al crear la cuenta; sin caducidad por ahora (caducar exigiría una columna nueva en `USUARIO`).
2. **Token:** mantener `sessionStorage`, aceptando que la sesión dura lo que dure la pestaña. Si se quiere que sobreviva al cerrar el navegador, la opción segura es una cookie `HttpOnly`, y eso obliga a tocar el backend y CORS.
3. **Revisión segundo a segundo:** va en este frontend y se construye al final, como dice la sección 12 de `INSTRUCCIONES-WEB.md`.

---

## 6. Hallazgos sobre `INSTRUCCIONES-WEB.md` (no se editó)

Archivo de Ángel. Estos puntos salieron de una lectura completa hecha **antes** de los
commits del 5 y 6 de octubre. Después se revisó solo lo marcado abajo; el resto **no se ha
vuelto a verificar** y conviene que su Claude lo compruebe contra la versión actual.

1. ~~**D-44 no se aplicó ahí.**~~ **Resuelto en `main`:** R-11 está eliminada y la ruta de comparación ya es entre grupos.
2. **¿Se analiza el Día 1?** **Sigue abierto.** La regla R-03 todavía dice que el Día 1 «se analiza (sus primeros 5 min) si la tanda es del grupo control», pero D-54 dice que el Día 1 solo confirma el video de habituación y **no se analiza**. Además §4 encola todos los videos. Hay que decidir y dejar los tres textos iguales.
3. **Errores sin distinguir.** El error solo sale de `deteccion`, y el mensaje se arma con la etapa, así que «no se pudo abrir el video» y «no se hallaron los cilindros» se ven igual. Falta la transición `preprocesamiento → error`.
4. **El SQL rechazaría el error del worker.** La restricción de `rutadiagnostico` choca con guardar la ruta antes de marcar el error. Debe hacerse en una sola actualización.
5. **Usuario desactivado:** conserva su token hasta una semana. El backend debe revisar `activo` en cada petición, y exigir `cambioRequerido` también del lado del servidor.
6. **Borrado al 90 % de disco:** puede borrar videos que todavía no se analizan, y no elimina las copias `_web.mp4` ni `_cajas.json`.
7. **Conducta activa:** falta en las columnas del CSV y XLSX, en el esquema de resultados (9.5) y en 9.8.
8. **Otros:** el backend «nunca escribe `nivelClasif`» pero la revisión lo recalcula; la secuencia de crear cuenta solo valida el correo duplicado (falta el identificador); el enlace de recuperación se puede reutilizar; el nginx de ejemplo no tiene HTTPS aunque §2 lo pide; la sección 9 dice «no hay mockups» pero existe `mockups/v2/`.

---

## 7. Lo que llegó de `main` el 6-oct y conviene mirar

Al unir `main` con esta rama, la revisión rápida de términos prohibidos encontró texto nuevo en la
zona de Ángel (no se tocó):

- `chapters/05_diseno.tex:409` y `:590` usan «número de **rata**» en el cuerpo. La regla del
  proyecto pide «espécimen».
- `chapters/05_diseno.tex:409`, `:589` y `:591` citan **D-55** y **D-04** dentro del texto. Un lector de
  la tesis no puede resolver esas citas (es el mismo problema que se corrigió en las fichas de
  casos de uso).
- Las fichas CU-25, CU-26 y CU-27 (zona de Vanesa) ya usan «la conducta que puso el sistema» en
  lugar de «propuesta»; se unieron sin problema con los cambios de esta rama.

---

## 8. Cómo revisar

```bash
git fetch origin
git log main..origin/accesos-login -p      # leer los commits completos, como pide CLAUDE.md
git diff main...origin/accesos-login --stat
latexmk -pdf -interaction=nonstopmode -outdir=build main.tex
```

Antes de cambiar algo, aplicar la regla de `CLAUDE.md`: **ninguna corrección sin una fuente de mayor rango**. Si algo de esta lista no tiene fuente, se anota como pregunta en `errores/preguntas-doctor.md` y no se resuelve a ojo.
