---
marp: true
published: false
size: 16:9
theme: lawer
paginate: true
footer: Carles Gonzàlez
style: |
  section { font-size: 30px; line-height: 1.3; padding: 54px 64px 70px; }
  section.side { font-size: 26px; }
  section.compact { font-size: 23px; }
  section h2 { font-size: 1.45em; }
  section h3 { font-size: 1.15em; }
  section.lead h1 { font-size: 2em; }
  section table { font-size: 0.9em; }
  section footer, section::after { font-size: 14px; }
---

<!-- Transcripció del PDF original 1-introduccio.pdf: 55 diapositives.
Es conserven el contingut i els errors originals; la revisió queda pendent.
Només les il·lustracions són imatges: el text, les llistes i les taules són Markdown editable. -->

<!-- Diapositiva 1 del PDF original -->

<!-- _class: lead -->

![bg](images/original/diapositiva-01.png)

# 1. Introducció a la intel·ligència artificial

### Models d'intel·ligència artificial

---

<!-- Diapositiva 2 del PDF original -->

## Què és la intel·ligència artificial?

| | |
| --- | --- |
| **Intel·ligència** | La intel·ligència és la capacitat d'aprendre, comprendre i resoldre problemes. |
| **Intel·ligència artificial** | La intel·ligència artificial és la inteligència exhibida per màquines. |
| **Màquina intel·ligent** | Una màquina intel·ligent és un sistema que pot percebre el seu entorn i prendre accions que maximitzen les seves possibilitats d'èxit en un objectiu. |

---

<!-- Diapositiva 3 del PDF original -->

<!-- _class: side -->

![bg right:45% fit](images/original/diapositiva-03.png)

## Agents intel·ligents (I)

- Un **agent** percep el seu entorn mitjançant **sensors** i actua sobre ell mitjançant **actuadors**.
- Un **agent intel·ligent** és un agent que actua de forma intel·ligent.
  - **Actuar de forma intel·ligent**: Actuar de forma que maximitza les seves possibilitats d'èxit en un objectiu.
  - **Objectiu**: Una funció que mesura el rendiment de l'agent en un entorn.

---

<!-- Diapositiva 4 del PDF original -->

<!-- _class: side -->

![bg right:45% fit](images/original/diapositiva-04.png)

## Agents intel·ligents (II)

- L'assignatura tracta sobre la **construcció d'agents intel·ligents**.
- Veurem:
  - Diferents **tècniques** per a construir agents intel·ligents.
  - Els seus **avantatges i inconvenients**.
  - Els seus **camps d'aplicació**.
  - Els seus **riscos i reptes ètics**.

---

<!-- Diapositiva 5 del PDF original -->

<!-- _class: lead -->

![bg](images/original/diapositiva-05.png)

# Una mica d'història

---

<!-- Diapositiva 6 del PDF original -->

<!-- _class: side -->

![bg right:45% fit](images/original/diapositiva-06.png)

## 1950: Alan Turing

- La prova de Turing és una proposta de test per a la intel·ligència d'una màquina
- La va proposar Alan Turing el 1950 en el seu article *"Computing Machinery and Intelligence"*.
- L'objectiu de la prova és determinar *si una màquina pot pensar*.

---

<!-- Diapositiva 7 del PDF original -->

<!-- _class: side -->

![bg right:45% fit](images/original/diapositiva-07.png)

## El test

- Un humà, aïllat en una habitació, ha de mantenir una conversa escrita amb **dues persones, una humana i una màquina**.
- Si l'humà *no pot distingir* entre les dues, la màquina es **considera que pensa**.

---

<!-- Diapositiva 8 del PDF original -->

## La pregunta de Turing

| | |
| --- | --- |
| **Poden pensar les màquines?:** | La pregunta de si les màquines poden pensar és massa vaga, i hauria de ser reemplaçada per una altra pregunta que pugui ser contestada per mitjà d'un sí o un no, que tingui una significació precisa. |
| **Poden les màquines fer el que els humans poden fer?:** | Aquesta nova pregunta té l'avantatge que és possible contestar-la definitivament i que molts arguments que s'han fet per contestar la pregunta original poden ser reutilitzats. \_\_ |

---

<!-- Diapositiva 9 del PDF original -->

<!-- _class: side -->

![bg right:45% fit](images/original/diapositiva-09.png)

