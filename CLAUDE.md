# Reglas del proyecto

## Commits y autoría
- NUNCA agregar `Co-Authored-By: Claude` ni ninguna referencia a Claude, Anthropic o IA en mensajes de commit.
- NUNCA agregar trailers de autoría de IA (`Co-Authored-By`, `Signed-off-by` con referencias a modelos).
- Los commits deben parecer escritos enteramente por el desarrollador.
- No mencionar herramientas de IA en ningún mensaje de commit, PR description ni comentario de código.

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
