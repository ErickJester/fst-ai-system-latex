# Comparativa de figuras del capítulo 5 contra el modelo vigente

> Las 31 figuras que trae `main.pdf` (compilado 2026-09-02, antes de la revisión del
> 3-sep) contra las fuentes nuevas que ya reflejan el modelo de BD vigente (artifacts
> v4/v5, `grafo_relacional_reconciliado.puml`, `clases.puml`, decisiones D-01 a D-19).
> Mapeo verificado contra los `\includegraphics` de `chapters/05_diseno.tex` y los
> comentarios "Reemplaza a…" de cada `.puml` nuevo.

| # | Figura | Fuente vieja | Fuente nueva (modelo vigente) | Estado |
|---|---|---|---|---|
| 5.1 | Arquitectura de software por capas | `arquitectura.png` | `arquitectura_software.puml` | 🟢 Lista |
| 5.2 | Diagrama de flujo del sistema | `arquitectura.png` *(misma imagen que 5.1 — dos figuras compartían fuente)* | `flujo_general.puml` | 🟢 Lista |
| 5.3 | Flujo del pipeline de análisis | `pipeline.png` | — | ⚪ Sin tocar — no depende del modelo de BD |
| 5.4 | ER conceptual | `entidadRelacion.png` (en realidad físico mal titulado) | `esquema_conceptual.tex` | 🟢 Lista |
| 5.5 | Esquema físico | `er2.png` | `esquema_fisico.puml` | 🟢 Lista — construida 15-sep sobre el grafo reconciliado + D-04, D-23, D-24 |
| 5.6–5.11 | Casos de uso (6, un paquete c/u) | `diagramas/puml/cu_*.puml` | *mismas fuentes* | 🟡 Sin rehacer — último toque fue previo al 3-sep. Faltan los 3 ajustes de C5-08 (sin tope de grupo, Día 1 opcional, quitar «seguir misma rata») |
| 5.12 | Registro de usuario por admin | `seq_registro.png` | `seq_crear_cuenta.puml` | 🟢 Lista — construida 15-sep, agrega el chequeo de rol (D-12) y `cambioRequerido` (D-25) |
| 5.13 | Inicio de sesión | `seq_login.png` | — | ⚪ Sin tocar |
| 5.14 | Cierre de sesión | `seq_logout.png` | — | ⚪ Sin tocar |
| 5.15 | Cambio de contraseña | `seq_cambio_pass_inv.png` | — | ⚪ Sin tocar |
| 5.16 | Gestión de usuarios (crear/desactivar) | `seq_gestion_usuarios.png` | `seq_gestion_usuarios.puml` | 🟢 Lista — construida 19-sep, quita la columna `rol`, agrega el chequeo de rol (D-12) y la regla del último Administrador activo (curso alterno 4a de CU-11) |
| 5.17 | Configuración de perfil | `seq_perfil.png` | — | ⚪ Sin tocar |
| 5.18 | Notificaciones | `seq_notificaciones.png` | — | ⚪ Sin tocar |
| 5.19 | Carga de video y encolado | `seq_carga.png` | `seq_carga_video.puml` | 🟢 Lista — agrega inferencia de tanda (D-19) |
| 5.20 | Análisis automático (Worker) | `seq_analisis.png` | `seq_analisis_automatico.puml` | 🟢 Lista |
| 5.21 | Consulta de progreso | `seq_progreso.png` | `seq_consulta_progreso.puml` | 🟢 Lista |
| 5.22 | Manejo de error | `seq_error.png` | *fusionada en* `seq_consulta_progreso.puml` | 🟢 Lista — ya no es diagrama aparte |
| 5.23 | Consulta de resultados | `seq_resultados.png` | `seq_consulta_resultados.puml` | 🟢 Lista |
| 5.24 | Descarga de reportes | `seq_reportes.png` | `seq_descarga_reportes.puml` | 🟢 Lista |
| 5.25 | Diagrama de clases | `clases.png` (viejo) | `clases.puml` | 🟢 Lista — reescrito 12-sep, cardinalidad Análisis–Video corregida el 15-sep (D-03) |
| 5.26–5.31 | Mockups de interfaz (6) | screenshots/mockups | — | ⚪ No aplica — no dependen del modelo de datos |

## Resumen

De 31 figuras:

- **13 ya tienen fuente nueva lista**: 5.1, 5.2, 5.4, 5.5, 5.12, 5.16, 5.19, 5.20,
  5.21, 5.22 (fusionada en 5.21), 5.23, 5.24, 5.25.
- **6 de casos de uso** (5.6–5.11) necesitan 3 ajustes textuales/de cardinalidad
  menores (C5-08).
- **12 son neutrales** al modelo de datos: pipeline (5.3), cinco de sesión/perfil
  (5.13–5.15, 5.17, 5.18) y seis mockups (5.26–5.31).

**Ninguna de las 13 "listas" está insertada todavía en `05_diseno.tex`** — ese archivo
sigue sin tocarse (bloque B de [`CAMBIOS-CAP5.md`](CAMBIOS-CAP5.md)).

---

*Generado: 2026-09-15. Actualizado: 2026-09-19 (5.12 y 5.16 pasan a listas).*
