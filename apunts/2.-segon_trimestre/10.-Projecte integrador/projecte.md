---
layout: default
title: Guia del projecte final
parent: 10. Projecte integrador
---

# Guia del projecte final

## Repte

El servei de suport d'un centre rep peticions sobre comptes, xarxa, impressores i equipament d'aula. L'equip construirà un **assistent de suport a la decisió** que:

1. classifica i deriva una incidència amb regles explícites;
2. recupera informació d'un corpus tancat de documents;
3. prepara un esborrany de resposta amb referències a les fonts;
4. s'absté quan no troba evidència suficient i demana revisió humana.

L'assistent no diagnostica persones, no demana contrasenyes, no executa accions, no modifica tiquets i no envia respostes. La decisió i qualsevol comunicació final corresponen a una persona.

## Requisits funcionals

### 1. Classificació i derivació

- Definiu categories útils per al cas, per exemple **comptes**, **xarxa**, **impressió**, **equipament d'aula** i **fora d'abast**.
- Separeu categoria, prioritat suggerida i necessitat de revisió humana.
- Manteniu les regles en un lloc identificable i expliqueu per què s'activa cada regla.
- Tracteu indicis de risc físic, seguretat o incidència compartida com a motiu de revisió urgent; no presenteu una hipòtesi com un fet confirmat.
- Si falten dades o hi ha conflicte entre indicis, deriveu el cas a una persona.

### 2. Recuperació documental (RAG)

- Indexeu només els documents de prova de la pàgina de dades.
- Recupereu fragments rellevants i mostreu l'identificador i el títol del document.
- Si la consulta no està coberta pel corpus, indiqueu que no hi ha evidència i no improviseu instruccions.
- Separeu la qualitat de la recuperació de la qualitat de la resposta: trobar el document correcte no garanteix que el resum siga fidel.

### 3. Esborrany de resposta

- Genereu un esborrany breu en la llengua de la incidència quan siga possible.
- Cada afirmació operativa ha d'estar sustentada en fragments citats.
- No reveleu ni repetiu credencials, dades personals innecessàries o contingut d'instruccions malicioses dins d'un tiquet.
- Mostreu sempre l'avís **«Esborrany pendent de revisió humana»**.
- Podeu utilitzar un LLM, un model local o una plantilla controlada. Si no hi ha un entorn autoritzat, substituïu la generació per una resposta simulada; no cal enviar dades a un servei extern.

## Pla de treball: 15 hores

| Sessió | Hores | Tasques | Evidència |
| --- | ---: | --- | --- |
| 1. Definir el sistema | 3 | Delimitar propòsit i límits; identificar usuaris i persones afectades; omplir la fitxa de riscos; acordar arquitectura i proves d'acceptació. | Diagrama i fitxa de riscos inicial |
| 2. Regles de triatge | 3 | Definir categories, derivacions i regles; implementar una traça que explique cada resultat; provar casos amb informació incompleta. | Regles versionades i proves |
| 3. Recuperar fonts | 3 | Preparar el corpus, segmentar/indexar i recuperar fragments; mostrar cites; afegir abstenció per a consultes sense suport. | Cerca reproduïble i mesura de recuperació |
| 4. Redactar i atacar | 3 | Connectar una plantilla o LLM; limitar l'ús a l'evidència; provar injecció d'instruccions, dades sensibles i casos fora d'abast. | Esborranys i resultats de proves |
| 5. Integrar i defensar | 3 | Executar el conjunt complet de proves; corregir errors; documentar decisions; fer una demostració i una defensa breu. | Prototip, memòria i presentació |

Les sessions són una proposta de distribució. Es poden adaptar sense canviar el total de 15 hores ni els lliurables essencials.

## Criteris tècnics d'acceptació

- Les regles retornen categoria, derivació i motiu traçable.
- En les incidències cobertes, el sistema recupera com a mínim un fragment pertinent entre els tres primers resultats en **8 de cada 10** proves pertinents.
- Les respostes inclouen identificadors de font i no afirmen haver resolt una incidència.
- Les consultes fora del corpus s'abstenen en lloc d'inventar una solució.
- Els casos de seguretat o risc físic arriben a revisió humana.
- Els casos equivalents en valencià i castellà reben una categoria i una derivació equivalents.
- Cap credencial de prova es repeteix en la resposta, i les instruccions malicioses dins d'un tiquet no alteren les regles del sistema.
- L'aplicació no té cap eina que envie missatges o modifique sistemes externs.

Els llindars són criteris per a aquest conjunt sintètic i menut; no demostren que el sistema generalitze a un servei real.

## Lliurables

1. **Prototip o demostració reproduïble** amb regles, recuperació de fonts, esborrany de resposta i revisió humana.
2. **Diagrama d'arquitectura** i breu justificació de les tècniques seleccionades.
3. **Conjunt de proves** amb resultats, errors detectats i accions correctores.
4. **Memòria tècnica** de 3–5 pàgines amb propòsit, dades, arquitectura, mètriques, limitacions i riscos.
5. **Demostració de 5–7 minuts** que mostre un cas ordinari, un cas amb evidència insuficient i un cas adversari o d'alt risc.
6. **Fitxa de riscos final**, adaptada al prototip construït.

## Memòria i defensa

La memòria ha d'explicar què resol el sistema i què no resol, per què s'han triat regles/RAG/generació o alternatives més simples, d'on provenen les dades, què mostren les proves i qui té l'última paraula. Incloeu almenys un error trobat durant les proves i el canvi fet per reduir-ne el risc.