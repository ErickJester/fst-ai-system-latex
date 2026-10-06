# Pendientes del documento — capítulos 1 a 5

**Verificado contra el LaTeX el 2026-10-05**, ítem por ítem. Reemplaza como lista de
trabajo a `CORRECCIONES.md` (25-ago), `errores/0X/errores.md` (2-sep),
`errores/REVISION-AGENTES-2026-10-03.md` y los bloques B–D de `CAMBIOS-CAP5.md`. Esos
archivos se conservan como evidencia (citas de la entrevista y motivos).

El trabajo está repartido en dos listas:

| Lista | Quién | Ítems |
|-------|-------|-------|
| [`PENDIENTES-VANESA.md`](PENDIENTES-VANESA.md) | Vanesa | 13 🔴 · 17 🟡 · 4 🟢 · 4 ❓ · 1 🔒 |
| [`PENDIENTES-ERICK.md`](PENDIENTES-ERICK.md) | Erick | 5 🔴 · 19 🟡 · 6 🟢 · 3 ❓ · 4 🔒 |

---

## Cómo se repartió

Por **archivo**, para que nadie edite lo mismo que el otro y no haya conflictos de merge.
A Vanesa le tocó lo que no depende de las decisiones del modelo de datos ni del
clasificador (texto de los caps. 1–3 con fuente en la entrevista, preliminares,
bibliografía y casos de uso, que ella diseñó). A Erick, lo que necesita ese contexto.

| Archivo o zona | Dueño |
|----------------|-------|
| `chapters/01_introduccion.tex`, `02_estado_arte.tex`, `03_marco_teorico.tex` | Vanesa, **salvo** los párrafos de preprocesamiento (CLAHE, fondo por mediana, EMA, BORIS) y del clasificador (ResNet, R(2+1)D, *gradient boosting*), que son de Erick |
| `front/resumen.tex`, `portada.tex`, `documento_tecnico.tex` | Vanesa |
| `front/glosario.tex`, `front/abreviaturas.tex` | Erick (Vanesa le pide entradas en su lista) |
| `bib/referencias.bib`, configuración de `biblatex` | Vanesa (Erick solo agrega citas al final, si las necesita) |
| `chapters/04_analisis.tex` | Erick |
| `chapters/05_diseno.tex`, sección «Diseño de casos de uso» (hoy 693–2333) | Vanesa |
| `chapters/05_diseno.tex`, todo lo demás | Erick |
| `diagramas/puml/cu_*.puml`, `gen_pngs.sh`, `figures/mermaid/cu_*.png` | Vanesa |
| Resto de `diagramas/` y `figures/` (modelo, secuencias, clases, estados, pipeline) | Erick |
| `back/`, `errores/`, `DISENO-BD.md`, `INSTRUCCIONES-WEB.md`, mockups | Erick |

## Reglas para no pisarse

1. **Cada quien marca su avance solo en su archivo** (`PENDIENTES-VANESA.md` o
   `PENDIENTES-ERICK.md`).
2. **Si lo tuyo obliga a tocar una zona del otro, no la edites: anótalo.** Vanesa escribe
   en la sección «Para Erick» de su lista; Erick le avisa a Vanesa (por ejemplo, si una
   decisión cambia una ficha de caso de uso).
3. **`git pull` antes de empezar y commits chicos** (uno por ítem o por grupo de ítems del
   mismo archivo). Antes de editar, leer los commits del otro, como pide `CLAUDE.md`.
4. **Compilar antes de hacer push** (`latexmk -pdf main.tex`), sin errores ni referencias
   rotas.

---

## Lo que ya está decidido — el texto no puede contradecirlo

Resumen de las decisiones vigentes que tocan el documento. El detalle y el motivo de cada
una están en `errores/preguntas-doctor.md` §6 (el número D-XX). **Si algo de esta lista
choca con lo que vas a escribir, gana esta lista**; si crees que está mal, no la cambies:
anótalo como pregunta (ver «Reglas de contenido», abajo).

> **Vigente al 2026-10-05.** Cuando una decisión nueva cambie algo de aquí, Erick actualiza
> esta sección en el mismo commit en que la registra; si no, la lista se vuelve vieja como
> los trackers.

**El estudio**
- **Experimento** = el estudio completo. Tiene **tres o más grupos** (en promedio 4) de
  tres tipos: control, referencia (fluoxetina) y tratamiento experimental; un tipo puede
  repetirse.
- **Grupo:** una o más tandas. Típicamente 6–8 especímenes, pero **no es regla**: el
  sistema acepta desde 2 (D-28).
- **Tanda:** de **2 a 4 especímenes** grabados juntos, siempre del mismo grupo, con uno o
  dos videos: Día 1 (20 min) y Día 2 (5 min) (D-28). Nunca «los cuatro cilindros» ni
  «cuatro ratas»: **de dos a cuatro**.
- Laboratorio: **Laboratorio de Bioquímica Estructural, Sección de Posgrado, ENMyH-IPN**.

**El video**
- Formatos **`.mp4` y `.mov`** (D-30). Se analizan **solo los primeros 300 s** (D-31). Un
  video vertical (cámara girada) **se rechaza** al subirlo (D-33). **Cámara web**, **vista
  lateral**.

