# Errores e inconsistencias — Preliminares

**Archivos:** `front/resumen.tex`, `front/glosario.tex`, `front/abreviaturas.tex`, `front/portada.tex`
**Última actualización:** 2026-08-29
**Fuentes de contraste:** entrevista formal (`docs/entrevista_sandino.docx`), respuestas directas del equipo

> Ver [../README.md](../README.md) para la jerarquía de fuentes y la escala de severidad.

**Resumen:** 0 altas · 2 medias · 0 bajas

> **Nota.** Los preliminares no son un capítulo, pero contienen hallazgos propios y uno de ellos
> es relevante para resolver un error del cap. 1: el resumen tiene la cifra correcta donde el
> capítulo la tiene mal.

---

## EF-01 — El resumen contradice al capítulo 1 en el tiempo de anotación (y el resumen es el correcto) 🟡

**Severidad:** Media · **Ubicación:** `front/resumen.tex:4` · **Fuente:** entrevista P12 · **Estado:** Pendiente
**Transversal:** T-03

**Dice el resumen:**
> «Anotar manualmente un experimento de nado forzado lleva entre una y dos horas **por video**.»

**Dice el cap. 1 (`01_introduccion.tex:101`):**
> «Anotar el video de 5 minutos de **un espécimen** […] lleva entre una hora y media y dos horas.»

**Dice la entrevista (P12):**
> «Para un video de 5 minutos con 4 ratas, el análisis manual tarda alrededor de 30 minutos por rata
> […] **un solo video toma aproximadamente 2 horas en total**.»

**Resolución:** el resumen es correcto —la cifra es por video—; el cap. 1 es el que está mal. La
corrección va en el capítulo, no aquí. Se registra en este archivo porque la discrepancia interna
entre resumen y capítulo es visible para cualquier lector que lea los dos.

**Matiz pendiente:** el resumen dice «un experimento […] por video», mezclando los dos términos.
Una vez que se introduzca el nivel **Tanda** (ver T-01), conviene reescribirlo como «Anotar
manualmente el video de una tanda lleva alrededor de dos horas».

---

## EF-02 — «dos evaluadores» contra tres analistas 🟡

**Severidad:** Media · **Ubicación:** `front/resumen.tex:7` · **Fuente:** entrevista P12 · **Estado:** Pendiente

**Dice el resumen:**
> «Si el protocolo requiere que **dos evaluadores** lo hagan de forma independiente para verificar
> consistencia, ese tiempo se duplica.»

**Dice la entrevista (P12):**
> «Además cada analista lo hace de forma independiente, entonces **con 3 analistas** se multiplica
> ese tiempo.»

**Corrección:** son tres analistas, y el tiempo se triplica, no se duplica.

Mismo error que E01-06 en el cap. 1. Corregir en ambos sitios a la vez para no dejar una versión
desalineada.

**Nota sobre la cifra agregada:** el resumen dice «cientos de horas-persona», que es vago pero
correcto con cualquiera de los dos supuestos (160 h o 240 h). No requiere corrección aritmética,
a diferencia del cap. 1, que sí afirma «más de 200» y solo llega con tres analistas.

---

## Revisión pendiente

| Archivo | Estado |
|---------|--------|
| `front/resumen.tex` | Revisado |
| `front/glosario.tex` | **Sin revisar** — 356 líneas. Verificar en particular la entrada `ISRS`, que según la decisión registrada en `CLAUDE.md` se conserva solo como definición de referencia |
| `front/abreviaturas.tex` | **Sin revisar** — contrastar contra la corrección 3 de la simulación de defensa (definir siglas en primera aparición: FST, CLAHE, BORIS, ISO/IEEE) |
| `front/documento_tecnico.tex` | **Sin revisar** |
| `front/portada.tex` | **Sin revisar** — verificar el nombre del laboratorio según entrevista PE |
| `front/advertencia.tex` | **Sin revisar** |
| `front/abstract.tex` | Vacío (0 líneas) |
| `front/agradecimientos.tex` | Vacío (0 líneas) |