## 1956 - 1974: Els inicis

- **1956**: *John McCarthy* - La conferència de Dartmouth. El naixement de la IA.
- **1957**: *Herbert Simon* - "En 10 anys el campió mundial d'escacs serà una màquina"
- **1958**: *Frank Rosenblatt* - El perceptró
- **1967**: *Marvin Minsky* - "En una generació, el problema de la IA estarà resolt"

---

<!-- Diapositiva 10 del PDF original -->

<!-- _class: side -->

![bg right:45% fit](images/original/diapositiva-10.png)

## 1974 - 1993: Hi ha esperança?

- **1974-1980**: Pocs avenços, desencantament i crisi de finançament (AI Winter)
- **Principis dels 80**: Apareixen els sistemes experts
- **1982 - 1992**: Projecte Japonès de la 5a generació
- **1987-1993**: Els sistemes experts fracassen. (II AI Winter)

---

<!-- Diapositiva 11 del PDF original -->

<!-- _class: side -->

![bg right:45% fit](images/original/diapositiva-11.png)

## 1997: Deep Blue

- Deep Blue guanya a Kasparov, el campió mundial d'escacs.
- Els sistemes experts són capaços de superar a humans en tasques específiques.
- Després de la victòria, IBM desmantella el projecte.
- **Els sistemes experts no són capaços de superar a humans en tasques generals.**

---

<!-- Diapositiva 12 del PDF original -->

<!-- _class: side -->

![bg right:45% fit](images/original/diapositiva-12.png)

## 2002: Roomba

- Roomba va ser el primer robot domèstic comercialitzat.
- És capaç de netejar una habitació sense cap mena d'ajuda humana.
- Detecta obstacles i els evita, i torna a la seva base quan s'acaba la bateria.
- **El 2017, Roomba va vendre més de 20 milions d'unitats.**

---

<!-- Diapositiva 13 del PDF original -->

<!-- _class: side compact -->

![bg right:45% fit](images/original/diapositiva-13.png)

## 2005: DARPA Grand Challenge

- Després de 4 anys de preparació, el 2004 es va celebrar la primera edició del DARPA Grand Challenge.
- Els participants havien de construir un vehicle autònom capaç de recórrer 240 km per un terreny desèrtic.
- Els vehicles havien de ser capaços de prendre decisions sense cap mena d'ajuda humana.
- Els 15 equips participants no van ser capaços de completar el recorregut.
- **El 2005, 5 equips van completar el recorregut**.

---

<!-- Diapositiva 14 del PDF original -->

<!-- _class: side -->

![bg right:45% fit](images/original/diapositiva-14.png)

## 2011: Watson

- Watson guanya a Jeopardy, un concurs de preguntes i respostes
- Va guanyar 1 milió de dòlars, que va donar a caritat.
- Watson és capaç de processar llenguatge natural i respondre preguntes.
- Va superar a dos dels millors jugadors de Jeopardy, que havien guanyat més de 3 milions de dòlars.

---

<!-- Diapositiva 15 del PDF original -->

<!-- _class: side -->

![bg right:45% fit](images/original/diapositiva-15.png)

## 2016: AlphaGo

- AlphaGo guanya a Lee Sedol, un dels millors jugadors de Go.
- El Go és un joc de tauler molt més complex que els escacs; fins aleshores, es considerava impossible de resoldre.
- El moviment 37 de la partida 2 va sorprendre a tots els experts. AlphaGo va fer un moviment mai vist i que va acabar guanyant la partida.

---

<!-- Diapositiva 16 del PDF original -->

<!-- _class: side -->

![bg right:45% fit](images/original/diapositiva-16.png)

## 2017: AlphaGo Zero

- AlphaGo Zero és capaç de jugar a Go sense cap mena d'informació sobre les regles.
- Apren a jugar a Go jugant contra si mateix.
- AlphaGo Zero va ser capaç de superar a AlphaGo amb només 3 dies d'entrenament.

---

<!-- Diapositiva 17 del PDF original -->

<!-- _class: side -->

![bg right:45% fit](images/original/diapositiva-17.png)

## 2020: GPT-3

- Forma part de la família de GPT-2, un model de llenguatge basat en xarxes neuronals.
- Algunes de les aplicacions de GPT-3:
  - Generar textos a partir d'un text d'entrada.
  - Traduir textos a un altre idioma.
  - Contestar preguntes.
  - Programar a partir de descripcions textuals.

