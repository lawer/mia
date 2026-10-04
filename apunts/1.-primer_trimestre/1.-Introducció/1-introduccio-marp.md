---
marp: true
published: false
size: 16:9
theme: lawer
class: default
_class: invert lead
paginate: true
_paginate: false
auto-scaling: true
footer: 🄯 Carles Gonzàlez - CC-BY-NC-SA
---

<style scoped>
h1, h2, h3, h4, h5, h6, p {
  color: #FFFFFF;
  font-weight: 800;
  text-shadow:
    0px 0px 3px #000000;
}
</style>

# Introducció a la intel·ligència artificial

### Models d'intel·ligència artificial

![bg opacity](../../images/portada.png)

---

<style scoped>section { font-size:32px; }</style>

## Què és la IA?

- **Intel·ligència**: capacitat d'aprendre, comprendre i resoldre problemes.
- **Intel·ligència artificial**: intel·ligència exhibida per màquines.
- Una màquina intel·ligent percep el seu entorn i pren accions per maximitzar les possibilitats d'èxit d'un objectiu.

---

## Agents intel·ligents

- Un **agent** percep l'entorn mitjançant sensors i actua amb actuadors.
- Un agent intel·ligent ha de:
  - tenir un objectiu mesurable;
  - interpretar l'estat de l'entorn;
  - seleccionar una acció;
  - avaluar el resultat i adaptar-se quan calga.

![bg right:35% fit](../../images/what-is-the-composition-for-agents-in-artificial-intelligence.png)

---

## Què estudiarem?

- Com formular un problema perquè un sistema el puga resoldre.
- Diferents tècniques per construir agents intel·ligents.
- Avantatges, limitacions i costos de cada tècnica.
- Camps d'aplicació i impacte sobre les persones.
- Com triar entre famílies de tècniques i entendre'n les limitacions.

---

<!--
_class: invert lead
-->

## Una mica d'història

![bg opacity](../../images/History.jpg)

---

<style scoped>section { font-size:31px; }</style>

## Fites rellevants

- **1950**: Turing proposa substituir la pregunta "pensen les màquines?" per un criteri observable.
- **1956**: conferència de Dartmouth i naixement del terme intel·ligència artificial.
- **Anys 80**: sistemes experts per automatitzar decisions en dominis concrets.
- **1997**: Deep Blue derrota Kasparov als escacs.
- **2016**: AlphaGo mostra el potencial de combinar aprenentatge i cerca.

---

## Models fundacionals

- Els Transformers han fet possibles models de llenguatge, visió i àudio a gran escala.
- Els models actuals poden ser **multimodals**: text, imatge, veu, vídeo i codi.
- També existeixen models oberts i models que poden executar-se localment.
- La capacitat no elimina els límits: poden equivocar-se, inventar informació o reproduir biaixos.

---

## Situació actual

- La IA ja és present en serveis, indústria, ciència, educació i administració.
- Un bon sistema no es valora només per la seua qualitat:
  - cost i latència;
  - privacitat i seguretat;
  - explicabilitat;
  - manteniment i dependència de proveïdors;
  - impacte sobre les persones afectades.

![bg right:35% fit](../../images/State of AI.png)

---

<!--
_class: invert lead
-->

## Tenim una màquina intel·ligent?

![bg opacity](../../images/8860931.jpg)

---

<style scoped>section { font-size:31px; }</style>

## Intel·ligència humana i computacional

| Intel·ligència humana | Intel·ligència computacional |
| --- | --- |
| Biològica | Computacional |
| General | Específica |
| Conscient | Inconscient |
| Emocional | Racional |
| Adaptativa | Dissenyada |

La IA no intenta reproduir necessàriament una persona: construeix sistemes capaços de resoldre tasques definides.

---

## IA estreta i IA general

- **IA estreta o feble**: resol molt bé una tasca específica, com classificar imatges o planificar una ruta.
- **IA general o forta**: podria generalitzar la seua capacitat a qualsevol tasca intel·lectual humana.
- Els sistemes que utilitzem actualment són IA estreta, fins i tot quan resulten molt versàtils.

---

## Racionalitat

- Una decisió racional és la que maximitza la probabilitat d'aconseguir un objectiu segons la informació disponible.
- No sempre existeix una única resposta correcta.
- Cal definir:
  - l'objectiu;
  - les restriccions;
  - el cost de les accions;
  - com mesurarem l'èxit;
  - què ha de fer el sistema quan no tinga prou evidència.

---

<!--
_class: invert lead
-->

## Paradigmes de la IA

![bg opacity](../../images/Rule-based-vs-Machine-Learning-upd-1-1536x799.png)

---

## Paradigma simbòlic

- Representa coneixement amb símbols, fets i regles.
- Permet inferir conclusions i explicar com s'ha pres una decisió.
- Exemples:
  - sistemes experts;
  - sistemes basats en regles;
  - raonament basat en casos;
  - planificació i satisfacció de restriccions.

![bg right:30% fit](../../images/sistema expert.png)

---

## Paradigma connexionista

- Representa la informació amb xarxes de neurones artificials.
- Aprén patrons a partir de dades.
- És útil en visió per computador, veu, llenguatge i control.
- Sovint ofereix menys explicabilitat que una solució basada en regles.

![bg right:30% fit](../../images/xarxa_neuronal.png)

---

## Paradigma estadístic

- Analitza dades per estimar probabilitats i prendre decisions.
- Inclou classificació, regressió, agrupament i detecció d'anomalies.
- La qualitat del resultat depén de les dades, les mètriques i el context d'ús.

---

## Tècniques de IA

| Necessitat | Tècnica possible |
| --- | --- |
| Decisió estable, auditable i normativa | Regles o sistema expert |
| Ruta, planificació o restriccions | Cerca, CSP o optimització |
| Predicció a partir d'exemples | Aprenentatge automàtic |
| Text, imatge, veu o codi | Xarxes neuronals i models fundacionals |
| Consulta de documentació canviant | Recuperació d'informació o RAG |

---

## Seleccionar una tècnica

Relacionem el problema amb la família de tècniques: regles per a condicions estables, cerca per a rutes i plans, aprenentatge per a patrons en dades, i recuperació o RAG per a documentació. La idoneïtat i els riscos d'ús es treballen al bloc següent.

---

<!--
_class: invert lead
-->

## Aplicacions de la IA

![bg opacity](../../images/How_Artificial_Intelligence_is_Being_Deployed_Today.png)

---

<style scoped>section { font-size:31px; }</style>

## Alguns dominis

- **Robòtica**: percepció, planificació i control en el món físic.
- **PLN**: traducció, classificació, resum, assistents i cerca documental.
- **Visió per computador**: classificació, detecció, segmentació i seguiment.
- **Recomanació**: productes, música, continguts o recursos.
- **Salut, finances, indústria i transport**: suport a decisions i automatització.

---

## Responsabilitat al llarg del mòdul

La tria tècnica té conseqüències per a les persones, les dades i l'organització. En el bloc següent aplicarem aquests criteris a biaixos, privacitat, verificació, supervisió i responsabilitat.

---

<!--
_class: invert lead
-->

# Idees clau

- La IA és un conjunt de tècniques, no una única tecnologia.
- El problema, les dades, el risc i el context determinen el model adequat.
- La qualitat inclou precisió, cost, seguretat, explicabilitat i impacte.
- Un sistema intel·ligent ha de conèixer també els seus límits.
