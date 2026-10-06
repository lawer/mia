---
layout: default
title: "Treball pràctic 1: anàlisi d'una aplicació d'IA"
parent: 1. Introducció i fonaments de la IA
nav_order: 1
---

# Treball pràctic 1: anàlisi d'una aplicació d'IA

## Propòsit

Tria una aplicació real d'intel·ligència artificial i explica **quin problema resol, com funciona a grans trets i quines tècniques de les estudiades en el tema 1.1 hi reconeixes**. Acaba valorant què permet fer, quins límits tenen les proves disponibles i quina informació encara necessitaries.

Amb aquest treball tanques la primera part del tema 1: aplica els conceptes d'agents, tècniques i àmbits d'ús a un cas concret. En la secció 1.2 estudiaràs amb més detall les persones afectades, els riscos i els controls.

## Tria del cas

Pot ser una aplicació comercial, un servei públic o un prototip de recerca. Tria un cas amb informació pública suficient sobre la tasca i el seu funcionament; no cal que siga una aplicació creada per un grup d'I+D, però sí que has de trobar almenys una font tècnica o primària fiable.

Exemples: un sistema de recomanació, un assistent de text, una eina de traducció, un sistema de diagnòstic assistit, un detector d'objectes, un robot o un agent que resol problemes mitjançant cerca. Pots proposar un altre cas si trobes documentació que permeta verificar-ne el funcionament.

**Abast:** analitza una aplicació concreta i una tasca principal. No intentes explicar tota una empresa, una família sencera de models o «la IA en medicina» en general. No cal programar ni crear un compte en cap servei.

## Informe

Extensió orientativa: **4–6 pàgines**, sense comptar portada, bibliografia i annexos. Treballa individualment o per parelles, d'acord amb l'organització de classe. Inclou aquests apartats:

### 1. Identificació i resum

- Nom de l'aplicació, organització o equip responsable, any aproximat i fonts consultades.
- Quin problema aborda i qui la utilitza?
- Resumeix en 100–150 paraules què fa, quina tècnica principal empra i quin resultat has trobat més rellevant.

### 2. Com funciona?

Descriu el sistema com una aplicació concreta, no com una «caixa màgica»:

| Element | Pregunta orientativa |
| --- | --- |
| Objectiu | Què intenta aconseguir i com es podria mesurar que ho fa bé? |
| Entrades | Quina informació rep: text, imatge, dades, accions o estat de l'entorn? |
| Mecanisme | Quina tècnica transforma les entrades en una predicció, resposta o acció? |
| Eixida o acció | Què produeix? Ho presenta a una persona o actua sobre l'entorn? |
| Context d'ús | En quines condicions i amb quins límits s'utilitza? |

No totes les fonts publiquen tots aquests detalls. Indica **«no documentat en les fonts consultades»** quan corresponga; no completes els buits amb suposicions.

### 3. Connexió amb els conceptes del tema 1.1

Identifica la tècnica o família de tècniques i justifica-ho amb evidència de les fonts. Segons el cas, pots parlar de regles, cerca, optimització, aprenentatge supervisat, no supervisat o per reforç, xarxes neuronals, generació de llenguatge, visió o robòtica. Explica només les que siguen pertinents.

Distingeix **tècnica** i **àmbit d'aplicació**: per exemple, PLN descriu un àmbit, mentre que un model supervisat o un transformer descriuen mecanismes o arquitectures que s'hi poden emprar. Una mateixa aplicació pot combinar-ne més d'un.

### 4. Quines proves hi ha?

- Quins resultats, exemples o mètriques publica la font?
- Amb quina tasca, dades i condicions es van obtindre?
- Hi ha comparació amb una alternativa o una referència humana?
- Què **no** demostren aquests resultats? Assenyala almenys una limitació de les proves.

Separa els resultats mesurats de les afirmacions promocionals. Si no hi ha una avaluació pública, explica-ho en lloc d'atribuir al sistema una eficàcia no comprovada.

### 5. Abast i valoració final

En un paràgraf o una taula breu, resumeix:

- un benefici concret que les fonts recolzen;
- una limitació o situació en què la tècnica podria fallar;
- una pregunta important que no pots resoldre amb la informació disponible;
- la teua conclusió: **on sembla útil i on no tens prou evidència per recomanar-la**.

No cal fer ací una auditoria legal o ètica completa. Guarda la pregunta «qui podria patir les conseqüències i quins controls calen?» per al bloc 1.2.

### 6. Bibliografia i traçabilitat

Inclou almenys **tres fonts**, citades també al cos de l'informe:

1. Una **font primària o tècnica**: article original, documentació tècnica, informe de l'equip desenvolupador o publicació del grup de recerca.
2. Una font **acadèmica o independent** que aporte context, verificació o una perspectiva diferent.
3. Una altra font fiable necessària per entendre l'àmbit o comprovar una afirmació concreta.

Per a cada font, anota autoria o entitat, títol, data, enllaç i data de consulta. Un cercador —Google Scholar, per exemple— serveix per trobar publicacions, però no substitueix la referència a l'article. Prioritza publicacions, universitats, organismes públics i documentació tècnica identificable; no uses una publicació en xarxes socials com a única prova d'una afirmació.

## Exposició breu

Prepara una explicació de **3 minuts** amb una sola diapositiva o esquema: problema → entrades → tècnica → eixida → evidència i límit. La resta del grup ha de poder entendre què fa l'aplicació sense llegir l'informe.

## Criteris d'avaluació

| Criteri | Pes |
| --- | ---: |
| Problema, tasca i context ben delimitats | 20 % |
| Explicació del funcionament i connexió correcta amb conceptes del tema 1.1 | 30 % |
| Qualitat, diversitat i citació de les fonts | 20 % |
| Interpretació dels resultats i de les seues limitacions | 20 % |
| Claredat de l'informe i de l'exposició | 10 % |

Es valora especialment distingir entre allò que la documentació confirma i allò que encara és incert. No es puntua la complexitat tècnica del sistema triat: una aplicació senzilla i ben analitzada és preferible a una de complexa descrita només amb frases promocionals.

## Pregunta de pas al tema 1.2

Després d'explicar com funciona, deixa oberta aquesta pregunta: **si l'aplicació es començara a utilitzar amb persones reals, qui podria resultar-ne afectat, quin error seria més greu i qui hauria de poder revisar-lo?** La reprendrem en el bloc següent.
