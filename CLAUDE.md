# Reglas del proyecto — TT 2026-B066

> Este archivo se carga en **cada** sesión: contiene solo reglas vigentes y punteros.
> El historial, la retroalimentación completa de la defensa y el detalle del diseño
> viven en archivos aparte que se abren cuando hacen falta.

---

## Commits y autoría

- NUNCA agregar `Co-Authored-By: Claude` ni ninguna referencia a Claude, Anthropic o IA
  en mensajes de commit.
- NUNCA agregar trailers de autoría de IA (`Co-Authored-By`, `Signed-off-by` con
  referencias a modelos).
- Los commits deben parecer escritos enteramente por el desarrollador.
- No mencionar herramientas de IA en ningún mensaje de commit, descripción de PR ni
  comentario de código.

---

## Jerarquía de fuentes de verdad

Cuando dos fuentes se contradicen, gana la de mayor rango. **El documento LaTeX es la de
menor autoridad**: es el destino de las correcciones, no el árbitro.

| Rango | Fuente |
|-------|--------|
| 1 | Respuestas directas del equipo en sesión de trabajo |
| 2 | Entrevista formal con el Dr. Sandino — `docs/entrevista_sandino.docx` |
| 3 | Transcripciones informales — `errores/fuentes/` |
| 4 | Retroalimentación de la simulación de defensa — `HISTORIAL.md` |
| 5 | Documento LaTeX — `chapters/`, `front/` |

**Regla:** ninguna corrección se aplica al LaTeX sin una fuente de rango superior que la
respalde. Si no hay fuente, se registra como *pregunta abierta*, no como error.

---

## Terminología obligatoria

| Nunca escribir | Escribir |
|----------------|----------|
| «inteligencia artificial» | **visión por computadora** (detección y seguimiento) y **aprendizaje supervisado** (clasificador) |
| «animales» | **espécimen** (sujeto individual) o **rata** (modelo animal en general) |
| «Laboratorio de Neurociencia Conductual» | **Laboratorio de Bioquímica Estructural, Sección de Posgrado, ENMyH-IPN** |
| «ISRS» en el cuerpo del texto | **fluoxetina (antidepresivo de referencia)** — la entrada de glosario sí se conserva |
| «cámara de celular» | **cámara web** |

### Términos en inglés con peso conceptual

- **Primera aparición:** `\textit{término}` seguido de `(traducción al español)`.
- **Apariciones posteriores:** solo `\textit{término}`.
- No aplica a siglas de uso común en español técnico (GPU, API, REST, JSON, CSV, PDF).

### Siglas

Definir en primera aparición: nombre completo + sigla entre paréntesis. Aplica a FST,
CLAHE, BORIS, IEEE, ISO, IEC.

---

## Prohibición vigente — métricas de validación

> ⚠️ Aplicado el 2026-04-30. **Provisional**, pendiente de confirmar con el Dr. Sandino.

**κ de Cohen, MAE y «gold standard» están eliminados de todos los `.tex`. NO reintroducirlos
sin confirmación explícita del usuario.**

En su lugar, OE-5 evalúa «el desempeño del clasificador con métricas de clasificación
estándar (precisión, \textit{recall} y F1 por clase)»; RNF-02 usa «F1 ≥ 85 % por clase».

**Por qué:** el clasificador se entrena con videos del laboratorio pero **sin** usar las
anotaciones manuales del Dr. Sandino, para evitar sobreentrenamiento en los patrones de un
solo anotador. Sin gold standard, κ y MAE no aplican.

**Pregunta abierta:** ¿es académicamente aceptable presentar TT-II con solo F1/precisión/
recall sobre conjunto de prueba propio? Hasta confirmarlo, F1 queda como marcador de
posición.

---

## Reglas de diagramas

- Lenguaje natural obligatorio: **sin SQL ni código** dentro de los diagramas.
- El login de administrador usa el mismo diagrama que el de investigador.
- «DER» se reserva para modelos conceptuales sin tipos ni llaves foráneas. El PlantUML con
  tablas, tipos y FKs es **esquema físico** o **modelo relacional**, nunca «DER».

---

## Dónde está cada cosa

| Necesitas | Abre |
|-----------|------|
| Trabajar en la base de datos | `DISENO-BD.md` — punto de partida obligatorio |
| Contradicciones detectadas en el LaTeX | `errores/README.md` y `errores/<capítulo>/` |
| Preparar una reunión con el Dr. Sandino | `errores/preguntas-doctor.md` |
| Correcciones pendientes de casos de uso y documento | `CORRECCIONES.md` |
| Los 22 ítems de la simulación de defensa | `HISTORIAL.md` |
| Diagramas y guion de la reunión del 3-sep | `Reunion_Sandino_2026-09-03.pdf` |

### Archivos del documento

`chapters/01`–`08` · `front/resumen.tex` · `front/glosario.tex` · `bib/referencias.bib`

---

## Estado en una línea

Cap. 1–4 revisados y corregidos. **Diseño de BD rehecho por completo**: etapas conceptual
y lógica cerradas, esquema en BCNF. Pendiente: reescribir el cap. 5 con el diseño nuevo,
las dos revisiones (Dr. Sandino sobre protocolo, Dra. Cordero sobre notación) y los 22
ítems de la presentación.
