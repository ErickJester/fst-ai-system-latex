# Preguntas pendientes

> Una por punto. Al responder, se borra de aquí. Si la respuesta debe persistir, se deja
> el tiempo necesario y luego se mueve al `.md` que corresponda.

Salen de la reauditoría del 11-oct (`hallazgosAgentes11oct-reauditoria/`). Cada punto dice
qué pasa hoy en el documento, qué opciones hay y cuál recomiendo. Si contestas «recomendado»,
aplico esa opción. Los marcados **(equipo)** también los resuelve Erick o los directores;
puedes contestar con tu mejor criterio y yo lo dejo registrado como tuyo, o me dices que lo
anote como pendiente para ellos.

Las preguntas para el laboratorio (Q-A a Q-H, incluidos el volumen de trabajo y cuántas
personas usan el sistema a la vez) están en `errores/preguntas-doctor.md`, no aquí.

---

## A. Diseño del sistema

1. **`Grupo agrupa Espécimen (2,N)` en el diagrama conceptual.** (DR-16) **(equipo)**
   - El modelo relacional no tiene esa relación (los especímenes cuelgan de la tanda, no del grupo). ¿Se rotula
     como relación derivada o se quita del conceptual? **Recomiendo rotularla como derivada.**

---

## B. Redacción y alcance

2. **Cap. 2: «las tres conductas» y los atributos de la ISO 25010.** (C2-06, C2-05)
   - **2a.** El cap. 2 habla de «las tres conductas del FST» y «3 salidas». Es correcto técnicamente (la cuarta
     es derivada), pero no la menciona. ¿Agrego una frase única («el sistema añade la conducta activa cuando…»)?
     **Recomiendo que sí.**
   - **2b.** El cap. 2 pone *functional correctness*, *time behaviour* y *usability* como si fueran del mismo
     nivel; en la norma ISO/IEC 25010:2011 las dos primeras son subcaracterísticas (de *functional suitability*
     y *performance efficiency*) y *usability* es una característica. ¿Lo corrijo para decir «características
     y subcaracterísticas»? **Recomiendo que sí,** y lo igualo en el cap. 1.

3. **URLs de los artifacts en `DISENO-BD.md`.** (MD-27)
   - El archivo tiene dos juegos de enlaces para los mismos tres artifacts (Conceptual, Lógico, Físico): los de
     la sección 4 («Actualizados el 2026-10-06») y los de la tabla de abajo. ¿Cuál es el vigente? Con tu
     respuesta dejo uno y marco el otro como anterior.

4. **DSAAN (Meng et al. 2024): ¿qué conductas separa?** (C2-01)
   - **Qué pasa hoy:** la tabla del cap. 2 dice que DSAAN **no** distingue las tres conductas, con «94 imágenes
     etiquetadas» y «88.7 % de precisión». No pude verificarlo: el artículo no trae resumen en Crossref y la
     búsqueda no lo encontró. Con tu respuesta anterior dejé el cap. 1 citando solo a Della Valle.
   - **Qué necesito de ti:** abrir el artículo (DOI 10.1016/j.jneumeth.2024.110212) y decirme (i) si clasifica
     inmovilidad frente a movimiento o también nado frente a escalamiento, (ii) si las cifras 94 y 88.7 % están
     ahí. Si separa las tres, cambio la tabla; si no, queda como está.

5. **Disponibilidad del 95 % (RNF-03).** (C4-13)
   - La entrevista solo dice «disponibilidad 24/7 sería ideal». El 95 % mensual lo puso el equipo sin fuente.
     ¿Se deja como criterio propio del equipo (con una nota) o se reformula sin cifra («se busca que esté
     disponible fuera del horario laboral para dejar análisis corriendo de noche»)? **Recomiendo la nota.**
