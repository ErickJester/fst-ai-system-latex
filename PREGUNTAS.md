# Preguntas pendientes

> Una por punto. Al responder, se borra de aquí. Si la respuesta debe persistir, se deja
> el tiempo necesario y luego se mueve al `.md` que corresponda.

Salen de la reauditoría del 11-oct (`hallazgosAgentes11oct-reauditoria/`). Cada punto dice
qué pasa hoy en el documento, qué opciones hay y cuál recomiendo. Si contestas «recomendado»,
aplico esa opción. Los marcados **(equipo)** o **(laboratorio)** también los resuelve Erick,
los directores o el Dr. Sandino; puedes contestar con tu mejor criterio y yo lo dejo
registrado como tuyo, o me dices que lo anote como pendiente para ellos.

---

## A. Diseño del sistema

1. **El video del Día 1: ¿existe en el sistema o no?** (MD-24, DR-06) **(equipo)**
   - **Qué pasa hoy:** D-54 dice que el Día 1 solo confirma que existe el video de habituación y no se analiza.
     Pero el modelo de datos obliga a que *todo* video tenga un análisis (`VIDEO — ANALISIS` es 1,1) y entre 2 y 4
     observaciones. Un video del Día 1 no tendría nada de eso. Además el cap. 5 dice «Día 1 y/o Día 2» y el
     apéndice dice «el Día 1 es opcional», que son dos lecturas distintas, y RN-12 todavía dice que el Día 1
     «verifica que los especímenes lleguen con el mismo nivel de estrés», cosa que el sistema ya no puede
     comprobar si no lo analiza.
   - **Opciones:** (a) el Día 1 no se sube al sistema: la tanda solo tiene el video del Día 2; (b) el Día 1 se sube
     y se guarda como `VIDEO`, pero sin análisis (`VIDEO — ANALISIS` pasa a 0..1); (c) el Día 1 sí se analiza y se
     retira D-54 (d).
   - **Recomiendo (b):** respeta D-54 y conserva la constancia de que el grupo tuvo habituación. Implica cambiar
     cardinalidades en el grafo, el físico, el apéndice D y la nota de RN-12.

2. **Revisión, copia H.264, pausa y reinicio (D-57 a D-60): ¿los aplico ya a los capítulos?** **(equipo)**
   - **Qué pasa hoy:** están registradas pero sin aplicar, porque cambian partes grandes: RN-04 («el investigador
     no inicia, pausa, cancela ni reinicia») ya no sería cierta, RN-14 y RF-32 (quién corrige), el estado
     «en pausa» del análisis, una tarea nueva del *worker* (la copia H.264) y las fichas de revisión.
   - **Lo que me falta saber para escribirlo bien:**
     - **2a.** Al terminar los 5 min de pausa sin que el usuario responda, ¿el análisis sigue con esos segundos
       marcados como «no se ve», se cancela, o queda en pausa indefinida?
     - **2b.** El recuadro que el usuario ajusta a mano, ¿se guarda (segundo, cilindro y coordenadas, lo que
       agrega una tabla al modelo) o solo se usa para repetir el análisis y se descarta?
     - **2c.** «Reiniciar el análisis»: ¿borra el resultado anterior (como el reanálisis de D-03) o conserva el
       anterior hasta que termine el nuevo?
   - **Recomiendo:** 2a sigue con «no se ve» y avisa; 2b se descarta (no agrega tablas); 2c reemplaza el resultado
     al terminar el nuevo. Con eso lo aplico en los capítulos 4 y 5 en un solo commit.

4. **¿La red de fusión (CNN) ya es la línea del proyecto?** (MD-26, DF-18, C3-04, MD-22) **(equipo)**
   - **Qué pasa hoy:** `PENDIENTES.md` dice «clasificador todavía no se elige» (candidatos: *gradient boosting*
     sobre rasgos y la R(2+1)D-18). Pero el repositorio `fst-etiquetador` ya implementa la «versión 5», una CNN 3D
     que se fusiona con una rama de medidas, y `pipeline_analisis.md` (8-oct) la presenta como flujo principal.
     El cap. 3 describe el *transfer learning* como cambiar solo la última capa.
   - **Opciones:** (a) sigue sin elegirse: la fusión es una variante del candidato de redes profundas; (b) la
     fusión es la línea: se registra una decisión nueva y se actualizan caps. 3 y 5.
   - **Recomiendo (a)** hasta tener las métricas de TT-II; solo ajusto el cap. 3 para decir que el candidato
     puede combinar la red con una rama de medidas.

