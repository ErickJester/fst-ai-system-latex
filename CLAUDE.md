# Reglas del proyecto — TT 2026-B066

> Este archivo se carga en **cada** sesión: contiene solo reglas vigentes y punteros.
> El historial, la retroalimentación completa de la defensa y el detalle del diseño
> viven en archivos aparte que se abren cuando hacen falta.

---

## Modo de lectura

Al iniciar cada sesión en este proyecto, activa el modo i-have-adhd (skill i-have-adhd) y
mantenlo activo hasta que el usuario diga "stop adhd mode" o "normal mode".

---

## Leer commits — el equipo trabaja sin avisar en el chat

Otros miembros del equipo (p. ej. ErickJester) comitean directo al repo sin pasar por
esta conversación. Si no se leen sus commits completos (diff, no solo el mensaje), se
trabaja con información vieja sin saberlo.

- **Al iniciar una conversación nueva:** `git log -1 -p` — leer completo el último commit.
- **Al primer mensaje de un día nuevo** (aunque la conversación ya esté en curso):
  `git log -3 -p` — leer completos los últimos tres commits.
- **Después de cualquier `git pull`:** leer completo cada commit que haya llegado, no
  solo el mensaje — `git log <HEAD-antes>..<HEAD-después> -p`, o `git log -p` acotado al
  rango que trajo el pull.

"Completo" significa el diff real, no `git log --oneline` ni solo el asunto del commit.

---

## Cómo hacer preguntas

El usuario tiene ADHD: nunca varias preguntas sueltas en una respuesta de chat. Antes de
anotar algo sin resolver, distingue **quién** lo resuelve:

1. **Pregunta para el laboratorio** → `errores/preguntas-doctor.md` §1–2 (Q-A, Q-B...).
2. **Decisión que el equipo/directores resuelven solos** → `errores/preguntas-doctor.md`
   §6 (D-01, D-02...).
3. **Tema para hablar a fondo, solo tú y el usuario** — si dice "hay que hablar de eso"
   refiriéndose a ti, no al equipo ni al doctor: **no documentar nada todavía.**
   Sostenerlo en la conversación; documentar solo la conclusión, cuando llegue.

Para tus propias preguntas puntuales al usuario (no las de arriba): escríbelas en
`PREGUNTAS.md` (raíz del repo, una por punto), avisa en el chat que hay preguntas nuevas
sin repetirlas ahí, y bórralas en cuanto se respondan. Si la respuesta debe persistir,
muévela al `.md` correspondiente antes de borrarla — `PREGUNTAS.md` no es guardado
permanente. Excepción: una sola pregunta aislada de desambiguación sí va directo en el
chat.

---

## No propagar actualizaciones sin que se pida

Resolver una decisión y registrarla en `errores/preguntas-doctor.md` (regla de arriba) es
lo único que se hace sin que lo pidan. **No** propagar esa decisión a los artifacts
publicados (Conceptual/Lógico/Físico), a `DISENO-BD.md`, a los `.puml` del grafo
relacional, ni a ningún otro archivo — aunque parezca el siguiente paso obvio y aunque ya
se haya hecho antes en la misma conversación. Esperar a que el usuario diga explícitamente
qué actualizar ("actualiza el artifact", "sincroniza X"). Si pide "que todo esté al
corriente" o similar, eso sí autoriza una pasada completa — pero una decisión resuelta,
por sí sola, no.

---

## Commits y autoría

- NUNCA agregar `Co-Authored-By: Claude` ni ninguna referencia a Claude, Anthropic o IA
  en mensajes de commit.
- NUNCA agregar trailers de autoría de IA (`Co-Authored-By`, `Signed-off-by` con
  referencias a modelos).
- Los commits deben parecer escritos enteramente por el desarrollador.
- No mencionar herramientas de IA en ningún mensaje de commit, descripción de PR ni
  comentario de código.
- **Antes de comitear**, resumir completo todo lo hecho **desde el último `git pull`**
  (no solo el diff que se va a comitear) — commits intermedios incluidos, si los hubo.
  Ese resumen completo es la base del mensaje, no el diff del momento aislado: evita
  mensajes fragmentados cuando se acumuló trabajo relacionado entre pulls.

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
- **Nunca reciclar un atributo o método de un diagrama viejo sin verificar que el grafo
  relacional vigente lo respalde.** Que algo existiera en el modelo viejo no es
  suficiente — hay que comprobar que la columna/atributo sigue existiendo en
  `grafo_relacional_final.puml` / `grafo_relacional_reconciliado.puml` antes de copiarlo.
  Si no está: no inventarlo ni copiarlo. Se quita del diagrama y se registra como hueco
  nuevo (`D-XX` en `errores/preguntas-doctor.md` §6), igual que D-08/D-09/D-10. Pasó dos
  veces en esta migración por copiar del diagrama de clases viejo sin este chequeo.

---

## Dónde está cada cosa

No se resume el estado del proyecto aquí — cambia demasiado rápido y este archivo debe
quedarse solo con reglas vigentes, no con una foto que se vuelve vieja en días.

| Necesitas | Abre |
|-----------|------|
| Trabajar en la base de datos, o ver el estado real del diseño | `DISENO-BD.md` — punto de partida obligatorio, siempre actualizado |
| Qué falta cambiar en el capítulo 5 y qué tan avanzado va | `CAMBIOS-CAP5.md` |
| Contradicciones detectadas en el LaTeX | `errores/README.md` y `errores/<capítulo>/` |
| Preguntas para el laboratorio y decisiones internas del equipo | `errores/preguntas-doctor.md` |
| Correcciones pendientes de casos de uso y documento | `CORRECCIONES.md` |
| Los 22 ítems de la simulación de defensa | `HISTORIAL.md` |
| Diagramas y guion de la reunión del 3-sep | `Reunion_Sandino_2026-09-03.pdf` |

### Archivos del documento

`chapters/01`–`08` · `front/resumen.tex` · `front/glosario.tex` · `bib/referencias.bib`
