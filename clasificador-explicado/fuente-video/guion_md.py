import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vid_main import ESCENAS, tiempos

out = ['# Guion del video: el clasificador explicado para niños', '',
       'Voz: Microsoft Sabina (es-MX), velocidad lenta. Los tiempos son del MP4.', '']
tot = 0.0
for i, sc in enumerate(ESCENAS):
    B, ds, total = tiempos(i)
    out.append('## %d. %s  (%d:%02d)' % (i + 1, sc['title'], int(tot // 60), int(tot % 60)))
    out.append('')
    for j, (disp, spk) in enumerate(sc['beats']):
        t = tot + B[j]
        out.append('- **%d:%02d** %s' % (int(t // 60), int(t % 60), disp))
    out.append('')
    tot += total
out.append('Duración total: %d:%02d' % (int(tot // 60), int(tot % 60)))
open(sys.argv[1], 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('ok', round(tot))
