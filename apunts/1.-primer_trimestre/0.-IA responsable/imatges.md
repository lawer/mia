---
layout: default
title: Crèdits visuals IA responsable
parent: 1.2 Ús responsable, segur i centrat en les persones
---

# Procedència dels recursos visuals

Creats el 6 d’octubre de 2026. Les il·lustracions generades són escenes fictícies i metàfores, no fotografies ni evidències d’un sistema real. No s’han emprat dades personals ni imatges de referència de persones.

| Fitxer | Procedència i funció |
| --- | --- |
| [supervisio-humana-ia.png](images/supervisio-humana-ia.png) | Generada amb el servei integrat image_gen; equip que revisa suggeriments i pot aturar el sistema. |
| [minimitzacio-dades-ia.png](images/minimitzacio-dades-ia.png) | Generada amb el servei integrat image_gen; metàfora de seleccionar dades necessàries. La il·lustració no descriu una arquitectura de seguretat. |
| [cicle-responsable.svg](images/cicle-responsable.svg) | Elaboració pròpia: cicle didàctic inspirat en la gestió de riscos. No és el diagrama oficial del NIST. |
| [matriu-confusio.svg](images/matriu-confusio.svg) | Elaboració pròpia; files de revisió i columnes de predicció. |
| [cicle-ia.svg](images/commons/cicle-ia.svg) | “AI system lifecycle assurance loop”, ISO Checklist editorial team amb OpenAI Codex (GPT-5), via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:AI_system_lifecycle_assurance_loop.svg), CC BY 4.0. Diagrama generat amb IA; es conserva sense modificacions i no és un estàndard oficial. |
| [cadena-evidencies-ia.svg](images/commons/cadena-evidencies-ia.svg) | “AI governance evidence chain”, ISO Checklist editorial team amb OpenAI Codex (GPT-5), via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:AI_governance_evidence_chain.svg), CC BY 4.0. Diagrama generat amb IA; es conserva sense modificacions i no és un estàndard oficial. |
| [accessibilitat.svg](images/commons/accessibilitat.svg) | Dave Braunschweig, [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Accessibility.svg), CC BY-SA 4.0. SVG original sense modificacions. |
| [cadenat.svg](images/commons/cadenat.svg) | Tango Desktop Project, derivat de RRZEicons, [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Lock.svg), domini públic. SVG original sense modificacions. |

Els SVG es regeneren amb `python scripts/build-ia-responsable-figures.py` des de l’arrel del repositori. Les dades es llegeixen directament de `exercicis.md`. Els esquemes propis segueixen la llicència CC-BY-NC-SA del material; les il·lustracions s’identifiquen expressament com a generades amb IA. No s’atribueixen a un fotògraf ni a una font externa.

## Prompts finals de generació

Eina: image_gen integrada, sense CLI ni imatges de referència. Els fitxers seleccionats s’han copiat al directori local `images/` sense modificar-los.

### Supervisió humana

```text
Use case: illustration-story. Asset type: educational slide illustration, landscape 3:2. Primary request: responsible artificial intelligence in a school IT support team. Editorial illustration with warm paper texture, precise clean forms, navy blue, teal and amber. Three adult IT staff with varied appearances collaboratively review a queue of support requests on a large screen, one person compares the suggestion to a paper checklist, another can pause the system using an obvious physical pause button. Human judgement is central; no humanoid robots, no glowing brains. The interface contains only abstract cards and simple icons, no text, no letters, no numbers. Calm credible classroom-friendly scene, uncluttered, generous margins, light ivory background. No logos or watermark.
```

### Minimització de dades

```text
Use case: illustration-story. Asset type: educational presentation illustration, landscape 3:2. Primary request: visual metaphor for personal-data minimisation in a school IT support workflow. A human hand selects only a small plain tool icon card and a broken-computer icon card to pass through a narrow opening toward a laptop. The unneeded identity portrait cards and a key remain safely in a separate closed transparent lockbox on the desk. Make the two destinations visually distinct, avoid suggesting all personal information is automatically anonymous. Editorial illustration with warm paper grain, precise clean shapes, navy blue, teal and amber on ivory, restrained and professional, generous margins. No text, no numbers, no logos, no watermark, no robot, no brain.
```
