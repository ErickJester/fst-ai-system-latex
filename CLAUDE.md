# Reglas del proyecto

## Commits y autoría
- NUNCA agregar `Co-Authored-By: Claude` ni ninguna referencia a Claude, Anthropic o IA en mensajes de commit.
- NUNCA agregar trailers de autoría de IA (`Co-Authored-By`, `Signed-off-by` con referencias a modelos).
- Los commits deben parecer escritos enteramente por el desarrollador.
- No mencionar herramientas de IA en ningún mensaje de commit, PR description ni comentario de código.

## Regla: nunca usar "inteligencia artificial" sin especificar la técnica
- El término "inteligencia artificial" es demasiado amplio e impreciso para describir el sistema.
- Cuando se haga referencia a los componentes de análisis del sistema, usar siempre las técnicas concretas: **visión por computadora** (detección y seguimiento de especímenes) y **aprendizaje supervisado** (clasificador de conductas).
- "Sistema web con visión por computadora y aprendizaje supervisado" ✅
- "Sistema web con inteligencia artificial" ❌
- Esta regla aplica al documento escrito, a la presentación y a cualquier otro material del TT.

## Regla: términos en inglés con peso significativo
- Todo término o frase en inglés con peso conceptual significativo (atributos ISO, nombres de paradigmas, términos técnicos propios) debe seguir este formato:
  - **Primera aparición:** `\textit{término en inglés}` seguido inmediatamente de `(traducción al español)`.
  - **Apariciones posteriores:** solo `\textit{término en inglés}`, sin paréntesis.
- No aplica a siglas de uso común en español técnico (GPU, API, REST, JSON, CSV, PDF, etc.).
- Ejemplos correctos ya aplicados: `\textit{performance efficiency}` (eficiencia de desempeño), `\textit{functional correctness}` (corrección funcional), `\textit{time behaviour}` (desempeño temporal), `\textit{usability}` (usabilidad).

## PENDIENTE IMPORTANTE — revisar menciones de métricas de validación
- **NO hacer aún.** Requiere revisión cuidadosa de todo el documento.
- En el Alcance (Incluido) se eliminó el bullet "Validación contra el gold standard del laboratorio con κ de Cohen y error absoluto medio."
- **Pendiente:** revisar y eliminar (o reubicar) todas las demás menciones de κ de Cohen, MAE (Mean Absolute Error / error absoluto medio) y \textit{gold standard} en el documento escrito, incluyendo: Propuesta de solución, Objetivo general (OE-5), Metodología, resumen.tex y cap. 4 (RNF-02, sec:umbrales). Hacer con cuidado para no romper la coherencia del documento.

---

# Retroalimentación — Primera Simulación de Defensa TT-I
**TT 2026-B066 · ESCOM-IPN**
**Frausto Robles Ángel Ali · Rodríguez Verdín Sandoval Vanesa**
**Directores: Dr. Israel Salas Ramírez · Dra. Alicia Marcela Ramírez Guzmán · Dr. César Sandino Reyes López**

Estas observaciones son **instrucciones de corrección obligatorias** derivadas de la simulación de defensa (≈2 h 20 min). El contenido técnico fue valorado como correcto en su fondo; los ajustes se concentran en tres ejes: (1) estructura y densidad de diapositivas, (2) rigor terminológico y de citación, y (3) corrección de los diagramas de ingeniería de software.

---

## Correcciones de PRIORIDAD ALTA (antes de la próxima simulación)

### 1. Corregir el nombre del laboratorio colaborador
El nombre que aparece en la presentación es **incorrecto**. El nombre correcto es:
- ❌ Laboratorio de Neurociencia Conductual, ENMyH-IPN
- ✅ **Laboratorio de Bioquímica Estructural, Sección de Posgrado, Escuela Nacional de Medicina y Homeopatía (ENMyH-IPN)**

Corregir en todas las diapositivas donde aparezca (Introducción, Planteamiento del problema, Portada) y también en el documento escrito del TT.

### 2. Reemplazar «animales» por «rata» o «espécimen»
El término «animales» implica un número indeterminado de sujetos de distintas especies y puede generar cuestionamientos éticos en el contexto del protocolo NOM-062.
- Usar **«espécimen»** cuando se habla de un sujeto individual en el contexto experimental.
- Usar **«rata»** cuando se refiere al modelo animal de forma general.
- Reemplazar en **todas** las ocurrencias en diapositivas y documento escrito.

