# Historial — TT 2026-B066

Archivo de consulta, **no se carga en cada sesión**. Contiene la retroalimentación de la
simulación de defensa y el registro de decisiones pasadas. Las reglas vigentes que salieron
de aquí ya están en `CLAUDE.md`; lo que queda es lo que todavía está pendiente de aplicar.

---

# Simulación de defensa TT-I — correcciones pendientes

**Directores:** Dr. Israel Salas Ramírez · Dra. Martha Rosa Cordero López
**Investigador colaborador:** Dr. César Sandino Reyes López
Documento original: `docs/Retroalimentacion_Simulacion_TT2026-B066_v2.docx`

El contenido técnico se valoró correcto en su fondo. Los ajustes están en tres ejes:
estructura y densidad de diapositivas, rigor terminológico y de citación, y corrección de
los diagramas de ingeniería de software.

> **Estado:** los ítems de terminología ya se aplicaron al documento escrito y son reglas
> en `CLAUDE.md`. **Los que siguen abajo son de la presentación y ninguno está aplicado.**

## Prioridad alta

| # | Acción |
|---|--------|
| 1 | Separar la diapositiva de Conclusiones TT-I de la de Plan TT-II |
| 2 | Separar la diapositiva de Riesgos de la de Reglas de negocio |
| 3 | Revisar los diagramas de casos de uso con la Dra. Cordero: la autenticación no es visible en el diagrama general, el `extend` no refleja las condiciones del flujo, y los casos de uso por paquete no se ven |
| 4 | Retirar la diapositiva de Validación y Métricas del flujo principal; dejarla como respaldo |
| 5 | Insertar un clip de video del Dr. Sandino en la diapositiva de Conductas del FST |

**Regla de los 20 segundos:** si el jurado no puede leer una diapositiva en 20 s, tiene
demasiado texto. Tiempo total objetivo: **18–20 minutos**.

## Prioridad media

| # | Acción |
|---|--------|
| 6 | Numeración de diapositivas en formato «X / N» |
| 7 | Plantilla institucional IPN-ESCOM con logos |
| 8 | Cita abreviada en cada diapositiva con datos externos («OMS, 2025», «Porsolt et al., 1977»). Bibliografía en el mismo formato que el documento escrito |
| 9 | Simplificar Conductas del FST a bullets de una línea; mover los sistemas de neurotransmisión a respuesta verbal |
| 10 | Eliminar la diapositiva de Marco Teórico de visión y aprendizaje profundo |
| 11 | Alinear cada conclusión con su objetivo específico («OE-1 cumplido: …») |
| 12 | Renombrar «Trabajo Futuro» a «Plan de Trabajo TT-II» y reducirlo a 3–4 bullets de alto nivel |
| 13 | Matriz de riesgos con semáforo y columna de plan de contingencia |
| 14 | Mostrar en Objetivos Específicos cuáles son de TT-I y cuáles de TT-II |
| 15 | Aclarar en Propuesta de Solución que el video que se analiza es el de 5 min del Día 2 |
| 16 | Agregar la tabla de grupos experimentales (control / referencia / tratamiento) |
| 17 | Metodología Scrum: mostrar el flujo real por integrante, no la teoría |
| 18 | Lenguaje accesible en toda la defensa — TT-I es Conceptualización |

---

# Decisiones y cambios aplicados

## Documento escrito — completado

- **Cap. 1:** antecedentes, planteamiento, propuesta, justificación y alcance reescritos con
  narrativa concreta y números (≈2 h por video, 32–40 videos/semestre, 200+ horas-persona).
  Tabla de grupos experimentales añadida. Declaración explícita de que el sistema **no
  diagnostica depresión**.
- **Cap. 4:** RF-01 a RF-31, RNF-01 a RNF-13 y RN-01 a RN-13 revisados. Nueva subsección
  `sec:umbrales` con la justificación de cada valor numérico.
- **`front/resumen.tex`:** reescrito para lector no especialista.
- **Terminología:** «animales», «ISRS» e «inteligencia artificial» eliminados del cuerpo.
- **Cronograma:** tablas Gantt compactadas a 12 actividades por integrante.

## Errores de compilación resueltos

| Error | Causa | Solución |
|-------|-------|----------|
| «Incompatible glue units» | `\,\%` dentro de `$...$` con babel-spanish | Porcentaje fuera del entorno math: `$\geq 85$\,\%` |
| biber WARN «year field 'n.d.'» | `year = {n.d.}` en `@misc` | Cambiar a `@online` y eliminar el campo |
| Subrayados rojos en VSCode | chktex activo | `"latex-workshop.chktex.enabled": false` |
| Desbordamiento de longtables | Anchos `p{}` menores al contenido | Ajuste en las 6 tablas del cap. 4 |

## Diseño de base de datos — rehecho por completo

Ver `DISENO-BD.md`. Resumen: el esquema anterior se descartó entero y se derivó uno nuevo
con las 15 actividades del método (8 conceptuales + 7 lógicas). De 4 tablas declaradas en
prosa a 11 relaciones en BCNF, con 29 restricciones documentadas.

---

# Contexto del protocolo

Todo lo que el Dr. Sandino ha respondido está consolidado en
**`errores/preguntas-doctor.md` §4 (Ya respondido)**, que es la fuente a consultar. No se
duplica aquí para no tener dos versiones que puedan divergir.
