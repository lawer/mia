---
layout: default
title: "Guia docent: IA responsable"
parent: 1.2 Ús responsable, segur i centrat en les persones
---

# Bloc 1.2: ús responsable, segur i centrat en les persones

## Propòsit

Aprendre a prendre una decisió d'enginyeria abans de construir o desplegar un sistema: quin problema resol, si la IA aporta valor respecte d'una alternativa simple, quines persones i dades poden quedar afectades, com provar errors previsibles i qui pot corregir-los. Una resposta tècnicament encertada no basta si l'ús produeix conseqüències inacceptables o no hi ha manera d'intervindre. L'alumnat aplica aquests criteris a una cua de suport tècnic i produeix una proposta de pilot revisable, amb riscos, proves, controls i criteris per continuar, limitar o aturar.

## Resultats d'aprenentatge

En acabar la unitat, l'alumnat podrà:

- redactar el problema, el benefici esperat i una alternativa de referència abans de proposar IA;
- identificar persones afectades, dades necessàries i decisions que no s'han de delegar;
- triar casos i mètriques que puguen revelar errors per idioma, canal o tipus d'incidència;
- relacionar cada risc prioritari amb un control, una prova i una persona responsable;
- recomanar provar, limitar o descartar l'ús i justificar què faria canviar la decisió.

## Materials

| Material | Enllaç |
| --- | --- |
| Presentació MARP | [PDF](0.-ia-responsable-marp.pdf) · [HTML](0.-ia-responsable-marp.html) |
| Apunts generats | [Continguts](continguts.md) |
| Fitxes de treball | [Exercicis i dades sintètiques](exercicis.md) |
| Recursos visuals | [Procedència i prompts](imatges.md) |

## Seqüència de treball

| Temps | Contingut i activitat | Evidència |
| --- | --- | --- |
| 30 min | 10 min d’introducció + 20 min d’exercici 1 | Alternativa, risc i control |
| 60 min | 10 min de dades i mètriques + 40 min d’exercici 2 + 10 min de correcció | Matrius i interpretació |
| 30 min | Supervisió, transparència, seguretat, marc normatiu i proporcionalitat | Controls aplicables al cas |
| 60 min | Taller sobre paper, amb prova de seguretat, defensa entre parelles d’equips i eixida individual | Fitxa i taula de proves |

**Total: 180 minuts.** Els exercicis 1 i 2 ocupen 60 minuts. La prova de seguretat forma part del taller, no és temps addicional. Si el grup necessita més suport, el càlcul de precisió positiva queda com a ampliació opcional.

La presentació té 31 diapositives. Atureu-la en «Activitat 2» abans de mostrar el gràfic amb la solució. En tot el bloc s’utilitzen dades fictícies i no cal accedir a cap servei d’IA. La defensa es fa simultàniament entre parelles d’equips per ajustar-la al temps disponible.

## Pràctica integradora

**Abast: disseny sobre paper, sense implementació.** Les proves es proposen i els resultats d’execució queden pendents; només les mètriques de l’exercici 2 es calculen amb prediccions donades.

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
| Quines mesures redueixen el risc? Qui n’és responsable? | |
| Quin criteri observable permet continuar, limitar o aturar el pilot? | |
| Quin risc residual queda després dels controls? | |
| Qui revisa els casos incerts? Com es corregeix o s'impugna una decisió? | |
| Quina informació s'ha de donar a les persones afectades? | |
| Quins són els límits del sistema i en quines condicions s'ha de deixar d'utilitzar? | |

### Criteris d'avaluació de la pràctica

- **Anàlisi del problema (25%)**: propòsit concret, afectats identificats i alternativa considerada.
- **Dades i riscos (25%)**: origen i minimització de dades, errors i possibles desigualtats.
- **Proves i mitigacions (30%)**: mètriques, casos de prova i controls coherents amb els riscos.
- **Supervisió i comunicació (20%)**: responsabilitats, revisió humana, límits i explicació comprensible.

## Connexió amb la resta del mòdul

La fitxa funciona com una porta de decisió al llarg del mòdul: en PLN s'afegiran proves d'instruccions malicioses i verificació de fonts; en visió, base jurídica adequada, representativitat i riscos de vigilància; en robòtica, límits físics, parada segura i cessió del control. Així, les proves tècniques de cada bloc també responen si el sistema és útil i controlable en el context d'ús.

La fitxa i els criteris es reprendran de manera integrada en el [projecte final de 15 hores]({% link apunts/2.-segon_trimestre/10.-Projecte integrador/projecte_integrador.md %}), on es combinen regles, recuperació documental, generació sota revisió i proves adversàries.

### Orientacions per avaluar

No penalitzeu una alternativa sense aprenentatge automàtic si està justificada. Valoreu que cada risc tinga un control, una prova i un responsable. Una revisió humana genèrica no és suficient: cal explicar recursos, autoritat i vies de correcció.

El solucionari i les orientacions de resposta es conserven en un document docent del repositori, exclòs del lloc publicat.

## Fonts per a consulta

- [Comissió Europea: marc regulador de la intel·ligència artificial](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [Comissió Europea: protecció de dades](https://commission.europa.eu/law/law-topic/data-protection_en)
- [EUR-Lex: Reglament (UE) 2024/1689](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=OJ%3AL_202401689)

Les fonts normatives són materials de consulta i poden actualitzar-se. Per aplicar-les a un cas real, cal consultar la versió oficial vigent i els responsables de protecció de dades o assessorament de l'organització.

- [NIST: AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [OWASP: Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)

Consulta de les fonts: 6 d’octubre de 2026. No s’hi fixa un calendari legal: per aplicar una obligació, cal comprovar el text vigent, el cas d’ús i el paper de l’organització.
