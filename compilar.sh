#!/usr/bin/env bash
#
# Compila un documento LaTeX del proyecto.
#
#   ./compilar.sh              -> compila main.tex      (documento principal)
#   ./compilar.sh casos_uso    -> compila casos_uso.tex (diagramas de casos de uso)
#
# El PDF se genera en build/.

MAIN="${1:-main}"
OUT=build

if [ ! -f "$MAIN.tex" ]; then
    echo "ERROR: no existe $MAIN.tex en $(pwd)"
    exit 1
fi

mkdir -p "$OUT"

echo "[1/4] pdflatex (primera pasada)..."
pdflatex -interaction=nonstopmode -output-directory="$OUT" "$MAIN.tex" > /dev/null || true

# biber solo si el documento usa bibliografía (biblatex genera el .bcf)
if [ -f "$OUT/$MAIN.bcf" ]; then
    echo "[2/4] biber (referencias)..."
    biber "$OUT/$MAIN" || { echo "ERROR: biber falló. Verifica que biber esté instalado."; exit 1; }
else
    echo "[2/4] biber omitido: $MAIN no usa bibliografía."
fi

echo "[3/4] pdflatex (segunda pasada)..."
pdflatex -interaction=nonstopmode -output-directory="$OUT" "$MAIN.tex" > /dev/null || true

echo "[4/4] pdflatex (tercera pasada, referencias cruzadas)..."
pdflatex -interaction=nonstopmode -output-directory="$OUT" "$MAIN.tex" > /dev/null || true

if [ -f "$OUT/$MAIN.pdf" ]; then
    echo ""
    echo "Listo: $OUT/$MAIN.pdf"
else
    echo "ERROR: no se generó el PDF. Revisa el log en $OUT/$MAIN.log"
    exit 1
fi
