# Localització al castellà

## Abast

Preparar una versió en castellà de tots els materials per a l'alumnat: pàgines i activitats Markdown, presentacions Marp i notebooks que s'utilitzen a classe. Les guies docents, els solucionaris i els materials històrics no publicats queden fora d'aquest abast.

Els noms de les funcions, les API, les variables i les dades tècniques es conserven quan traduir-los alteraria el codi o l'exemple. Es tradueixen les explicacions, els comentaris i els textos que veu l'alumnat. Els fitxers de dades i les imatges no es dupliquen si no contenen text didàctic que calga localitzar.

## Convenció

- La versió en castellà conviu amb l'original i acaba en `-es` (`tema-es.md`, `exercici-es.ipynb`).
- Els continguts Marp generats en castellà van a `continguts-es.md`, per no substituir els continguts valencians.
- Les pàgines de castellà indiquen `nav_exclude: true`; s'hi accedeix des de la versió valenciana i des del selector d'idioma.
- Les imatges, les dades i els enllaços tècnics es comparteixen sempre que siga possible.

## Estat

- [x] Generador Marp: separa els continguts en `continguts-es.md` i conserva els originals valencians.
- [x] Selector d'idioma al peu de pàgina per a les pàgines que tenen parella traduïda.
- [x] Índex en castellà i navegació de les dues avaluacions.
- [x] Pàgines, activitats, exercicis, treball pràctic i materials del projecte integrador per als temes 1–10.
- [x] Les 10 presentacions dels temes tenen font Marp, HTML i PDF en castellà: 0, 1, 3.1, 3.2, 4, 5, 6, 7, 8 i 9. S'ha comprovat que cada PDF té el mateix nombre de pàgines que l'original (31, 56, 38, 78, 76, 27, 51, 112, 98 i 44, respectivament).
- [x] Les dues presentacions addicionals enllaçades des de l'índex —Scrapy i la xarrada sobre IA en l'educació— també tenen font Marp, HTML i PDF en castellà; conserven les 26 i 23 pàgines dels originals.
- [x] S'han tret del web compilat les còpies PDF antigues i no enllaçades dels temes quan ja existia una presentació Marp vigent, per evitar oferir versions divergents sense localitzar. També s'ha tret un PDF de referència extern que no estava enllaçat. Els fitxers es conserven al repositori; els enllaços dels materials apunten a les versions vigents. També s'ha corregit l'enllaç antic de la presentació del tema 5.
- [x] 63 notebooks públics traduïts; els tres notebooks addicionals que no tenen parella són còpies de treball dins `historic/` i queden fora dels materials publicats. El codi executable s'ha conservat; només s'han traduït les explicacions i els comentaris pertinents.
- [x] Pàgines dels temes 6–9 enllacen també els notebooks complementaris públics que no apareixien a les taules originals.
- [x] Auditoria estàtica de 140 enllaços locals en les pàgines i fonts castellanes: cap enllaç trencat. Els recursos addicionals de l'índex castellà apunten a les presentacions localitzades.
- [x] Compilació completa del web amb les gemmes disponibles: `JEKYLL_NO_BUNDLER_REQUIRE=true jekyll build`. S'han generat les pàgines castellanes i els recursos del lloc.

Els materials històrics no publicats, les guies docents i els solucionaris queden deliberadament fora de l'abast. `portal.md` és una presentació per a la gestió docent del web, no està enllaçada des de la navegació de l'alumnat i no forma part d'aquesta versió.

La compilació mostra avisos de Sass per funcions obsoletes i dos conflictes de destinació previs entre `present_sagunt.md`/`present_sagunt.html` i `scrapy_marp.md`/`scrapy_marp.html`; no impedeixen generar el lloc ni afecten els materials castellans.