---

<!-- Diapositiva 18 del PDF original -->

<!-- _class: side -->

![bg right:45% fit](images/original/diapositiva-18.png)

## 2021: DALL·E

- DALL·E és capaç de generar imatges a partir d'una descripció textual.
- Funciona de forma similar a GPT-3, però en comptes de generar text, genera imatges.
- Disposa d'una base de dades de 12GB d'imatges i textos.

---

<!-- Diapositiva 19 del PDF original -->

<!-- _class: side -->

![bg right:45% fit](images/original/diapositiva-19.png)

## 2022: GPT-4

- Al igual que GPT-3, GPT-4 és un model de llenguatge basat en l'arquitectura transformer.
- GPT-4 utilitza 10 bilions de paràmetres, 100 vegades més que GPT-3.
- És capaç de generar textos, imatges, codi, música, etc.

---

<!-- Diapositiva 20 del PDF original -->

<!-- _class: side -->

![bg right:45% fit](images/original/diapositiva-20.png)

## Situació actual

- Els avenços en IA són constants.
- La IA està present en molts aspectes de la nostra vida.
- És una tecnologia amb moltes aplicacions...
- ... amb molts riscos.
- ... i amb reptes ètics i morals per resoldre.

---

<!-- Diapositiva 21 del PDF original -->

## Mon laboral

- Els avenços en IA estan transformant el mercat laboral.
- La IA està substituint a humans en moltes tasques.
- Al mateix temps, la IA està creant nous llocs de treball.
- Aquest és un procés que no s'aturarà i, per tant, cal adaptar-se.
- Intentarem que aquest curs us ajudi a millorar la vostra ocupabilitat en aquest nou mercat laboral.

---

<!-- Diapositiva 22 del PDF original -->

<!-- _class: lead -->

![bg](images/original/diapositiva-22.png)

# Tenim ja una màquina intel·ligent?

---

<!-- Diapositiva 23 del PDF original -->

![bg](images/original/diapositiva-23.png)

## Intel·ligència humana (I)

- És una capacitat molt complexa, com a resultat de milions d'anys d'evolució.
- Alguns dels aspectes de la intel·ligència humana:
  - Aprendre
  - Resoldre problemes
  - Adaptar-se a nous entorns
  - Prendre decisions
  - Comunicar-se i col·laborar amb altres humans
  - Sentir emocions

---

<!-- Diapositiva 24 del PDF original -->

## Intel·ligència humana (II)

- La intel·ligència humana és molt més que la suma de les seves parts.
- Encara sabem molt poc sobre com funciona.
- Turing va proposar que és el resultat de la interacció entre molts processos simples.
- Aquesta és la idea que ha inspirat el disseny de molts algoritmes d'IA.
- Però, **és suficient per a crear una màquina intel·ligent**?

---

<!-- Diapositiva 25 del PDF original -->

<!-- _class: side -->

![bg right:45% fit](images/original/diapositiva-25.png)

## Intel·ligència computacional

- *La intel·ligència artificial intenta entendre i modelar la intel·ligència humana com a un procés computacional.*
- Així, intentem construir sistemes **la computació dels quals** aconsegueixi o s'aproximi a una noció desitjada d' intel·ligència.
- Per tant, la IA és part de la **Ciència de la Computació**.

---

<!-- Diapositiva 26 del PDF original -->

## I. computacional vs. I. humana

| Intel·ligència humana | Intel·ligència computacional |
| --- | --- |
| Biològica | Computacional |
| General | Específica |
| Conscient | Inconscient |
| Emocional | Racional |
| Adaptativa | Estàtica |
| Evolutiva | Dissenyada |

---

<!-- Diapositiva 27 del PDF original -->

## Tipus d'intel·ligència artificial

- **IA feble**: La IA és capaç de superar a humans en tasques específiques.
  - No significa que no siga potent.
  - Alguns experts prefireixen el nom **IA estreta**
- **IA forta**: La IA és capaç de superar a humans en tasques generals.
  - També es coneix com **IA general** o **AGI** (artificial general intelligence).
  - Es comportaria com un humà en qualsevol situació, generalitzant el seu coneixement.
  - No existeix encara (tal vegada per sort - singularitat tecnològica).