### 3. Definir siglas en primera aparición
Regla: en la primera aparición escribir el nombre completo seguido de la abreviatura entre paréntesis. Ejemplo: «Forced Swim Test (FST)». A partir de la segunda aparición puede usarse únicamente la sigla.

| Sigla | Significado completo | Dónde definir |
|-------|---------------------|---------------|
| FST | Forced Swim Test | Introducción: «Prueba de Nado Forzado (FST)» |
| ISRS | Inhibidores Selectivos de Recaptura de Serotonina | Ver corrección §5 — reemplazar por «fluoxetina» |
| CLAHE | Contrast Limited Adaptive Histogram Equalization | Primera aparición en Pipeline |
| BORIS | Behavioral Observation Research Interactive Software | Primera aparición en Validación |
| MAE | Mean Absolute Error (Error Absoluto Medio) | Primera aparición en Validación |
| IEEE / ISO / IEC | Institute of Electrical and Electronics Engineers / International Organization for Standardization / International Electrotechnical Commission | Escribir completo al menos una vez en Objetivos o Justificación |

### 4. Sustituir «ISRS + fluoxetina» → solo «fluoxetina»
El Dr. Sandino recomendó no usar la sigla ISRS porque abre preguntas técnicas de farmacología que los expositores no necesitan manejar.
- En la diapositiva de Conductas del FST: reemplazar «sistema serotoninérgico (ISRS como fluoxetina)» por **«fluoxetina (antidepresivo de referencia)»**.
- Conservar la desipramina como ejemplo del sistema noradrenérgico.
- Respuesta preparada si el jurado pregunta: «Es el antidepresivo más utilizado en la clínica; nos sirve como grupo de referencia para comparar el efecto de nuevos tratamientos».

### 5. Separar diapositivas densas
Las siguientes diapositivas contienen demasiado contenido. **Separar en diapositivas independientes:**
- **Conclusiones TT-I** | **Plan TT-II** (actualmente juntas)
- **Riesgos** | **Reglas de negocio** (actualmente juntas)

Regla de los 20 segundos: si el jurado no puede leer una diapositiva en 20 s, tiene demasiado texto. Ajustar el tiempo total a **18-20 minutos** (actualmente se exceden 6 minutos).

### 6. Revisar y corregir diagramas de casos de uso con la Dra. Martha Cordero
Los casos de uso tienen errores de construcción:
- La autenticación (Paquete 1) no es visible en el diagrama general.
- El uso de «extend» no refleja correctamente las condiciones del flujo.
- Los casos de uso por paquete no están visibles para el jurado.

**Acción: Agendar revisión urgente con la Dra. Martha Rosa Cordero López antes de la defensa.**

Al presentar el diagrama de arquitectura, mencionar explícitamente qué casos de uso contiene cada paquete. Incluir los diagramas de casos de uso por paquete como diapositivas de respaldo (disponibles si el jurado las pide, no en el flujo principal).

### 7. Retirar diapositiva de Validación y Métricas del flujo principal
Las métricas (kappa, F1, MAE) aparecen como objetivos sin datos reales. Presentar números esperados sin evidencia es un riesgo: si en TT-II no se alcanzan, el jurado lo recordará.
- **Retirar del flujo principal** y preparar como diapositiva de respaldo.
- Para TT-II: solicitar formalmente al Dr. Sandino los reportes manuales de los videos ya analizados (gold standard real).

### 8. Insertar video del Dr. Sandino en diapositiva de Conductas FST
El jurado necesita ver al menos un clip para entender qué reto técnico representa detectar automáticamente inmovilidad, nado y escalamiento.
- Solicitar al Dr. Sandino los clips de video cortos de su presentación (ya subida al canal de Teams).
- Insertar en la diapositiva «Conductas del FST» o «Planteamiento del problema» al menos un clip que muestre cada conducta brevemente, con texto: «Esto es lo que el sistema debe detectar automáticamente».
- Usar el video como ancla narrativa: primero mostrar el video, luego explicar por qué hacerlo manualmente es inviable.

---

## Correcciones de PRIORIDAD MEDIA

### 9. Activar numeración de diapositivas
Activar en el pie de página. Formato: **«X / N»** (número actual / total).

### 10. Cambiar a plantilla institucional IPN-ESCOM
- Fondo blanco o institucional con los logos del IPN y ESCOM en encabezado o pie de página.
- El número de diapositiva debe ser visible en todas las pantallas.

