import os, runpy

# Version de diapositiva del esquema conceptual: la misma geometria que gen_conceptual.py (D-108),
# para que la figura de la presentacion y la del documento no se separen. Se exporta a mayor escala.
# Uso: py -I -X utf8 gen_conceptual_s.py salida.html
runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gen_conceptual.py'), run_name='__main__')
