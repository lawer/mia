# Prompt: auditoria integral del curs de Models d’Intel·ligència Artificial

Actua com a comissió de revisió curricular, especialista en intel·ligència artificial, docent del nivell corresponent i auditor/a tècnic/a de materials educatius. Audita **tot el curs** del repositori: totes les avaluacions i unitats, presentacions, continguts, exercicis, projectes, rúbriques, notebooks, recursos visuals, pàgines web i eines de compilació. Desa les troballes en `scripts/auditoria_curs.md`, en Markdown llegible per l’equip docent. En acabar, mostra un resum breu amb l’enllaç a l’informe.

## Preparació i abast

1. Llig les instruccions del repositori (`AGENTS.md` o equivalents). Identifica la branca, l’estat del repositori i els canvis previs; no els revertisques.
2. Fes inventari de totes les unitats, materials editables i generats, materials docents, solucionaris, notebooks, dades i recursos enllaçats. Comprova la configuració de publicació i la navegació efectiva; no deduïsques que un fitxer és privat pel nom.
3. Revisa l’índex general, cadascuna de les avaluacions i totes les unitats, inclosos els recursos que s’obrin en serveis externs com Colab. Diferencia els continguts que l’alumnat veu dels materials interns de docència.
4. Registra data, eines i fonts. Quan una comprovació siga impossible, concreta què no s’ha pogut verificar i per què.

## Dimensions de l’auditoria

### Coherència curricular i planificació

- Contrasta objectius, resultats d’aprenentatge, seqüència, prerequisits, nivell, terminologia i dependències entre unitats, pràctiques i projecte final.
- Comprova que hores per bloc i durades locals siguen coherents amb el total declarat, les activitats, les pauses, el treball fora de l’aula i la càrrega real.
- Revisa estructura trimestral, numeració, noms, jerarquia, enllaços, itineraris de l’alumnat i relació entre teoria, pràctica i avaluació.
- Detecta repeticions, llacunes, contingut fora de seqüència, tasques redundants i temes que no contribueixen a cap objectiu visible.

### Correcció i actualització tècnica

- Verifica definicions, algoritmes, fórmules, exemples, mètriques, gràfiques, pseudocodi, codi, dades i conclusions de cada àrea del curs: fonaments i agents; cerca, heurístiques, jocs, optimització i CSP; sistemes basats en regles i lògica difusa; aprenentatge automàtic; PLN, embeddings, Transformers i RAG; visió artificial; robòtica; seguretat, privacitat i ús responsable.
- Separa simplificacions didàctiques acceptables d’errors conceptuals. Comprova que no es confonguen tasques, mètodes, arquitectures, models, eines i àmbits d’aplicació; que els exemples no presenten resultats de benchmark com a garanties; i que els exercicis tinguen resultats reproduïbles.
- Detecta dependències, APIs, versions, plataformes, models, conjunts de dades i enllaços obsolets o fràgils. Per a continguts canviants, verifica l’estat actual amb fonts primàries: documentació oficial, articles originals, estàndards i organismes públics. Anota al report enllaç directe, autoria o entitat i data de consulta.
- Revisa normativa en fonts oficials vigents i limita les conclusions al que aquestes fonts sostenen. Distingeix recomanacions, estàndards voluntaris i obligacions legals.
- No afiges tecnologies noves per novetat: explica quin objectiu cobreixen, què cal actualitzar i quin temps o contingut substituirien.

### Qualitat didàctica i avaluació

- Comprova alineació entre objectius, explicacions, exercicis, projecte, rúbriques i evidències d’aprenentatge.
- Valora prerequisits, bastides, càrrega cognitiva, participació activa, transferència, inclusió, accessibilitat i adequació al nivell.
- Revisa que les activitats expliquen què s’ha de lliurar, amb quins criteris, quins recursos calen, quant de temps requereixen i si es fan individualment o en equip.
- Comprova solucions, dades d’exemple, sortides de codi i respostes esperades. Busca diferències entre les instruccions i la rúbrica, i tasques no avaluades o criteris que no s’han ensenyat.
- Per a notebooks, inspecciona dependències, cel·les executables, ordre d’execució, descàrregues, dades, permisos, cost i necessitat de credencials. Executa’ls només quan siga viable i registra l’abast exacte de les proves.