### 11. Agregar citas en cada diapositiva que use datos externos
- Agregar nota al pie o texto pequeño con referencia abreviada en cada diapositiva que cite una fuente externa (OMS, Porsolt 1977, normas ISO/IEEE). Ejemplo: «(OMS, 2025)», «(Porsolt et al., 1977)».
- La diapositiva de Bibliografía debe estar en el **mismo formato que el documento escrito** (IEEE o APA).
- Si se usan los videos del Dr. Sandino como material embebido, incluir la cita correspondiente.
- En el documento escrito: los fármacos de ejemplo (fluoxetina, desipramina) deben estar **descritos y referenciados formalmente** en el Word del TT.

### 12. Simplificar diapositiva de Conductas del FST a bullets de una línea
Reducir cada tarjeta a: nombre de la conducta + una línea descriptiva. Ejemplo:
- «Nado activo — movimiento horizontal en el agua»
- «Inmovilidad — el espécimen flota»
- «Escalamiento — movimiento hacia las paredes del cilindro»

Eliminar los párrafos sobre sistemas de neurotransmisión (guardarlos para respuesta verbal al jurado). Sustituir texto extenso por el clip de video del Dr. Sandino.

### 13. Eliminar diapositiva de Marco Teórico de Visión y Aprendizaje Profundo
Eliminar la diapositiva de Marco Teórico (sustracción de fondo, ByteTrack, ResNet-18, Transfer Learning). El jurado evaluará lo técnico a través de la arquitectura y los casos de uso, no de las definiciones teóricas. Si el jurado pregunta sobre alguna tecnología, la respuesta se da verbalmente con apoyo de la diapositiva de Diseño del Pipeline.

### 14. Alinear Conclusiones con cada Objetivo Específico de TT-I
Las conclusiones deben tener correspondencia explícita con cada objetivo específico. Formato sugerido:
- «OE-1 cumplido: se revisaron N herramientas existentes y se identificó la brecha [...]»
- «OE-2 cumplido: se documentó el protocolo del Dr. Sandino [...]»
- «OE-3 cumplido: se diseñó la arquitectura conforme a ISO/IEC/IEEE 12207 [...]»

### 15. Renombrar «Trabajo Futuro» a «Plan de Trabajo TT-II»
- «Trabajo Futuro» se usa únicamente para extensiones post-TT-II.
- «Plan de Trabajo TT-II» debe limitarse a **3-4 bullets de alto nivel**. Ejemplo: «Implementar el backend y frontend», «Entrenar el clasificador con los videos del laboratorio», «Validar contra gold standard», «Desplegar con Docker Compose».
- No poner más detalle: si se comprometen a Docker Compose o pruebas de usabilidad, el jurado los evaluará en eso.

### 16. Reformatear matriz de riesgos con semáforo y columna de contingencia
Rediseñar la tabla con las columnas: ID | Descripción | Nivel | Estado | Plan de contingencia

| ID | Descripción | Nivel | Estado | Plan de contingencia |
|----|------------|-------|--------|---------------------|
| R-01 | Videos con reflejos o pelaje claro (conf. < 0.70) | 🔴 Alto | Pendiente | CLAHE adaptativo + reporte PDF de diagnóstico (RN-11) |
| R-02 | Dataset insuficiente para κ > 0.80 | 🔴 Alto | En proceso | Anotación en BORIS + data augmentation + fallback conducta activa |
| R-03 | Laboratorio no entrega registros a tiempo | 🟡 Medio | Controlado | Calendario pactado · anotación anticipada con videos ya recibidos |
| R-04 | Tiempo de análisis excede lo aceptable | 🟡 Medio | Por medir | Medir tiempo por etapa del pipeline · evaluar GPU opcional |
| R-05 | Integración cola asíncrona compleja | 🟡 Medio | Pendiente | Contratos API definidos · pruebas end-to-end desde sprint 1 |

### 17. Mostrar distribución TT-I / TT-II en diapositiva de Objetivos Específicos
La diapositiva de objetivos debe mostrar claramente cuáles se cumplen en TT-I y cuáles en TT-II:

| # | Objetivo específico | TT-I | TT-II |
|---|---------------------|------|-------|
| OE-1 | Revisar el estado del arte en análisis automatizado del FST | ✓ | |
| OE-2 | Documentar el protocolo experimental del laboratorio (ENMyH-IPN) | ✓ | |
| OE-3 | Diseñar la arquitectura del sistema conforme a ISO/IEC/IEEE 12207:2017 | ✓ | |
| OE-4 | Implementar el módulo de análisis conductual (pipeline + clasificador) | | ✓ |
| OE-5 | Validar el desempeño (κ de Cohen y MAE vs. gold standard) | | ✓ |
| OE-6 | Cuantificar la reducción de tiempo vs. proceso manual | | ✓ |