---

<!-- Diapositiva 28 del PDF original -->

<!-- _class: lead -->

![bg](images/original/diapositiva-28.png)

# Racionalitat

---

<!-- Diapositiva 29 del PDF original -->

- Els humans *no sempre prenen les millors decisions*; l'IA pot ajudar-nos en aquestes tasques.
- **Però, què és una decisió racional?**
  - Una decisió racional és aquella que **maximitza la probabilitat** d'aconseguir un objectiu.
  - Per tant, entendrem que una màquina **intel·ligent** és aquella que **pren decisions racionals**.

---

<!-- Diapositiva 30 del PDF original -->

<!-- _class: lead -->

![bg](images/original/diapositiva-30.png)

# Paradigmes de la IA

---

<!-- Diapositiva 31 del PDF original -->

<!-- _class: side -->

![bg right:45% fit](images/original/diapositiva-31.png)

## Definicions

- **Paradigma**: Enfoca la resolució de problemes des d'un punt de vista concret.
- **Paradigma de la IA**: Model o patró que serveix de referència per a imitar-lo o copiar-lo en el disseny de sistemes intel·ligents.

---

<!-- Diapositiva 32 del PDF original -->

<!-- _class: side -->

![bg right:45% fit](images/original/diapositiva-32.png)

## Paradigma simbòlic

- **Símbol**: Representació de la realitat.
- El paradigma simbòlic està basat en l'ús de símbols per a representar coneixement.
- Els símbols poden ser manipulats per a inferir noves conclusions.
- La intel·ligència és el resultat de la manipulació de símbols.
- Utilitats: **Sistemes experts**, **sistemes basats en regles**, **sistemes basats en casos**, etc.

---

<!-- Diapositiva 33 del PDF original -->

<!-- _class: side -->

![bg right:45% fit](images/original/diapositiva-33.png)

## Paradigma connexionista

- El paradigma connexionista està basat en la **simulació de xarxes neuronals**.
- Les xarxes neuronals són un model computacional que intenta imitar el funcionament del cervell humà.
- La intel·ligència és el resultat de la interacció entre molts processos simples.
- Utilitats: **Xarxes neuronals**, **sistemes basats en aprenentatge**, etc.

---

<!-- Diapositiva 34 del PDF original -->

<!-- _class: side -->

![bg right:45% fit](images/original/diapositiva-34.png)

## Paradigma estadístic

- El paradigma estadístic està basat en l'**anàlisi estadística**.
- La intel·ligència és el resultat de l'anàlisi de grans quantitats de dades.
- Els sistemes basats en aquest paradigma són capaços d'**aprendre** a partir de dades.
- Utilitats: **sistemes de recomanació**, **processament de llenguatge natural**, etc.

---

<!-- Diapositiva 35 del PDF original -->

<!-- _class: lead -->

![bg](images/original/diapositiva-35.png)

# Tècniques de la IA

---

<!-- Diapositiva 36 del PDF original -->

## Definicions

- **Técnica**: Conjunt de procediments o recursos que s'han d'aplicar per a aconseguir un objectiu.
- **Tècniques de la IA**: Conjunt de tècniques, algorismes i mètodes que s'apliquen per a resoldre problemes d'IA.
- Combinant diferents paradigmes, podem obtenir **diferents tècniques**.

---

<!-- Diapositiva 37 del PDF original -->

## Tècniques de la IA

- Algunes de les tècniques més utilitzades són:
  - **Sistemes experts**
  - **Xarxes neuronals**
  - **Algorismes genètics**
  - **Sistemes multiagent**
  - **Algorismes de cerca**
  - **Algorismes de planificació**
  - **Algorismes d'aprenentatge**

---

<!-- Diapositiva 38 del PDF original -->

<!-- _class: side -->

![bg right:45% fit](images/original/diapositiva-38.png)

## Sistemes experts

- Un sistema expert és un sistema que utilitza coneixement expert per a resoldre problemes.
- El coneixement expert és el coneixement que té un expert en un domini concret.
- Permiten automatitzar tasques que requeririen l'ajuda d'un expert.

---

<!-- Diapositiva 39 del PDF original -->

## Sistemes experts (II)

### Sistemes basats en casos