5. **Una cardinalidad del modelo de datos** (DR-08) **(equipo)**
   - **5b.** `INTERVALO — PRESENTA` está dibujada como (2,4), pero el texto dice que siempre hay una fila por
     cada una de las cuatro conductas, incluso con valor 0. ¿Siempre 4 filas? **Recomiendo que sí** y la
     cardinalidad queda (4,4).

7. **RN-16 (siempre un Administrador activo): ¿también cuando se quita el rol?** (C4-20)
   - **Qué pasa hoy:** RN-16 solo cubre *desactivar* la última cuenta de Administrador. RF-05 también deja
     «modificar» cuentas. Si el Administrador puede quitarle el rol a otra cuenta (o a sí mismo), el sistema
     podría quedarse sin ninguno de otra forma.
   - **Recomiendo:** ampliar RN-16: «rechaza desactivar o quitar el rol a la última cuenta de Administrador
     activa», si el rol se puede editar desde la interfaz. Si el rol no se edita, lo dejo como está.

8. **Panel de administración: ¿muestra «el modelo del clasificador en uso»?** (C5-10) **(equipo)**
   - **Qué pasa hoy:** el cap. 5 lo dice en la pantalla de administración, pero ningún requisito (RF-28/29) lo
     pide, y el modelo no se guarda en la base de datos (es constante del pipeline).
   - **Recomiendo:** quitarlo del texto y del mockup.

---

## B. Redacción y alcance

10. **Docker Compose: ¿cuenta como «despliegue»?** (C1-20, MD-37)
    - **Qué pasa hoy:** D-62 dice que el despliegue no queda registrado. Quité «despliegue» del documento, pero
      Docker sigue apareciendo como *empaquetado*: cronograma de Ángel («Empaquetado con Docker Compose»),
      *stack* del cap. 1, RNF-10 (portabilidad), la sección de Docker del cap. 3, la tabla de herramientas y
      los costos del cap. 4.
    - **Opciones:** (a) Docker se queda como herramienta de desarrollo y empaquetado, sin hablar de servidores ni
      de entornos de producción; (b) se quita Docker del cronograma y de RNF-10, pero se conserva en
      herramientas; (c) se quita Docker por completo del documento.
    - **Recomiendo (a),** que es como lo dejé.

11. **Fecha de la portada y del documento técnico.** (MD-08)
    - Hoy dice «Mayo 2026» en `portada.tex` y `documento_tecnico.tex`. ¿Qué fecha va? (mes y año de entrega).
      Si «Mayo 2026» es la correcta, cierro el pendiente A-14 con esa nota.

12. **Repetibilidad como criterio de aceptación.** (C3-05)
    - **Qué pasa hoy:** los caps. 1 y 2 la llaman «el criterio principal del laboratorio» (el mismo video
      analizado varias veces debe dar el mismo resultado, con variación máxima de 5 a 10 %), pero ningún
      requisito no funcional ni el cap. 3 la recogen, y el cap. 1 dice que los criterios de aceptación son tres
      (corrección funcional, tiempo y usabilidad).
    - **Opciones:** (a) agrego un RNF de repetibilidad, una subsección en el cap. 3 y lo cuento como cuarto
      criterio; (b) la dejo solo como contexto en los caps. 1 y 2 y cambio «criterio principal» por «criterio
      que mencionó el laboratorio».
    - **Recomiendo (a):** viene de la entrevista (P13) y de `PENDIENTES-ERICK.md` (M-1c).

13. **¿La meta de F1 ≥ 85 % incluye la conducta activa?** (C3-14, C4-21) **(equipo)**
    - Hoy RNF-02 mide F1 por conducta para nado, inmovilidad y escalamiento. La conducta activa se *deriva*
      cuando el clasificador no decide entre nado y escalamiento, así que no es una salida directa del modelo.
    - **Recomiendo:** la meta aplica a las tres conductas directas; la conducta activa se reporta pero no se
      exige. Lo escribo así en RNF-02 y en el cap. 3.

14. **Cap. 2: «las tres conductas» y los atributos de la ISO 25010.** (C2-06, C2-05)
    - **14a.** El cap. 2 habla de «las tres conductas del FST» y «3 salidas». Es correcto técnicamente (la cuarta
      es derivada), pero no la menciona. ¿Agrego una frase única («el sistema añade la conducta activa cuando…»)?
      **Recomiendo que sí.**
    - **14b.** El cap. 2 pone *functional correctness*, *time behaviour* y *usability* como si fueran del mismo
      nivel; en la norma ISO/IEC 25010:2011 las dos primeras son subcaracterísticas (de *functional suitability*
      y *performance efficiency*) y *usability* es una característica. ¿Lo corrijo para decir «características
      y subcaracterísticas»? **Recomiendo que sí,** y lo igualo en el cap. 1.