### 18. Aclarar en Propuesta de Solución qué video se analiza
Corregir la descripción del flujo experimental:
- **Día 1 (20 min):** estrés agudo. Solo se analizan manualmente los primeros 5 min del grupo control como referencia basal. El sistema NO procesa los 20 min completos.
- **Día 2 (5 min):** este es el video principal que el sistema debe analizar. Se graba 24 h después del estrés. Aquí se cuantifican las tres conductas para cada espécimen por grupo experimental.
- «Carga de videos» en la Propuesta de Solución se refiere a los videos de 5 min del Día 2 (y opcionalmente los 5 min iniciales del Día 1 como referencia basal del grupo control).

### 19. Agregar tabla de grupos experimentales
Agregar en Introducción o Planteamiento del problema una tabla de 3 filas:

| Grupo | Intervención |
|-------|-------------|
| Control | Sin tratamiento. Solo estrés por nado (20 min Día 1 + 5 min Día 2). Establece la conducta base. |
| Referencia antidepresivo | Recibe fluoxetina u otro antidepresivo conocido. Muestra cómo cambian las conductas con un fármaco de efecto comprobado. |
| Tratamiento experimental | Recibe la nueva molécula o intervención (ej. acupuntura). Sus conductas se comparan con los dos grupos anteriores. |

Siempre se usan mínimo 6-8 ratas por grupo. Si el tratamiento tiene efecto, las conductas del grupo experimental se parecerán a las del grupo que recibió el fármaco conocido.

### 20. Metodología Scrum: mostrar flujo real, no teoría
En lugar de explicar qué es Scrum (qué es un daily o un sprint), mostrar **cómo lo aplicaron**:
- Qué tareas tiene el Backlog.
- Qué hace Vanesa, qué hace Ángel.
- Cómo interactuaron con el Dr. Sandino en las revisiones de cada sprint.

### 21. Tono de la exposición: lenguaje accesible (regla de la «Conceptualización»)
TT-I es Conceptualización. El lenguaje de la defensa debe ser accesible para cualquier persona, no solo para expertos. Evitar tecnicismos innecesarios (tanto médicos como de programación). El objetivo es que cualquier persona entienda: la problemática, por qué lo hacen y cómo lo resolvieron. El documento escrito también debe seguir este principio de claridad.

---

## Contexto técnico del Dr. Sandino (dominar para responder al jurado)

### Protocolo FST en el laboratorio
- El experimento usa entre **6 y 8 especímenes por grupo**.
- Día 1: 20 min de nado forzado (genera estrés). Solo los primeros 5 min del grupo control se analizan como referencia basal.
- Día 2 (24 h después): **5 min de nado forzado**. Este es el video que el sistema debe analizar para todos los grupos.
- El grupo control no recibe ningún tratamiento — solo nado forzado sin fármacos ni placebo.

### Sobre el entrenamiento del modelo y el riesgo de over-fitting
- Entrenar con **clips cortos donde la conducta sea inequívoca** (claramente escalando, claramente nadando, claramente inmóvil), no con videos completos de 5 min.
- Conducta más fácil de reconocer: **escalamiento** (movimiento de patas delanteras hacia las paredes).
- Más difíciles de distinguir: **nado vs. inmovilidad** en el límite.
- Una vez entrenado, usar los videos ya analizados manualmente como conjunto de prueba (umbral razonable: 80% o más de concordancia con el análisis manual).
- NO usar los reportes manuales para entrenamiento: riesgo de sobre-entrenamiento en esos patrones específicos.

### Material disponible del Dr. Sandino
- Su presentación del año anterior (con videos embebidos del FST) está en el canal de Teams.
- Ya proporcionó videos al equipo para iniciar el desarrollo.
- Los reportes manuales de esos videos (gold standard) están en preparación — **solicitar formalmente**.
- Está disponible para resolver dudas sobre el protocolo, los tratamientos y la descripción de las conductas.

---

## Tabla resumen de acciones (priorizada)

