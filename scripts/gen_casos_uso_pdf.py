"""
Genera docs/casos_uso.pdf: los seis diagramas de casos de uso del capítulo 5,
cada uno en una página completa en orientación horizontal (carta apaisada).

Alternativa a casos_uso.tex para cuando no hay una distribución de TeX instalada.
El resultado es equivalente: mismo contenido, mismo orden, mismo criterio de escalado.

Los demás diagramas del documento están en gen_diagramas_pdf.py.

Ejecutar desde la raíz del repositorio:
    python scripts/gen_casos_uso_pdf.py
"""
from pathlib import Path

from pdf_diagramas import construir

REPO = Path(__file__).resolve().parent.parent
FIGS = REPO / "figures" / "mermaid"
OUT = REPO / "docs" / "casos_uso.pdf"

DIAGRAMAS = [
    (FIGS / "cu_vision_general.png", "Visión general del sistema"),
    (FIGS / "cu_paquete1.png", "Paquete 1 — Autenticación y gestión de usuarios"),
    (FIGS / "cu_paquete2.png", "Paquete 2 — Gestión de experimentos y carga de video"),
    (FIGS / "cu_paquete3.png", "Paquete 3 — Análisis conductual"),
    (FIGS / "cu_paquete4.png", "Paquete 4 — Resultados y reportes"),
    (FIGS / "cu_paquete5.png", "Paquete 5 — Dashboard, notificaciones y administración"),
]


if __name__ == "__main__":
    construir(
        salida=OUT,
        diagramas=DIAGRAMAS,
        subtitulo="Diagramas de casos de uso",
        titulo_pdf="Diagramas de casos de uso — TT 2026-B066",
    )
