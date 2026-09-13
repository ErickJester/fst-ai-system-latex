# Preguntas pendientes

> Una por punto. Al responder, se borra de aquí. Si la respuesta debe persistir, se deja
> el tiempo necesario y luego se mueve al `.md` que corresponda.

---

**1. D-08 — ¿cómo distingue el sistema a un Investigador de un Administrador en la BD?**
`USUARIO` en el esquema reconciliado no tiene columna `rol` ni tabla de subtipo. Sin esto
no hay forma de saber los permisos de un usuario al leerlo. Kendall & Kendall (p. 405)
sugiere un **subtipo de entidad** (relación 1:1, `ADMINISTRADOR` como extensión opcional
de `USUARIO`) en vez de una columna `rol`. ¿Vamos con esa opción, con una columna `rol`
simple, o lo dejamos pendiente por ahora y avanzo el diagrama de clases sin resolverlo
(solo con la herencia UML `Investigador`/`Administrador`, sin decidir cómo se persiste)?

**2. D-09 — ¿dónde vive el seguimiento de progreso del análisis?**
`ANALISIS` no tiene `progresoPct`/`error`/`iniciadoEn`/`finalizadoEn`, pero el endpoint
`GET /experiments/{id}/status` promete el progreso en porcentaje. ¿Se agregan esas
columnas a `ANALISIS`, o el progreso es un dato transitorio que vive solo en el `Worker`
mientras corre (y no se persiste)? Mientras no se decida, el diagrama de clases no puede
incluir `actualizarProgreso()`/`marcarError()` con respaldo en la BD.