| # | Acción | Prioridad | Responsable |
|---|--------|-----------|-------------|
| 1 | Corregir nombre del laboratorio (Bioquímica Estructural, ENMyH-IPN) | 🔴 Alta | Ángel + Vanesa |
| 2 | Reemplazar «animales» por «rata» o «espécimen» en todo el material | 🔴 Alta | Ángel + Vanesa |
| 3 | Definir siglas en primera aparición (FST, CLAHE, BORIS, MAE, ISO/IEEE) | 🔴 Alta | Ángel + Vanesa |
| 4 | Sustituir «ISRS + fluoxetina» por solo «fluoxetina (antidepresivo de referencia)» | 🔴 Alta | Ángel |
| 5 | Separar diap. Conclusiones TT-I y Plan TT-II | 🔴 Alta | Ángel + Vanesa |
| 6 | Separar diap. Riesgos y Reglas de negocio | 🔴 Alta | Ángel + Vanesa |
| 7 | Revisar y corregir diagramas de casos de uso con Dra. Martha Cordero | 🔴 Alta | Ángel — agendar urgente |
| 8 | Retirar diap. Validación y Métricas del flujo principal (queda como backup) | 🔴 Alta | Ángel |
| 9 | Insertar video del Dr. Sandino en diap. Conductas FST / Planteamiento | 🔴 Alta | Ángel — descargar de Teams |
| 10 | Activar numeración de diapositivas (formato X / N) | 🟡 Media | Vanesa |
| 11 | Cambiar a plantilla institucional IPN-ESCOM con logos | 🟡 Media | Vanesa |
| 12 | Agregar citas en cada diapositiva que use datos externos | 🟡 Media | Ángel + Vanesa |
| 13 | Simplificar diap. Conductas del FST a bullets de una línea | 🟡 Media | Vanesa |
| 14 | Eliminar diap. Marco Teórico de Visión y Aprendizaje Profundo | 🟡 Media | Ángel |
| 15 | Alinear Conclusiones con cada OE de TT-I (una conclusión por OE) | 🟡 Media | Vanesa |
| 16 | Renombrar «Trabajo Futuro» a «Plan TT-II» y reducir a 3-4 bullets | 🟡 Media | Ángel + Vanesa |
| 17 | Reformatear matriz de riesgos con semáforo + columna Plan de contingencia | 🟡 Media | Ángel |
| 18 | Mostrar distribución TT-I / TT-II en diap. Objetivos Específicos | 🟡 Media | Ángel + Vanesa |
| 19 | Aclarar en Propuesta de Solución que el video a analizar es el de 5 min Día 2 | 🟡 Media | Vanesa |
| 20 | Agregar tabla de grupos experimentales (control / referencia / tratamiento) | 🟡 Media | Vanesa |
| 21 | Detallar flujo Scrum real por integrante (no teoría) | 🟡 Media | Ángel + Vanesa |
| 22 | Lenguaje accesible en toda la defensa y el documento escrito | 🟡 Media | Ángel + Vanesa |

---

# Estado del proyecto — documento LaTeX (fst-ai-system-latex)

> Última actualización: 2026-04-30. Refleja todas las sesiones de trabajo con asistencia de IA.

## Cambios ya aplicados al repositorio (commit 514930d)

### chapters/01_introduccion.tex
- **Tablas Gantt de cronograma** (sección Metodología): reemplazadas dos `sidewaystable` con ~35-40 filas por tablas compactas de 12 actividades por integrante. Columnas: actividad + 12 meses. `\small`, `\arraystretch=1.4`, `\tabcolsep=4pt`.
- **Fila "Revisiones"**: texto cambiado a "Revisiones mensuales con directores e investigador del laboratorio" (meses Feb–Jun, ambas tablas).

### chapters/04_analisis.tex
**Requisitos funcionales (RF):**
- RF-07: resuelto [PENDIENTE] — autoregistro + aprobación admin + notificaciones email
- RF-08: "El sistema debe aceptar únicamente archivos en formato .mp4"
- RF-09: Día 1 = "sesión de estrés"; solo se analizan primeros 5 min del grupo control
- RF-11: "entre 1 y 4 según el diseño experimental"
- RF-13, RF-16, RF-29: corregidos a lenguaje imperativo ("debe ejecutar", "debe mostrar", "debe poder ver")
- RF-17: añadido "El buceo se clasifica como nado activo"
- RF-21: exportación CSV + XLSX con columnas Tiempo(min:seg)/Nado/Escalamiento/Inmovilidad; PDF para reporte diagnóstico
- RF-30 (nuevo, tras RF-17): duración mínima de episodio ≥ 3 segundos consecutivos
- RF-31 (nuevo, tras RF-29): estadísticos de grupo — media, desviación estándar y varianza por conducta

**Requisitos no funcionales (RNF):**
- RNF-02: concordancia ≥ 85 % con anotación experta (no tiempo de procesamiento)
- RNF-03: disponibilidad 24/7, ≥ 95 % mensual
- RNF-04: todos los investigadores con cuenta activa pueden ver todos los experimentos (ref RN-08)
- RNF-10: "servidor institucional provisto por la ESCOM"
- RNF-13: máximo 4 usuarios en el mismo periodo, cola secuencial (ref RN-04)

