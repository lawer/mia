---
layout: default
title: Fitxa d’exercicis 1.1 · Introducció a la IA
parent: 1. Introducció i fonaments de la IA
nav_order: 2
---

# Fitxa d’exercicis 1.1 · Introducció a la IA

**Durada orientativa: 50–60 minuts.** Treballa individualment o en parella. Els casos són didàctics; no cal programar ni usar serveis externs. Anota les raons de les teues decisions: una etiqueta sense justificació no és suficient.

## 1. Descriu un agent: el robot aspirador

**Temps: 12 minuts.** Un robot aspirador recorre una casa, evita obstacles, neteja i torna a la base quan la bateria és baixa.

Completa la taula amb informació del cas. Si alguna dada no està especificada, escriu «no indicada» en lloc d’inventar-la.

| Component | Descripció |
| --- | --- |
| Objectiu de l’agent | |
| Entorn | |
| Sensors: què pot percebre? | |
| Actuadors: com pot actuar? | |
| Mesura de rendiment | |

1. Proposa dues mesures de rendiment que puguen entrar en conflicte, com ara temps i consum d’energia.
2. Descriu una situació en què una acció raonable amb la informació disponible tinga un resultat desfavorable.
3. Explica per què «racional» no vol dir «sempre encerta».

## 2. Tria una tècnica que encaixe amb la tasca

**Temps: 18 minuts.** Relaciona cada tasca amb una tècnica o combinació de tècniques. Usa opcions com càlcul o regla, cerca, sistema expert, aprenentatge supervisat, no supervisat o per reforç, o generació de llenguatge amb fonts. Es poden repetir opcions.

| Tasca | Tècnica probable | Quina informació necessita? | Què podria eixir malament? |
| --- | --- | --- | --- |
| A. Calcular l’import d’una compra a partir de preus i quantitats coneguts. | | | |
| B. Trobar una ruta de cost mínim en un mapa amb carrers tancats. | | | |
| C. Classificar missatges com a correu brossa o legítim a partir d’exemples etiquetats. | | | |
| D. Agrupar peticions semblants quan encara no hi ha categories assignades. | | | |
| E. Aprendre a jugar a un joc rebent una recompensa per cada partida. | | | |
| F. Redactar una resposta a partir d’un reglament i assenyalar el fragment que la justifica. | | | |
| G. Aplicar «si la temperatura supera el límit, activa l’alarma» a una lectura d’un sensor. | | | |

Després, tria dues files i explica per què una alternativa més simple o una combinació de tècniques podria ser millor.

**Recordatori:** PLN, visió i robòtica descriuen àmbits o tipus de tasca; supervisat, cerca i regles descriuen tècniques o mecanismes. Una aplicació pot combinar-ne més d’un.

## 3. Compara decisions amb rendiment esperat

**Temps: 10 minuts.** Un robot pot arribar a una sala per una de dues rutes. Per simplificar, només considerem el temps total esperat.

| Ruta | Temps normal | Probabilitat de bloqueig | Temps addicional si es bloqueja |
| --- | ---: | ---: | ---: |
| A | 8 min | 20 % | 20 min |
| B | 11 min | 2 % | 20 min |

Calcula el temps esperat de cada ruta amb la fórmula «temps normal + probabilitat de bloqueig × temps addicional». Quina ruta triaries amb aquest criteri?

1. Indica quin objectiu estàs optimitzant.
2. Digues quina informació podria fer canviar la decisió (per exemple, consum, seguretat o una restricció de pas).
3. Explica per què aquesta tria no prova que el robot siga intel·ligent en qualsevol altre sentit.

## 4. Què demostra una fita?

**Temps: 10 minuts.** Per a cada afirmació, escriu què permet concloure la fita i què no permet concloure. Si falta evidència, especifica quina prova addicional demanaries.

| Fita o exemple | Conclusió que sí que està justificada | Conclusió que no està justificada encara |
| --- | --- | --- |
| Un programa guanya una partida d’escacs a una campiona. | | |
| Un sistema supera una prova de conversa breu. | | |
| Un model classifica imatges amb un encert alt en una col·lecció de prova. | | |
| Un robot completa una tasca en un entorn controlat. | | |

## 5. Eixida breu: prepara el treball pràctic

Tria una aplicació d’IA que pugues documentar i completa aquest esquema en cinc línies:

**Problema i usuari → entrades → tècnica probable → eixida o acció → resultat que buscaré en una font fiable.**

Abans de donar-la per bona, comprova que siga una aplicació concreta i que les fonts permeten distingir els fets de les afirmacions promocionals. La [guia del treball pràctic 1](treball-practic-1.md) explica l’informe i els criteris d’avaluació.

## Autoavaluació

Marca cada afirmació que ja pots justificar amb un exemple:

- [ ] Puc descriure un agent amb entorn, sensors, actuadors i una mesura de rendiment.
- [ ] Puc distingir una tasca de cerca, una regla i diferents tipus d’aprenentatge.
- [ ] Puc explicar què mesura una prova i què no permet concloure.
- [ ] Puc donar una raó per la qual el sistema podria fallar en un altre context.