- S'intenta resoldre un problema a partir de casos similars resolts anteriorment.
- Es recuperen casos similars i s'adapten a la nova situació.
- Una vegada solucionat el problema, el cas es guarda per a utilitzar-lo en el futur.
- D'aquesta forma, el sistema va aprenent a resoldre problemes més complexos.
- Camps d'aplicació: **Medicina**, **enginyeria**, **disseny**, etc.

---

<!-- Diapositiva 40 del PDF original -->

## Sistemes experts (III)

### Sistemes basats en regles

- Es defineixen regles que representen coneixement.
- Les regles seran definides per humans experts en el domini.
- El sistema inferirà noves regles a partir de les regles existents.
- Útils en dominis on falten experts.
- Camps d'aplicació: **Diagnòstic mèdic**, **control de processos**, **sistemes de recomanació**, etc.

---

<!-- Diapositiva 41 del PDF original -->

## Sistemes experts (IV)

### Sistemes basats en lògica difusa

- Útils per a representar coneixement amb incertesa.
- Cada regla té un grau de certesa i es pot aplicar parcialment.
- Permeten definir regles amb vocabulari semblant al dels humans: "molt", "poc", "bastant", etc.
- Camps d'aplicació: **Robòtica**, **control de processos**, **sistemes de recomanació**, etc.

---

<!-- Diapositiva 42 del PDF original -->

<!-- _class: side compact -->

![bg right:45% fit](images/original/diapositiva-42.png)

## Xarxes neuronals

- Les xarxes neuronals són un model computacional que intenta imitar el funcionament del cervell humà.
- Diferents capes de neurones (nodes) interconnectades mijançant sinapsis (arcs) amb pesos.
- Les neurones s'activen en funció de les neurones de la capa anterior.
- Una capa d'entrada, una capa de sortida i podem tenir capes ocultes.
- Poden ser utilitzades per a resoldre problemes de classificació, regressió, etc.

---

<!-- Diapositiva 43 del PDF original -->

## Tipus de xarxes neuronals

- **Perceptrons**: Les xarxes neuronals més simples.
- **Xarxes neuronals profundes**: Xarxes neuronals amb múltiples capes ocultes.
- **Xarxes neuronals recurrents**: Xarxes neuronals amb connexions cícliques.
- **Xarxes neuronals convolucionals**: Xarxes neuronals amb capes convolucionals (filtres).

---

<!-- Diapositiva 44 del PDF original -->

<!-- _class: side -->

![bg right:45% fit](images/original/diapositiva-44.png)

## Algorismes genètics

- Els algorismes genètics són una tècnica d'**optimització** basada en la teoria de l'evolució de Darwin.
- Es tracta de generar una població d'individus i aplicar-los operadors genètics.
- Els individus més aptes (**els més ben adaptats al seu entorn**) tenen més probabilitats de reproduir-se.
- Útils per a resoldre problemes d'**optimització i de cerca**.

---

<!-- Diapositiva 45 del PDF original -->

<!-- _class: side -->

![bg right:45% fit](images/original/diapositiva-45.png)

## Sistemes multiagent

- Un sistema multiagent és un sistema compost per diversos agents que interactuen entre ells.
- Un agent és un sistema computacional que actua en un entorn.
- Els agents poden ser **reactius**, **deliberatius** o **socials**.
- Útils per a resoldre problemes de **planificació**, **disseny**, **control**, etc.

---

<!-- Diapositiva 46 del PDF original -->

<!-- _class: side compact -->

![bg right:45% fit](images/original/diapositiva-46.png)

## Algorismes de cerca

- Un algorisme de cerca és un algorisme que permet trobar una solució a un problema.
- Els algorismes de cerca més utilitzats són:
  - **Cerca no informada**: Cerca en amplada, cerca en profunditat, cerca en profunditat limitada, cerca en profunditat iterativa, cerca bidireccional, etc.
  - **Cerca informada**: Cerca per avarícia, cerca de cost uniforme, cerca en profunditat limitada, cerca en profunditat iterativa, cerca bidireccional, etc.
- Útils per a resoldre problemes de **planificació**, **disseny**, **control**, etc.

---

<!-- Diapositiva 47 del PDF original -->

<!-- _class: side compact -->

![bg right:45% fit](images/original/diapositiva-47.png)

## Algorismes d'aprenentatge

