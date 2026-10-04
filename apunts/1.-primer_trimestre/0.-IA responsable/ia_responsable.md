---
title: 0. IA responsable, segura i centrada en les persones
parent: 1. Primera Avaluació
layout: default
has_children: true
has_toc: false
nav_order: 0
---

# 0. IA responsable, segura i centrada en les persones

**Durada orientativa: 5 hores.** Unitat d'obertura del mòdul 5071. Presenta criteris que es reprendran en les pràctiques de cerca, sistemes basats en regles, lògica difusa, PLN, visió i robòtica.

## Propòsit

Aprendre a decidir si convé utilitzar IA en un problema, identificar les persones i dades afectades, anticipar errors i perjudicis, i dissenyar controls proporcionats. L'objectiu no és memoritzar una llista de principis, sinó aplicar-los abans i després de construir un sistema.

## Resultats d'aprenentatge

En acabar la unitat, l'alumnat podrà:

- descriure el propòsit d'un sistema i les persones que en poden rebre els efectes;
- justificar quan una regla, una consulta o una revisió humana són preferibles a un model;
- detectar riscos de privacitat, biaix, seguretat, accessibilitat i ús inadequat;
- triar mètriques i casos de prova que facen visibles errors desiguals;
- establir supervisió, alternatives i vies de revisió humana;
- documentar riscos, mitigacions, límits i responsabilitats amb una fitxa breu.

## Materials

| Material | Enllaç |
| --- | --- |
| Presentació MARP | [PDF](0.-ia-responsable-marp.pdf) · [HTML](0.-ia-responsable-marp.html) |
| Apunts generats | [Continguts](continguts.md) |

## Seqüència de treball

| Sessió | Contingut i activitat | Evidència |
| --- | --- | --- |
| 1 h | Propòsit, context, persones afectades i cost de l'error. Decidir si cal IA. | Declaració del problema i alternatives |
| 1 h | Dades, representativitat, biaix i mètriques per grups. Analitzar exemples sintètics. | Taula de riscos i proves |
| 1 h | Privacitat, minimització, procedència i seguretat de dades. | Inventari de dades i controls |
| 1 h | Transparència, accessibilitat, supervisió humana i marc normatiu. | Mesures de supervisió i comunicació |
| 1 h | Cas integrador: classificar peticions fictícies de suport tècnic i defensar el disseny. | Fitxa de riscos completa i presentació breu |

Les sessions poden adaptar-se al calendari. En la pràctica s'utilitzen dades fictícies; no s'han d'introduir dades reals d'alumnat, famílies o personal en eines públiques.

## Pràctica integradora

Un centre vol classificar les peticions fictícies de suport tècnic per ajudar a ordenar la cua. L'eina no pot tancar peticions ni decidir quines persones reben un servei. L'equip ha de:

1. definir per a què serviria el sistema i considerar una alternativa sense IA;
2. enumerar dades necessàries i dades que cal excloure;
3. comprovar si diferències d'idioma, vocabulari o canal d'entrada canvien els errors;
4. seleccionar exemples de prova i mètriques, incloent-hi errors per grup o tipus de petició;
5. establir quan una persona revisa, corregeix o anul·la una recomanació;
6. descriure què es registra, qui hi accedeix i com es comunica l'ús de l'eina.

## Fitxa d'anàlisi de riscos

Cal completar aquesta fitxa abans d'una pràctica amb dades o resultats que puguen afectar persones. En exercicis purament algorítmics, es pot respondre breument o marcar «no aplicable» amb una justificació.

| Pregunta | Resposta de l'equip |
| --- | --- |
| Quin problema i quin propòsit té el sistema? | |
| Qui el farà servir i qui en pot rebre l'efecte? | |
| Es pot resoldre sense IA? Quina alternativa hi ha? | |
| Quines dades s'utilitzen? D'on provenen? Hi ha dades personals o llicències a comprovar? | |
| Quins errors són previsibles? Qui en pot eixir més perjudicat? | |
| Quines mètriques i casos de prova faran visibles aquests errors? | |
| Quines mesures redueixen el risc? | |
| Qui revisa els casos incerts? Com es corregeix o s'impugna una decisió? | |
| Quina informació s'ha de donar a les persones afectades? | |
| Quins són els límits del sistema i en quines condicions s'ha de deixar d'utilitzar? | |

### Criteris d'avaluació de la pràctica

- **Anàlisi del problema (25%)**: propòsit concret, afectats identificats i alternativa considerada.
- **Dades i riscos (25%)**: origen i minimització de dades, errors i possibles desigualtats.
- **Proves i mitigacions (30%)**: mètriques, casos de prova i controls coherents amb els riscos.
- **Supervisió i comunicació (20%)**: responsabilitats, revisió humana, límits i explicació comprensible.

## Connexió amb la resta del mòdul

La fitxa es reutilitzarà, adaptada, en pràctiques amb dades, models o dispositius físics. Per exemple, en PLN s'afegiran proves d'instruccions malicioses i verificació de fonts; en visió, consentiment, representativitat i vigilància; en robòtica, límits físics, parada segura i cessió del control.

## Fonts per a consulta

- [Comissió Europea: marc regulador de la intel·ligència artificial](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [Comissió Europea: protecció de dades](https://commission.europa.eu/law/law-topic/data-protection_en)
- [EUR-Lex: Reglament (UE) 2024/1689](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=OJ%3AL_202401689)

Les fonts normatives són materials de consulta i poden actualitzar-se. Per aplicar-les a un cas real, cal consultar la versió oficial vigent i els responsables de protecció de dades o assessorament de l'organització.
