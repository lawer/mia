---
layout: default
title: Exercicis IA responsable
parent: 1.2 Ús responsable, segur i centrat en les persones
---

# Exercicis d'aula: decidir, mesurar i revisar

**Durada total orientativa: 60–75 minuts.** Es poden fer en parelles. Tots els casos i registres són ficticis; no s'han d'afegir dades reals de l'alumnat o del centre.

## Exercici 1. Cal usar IA per a aquest problema?

**Temps:** 25–30 minuts.

Per a cada cas, trieu una opció: **regla convencional**, **cerca o optimització**, **model d'aprenentatge automàtic**, **generació amb recuperació de fonts**, o **cap decisió automatitzada**. Es pot combinar més d'una tècnica.

Completeu la taula i justifiqueu la resposta amb una frase.

| Cas | Opció triada | Per què és adequada? | Error o risc principal | Control necessari |
| --- | --- | --- | --- | --- |
| 1. Calcular el total d'una factura a partir de quantitats i preus coneguts. | | | | |
| 2. Trobar una ruta per a un robot en un mapa amb obstacles i zones prohibides. | | | | |
| 3. Classificar peticions de suport tècnic a partir d'exemples ja revisats. | | | | |
| 4. Redactar una resposta a partir del reglament intern i indicar quina font la justifica. | | | | |
| 5. Decidir automàticament si una persona rep una beca a partir del seu historial personal. | | | | |

**Preguntes de posada en comú**

- En quin cas una regla simple és més fàcil d'auditar que un model?
- En quin cas és essencial que una persona puga revisar o anul·lar el resultat?
- Què hauríem de saber abans d'usar les dades d'un cas real?

**Evidència:** taula completada amb una justificació, un risc i un control per cas.

## Exercici 2. Quins errors veu la mitjana i quins amaga?

**Temps:** 35–45 minuts.

Un classificador fictici suggereix si una petició de suport tècnic és urgent. La columna «Urgent segons revisió» és una etiqueta sintètica preparada per a l'exercici; no representa judicis sobre cap persona. El model només hauria de fer una recomanació, que revisaria una persona.

| Codi | Idioma de la petició | Urgent segons revisió | El model marca urgent |
| --- | --- | --- | --- |
| V01 | Valencià | Sí | Sí |
| V02 | Valencià | Sí | No |
| V03 | Valencià | Sí | Sí |
| V04 | Valencià | Sí | No |
| V05 | Valencià | Sí | Sí |
| V06 | Valencià | No | Sí |
| V07 | Valencià | No | No |
| V08 | Valencià | No | No |
| V09 | Valencià | No | No |
| V10 | Valencià | No | No |
| E01 | Castellà | Sí | Sí |
| E02 | Castellà | Sí | Sí |
| E03 | Castellà | Sí | Sí |
| E04 | Castellà | Sí | Sí |
| E05 | Castellà | Sí | Sí |
| E06 | Castellà | No | Sí |
| E07 | Castellà | No | No |
| E08 | Castellà | No | No |
| E09 | Castellà | No | No |
| E10 | Castellà | No | No |

### Tasques

1. Per a cada idioma, compteu **vertaders positius (VP)**, **falsos negatius (FN)**, **falsos positius (FP)** i **vertaders negatius (VN)**.
2. Calculeu:
   - **encert global** = (VP + VN) / total;
   - **detecció d'urgències** = VP / (VP + FN);
   - **urgències no detectades** = FN / (VP + FN).
3. Compareu els dos idiomes. En quina situació el model deixa escapar més peticions urgents?
4. Expliqueu per què una mitjana global pot ocultar diferències importants.
5. Proposeu dues comprovacions addicionals abans de concloure que hi ha un problema sistemàtic.
6. Indiqueu què hauria de fer el sistema quan no està segur i qui pot revisar la recomanació.

### Full de resultats

| Idioma | VP | FN | FP | VN | Encert global | Detecció d'urgències | Urgències no detectades |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Valencià | | | | | | | |
| Castellà | | | | | | | |

**Precaució:** només hi ha deu exemples per idioma. El conjunt és equilibrat i fabricat expressament; no permet generalitzar a persones reals ni demostrar per si sol una causa del comportament. Les etiquetes de revisió també poden ser discutibles. Cal més informació, proves representatives i una anàlisi del procés de dades.

**Evidència:** càlculs, una explicació de les limitacions i una mesura de supervisió.

## Connexió amb la pràctica integradora

En la pràctica de la cua de suport tècnic, reutilitzeu el raonament dels exercicis:

- justifiqueu per què una eina d'IA aporta valor enfront d'una regla o d'una cua manual;
- definiu què vol dir «urgent» abans de comparar prediccions;
- examineu errors per idioma, tipus de petició o una altra condició pertinent;
- establiu una revisió humana i una via per corregir la categoria o prioritat.
