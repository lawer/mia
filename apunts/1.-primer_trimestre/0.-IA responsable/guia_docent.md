---
layout: default
title: Guia docent: IA responsable
parent: 1.2 Ús responsable, segur i centrat en les persones
---

# Bloc 1.2: ús responsable, segur i centrat en les persones

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
| Fitxes de treball | [Exercicis i dades sintètiques](exercicis.md) |

## Seqüència de treball

| Sessió | Contingut i activitat | Evidència |
| --- | --- | --- |
| 30 min | Propòsit, persones afectades, cost de l'error i decisió d'usar IA o no. Exercici 1 en parelles. | Justificacions breus amb risc i control |
| 60 min | Dades, biaix i mètriques per grups. Exercici 2 amb dades sintètiques i posada en comú. | Matrius de confusió, mètriques i cauteles |
| 30 min | Privacitat, transparència, seguretat i supervisió humana: triar els controls imprescindibles per al cas. | Inventari de dades i controls prioritaris |
| 60 min | Cas integrador: classificar peticions fictícies de suport tècnic, completar la fitxa de riscos i defensar el disseny. | Fitxa de riscos i defensa breu |

La seqüència suma 3 hores. Les activitats d'exercicis ocupen aproximadament 60–75 minuts; la resta es dedica a explicació breu, discussió i cas integrador. En la pràctica s'utilitzen dades fictícies; no s'han d'introduir dades reals d'alumnat, famílies o personal en eines públiques.

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

La fitxa i els criteris es reprendran de manera integrada en el [projecte final de 15 hores]({% link apunts/2.-segon_trimestre/10.-Projecte integrador/projecte_integrador.md %}), on es combinen regles, recuperació documental, generació sota revisió i proves adversàries.

## Fonts per a consulta

- [Comissió Europea: marc regulador de la intel·ligència artificial](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [Comissió Europea: protecció de dades](https://commission.europa.eu/law/law-topic/data-protection_en)
- [EUR-Lex: Reglament (UE) 2024/1689](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=OJ%3AL_202401689)

Les fonts normatives són materials de consulta i poden actualitzar-se. Per aplicar-les a un cas real, cal consultar la versió oficial vigent i els responsables de protecció de dades o assessorament de l'organització.