### Veu, llengua i accessibilitat

- Revisa tot el text destinat a l’alumnat: valencià, ortografia, puntuació, consistència terminològica, claredat, inclusivitat i instruccions directes.
- Detecta notes editorials, comentaris per a qui projecta, llenguatge intern o docent, avisos de generació i respostes incorporades al material públic.
- Comprova estructura semàntica, contrast, grandària i llegibilitat, text alternatiu, enllaços descriptius, dependència del color, taules i formats accessibles.

### Publicació, privacitat i drets

- Comprova què es publica realment al web, incloent PDF, HTML, continguts generats, fitxers descarregables i enllaços a serveis externs. Localitza solucionaris, claus, comentaris ocults, cel·les de sortida i respostes incrustades.
- Verifica exclusions, navegació, fitxers docents, dades personals, secrets, tokens, informació privada i instruccions que puguen fer pujar dades sensibles a plataformes externes.
- Revisa l’origen, pertinència, crèdits, llicències i accessibilitat de les imatges, conjunts de dades, fragments de codi i documents de tercers.

### Auditoria tècnica del repositori

- Valida front matter, rutes amb accents i espais, enllaços locals, imatges, recursos, pàgines inexistents, duplicats, noms de fitxer, ordre de navegació, configuració de Jekyll i generació de Marp.
- Compara fonts i materials generats per detectar divergències i artefactes desactualitzats.
- Executa les proves, compilacions i comprovacions pertinents de tot el lloc. Anota l’ordre, resultat i error literal rellevant; no afirmes que una compilació ha passat si queda incompleta.

## Criteris per a les troballes

- Prioritza per impacte: **bloquejant** (risc danyós o curs incapaç de complir l’objectiu), **important** (error que afecta l’aprenentatge, l’avaluació, la seguretat o la publicació) i **menor** (millora de claredat o manteniment).
- Cada troballa inclou ID, prioritat, curs/unitat, fitxer i línia o secció, evidència observable, impacte concret, recomanació i font externa quan corresponga.
- Separa defectes confirmats, riscos i preguntes que requereixen decisió docent. No presentes conjectures com a fets ni ompligues el report amb estil editorial de poca conseqüència.
- Si tens autorització per corregir, fes-ho després d’escriure l’auditoria i limita els canvis automàtics a errades locals inequívoces. No alteres objectius, nivell, hores, criteris o privacitat sense deixar clara la proposta i els seus costos. Actualitza els generats i torna a validar.

## Estructura de `scripts/auditoria_curs.md`

1. **Abast i mètode**: data, unitats i artefactes revisats, comprovacions fetes i límits.
2. **Valoració general**: estat global, punts forts i riscos prioritaris.
3. **Inventari del curs**: avaluacions, unitats, tipus de material, visibilitat i estat de compilació.
4. **Troballes prioritzades**: fitxer, evidència, impacte, recomanació i font.
5. **Revisió tècnica per àrea**: què és sòlid, què cal actualitzar i què falta verificar.
6. **Revisió didàctica i d’avaluació**: coherència, càrrega, activitats, projecte i rúbriques.
7. **Publicació, privacitat, accessibilitat i llicències**.
8. **Propostes de revisió ordenades**: accions concretes, dependències i cost orientatiu; separa correccions clares de decisions docents.
9. **Canvis aplicats** (si n’hi ha) i **validació** amb resultats exactes.

No inclogues conclusions sense evidència. Si una unitat o artefacte no s’ha pogut revisar a fons, enumera’l com a pendent en lloc d’insinuar cobertura completa.