15. **OE-6 y el alcance dicen «documentar y no garantizar» otro paradigma, pero RNF-11 exige que el módulo se
    pueda reconfigurar.** (C1-18)
    - **Opciones:** (a) es solo una nota de trabajo futuro: RNF-11 pasa a «el diseño debe permitir documentar los
      cambios necesarios»; (b) es requisito de diseño: OE-6 y el alcance dicen que el diseño es modular pero que
      validarlo con otros paradigmas queda fuera.
    - **Recomiendo (b):** respeta RNF-11 y no promete de más.

16. **«PDF final» y «resumen ejecutivo».** (C4-14) **(equipo)**
    - **Qué pasa hoy:** RF-18, RF-22 y la factibilidad mencionan un «PDF final», un «resumen ejecutivo» y un
      «PDF de calidad del video» sin definirlos; el apéndice D solo define el formato PDF.
    - **Recomiendo:** dos PDF con nombre fijo: «reporte de resultados» (el que marca los fragmentos «no se ve») y
      «reporte de diagnóstico» (el de RN-11, cuando el análisis falla).

17. **URLs de los artifacts en `DISENO-BD.md`.** (MD-27)
    - El archivo tiene dos juegos de enlaces para los mismos tres artifacts (Conceptual, Lógico, Físico). ¿Cuál
      es el vigente? Con tu respuesta dejo uno y marco el otro como anterior.

18. **DSAAN (Meng et al. 2024): ¿qué conductas separa?** (C2-01)
    - **Qué pasa hoy:** la tabla del cap. 2 dice que DSAAN **no** distingue las tres conductas, con «94 imágenes
      etiquetadas» y «88.7 % de precisión». No pude verificarlo: el artículo no trae resumen en Crossref y la
      búsqueda no lo encontró. Con tu respuesta anterior dejé el cap. 1 citando solo a Della Valle.
    - **Qué necesito de ti:** abrir el artículo (DOI 10.1016/j.jneumeth.2024.110212) y decirme (i) si clasifica
      inmovilidad frente a movimiento o también nado frente a escalamiento, (ii) si las cifras 94 y 88.7 % están
      ahí. Si separa las tres, cambio la tabla; si no, queda como está.

---

## C. Para el laboratorio (Dr. Sandino)

19. **Técnica de cuantificación del laboratorio (Q-A).** (C4-10)
    - **Qué pasa hoy:** RN-15 dice que el laboratorio «la ha usado en parte de sus análisis manuales» (bloques de
      5 s con la conducta predominante). La transcripción describe otra cosa: mirar al espécimen en el
      instante 0:05, 0:10, 0:15… y anotar qué hace *en ese instante*. Q-A sigue sin respuesta.
    - **Pregunta al laboratorio:** ¿cuál de las dos técnicas usan: conducta predominante de cada periodo de 5 s, o
      conducta del instante cada 5 s? Mientras no respondan, propongo quitar la frase «El laboratorio la ha
      usado» y decir solo que sigue a Detke et al. según Craft et al.

20. **Volumen de trabajo del laboratorio.** (C1-07, C3-02)
    - **Qué pasa hoy:** los caps. 1, 3 y 4 dan tres cuentas distintas: «32 a 40 videos por semestre»; «3 a 4
      experimentos de unos 8 videos» (24 a 32); y, antes de hoy, «3 a 5 con 6 a 9 videos» (18 a 45). Ya unifiqué
      el cap. 4 a «3 a 4 experimentos» y «alrededor de 8 videos», pero la entrevista misma no cuadra.
    - **Pregunta al laboratorio:** ¿cuántos experimentos hacen por semestre y cuántos videos del Día 2 salen de
      cada uno?

21. **Disponibilidad del 95 % (RNF-03).** (C4-13)
    - La entrevista solo dice «disponibilidad 24/7 sería ideal». El 95 % mensual lo puso el equipo sin fuente.
      ¿Se deja como criterio propio del equipo (con una nota) o se reformula sin cifra («se busca que esté
      disponible fuera del horario laboral para dejar análisis corriendo de noche»)? **Recomiendo la nota.**

22. **`Grupo agrupa Espécimen (2,N)` en el diagrama conceptual.** (DR-16) **(equipo)**
    - El modelo relacional no tiene esa relación (los especímenes cuelgan de la tanda, no del grupo). ¿Se rotula
      como relación derivada o se quita del conceptual? **Recomiendo rotularla como derivada.**
