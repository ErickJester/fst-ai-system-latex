#!/bin/bash
PUML_DIR=/home/vane/fst-ai-system-latex/diagramas/puml
OUT_DIR=/home/vane/fst-ai-system-latex/figures/mermaid
JAR=/tmp/plantuml.jar

for f in cu_vision_general cu_paquete1 cu_paquete2 cu_paquete3 cu_paquete4 cu_paquete5; do
  java -Djava.awt.headless=true -jar $JAR -tpng $PUML_DIR/$f.puml -o $OUT_DIR 2>&1
  echo "Generated: $f.png -> $?"
done
