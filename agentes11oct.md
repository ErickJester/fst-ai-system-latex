# agentes11oct — auditoría del 11-oct, decisiones y aplicación

**Fecha:** 2026-10-11 · **Rama de trabajo:** `decisiones-11oct` (local, creada desde `origin/accesos-login`, sin comitear ni subir) · **Base auditada:** `main` en `da96c00` / `00f045a`.

Este archivo junta tres cosas: lo que se auditó, lo que se decidió y aplicó en la rama, y lo que falta.

---

## 1. Dónde está cada cosa

| Qué | Dónde |
|---|---|
| Primera auditoría (9 agentes, 177 hallazgos) | `hallazgosAgentes11oct/` en `main` (commit `00f045a`). Resumen en `00_resumen.md` |
| Reauditoría de Vanesa (181 hallazgos) | `hallazgosAgentes11oct-reauditoria/` en `origin/accesos-login` |
| Cierre de la primera auditoría contra la rama de Vanesa (`fd3d543`) | `hallazgosAgentes11oct/10_cierre-contra-accesos-login.md` (sin comitear): 76 resueltos, 19 parciales, 82 sin resolver |
| Decisiones registradas | `errores/preguntas-doctor.md` §6, filas **D-66 a D-77** (sin comitear) |
| Cambios aplicados | rama local `decisiones-11oct` (21 archivos modificados, sin comitear) |

Ramas: `main` (`00f045a`), `accesos-login` de Vanesa (`8f004d8`) y `decisiones-11oct`, que parte de la de Vanesa. Ninguna se ha mezclado con otra.

---

## 2. Qué se hizo

### 2.1 Primera auditoría (solo lectura)
- Nueve agentes en paralelo: caps. 1 a 5, diagramas relacional y de clases, diagramas de flujo/CU/secuencia, reglas en `.md` y terminología.
- Resultado: 177 entradas (19 Alta, 81 Media, 77 Baja, 43 preguntas abiertas), que se reducen a 13 problemas Altos distintos.
- Se comiteó y subió a `main` (`00f045a`).

### 2.2 Cierre contra la rama de Vanesa
- Cada hallazgo se contrastó contra `accesos-login` (`fd3d543`). De las 19 Altas: 14 resueltas, 4 parciales (casi todas por PNG sin regenerar) y 1 sin tocar (`clases.png`).
- Después Vanesa regeneró los PNG (`8f004d8`); ese estado no se re-verificó.

### 2.3 Verificaciones que se hicieron
- **DSAAN (Meng et al. 2024):** solo clasifica inmovilidad (ratón, nado forzado y suspensión de la cola); 94 imágenes y 88.70 % sí aparecen. El nombre del resumen es *Dual-Stream **Activity Analysis** Network*, no *Attention-Augmented*.
- **URLs de los artifacts:** el juego vigente es `claude.ai/artifact/Y7uJ7…`, `FJtL6…` y `972fCk…` (actualizados el 6-oct).
- **Técnica de 5 s:** el Dr. Sandino describió en la reunión del 3-sep (min. 10:50) un muestreo instantáneo «exactamente a los 15 segundos». Craft et al. (2010), texto completo en PMC, dice «predominant behavior» y cita a Detke. De Detke solo se leyó el resumen.
- **Código de `fst-etiquetador`** (llamado `fst_auto` en los documentos): la fusión es `cnn/fst_cnn.py` v5 y la versión por segundo es `fst_cnn_seg.py`. No genera video anotado ni copia H.264; solo CSVs. La versión por segundo nunca se corrió ni se entrenó.
- **Compilación:** `main.tex` compila sin errores ni referencias/citas rotas con los cambios de la rama.

---

## 3. Decisiones tomadas hoy (usuario) y su estado

| ID | Decisión | Estado |
|---|---|---|
| D-66 | La CNN de fusión es el clasificador; el *gradient boosting* queda como etiquetador y fuente de los 15 rasgos | Aplicado |
| D-67 | Sin respuesta en 5 min de pausa, el análisis se **cancela** | Aplicado |
| D-68 | Reiniciar **borra** el resultado anterior al empezar | Aplicado |
| D-69 | El sistema borra los videos a los 30 días, de forma automática | Aplicado |
| D-70 | Portada y documento técnico: «Fecha pendiente» | Aplicado |
| D-71 | Día 1: se sube, se guarda y **no se analiza** | Aplicado |
| D-72 | El Administrador puede cambiar el rol; RN-16 también prohíbe quitárselo al último | Aplicado |
| D-73 | Docker solo como herramienta de empaquetado | Sin cambio necesario |
| D-74 | Repetibilidad: RNF-14, subsección en el cap. 3, cuarto criterio | Aplicado |
| D-75 | RNF-11 es diseño modular; validar otros paradigmas queda fuera | Aplicado |
| D-76 | Dos PDF: «reporte de resultados» y «reporte de diagnóstico» | Aplicado |
| D-77 | El laboratorio usa muestreo instantáneo cada 5 s; el sistema, la conducta predominante del periodo | Aplicado |
| D-57 a D-60 | Revisión, copia H.264, pausa y reinicio | Aplicado junto con las anteriores |

