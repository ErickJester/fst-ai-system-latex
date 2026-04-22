#!/usr/bin/env bash

MAIN=main
OUT=build

mkdir -p "$OUT"

echo "[1/4] pdflatex (primera pasada)..."
pdflatex -interaction=nonstopmode -output-directory="$OUT" "$MAIN.tex" > /dev/null || true

echo "[2/4] biber (referencias)..."
biber "$OUT/$MAIN" || { echo "ERROR: biber falló. Verifica que biber esté instalado."; exit 1; }

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