**Reglas de negocio (RN):**
- RN-08: todos los investigadores pueden ver todos los experimentos; Admin puede además modificar/desactivar cuentas
- RN-11: limpiados párrafos duplicados y contradictorios sobre umbral de confianza 0.70

**Nueva subsección:** `\subsection{Justificación de umbrales y valores numéricos}` con `\label{sec:umbrales}`:
- 0.70 confianza: pruebas preliminares del laboratorio (sec:fact_tecnologica)
- ≥ 85 % concordancia: declarado por Dr. Sandino en entrevista
- 3 s duración de episodio: estándar manual del laboratorio
- 30 días retención: confirmado en entrevista
- 4 usuarios capacidad: declarado en entrevista
- 80/90 % umbrales de disco: gestión de capacidad estándar (pressman2014)

**Anchos de columna corregidos (tablas longtable):**
```
RF table:    |p{1.1cm}|p{2.8cm}|p{5.7cm}|p{1.3cm}|p{2.2cm}|
RNF table:   |p{1.2cm}|p{2.9cm}|p{5.2cm}|p{3.8cm}|
Herr CV:     |p{2.7cm}|p{4.4cm}|p{4.8cm}|p{1.3cm}|
Herr ML+Web: |p{2.7cm}|p{5.2cm}|p{5.2cm}|
Risk table:  |p{0.9cm}|p{3.4cm}|p{1.3cm}|p{1.7cm}|p{1.1cm}|p{4.1cm}|
```

### bib/referencias.bib
- Entrada `noldus_ethovision`: `@misc` → `@online`, eliminado `year = {n.d.}` (causaba WARN de biber por valor no entero); conservado `urldate = {2026-02-01}`.

### .vscode/settings.json
- Añadidos: `"latex-workshop.chktex.enabled": false` y `"latex-workshop.linting.chktex.enabled": false`

---

## Errores de compilación resueltos

| Error | Causa | Solución |
|-------|-------|----------|
| "Incompatible glue units" (líneas 298, 302, 310, 412) | `\,\%` dentro de `$...$` con babel-spanish redefine `\%` | `$\geq 85$\,\%` — porcentaje fuera del entorno math |
| biber WARN "year field 'n.d.' is not an integer" | `year = {n.d.}` en entrada `@misc` | Cambiar a `@online` y eliminar campo `year` |
| Subrayados rojos en VSCode (no errores reales) | chktex linter activo en LaTeX Workshop | `"latex-workshop.chktex.enabled": false` |
| Desbordamiento de columnas en longtables | Anchos declarados menores al contenido real | Ajuste de `p{Xcm}` en todas las tablas afectadas |

---

## Pendiente — PRIORIDAD 1 (claridad del proyecto)

Estas tareas fueron confirmadas como alta prioridad por el usuario pero están **en pausa** — trabajo en documento escrito, NO en presentación.

### 1. Cap. 1 — Antecedentes
Reescribir con narrativa concreta antes/después: investigador con cronómetro frente a sistema automatizado. No iniciar con genérico "las herramientas computacionales han transformado...".

### 2. Cap. 1 — Planteamiento del problema
Agregar números concretos:
- ~2 h por video × 3 analistas = ~6 horas-persona por video
- 32-40 videos por semestre = hasta ~240 horas-persona manuales por semestre

### 3. Cap. 1 — Propuesta de solución
Agregar descripción simple "cargar video → obtener reporte" ANTES de la descripción técnica del pipeline.

### 4. Cap. 1 — Justificación
Cuantificar impacto en reproducibilidad; explicar por qué la consistencia importa para la calidad de publicación.

### 5. Cap. 1 — Alcance
Añadir declaración explícita: el sistema **NO diagnostica depresión** y **no es una herramienta clínica**. Es un instrumento de apoyo al investigador en farmacología preclínica.

### 6. front/resumen.tex
Reescribir completo para lector no especialista:
- Eliminar "frame a frame" redundante
- Agregar impacto concreto (tiempo, reproducibilidad)
- Aclarar que es investigación preclínica, no herramienta clínica

### 7. Tabla de grupos experimentales (corrección #19 de simulación)
Agregar en Introducción o Planteamiento — tabla de 3 filas:

| Grupo | Intervención |
|-------|-------------|
| Control | Sin tratamiento. Establece conducta base. |
| Referencia (fluoxetina) | Antidepresivo de efecto conocido. Referencia positiva. |
| Tratamiento experimental | Nueva molécula o intervención. Se compara con los dos grupos anteriores. |