---

## 4. Lo aplicado en la rama `decisiones-11oct`

**Cap. 1** — criterios de aceptación pasan a cuatro; el video del Día 1 se guarda; OE-6 y «otros paradigmas» como diseño modular sin validación.
**Cap. 2** — se quitan los «dos candidatos»: el *gradient boosting* etiqueta y la R(2+1)D-18 fusionada es el clasificador.
**Cap. 3** — portada del capítulo, sección del *gradient boosting*, *transfer learning* (la red se ajusta completa y lleva rama de medidas), clasificación con rama de medidas, subsección de repetibilidad.
**Cap. 4** — RF-05, RF-09, RF-15, RF-18, RF-22, RF-32; RN-03, RN-04, RN-12, RN-14, RN-15 (con D-77), RN-16 y **RN-17 nueva**; **RNF-14 nuevo** y RNF-11; justificaciones de umbrales; filas de herramientas; «cuatro criterios».
**Cap. 5** — ciclo de vida (pausa, cancelación, reinicio) y precedencia de estados; Módulo 3 (red de fusión, entrenamiento, estado de la red); Módulo 4 (cinco salidas, con la copia H.264); descripciones de VIDEO y ANALISIS; CU-05, CU-07, CU-11, CU-14 (actor «Sistema») y CU-25; pantalla de progreso; reporte de resultados en la API y en los resultados.
**Preliminares** — portada y documento técnico; glosario (CNN y ResNet).
**Apéndice D** — `estado_analisis` suma `en pausa` y `cancelado`; `tipo_notificacion` suma `analisis en pausa` y `analisis cancelado`; descripciones de VIDEO, ANALISIS y OBSERVACION.
**Diagramas** — `esquema_fisico.puml`, `grafo_relacional_3_vigente.puml`, `clases.puml` y `esquema_conceptual.tex` (cardinalidades del Día 1); `estados_analisis.puml` y `estados_experimento.puml`; `seq_revision_segundos.puml` y `seq_analisis_automatico.puml`; `cu_paquete5.puml` (actor «Sistema»).
**Registro** — `PENDIENTES.md` («Lo que ya está decidido»), `DISENO-BD.md` (bloque «Cambios del 11-oct») y `errores/preguntas-doctor.md` (D-66 a D-77, y D-57 a D-60 marcadas como aplicadas).

Cardinalidades que cambiaron por D-71: `VIDEO–ANALISIS` (1,1) → **(0,1)**; `VIDEO–OBSERVACION` (2,4) → **(0,4)**; `ESPECIMEN–OBSERVACION` (1,2) → **(0,1)**.

### Suposiciones que añadí por consecuencia (revisar)
- Estados `en pausa` y `cancelado` en el dominio del análisis y su precedencia en el estado agregado del experimento.
- Tipos de aviso `analisis en pausa` y `analisis cancelado`.
- `RNF-14`: «variación máxima de entre el 5 y el 10 %» tomado de la entrevista P13, a verificar en TT-II.
- No se decidió si se guarda el recuadro que el usuario ajusta; el texto no lo afirma.

---

## 5. Lo que falta

### 5.1 Conflicto con las respuestas de Vanesa (decidir entre ustedes antes de aplicar o mezclar)
Vanesa respondió las mismas preguntas y su Claude planea aplicar cambios en su rama (aún no lo hizo; `accesos-login` sigue en `8f004d8`).