- Un algorisme d'aprenentatge és un algorisme que permet aprendre a partir de dades.
- Els algorismes d'aprenentatge més utilitzats són:
  - **Aprenentatge supervisat**: Classificació, regressió, etc.
  - **Aprenentatge no supervisat**: Clustering, etc.
  - **Aprenentatge per reforç**: Q-learning, etc.

---

<!-- Diapositiva 48 del PDF original -->

<!-- _class: lead -->

![bg](images/original/diapositiva-48.png)

# Aplicacions de la IA

---

<!-- Diapositiva 49 del PDF original -->

<!-- _class: side -->

![bg right:45% fit](images/original/diapositiva-49.png)

## Robòtica

- La robòtica és una de les aplicacions més conegudes de la IA.
- La robòtica és la ciència i la tecnologia de robots.
- Un robot és un sistema capaç d'interactuar amb el seu entorn.
- Els robots poden ser **autònoms** o **teleoperats**.
- Camps d'aplicació: **Indústria**, **sanitat**, **exploració espacial**, **militar**, **domèstic**, etc.

---

<!-- Diapositiva 50 del PDF original -->

<!-- _class: side -->

![bg right:45% fit](images/original/diapositiva-50.png)

## Processament de llenguatge natural

- Acumula molt del desenvolupament de la IA.
- El processament de llenguatge natural és la capacitat d'un ordinador per a entendre el llenguatge humà.
- Els humans utilitzem el llenguatge per a comunicar-nos i per a transmetre coneixement.
- Camps d'aplicació: **Traducció automàtica**, **reconeixement de veu**, **resum de textos**, **chatbots**, etc.

---

<!-- Diapositiva 51 del PDF original -->

<!-- _class: side compact -->

![bg right:45% fit](images/original/diapositiva-51.png)

## Visió per computador

- La visió per computador és la capacitat d'un ordinador per a entendre imatges.
- Els humans utilitzem la visió per a entendre el món que ens envolta.
- Ens permet identificar objectes, persones, colors, etc.
- Camps d'aplicació: **Reconeixement facial**, **reconeixement d'objectes**, **reconstrucció 3D**, **reconstrucció de models**, **reconstrucció de paisatges**, **reconstrucció de monuments**, etc.

---

<!-- Diapositiva 52 del PDF original -->

<!-- _class: side compact -->

![bg right:45% fit](images/original/diapositiva-52.png)

## Sistemes de recomanació

- Un sistema de recomanació és un sistema que recomana un conjunt d'elements a un usuari.
- Els humans utilitzem la recomanació per a prendre decisions.
- L'accés a grans quantitats de dades ha fet que els sistemes de recomanació siguin cada vegada més importants.
- Camps d'aplicació: **Recomanació de productes**, **recomanació de música**, **recomanació de pel·lícules**, **recomanació de llibres**, **recomanació de notícies**, etc.

---

<!-- Diapositiva 53 del PDF original -->

<!-- _class: side -->

![bg right:45% fit](images/original/diapositiva-53.png)

## Jocs

- Els jocs ens serveixen per a entendre la intel·ligència.
- Els humans utilitzem els jocs per a aprendre, per a divertir-nos i per a competir.
- El tindre molts sistemes prenent decisions en un entorn controlat els fa ser un bon banc de proves per a la IA.
- Camps d'aplicació: **Jocs de tauler**, **jocs de cartes**, **jocs de rol**, **jocs d'estratègia**, **etc**.

---

<!-- Diapositiva 54 del PDF original -->

## Altres aplicacions

- **Medicina**: Diagnòstic mèdic, cirugia, medicina personalitzada.
- **Enginyeria**: Disseny, control de processos.
- **Finances**: Predicció de mercats, recomanació d'inversions.
- **Militar**: Drones, armes autònomes.
- **Domèstic**: Robots, assistents virtuals, domòtica.
- **Transport**: Vehicles autònoms, planificació de rutes.

---

<!-- Diapositiva 55 del PDF original -->

## Referències

- [Artificial Intelligence: A Modern Approach](http://aima.cs.berkeley.edu/)
- [Artificial Intelligence: Foundations of Computational Agents](http://artint.info/2e/html/ArtInt2e.html)
- [Deep Learning](https://www.deeplearningbook.org/)
- [Machine Learning](https://www.cs.ubc.ca/~murphyk/MLbook/)
- [Fast.ai](https://www.fast.ai/)