Mínimo 6-8 ratas por grupo. Si hay efecto, el perfil conductual del grupo experimental se parecerá al del grupo de referencia.

---

## Cambios de claridad aplicados (sesión 2026-04-30, segunda parte)

### chapters/01_introduccion.tex — detalle por sección

#### Antecedentes
- **Párrafo 1 reemplazado.** Se eliminó el arranque genérico ("El análisis del comportamiento animal con herramientas computacionales cambió..."). Ahora abre con la escena concreta del laboratorio: investigador, cronómetro, video cuadro a cuadro, anotación a mano, proceso repetido por cada evaluador adicional.
- La información de fondo (depresión, escala, FST, NOM-062, herramientas existentes) se conservó íntegra; solo cambió el orden: lo concreto primero, el contexto después.
- "animales de laboratorio" → "ratas de laboratorio" (párrafo NOM-062).
- "sin intervenir en ningún procedimiento con las ratas" → "sin intervenir en ningún procedimiento con los especímenes".

#### Planteamiento del problema
- **Añadido antes de los bullets:** números concretos del proceso actual.
  - Anotar un video de 5 min lleva entre 1.5 y 2 h.
  - Con doble anotación, ese tiempo se multiplica.
  - Por semestre: 32–40 videos → más de 200 horas-persona solo en anotación.
- **Bullet "Tiempo"** reescrito: ahora dice "Costo de tiempo" y referencia el volumen de anotación.
- **Bullet "Variabilidad"** ampliado: explica la consecuencia concreta — dos evaluadores obtienen tiempos distintos → el investigador decide qué número publicar sin criterio formal → problema de reproducibilidad.
- Frase de cierre actualizada para mencionar la dificultad de comparar resultados con otros grupos de investigación.

#### Propuesta de solución
- **Añadidos dos párrafos al inicio** (antes de cualquier descripción técnica):
  1. Descripción en lenguaje llano: "el investigador sube el video... en minutos genera un reporte... Lo que hoy lleva horas, el sistema lo produce con los mismos criterios cada vez."
  2. Declaración explícita: **"El sistema no diagnostica depresión ni produce información de uso clínico; su propósito es reemplazar la anotación manual de videos experimentales."**
- El resto de la sección (pipeline + plataforma web + validación) se conservó sin cambios.

#### Justificación
- **Sección reemplazada completa.** El texto original tenía 2 frases ("tiene tres problemas... Un sistema resuelve los tres"). La versión nueva tiene 4 párrafos:
  1. Cuantificación del costo de tiempo: 200+ horas-persona/semestre.
  2. Impacto en reproducibilidad: por qué los datos inconsistentes son un problema científico (publicabilidad, comparación entre laboratorios). Añade el argumento: "si hay error, es el mismo error en todos los casos — documentable y corregible, no aleatorio."
  3. Brechas de las herramientas existentes (consolidado del texto anterior + lenguaje más directo).
  4. Párrafo de calidad ISO/IEC 25010:2023 conservado, con ligeros ajustes de redacción.

#### Alcance — Fuera del alcance
- **Añadido como primer bullet:**
  > "Diagnóstico clínico de ningún tipo. El sistema mide conductas dentro de un protocolo experimental preclínico; no produce información de uso clínico ni permite inferir diagnósticos de depresión u otros trastornos, ni en ratas ni en humanos."

### front/resumen.tex
- **Reescrito completo.** Los cambios principales:
  - Abre con la escena concreta: investigador anotando a mano, horas por video, cientos de horas por semestre.
  - Eliminado "frame a frame (frame a frame)" — la redundancia desapareció.
  - "paradigma experimental estándar" → explicado en lenguaje directo ("la prueba conductual más usada para evaluar el efecto de antidepresivos en ratas antes de pasar a ensayos en humanos").
  - Añadida declaración explícita: **"El sistema no diagnostica depresión ni produce información de uso clínico."**
  - Añadidos los números de escala (32–40 videos/semestre, cientos de horas-persona).
  - Palabras clave actualizadas: "farmacología conductual" → "análisis conductual preclínico" y "farmacología experimental" (más concreto para lector no especialista).
  - Las referencias a las normas ISO se mantienen en el último párrafo técnico.

---

## Pendiente — PRIORIDAD 1 (completado)

~~1–7: Todos los ítems de claridad del documento escrito (cap. 1 + resumen.tex) fueron aplicados en la sesión del 2026-04-30.~~

---