| # | Vanesa | Usuario |
|---|---|---|
| 1 | Día 1 opcional y, si se sube, se analizan sus primeros 5 min; retira D-54(d); `VIDEO–ANALISIS` en (1,1) | Se sube, se guarda y no se analiza; (0,1) |
| 2a | Tras 5 min de pausa sin respuesta, el análisis sigue con «no se ve» | Se cancela |
| 2c | Reiniciar reemplaza al terminar el nuevo | Se borra al empezar |
| 11 | La fecha se queda en «Mayo 2026» | «Fecha pendiente» |
| 9 | El worker borra a los 30 días | El sistema, sin precisar |
| 19 | RN-15 «vista resumida», sin comparar contra el análisis manual | D-77: conserva Craft/Detke y dice que no equivale al conteo por eventos |
| 22 | Quitar `Grupo agrupa Espécimen` del conceptual | Sin decidir |

El punto 1 es el más serio (modelo de datos). Coincide con la entrevista P4, pero contradice D-54(d). Conviene confirmarlo con el Dr. Sandino.

### 5.2 Cosas por hacer en el repositorio
- **Regenerar los PNG** de las figuras modificadas (estados, secuencias, esquema físico, conceptual, `cu_paquete5`). No hay `plantuml.jar` en esta máquina.
- **Compilar los `.puml`** para comprobar la sintaxis de los cambios.
- **`INSTRUCCIONES-WEB.md`** y los `.md`, `.html` y `.py` de `diagramas/diagram_design/`: siguen con las reglas anteriores (Día 1, pausa, reinicio, quién borra).
- **`CLAUDE.md`:** dice «F1 por clase»; D-65 fija «por conducta».
- **Video anotado:** el módulo 4 lo conserva, aunque el código no lo genera. No se decidió (DF-09).
- **Los tres artifacts** (Conceptual, Lógico, Físico) no reflejan D-66 a D-77.
- **Mockups v2** de resultados y revisión: revisar la pantalla de eliminar y las nuevas notificaciones.
- **Comitear y subir** la rama cuando se decida; hoy está solo local.

### 5.3 Pendientes que esperan tu confirmación (recomendados, no aplicados)
- `etapa`, `nivelClasif` y `fechaAnalisis` nulas hasta que el worker las llena.
- `INTERVALO–PRESENTA` en (4,4).
- `SEGUNDO.origen` con cuatro valores (quitar `sin_revisar` y `humano_ciego`).
- Quitar «el modelo del clasificador en uso» del panel de administración.
- Cap. 2: frase de la conducta activa y corrección de los atributos de la ISO 25010 (también en el cap. 1).
- Meta de F1 ≥ 85 % solo sobre las tres conductas directas (RNF-02 y cap. 3).
- Unificar las URLs de los artifacts en `DISENO-BD.md`.
- Nota del 95 % de disponibilidad (RNF-03) y cifras de volumen citadas tal cual de la entrevista.
- Corregir el nombre de DSAAN a «Dual-Stream Activity Analysis Network» (verificar contra el artículo).

### 5.4 Preguntas abiertas con terceros
- **Laboratorio (Dr. Sandino):** si usan predominancia o instante para los bloques de 5 s (D-77 registra el instante); confirmar el Día 1; y el volumen real (la entrevista P19 da 24 a 32 videos con «3 a 4 experimentos de unos 8» pero dice 32 a 40).
- **Detke et al. (1995):** falta leer su sección de métodos (es de pago) para confirmar si dice «predominante» o «instante».

### 5.5 Riesgos técnicos del clasificador (`fst-etiquetador`)
- `fst_cnn_seg.py` y `probar_seg.py` no se han corrido ni entrenado; no hay métricas de la fusión por segundo.
- Solo hay 3 hojas ciegas de 2 videos (~1,000 segundos); la validación por video entrena con uno solo en cada parte.
- Las métricas viejas eran circulares (97 % de las filas de `_mano.csv` eran la propuesta de la máquina). La prueba ciega dio kappa +0.343 y F1 de 0.62, 0.61 y 0.54, lejos del 0.85 de RNF-02.
- Posible fuga: la rama de medidas recibe los mismos 15 rasgos con los que el etiquetador produjo la mayoría de las etiquetas (inferencia).
- No hay semillas fijas; los resultados no son exactamente reproducibles.
- El commit `30b2226` de ese repo trae un `Co-Authored-By` de Claude, que las reglas del proyecto prohíben.

---

## 6. Orden sugerido
1. Resolver con Vanesa los puntos 1, 2a, 2c y 11 de la sección 5.1.
2. Confirmar o descartar las recomendaciones de la sección 5.3.
3. Regenerar PNG y compilar los `.puml`.
4. Actualizar `INSTRUCCIONES-WEB.md`, `diagram_design/` y `CLAUDE.md`.
5. Comitear la rama y mezclarla con la de Vanesa.
