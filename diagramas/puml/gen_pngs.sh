#!/bin/bash
# Regenera los PNG de los casos de uso. Se ejecuta desde cualquier carpeta.
# Requiere Java y el jar de PlantUML; indica su ruta con PLANTUML_JAR (por defecto, plantuml.jar
# en la raiz del repositorio).
REPO_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
PUML_DIR="$REPO_DIR/diagramas/puml"
OUT_DIR="$REPO_DIR/figures/mermaid"
JAR="${PLANTUML_JAR:-$REPO_DIR/plantuml.jar}"

for f in cu_vision_general cu_paquete1 cu_paquete2 cu_paquete3 cu_paquete4 cu_paquete5; do
  java -Djava.awt.headless=true -jar "$JAR" -tpng "$PUML_DIR/$f.puml" -o "$OUT_DIR" 2>&1
  echo "Generated: $f.png -> $?"
done