**El análisis**
- Arranca solo al terminar la carga; el investigador no lo inicia, pausa, cancela ni
  reinicia (RN-04). Reanalizar **reemplaza** el resultado anterior (D-03).
- Pipeline de **tres etapas**: preprocesamiento, localización de los cilindros y
  clasificación (D-16). **Sin YOLO, ByteTrack ni ningún *tracker***: un espécimen por
  cilindro, detectado por sustracción de fondo (CLA-02). YOLO solo aparece como trabajo
  revisado en el cap. 2.
- **Clasificador: todavía no se elige.** Candidatos: *gradient boosting* sobre rasgos y
  R(2+1)D-18 (CLA-03). No escribir ResNet-50 ni Random Forest, ni cifras de desempeño.
- **Cuatro conductas:** nado activo, inmovilidad, escalamiento y **conducta activa** (cuando
  no se distingue nado de escalamiento) (D-29, RN-13).
- **Cada segundo recibe una conducta, sin duración mínima.** El sistema detecta conductas
  breves de **unos 2 s**; los resultados se muestran también en bloques de 5 s (D-49).
  Nunca «mínimo de 3 s».
- **Sin umbral de confianza de detección (0.70) ni códigos de error** (D-32, D-47). Los
  errores son dos: el video no se pudo abrir o no se encontraron los cilindros.
- **Sin vista en vivo.** Al terminar, el usuario revisa y corrige segundo a segundo
  (D-34, D-35). El progreso se muestra por etapa (D-22).
- **Entrenamiento sin las anotaciones del laboratorio** (D-26, `CLAUDE.md`). Métricas:
  precisión, *recall* y F1 por clase; **nunca** κ de Cohen, MAE ni «gold standard».

**Los resultados**
- Se comparan **grupos entre sí con el Día 2**. **No existe** comparación Día 1 contra
  Día 2 (D-44). El desglose por minuto es obligatorio, no opcional.

**Usuarios y datos**
- **No hay autorregistro:** solo el Administrador crea cuentas (D-01). El Administrador es
  un investigador con permisos extra, no otro tipo de usuario (D-08). El alta pide
  identificador institucional, nombre, apellidos y correo; la contraseña temporal la genera
  el sistema (D-38).
- **Cualquier dominio de correo** (sin `@ipn.mx`, D-46). El sistema **sí envía correos**
  (D-45). **Sin bloqueo por intentos** (D-48) ni registro de último acceso (D-37). Cerrar
  sesión = el navegador descarta el token (D-36).
- Todos ven todos los experimentos; **solo quien lo creó o un administrador lo elimina**
  (D-43, RN-08).
- Los videos se borran a los 30 días; si el disco pasa del 90 % se adelanta el borrado de
  los más antiguos y se avisa (D-39). Resultados y reportes se conservan siempre.

## Reglas de contenido

1. **Ninguna corrección sin fuente de rango superior** (jerarquía de `CLAUDE.md`: equipo >
   entrevista > transcripciones > simulación de defensa > LaTeX). Cada ítem de las listas
   ya trae su fuente; si al corregir necesitas afirmar algo nuevo, búscale fuente.
2. **Si no hay fuente o algo contradice la lista de arriba, no lo inventes ni lo
   resuelvas:** anótalo (Vanesa en «Para Erick» de su lista) para registrarlo en
   `errores/preguntas-doctor.md`.
3. **No reintroducir nada que ya se quitó**, aunque aparezca en un archivo viejo, un
   tracker o un diagrama huérfano. Los trackers viejos son evidencia, no instrucciones.
4. **Diagramas:** lenguaje natural, sin código ni SQL; nada se copia de un diagrama viejo
   sin verificarlo contra `grafo_relacional_3_vigente.puml` (`CLAUDE.md`).
5. **Corregir solo lo que pide el ítem.** Si ves otro problema, anótalo en vez de
   arreglarlo de paso: evita pisar la zona del otro.

---

## Ya resueltos (para cerrar en los trackers viejos)

- **errores/:** E01-01, 02, 03, 09 (D-49), 10, 12 · E02-03, 04, 05 · E03-02, 06 (D-49), 07 · E04-01, 02, 03, 04.
- **CORRECCIONES:** CU-04, 07, 08, 09, 13, 14 (D-43), 16, 20 · ESC-04 (el borrado al 90 % se queda: RN-05, D-51), ESC-05, ESC-06 · DOC-01 (apéndice D), DOC-09 y DOC-10 (sin objeto) · DOC-11.
- **Agentes §1:** todo §1.1 a §1.3; terminología prohibida en los capítulos; BCNF y D-04 ya explicados en el cap. 5; cierre de sesión; huecos §4.1–4.3 y §4.6–4.8 (D-37, D-41, D-42, D-43).

## Fuera de «hasta el cap. 5»

- **DOC-02:** no hay capítulo de conclusiones (caps. 6–8 comentados en `main.tex`).
- **D-51 sin aplicar:** `INSTRUCCIONES-WEB.md` (DDL y semilla), comentario de `seq_analisis_automatico.puml`, artifacts y cap. 6.
- Archivos huérfanos con el modelo viejo que no entran al documento (`ciclo_vida_experimento.puml`, `seq_analisis.png`, `seq_registro.png`, `figures/mermaid/clases.png`, `casos_uso.png`, `cu_*.png` de `diagramas/`).
