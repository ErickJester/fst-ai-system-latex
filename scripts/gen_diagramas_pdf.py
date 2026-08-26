"""
Genera docs/diagramas.pdf: todos los diagramas del documento EXCEPTO los de
casos de uso, que tienen su propio PDF (ver gen_casos_uso_pdf.py).

Son 19 diagramas del capítulo 5, en el mismo orden en que aparecen en el
documento: arquitectura, base de datos, clases y los trece de secuencia.
Cada uno ocupa una página completa en carta horizontal.

No incluye los mockups de interfaz (son capturas de pantalla, no diagramas)
ni los logos institucionales.

Ejecutar desde la raíz del repositorio:
    python scripts/gen_diagramas_pdf.py
"""
from pathlib import Path

from pdf_diagramas import construir

REPO = Path(__file__).resolve().parent.parent
FIGS = REPO / "figures" / "mermaid"
DIAG = REPO / "diagramas"
OUT = REPO / "docs" / "diagramas.pdf"

# (ruta de la imagen, título). El orden sigue al del capítulo 5.
DIAGRAMAS = [
    # ── Arquitectura y flujo ──────────────────────────────────────────
    (FIGS / "arquitectura_software.png", "Arquitectura de software por capas tecnológicas"),
    (FIGS / "arquitectura.png",          "Flujo general del sistema"),
    (FIGS / "pipeline.png",              "Pipeline de análisis conductual"),

    # ── Base de datos ─────────────────────────────────────────────────
    (FIGS / "entidadRelacion.png",       "Modelo entidad-relación conceptual"),
    (FIGS / "er2.png",                   "Esquema físico de la base de datos"),

    # ── Clases ────────────────────────────────────────────────────────
    (DIAG / "clases.png",                "Diagrama de clases del sistema"),

    # ── Secuencia: autenticación y gestión de usuarios ────────────────
    (FIGS / "seq_registro.png",          "Secuencia — Registro de usuario por el administrador"),
    (FIGS / "seq_login.png",             "Secuencia — Inicio de sesión"),
    (FIGS / "seq_logout.png",            "Secuencia — Cierre de sesión"),
    (FIGS / "seq_cambio_pass_inv.png",   "Secuencia — Cambio de contraseña"),
    (FIGS / "seq_gestion_usuarios.png",  "Secuencia — Gestión de usuarios"),
    (FIGS / "seq_perfil.png",            "Secuencia — Configuración de perfil"),

    # ── Secuencia: notificaciones ─────────────────────────────────────
    (FIGS / "seq_notificaciones.png",    "Secuencia — Generación y consulta de notificaciones"),

    # ── Secuencia: análisis, resultados y reportes ────────────────────
    (FIGS / "seq_carga.png",             "Secuencia — Carga de video y encolado del análisis"),
    (FIGS / "seq_analisis.png",          "Secuencia — Análisis automático"),
    (FIGS / "seq_progreso.png",          "Secuencia — Consulta de progreso"),
    (FIGS / "seq_error.png",             "Secuencia — Manejo de error de calidad de video"),
    (FIGS / "seq_resultados.png",        "Secuencia — Consulta de resultados"),
    (FIGS / "seq_reportes.png",          "Secuencia — Descarga de reportes"),
]


if __name__ == "__main__":
    construir(
        salida=OUT,
        diagramas=DIAGRAMAS,
        subtitulo="Diagramas del sistema",
        titulo_pdf="Diagramas del sistema — TT 2026-B066",
    )