## Cambios aplicados en rama `claridad-documento` (sesión 2026-04-30, tercera parte)

### Tabla de grupos experimentales (cap. 1 Antecedentes)
- **Tabla~\ref{tab:grupos_experimentales} añadida** al final de Antecedentes, antes de Planteamiento.
- Tres filas: Control (sin tratamiento, línea base), Referencia/fluoxetina (efecto conocido), Tratamiento experimental (molécula nueva). Descripción del criterio de decisión por similitud de perfil conductual.
- Párrafo introductorio: "las ratas se dividen en tres grupos de entre 6 y 8 especímenes cada uno."

### "animales" eliminado en todo el documento
- `01_introduccion.tex`: "modelos animales" → "modelos preclínicos con roedores"
- `02_estado_arte.tex`: "seguimiento de animales" → "seguimiento de roedores" (3 ocurrencias: intro, EthoVision, título de sección)
- `03_marco_teorico.tex`: "modelos animales" → "modelos preclínicos" (subsección y texto), "modelo animal" → "modelo preclínico"
- `05_diseno.tex`: entidad BD `\textbf{animales}` → `\textbf{especímenes}`
- **0 ocurrencias residuales** (verificado con grep).

### "ISRS" eliminado del cuerpo del texto
- `03_marco_teorico.tex`: "ISRS (como la fluoxetina)" → "antidepresivos como la fluoxetina (antidepresivo de referencia)"
- `front/glosario.tex`: 3 menciones de ISRS en entradas de Conducta de nado activo, Dopaminérgico y Serotoninérgico → reemplazadas por "fluoxetina" o "antidepresivos como la fluoxetina"
- La **entrada de glosario** `\textbf{ISRS}` se conserva como definición de referencia. Es la única ocurrencia que queda.

### Regla de inglés con traducción en cap. 4
- `\textit{user error protection}` → añadida traducción `(protección contra errores del usuario)` en primera aparición (RF-15).
- Los demás términos ISO en cap. 4 (`time behaviour`, `functional correctness`, `usability`) son usos posteriores a cap. 1, donde ya tienen traducción. ✓
- `\textit{tracking}` en RF-13 ya tenía formato correcto: "seguimiento de ratas (\textit{tracking})". ✓

### RF-04 corregido (consistencia con RN-08)
- Texto anterior: "Investigador (acceso a sus propios experimentos)"
- **Inconsistencia con RN-08**, que dice que todos los investigadores ven todos los experimentos.
- Texto nuevo: "Investigador (puede consultar todos los experimentos del laboratorio) y Administrador (mismos permisos que el Investigador, más la capacidad de aprobar registros, modificar y desactivar cuentas)."

### Overflows en longtables cap. 4
- **No verificable por terminal**: `pdflatex` no está en el PATH del sistema. Compilar desde LaTeX Workshop (Ctrl+S) para confirmar.

---

## Pendiente — Único ítem del documento

- **Revisar menciones de métricas de validación (κ de Cohen, MAE, gold standard)**: el bullet se eliminó del Alcance, pero las menciones siguen en Propuesta de solución, OE-5, resumen.tex, cap. 4 (RNF-02, sec:umbrales), caps. 2, 3, 5 y 7. Requiere decisión sobre qué se elimina, qué se reubica y qué se conserva como marco teórico. **Hacer con revisión cuidadosa.**

---

## Pendiente — Presentación (fuera del documento escrito)

- Presentación (gen_presentacion.py / gen_guion.py): mismas mejoras narrativas que cap. 1 — tarea separada, no iniciada.
- Los 22 ítems de la simulación de defensa para las diapositivas siguen pendientes.

---

## Referencia rápida — archivos clave

| Archivo | Contenido |
|---------|-----------|
| `chapters/01_introduccion.tex` | Introducción, motivación, planteamiento, propuesta, justificación, alcance, metodología, cronograma, tabla de grupos experimentales |
| `chapters/02_estado_arte.tex` | Estado del arte, herramientas, técnicas de visión |
| `chapters/03_marco_teorico.tex` | Marco teórico: depresión, FST, conductas, métricas |
| `chapters/04_analisis.tex` | RF, RNF, RN, herramientas, riesgos, justificación de umbrales |
| `chapters/05_diseno.tex` | Diseño: arquitectura, BD, pipeline |
| `front/resumen.tex` | Resumen ejecutivo |
| `front/glosario.tex` | Glosario de términos |
| `bib/referencias.bib` | Bibliografía BibLaTeX |
| `.vscode/settings.json` | Configuración LaTeX Workshop, chktex desactivado |
