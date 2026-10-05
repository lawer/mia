#!/usr/bin/env python3
"""Regenera els SVG didàctics del tema 1.2 a partir de la taula d'exercicis.
Ús: python scripts/build-ia-responsable-figures.py (només biblioteca estàndard).
"""
from pathlib import Path
from html import escape
import re

BASE = Path(__file__).resolve().parents[1] / 'apunts/1.-primer_trimestre/0.-IA responsable'
OUT = BASE / 'images'
OUT.mkdir(exist_ok=True)
NAVY, TEAL, AMBER, RED = '#17364b', '#187f86', '#edb34f', '#ab3b46'

def svg(name, title, desc, body, height=440):
    head = f'<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="{height}" viewBox="0 0 1100 {height}" role="img" aria-labelledby="title desc"><title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc><rect width="1100" height="{height}" fill="#fff"/><g font-family="DejaVu Sans,Arial,sans-serif" fill="{NAVY}">'
    (OUT / name).write_text(head + body + '</g></svg>\n')

def text(x, y, value, size=23, fill=NAVY, anchor='start', weight='normal'):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}">{escape(value)}</text>'

def box(x, y, w, h, fill):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="15" fill="{fill}"/>'

# Extract the same 20 synthetic records used by learners.
rows = re.findall(r'^\| ([VE]\d{2}) \| (Valencià|Castellà) \| (Sí|No) \| (Sí|No) \|$', (BASE / 'exercicis.md').read_text(), re.M)
assert len(rows) == 20, 'Expected 20 synthetic records'
counts = {}
for label in ['Valencià', 'Castellà', 'Total']:
    items = [r for r in rows if label == 'Total' or r[1] == label]
    vp = sum(r[2:] == ('Sí', 'Sí') for r in items)
    fn = sum(r[2:] == ('Sí', 'No') for r in items)
    fp = sum(r[2:] == ('No', 'Sí') for r in items)
    vn = sum(r[2:] == ('No', 'No') for r in items)
    counts[label] = (vp, fn, fp, vn)
    print(label, counts[label], 'encert', (vp+vn)/len(items), 'detecció', vp/(vp+fn))

body = ''
steps = [('Definir', 'Propòsit i límits'), ('Identificar', 'Persones i riscos'), ('Provar', 'Errors i controls'), ('Supervisar', 'Revisió i resposta'), ('Revisar', 'Canvis i incidents')]
for i, (a,b) in enumerate(steps):
    x = 15+i*218
    body += box(x,85,195,150,'#e7f1f1')+text(x+97,123,str(i+1),27,TEAL,'middle','bold')+text(x+97,161,a,25,NAVY,'middle','bold')+text(x+97,198,b,17,NAVY,'middle')
    if i<4:body += text(x+204,168,'→',25,TEAL,'middle')
body += '<path d="M985 253 V295 H115 V253" fill="none" stroke="#187f86" stroke-width="4"/>'
body += text(115,260,'↑',28,TEAL,'middle')+text(550,344,'Tornar a provar quan canvia el sistema o el context',23,NAVY,'middle')
svg('cicle-responsable.svg','Cicle de treball responsable','Definir, identificar, provar, supervisar i revisar; repetir el cicle després dels canvis.',body,370)

body=text(680,35,'PREDICCIÓ DEL MODEL',22,NAVY,'middle','bold')+text(440,75,'Urgent',25,NAVY,'middle')+text(830,75,'No urgent',25,NAVY,'middle')
body+=text(20,180,'REVISIÓ',19,NAVY,'start','bold')+text(20,212,'Urgent',23)+text(20,352,'No urgent',23)
for x,y,a,b,c,fill in [(245,105,'VP','Urgent detectada','Prioritat correcta','#d5ece9'),(635,105,'FN','Urgent no detectada','Risc de retard','#f8e3de'),(245,265,'FP','Alerta innecessària','Desplaça altres casos','#fff0cc'),(635,265,'VN','No urgent ben identificada','Cua ordinària','#d5ece9')]:
    body+=box(x,y,365,140,fill)+text(x+182,y+38,a,30,NAVY,'middle','bold')+text(x+182,y+78,b,21,NAVY,'middle')+text(x+182,y+111,c,18,NAVY,'middle')
svg('matriu-confusio.svg','Matriu de confusió','Files: realitat segons revisió. Columnes: predicció. VP i VN són encerts; FN i FP són errors.',body)

body=''
for panel,(title,metric) in enumerate([('Encert',lambda v:(v[0]+v[3])/sum(v)),('Detecció d’urgències',lambda v:v[0]/(v[0]+v[1]))]):
    left=90+panel*550;top=65;base=330
    body+=text(left+190,32,title,26,NAVY,'middle','bold')
    for pct in range(0,101,20):
        y=base-pct*2.35
        body+=f'<line x1="{left}" y1="{y}" x2="{left+405}" y2="{y}" stroke="#dbe3e7"/>'+text(left-12,y+6,str(pct)+'%',16,NAVY,'end')
    for i,(label,v) in enumerate(counts.items()):
        pct=round(metric(v)*100);x=left+22+i*134;h=pct*2.35;color=[TEAL,NAVY,'#82745a'][i]
        body+=box(x,base-h,95,h,color)+text(x+47,base-h-12,str(pct)+'%',24,color,'middle','bold')+text(x+47,365,label,20,NAVY,'middle')
body+=text(550,418,'Dades sintètiques: 10 peticions i 5 urgències per idioma',20,NAVY,'middle')
svg('errors-per-idioma.svg','La mitjana amaga diferències','Encert: valencià 70%, castellà 90%, total 80%. Detecció: valencià 60%, castellà 100%, total 80%.',body)
