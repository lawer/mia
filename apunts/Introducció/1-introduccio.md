autoscale: true
footer: Carles Gonzàlez
slidenumbers: true

## 1. Introducció a la intel·ligència artificial

### Models d'intel·ligència artificial

![](images/portada.png)

---

# Què és la intel·ligència artificial?

|                               |                                                                                                                                                       |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Intel·ligència**            | La intel·ligència és la capacitat d'aprendre, comprendre i resoldre problemes.                                                                        |
| **Intel·ligència artificial** | La intel·ligència artificial és la inteligència exhibida per màquines.                                                                                |
| **Màquina intel·ligent**      | Una màquina intel·ligent és un sistema que pot percebre el seu entorn i prendre accions que maximitzen les seves possibilitats d'èxit en un objectiu. |

---

## Agents intel·ligents (I)

* Un **agent** percep el seu entorn mitjançant **sensors** i actua sobre ell mitjançant **actuadors**.
* Un **agent intel·ligent** és un agent que actua de forma intel·ligent. 
  * **Actuar de forma intel·ligent**: Actuar de forma que maximitza les seves possibilitats d'èxit en un objectiu.
  * **Objectiu**: Una funció que mesura el rendiment de l'agent en un entorn.

![right fit 100%](images%2Fwhat-is-the-composition-for-agents-in-artificial-intelligence.png)

---

## Agents intel·ligents (II)

* L'assignatura tracta sobre la **construcció d'agents intel·ligents**.
* Veurem: 
  * Diferents **tècniques** per a construir agents intel·ligents. 
  * Els seus **avantatges i inconvenients**.
  * Els seus **camps d'aplicació**.
  * Els seus **riscos i reptes ètics**.

![right ](images%2F0%20Yf3CJXTzM1sKyKOa.jpg)

---

# Una mica d'història

![](images/History.jpg)

---

## 1950: Alan Turing

![right](images%2Falan-mathison-turing_d8b50689.jpg)

* La prova de Turing és una proposta de test per a la intel·ligència d'una màquina
* La va proposar Alan Turing el 1950 en el seu article _"Computing Machinery and Intelligence"_.

* L'objectiu de la prova és determinar _si una màquina pot pensar_.

---

### El test

* Un humà, aïllat en una habitació, ha de mantenir una conversa escrita amb **dues persones, una
  humana i una màquina**.

* Si l'humà _no pot distingir_ entre les dues, la màquina es **considera que pensa**.

![right](images%2Fturing_test.png)

---

### La pregunta de Turing

|                                                          |                                                                                                                                                                                                                                                           |
|:--------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
|             **Poden pensar les màquines?**:              |                         _La pregunta de si les màquines poden pensar és massa vaga, i hauria de ser reemplaçada per una altra pregunta que pugui ser contestada per mitjà d'un sí o un no, que tingui una significació precisa._                          |
| **Poden les màquines fer el que els humans poden fer?**: | Aquesta nova pregunta té l'avantatge que és possible contestar-la definitivament i que molts arguments que s'han fet per contestar la pregunta original poden ser reutilitzats.                                                                        __ |

---

## 1956 - 1974: Els inicis

* **1956**: _John McCarthy_ - La conferència de Dartmouth. El naixement de la IA.
* **1957**: _Herbert Simon_ - "En 10 anys el campió mundial d'escacs serà una màquina"
* **1958**: _Frank Rosenblatt_ - El perceptró
* **1967**: _Marvin Minsky_ - "En una generació, el problema de la IA estarà resolt"

![right](images%2F1%20tVuiuwvFXtByodoO1B46CQ.png)

---

## 1974 - 1993: Hi ha esperança?

* **1974-1980**: Pocs avenços, desencantament i crisi de finançament (AI Winter)
* **Principis dels 80**: Apareixen els sistemes experts
* **1982 - 1992**: Projecte Japonès de la 5a generació
* **1987-1993**: Els sistemes experts fracassen. (II AI Winter)

![right](images%2FIMG_0430.JPG.2a37776a69d98ce7cf1794fdb15c4083.png)

---

## 1997: Deep Blue

* Deep Blue guanya a Kasparov, el campió mundial d'escacs.
* Els sistemes experts són capaços de superar a humans en tasques específiques.
* Després de la victòria, IBM desmantella el projecte.
* **Els sistemes experts no són capaços de superar a humans en tasques generals.**

![right](images%2FDeepBlue.png)

---

## 2002: Roomba

* Roomba va ser el primer robot domèstic comercialitzat.
* És capaç de netejar una habitació sense cap mena d'ajuda humana.
* Detecta obstacles i els evita, i torna a la seva base quan s'acaba la bateria.
* **El 2017, Roomba va vendre més de 20 milions d'unitats.**

![right](images%2Firobot-roomba-692-2332085.png)

---

## 2005: DARPA Grand Challenge

* Després de 4 anys de preparació, el 2004 es va celebrar la primera edició del DARPA Grand Challenge.
* Els participants havien de construir un vehicle autònom capaç de recórrer 240 km per un terreny desèrtic.
* Els vehicles havien de ser capaços de prendre decisions sense cap mena d'ajuda humana.
* Els 15 equips participants no van ser capaços de completar el recorregut.
* **El 2005, 5 equips van completar el recorregut**.

![right](images/darpa.png)

---

## 2011: Watson

* Watson guanya a Jeopardy, un concurs de preguntes i respostes
* Va guanyar 1 milió de dòlars, que va donar a caritat.
* Watson és capaç de processar llenguatge natural i respondre preguntes.
* Va superar a dos dels millors jugadors de Jeopardy, que havien guanyat més de 3 milions de dòlars.

![right](images%2Fwatson31.png)

---

## 2016: AlphaGo

* AlphaGo guanya a Lee Sedol, un dels millors jugadors de Go.
* El Go és un joc de tauler molt més complex que els escacs; fins aleshores, es considerava impossible de resoldre.
* El moviment 37 de la partida 2 va sorprendre a tots els experts. AlphaGo va fer un moviment mai vist i que va acabar
  guanyant la partida.

![right](images%2F2908.png)

---

## 2017: AlphaGo Zero

* AlphaGo Zero és capaç de jugar a Go sense cap mena d'informació sobre les regles.
* Apren a jugar a Go jugant contra si mateix.
* AlphaGo Zero va ser capaç de superar a AlphaGo amb només 3 dies d'entrenament.

![right](images%2F1%20m_phP_gghFLtbXnV2tQaog.png)

---

## 2020: GPT-3

* Forma part de la família de GPT-2, un model de llenguatge basat en xarxes neuronals.
* Algunes de les aplicacions de GPT-3:
    * Generar textos a partir d'un text d'entrada.
    * Traduir textos a un altre idioma.
    * Contestar preguntes.
    * Programar a partir de descripcions textuals.

![right](images%2FNew-Version-of-GPT-3-A-Game-Changing-Language-Model-by-Open-A.jpg)

---

## 2021: DALL·E

* DALL·E és capaç de generar imatges a partir d'una descripció textual.
* Funciona de forma similar a GPT-3, però en comptes de generar text, genera imatges.
* Disposa d'una base de dades de 12GB d'imatges i textos.

![right](images%2Ftrump-863x570.png)

---

## 2022: GPT-4

* Al igual que GPT-3, GPT-4 és un model de llenguatge basat en l'arquitectura transformer.
* GPT-4 utilitza 10 bilions de paràmetres, 100 vegades més que GPT-3.
* És capaç de generar textos, imatges, codi, música, etc.

![right](images%2FGPT-4-768x427.jpg)

---

## Situació actual

![right](images%2FState%20of%20AI.png)

* Els avenços en IA són constants.
* La IA està present en molts aspectes de la nostra vida.
* És una tecnologia amb moltes aplicacions...
* ... amb molts riscos.
* ... i amb reptes ètics i morals per resoldre.

---

## Mon laboral

* Els avenços en IA estan transformant el mercat laboral.
* La IA està substituint a humans en moltes tasques.
* Al mateix temps, la IA està creant nous llocs de treball.
* Aquest és un procés que no s'aturarà i, per tant, cal adaptar-se.
* Intentarem que aquest curs us ajudi a millorar la vostra ocupabilitat en aquest nou mercat laboral.

---

# Tenim ja una màquina intel·ligent?

![](images%2F8860931.jpg)

---

## Intel·ligència humana (I)

* És una capacitat molt complexa, com a resultat de milions d'anys d'evolució.
* Alguns dels aspectes de la intel·ligència humana:
    * Aprendre
    * Resoldre problemes
    * Adaptar-se a nous entorns
    * Prendre decisions
    * Comunicar-se i col·laborar amb altres humans
    * Sentir emocions

![](images%2Fp04fm4sp.png)

---

## Intel·ligència humana (II)

* La intel·ligència humana és molt més que la suma de les seves parts.
* Encara sabem molt poc sobre com funciona.
* Turing va proposar que és el resultat de la interacció entre molts processos simples.
* Aquesta és la idea que ha inspirat el disseny de molts algoritmes d'IA.
* Però, **és suficient per a crear una màquina intel·ligent**?

---

## Intel·ligència computacional

![right](images%2Finteligencia-computacional-1.jpg)

* _La intel·ligència artificial intenta entendre i modelar la intel·ligència humana com a un procés computacional._
* Així, intentem construir sistemes **la computació dels quals** aconsegueixi o s'aproximi a una noció desitjada d'
  intel·ligència.
* Per tant, la IA és part de la **Ciència de la Computació**.

---

## I. computacional vs. I. humana

| Intel·ligència humana | Intel·ligència computacional |
|-----------------------|------------------------------|
| Biològica             | Computacional                |
| General               | Específica                   |
| Conscient             | Inconscient                  |
| Emocional             | Racional                     |
| Adaptativa            | Estàtica                     |
| Evolutiva             | Dissenyada                   |

---

## Tipus d'intel·ligència artificial

* **IA feble**: La IA és capaç de superar a humans en tasques específiques.
  * No significa que no siga potent.
  * Alguns experts prefireixen el nom **IA estreta**
* **IA forta**: La IA és capaç de superar a humans en tasques generals.
  * També es coneix com **IA general** o **AGI** (artificial general intelligence).
  * Es comportaria com un humà en qualsevol situació, generalitzant el seu coneixement.
  * No existeix encara (tal vegada per sort - singularitat tecnològica).

---

## [fit] Racionalitat

![](images%2F98a0e0963f9ad65083de_808xFull.png)

---
          
* Els humans _no sempre prenen les millors decisions_; l'IA pot ajudar-nos en aquestes tasques.
* **Però, què és una decisió racional?**
    * Una decisió racional és aquella que **maximitza la probabilitat** d'aconseguir un objectiu.
    * Per tant, entendrem que una màquina **intel·ligent** és aquella que **pren decisions racionals**.

---

# Paradigmes de la IA

![](images%2FThinkstockPhotos-801680832.jpg)

---

## Definicions

* **Paradigma**: Enfoca la resolució de problemes des d'un punt de vista concret.
* **Paradigma de la IA**: Model o patró que serveix de referència per a imitar-lo o copiar-lo en el disseny de sistemes
  intel·ligents.

![right](images%2Fnoun-algorithm-4894723.png)

---

## Paradigma simbòlic

* **Símbol**: Representació de la realitat.
* El paradigma simbòlic està basat en l'ús de símbols per a representar coneixement.
* Els símbols poden ser manipulats per a inferir noves conclusions.
* La intel·ligència és el resultat de la manipulació de símbols.
* Utilitats: **Sistemes experts**, **sistemes basats en regles**, **sistemes basats en casos**, etc.

![right](..%2F..%2F..%2FDownloads%2Fdivisio-blog_illustrationen_Entscheidungsbaum-Beispiel-1-1024x1024.webp)

---

## Paradigma connexionista

* El paradigma connexionista està basat en la **simulació de xarxes neuronals**.
* Les xarxes neuronals són un model computacional que intenta imitar el funcionament del cervell humà.
* La intel·ligència és el resultat de la interacció entre molts processos simples.
* Utilitats: **Xarxes neuronals**, **sistemes basats en aprenentatge**, etc.

![right](images%2Fxarxa_neuronal.png)

---


## Paradigma estadístic

* El paradigma estadístic està basat en l'**anàlisi estadística**.
* La intel·ligència és el resultat de l'anàlisi de grans quantitats de dades.
* Els sistemes basats en aquest paradigma són capaços d'**aprendre** a partir de dades.
* Utilitats: **sistemes de recomanació**, **processament de llenguatge natural**, etc.

![right](..%2F..%2F..%2FDownloads%2F0%20oPJfynmi4gRfBws1.png)

---

# Tècniques de la IA
![](images%2FRule-based-vs-Machine-Learning-upd-1-1536x799.png)

---

## Definicions

* **Técnica**: Conjunt de procediments o recursos que s'han d'aplicar per a aconseguir un objectiu.
* **Tècniques de la IA**: Conjunt de tècniques, algorismes i mètodes que s'apliquen per a resoldre problemes d'IA.
* Combinant diferents paradigmes, podem obtenir **diferents tècniques**.

---

## Tècniques de la IA

* Algunes de les tècniques més utilitzades són:
    * **Sistemes experts**
    * **Xarxes neuronals**
    * **Algorismes genètics**
    * **Sistemes multiagent**
    * **Algorismes de cerca**
    * **Algorismes de planificació**
    * **Algorismes d'aprenentatge**

---


## Sistemes experts

* Un sistema expert és un sistema que utilitza coneixement expert per a resoldre problemes.
* El coneixement expert és el coneixement que té un expert en un domini concret.
* Permiten automatitzar tasques que requeririen l'ajuda d'un expert.

![right](images%2Fsistema%20expert.png)

---

## Sistemes experts (II)

### Sistemes basats en casos

* S'intenta resoldre un problema a partir de casos similars resolts anteriorment.
* Es recuperen casos similars i s'adapten a la nova situació.
* Una vegada solucionat el problema, el cas es guarda per a utilitzar-lo en el futur.
* D'aquesta forma, el sistema va aprenent a resoldre problemes més complexos.
* Camps d'aplicació: **Medicina**, **enginyeria**, **disseny**, etc.

---

## Sistemes experts (III)
### Sistemes basats en regles

* Es defineixen regles que representen coneixement.
* Les regles seran definides per humans experts en el domini.
* El sistema inferirà noves regles a partir de les regles existents.
* Útils en dominis on falten experts.
* Camps d'aplicació: **Diagnòstic mèdic**, **control de processos**, **sistemes de recomanació**, etc.

---

## Sistemes experts (IV)
### Sistemes basats en lògica difusa

* Útils per a representar coneixement amb incertesa.
* Cada regla té un grau de certesa i es pot aplicar parcialment.
* Permeten definir regles amb vocabulari semblant al dels humans: "molt", "poc", "bastant", etc.
* Camps d'aplicació: **Robòtica**, **control de processos**, **sistemes de recomanació**, etc.

---

## Xarxes neuronals

* Les xarxes neuronals són un model computacional que intenta imitar el funcionament del cervell humà.
* Diferents capes de neurones (nodes) interconnectades mijançant sinapsis (arcs) amb pesos.
* Les neurones s'activen en funció de les neurones de la capa anterior.
* Una capa d'entrada, una capa de sortida i podem tenir capes ocultes.
* Poden ser utilitzades per a resoldre problemes de classificació, regressió, etc.

![right](images%2Ftypes-of-artificial-neural-networks.jpg)

---

### Tipus de xarxes neuronals

* **Perceptrons**: Les xarxes neuronals més simples.
* **Xarxes neuronals profundes**: Xarxes neuronals amb múltiples capes ocultes.
* **Xarxes neuronals recurrents**: Xarxes neuronals amb connexions cícliques.
* **Xarxes neuronals convolucionals**: Xarxes neuronals amb capes convolucionals (filtres). 

---

## Algorismes genètics

* Els algorismes genètics són una tècnica d'**optimització** basada en la teoria de l'evolució de Darwin.
* Es tracta de generar una població d'individus i aplicar-los operadors genètics.
* Els individus més aptes (**els més ben adaptats al seu entorn**) tenen més probabilitats de reproduir-se.
* Útils per a resoldre problemes d'**optimització i de cerca**.

![right](images%2Fgenetic.png)

---

## Sistemes multiagent

* Un sistema multiagent és un sistema compost per diversos agents que interactuen entre ells.
* Un agent és un sistema computacional que actua en un entorn.
* Els agents poden ser **reactius**, **deliberatius** o **socials**.
* Útils per a resoldre problemes de **planificació**, **disseny**, **control**, etc.

![right](images%2Ffile159604.jpg)

---

## Algorismes de cerca

* Un algorisme de cerca és un algorisme que permet trobar una solució a un problema.
* Els algorismes de cerca més utilitzats són:
    * **Cerca no informada**: Cerca en amplada, cerca en profunditat, cerca en profunditat limitada, cerca en
      profunditat iterativa, cerca bidireccional, etc.
    * **Cerca informada**: Cerca per avarícia, cerca de cost uniforme, cerca en profunditat limitada, cerca en
      profunditat iterativa, cerca bidireccional, etc.
* Útils per a resoldre problemes de **planificació**, **disseny**, **control**, etc.

![right](images%2FA-Star-Search-Algorithm.png)

---

## Algorismes d'aprenentatge

* Un algorisme d'aprenentatge és un algorisme que permet aprendre a partir de dades.
* Els algorismes d'aprenentatge més utilitzats són:
    * **Aprenentatge supervisat**: Classificació, regressió, etc.
    * **Aprenentatge no supervisat**: Clustering, etc.
    * **Aprenentatge per reforç**: Q-learning, etc.

![right](images%2FE3ybEzqXEAAlaKM.jpg)

---

# Aplicacions de la IA

![How_Artificial_Intelligence_is_Being_Deployed_Today.png](images%2FHow_Artificial_Intelligence_is_Being_Deployed_Today.png)

---

## Robòtica

* La robòtica és una de les aplicacions més conegudes de la IA.
* La robòtica és la ciència i la tecnologia de robots.
* Un robot és un sistema capaç d'interactuar amb el seu entorn.
* Els robots poden ser **autònoms** o **teleoperats**.
* Camps d'aplicació: **Indústria**, **sanitat**, **exploració espacial**, **militar**, **domèstic**, etc.

![right](images%2FFacebook-Robots-00.webp)

--- 

## Processament de llenguatge natural

* Acumula molt del desenvolupament de la IA.
* El processament de llenguatge natural és la capacitat d'un ordinador per a entendre el llenguatge humà.
* Els humans utilitzem el llenguatge per a comunicar-nos i per a transmetre coneixement.
* Camps d'aplicació: **Traducció automàtica**, **reconeixement de veu**, **resum de textos**, **chatbots**, etc.

![right](images%2Fcbfff140-d7b5-4c25-9541-fe249e75a217_media-libre-aspect-ratio_default_0.jpg)

---

## Visió per computador

* La visió per computador és la capacitat d'un ordinador per a entendre imatges.
* Els humans utilitzem la visió per a entendre el món que ens envolta.
* Ens permet identificar objectes, persones, colors, etc.
* Camps d'aplicació: **Reconeixement facial**, **reconeixement d'objectes**, **reconstrucció 3D**, **reconstrucció de
  models**, **reconstrucció de paisatges**, **reconstrucció de monuments**, etc.

![right](images%2FComputervision_banner.webp)

---

## Sistemes de recomanació

* Un sistema de recomanació és un sistema que recomana un conjunt d'elements a un usuari.
* Els humans utilitzem la recomanació per a prendre decisions.
* L'accés a grans quantitats de dades ha fet que els sistemes de recomanació siguin cada vegada més importants.
* Camps d'aplicació: **Recomanació de productes**, **recomanació de música**, **recomanació de pel·lícules**,
  **recomanació de llibres**, **recomanació de notícies**, etc.

![right fit](images%2Fimg-3.png)

---

## Jocs

* Els jocs ens serveixen per a entendre la intel·ligència.
* Els humans utilitzem els jocs per a aprendre, per a divertir-nos i per a competir.
* El tindre molts sistemes prenent decisions en un entorn controlat els fa ser un bon banc de proves per a la IA.
* Camps d'aplicació: **Jocs de tauler**, **jocs de cartes**, **jocs de rol**, **jocs d'estratègia**, **etc**.

![right fit](images%2F2825132-637490944552534550-16x9-1.jpg)

---

## Altres aplicacions

* **Medicina**: Diagnòstic mèdic, cirugia, medicina personalitzada.
* **Enginyeria**: Disseny, control de processos.
* **Finances**: Predicció de mercats, recomanació d'inversions.
* **Militar**: Drones, armes autònomes.
* **Domèstic**: Robots, assistents virtuals, domòtica.
* **Transport**: Vehicles autònoms, planificació de rutes.

---

# Referències

* [Artificial Intelligence: A Modern Approach](http://aima.cs.berkeley.edu/)
* [Artificial Intelligence: Foundations of Computational Agents](http://artint.info/2e/html/ArtInt2e.html)
* [Deep Learning](https://www.deeplearningbook.org/)
* [Machine Learning](https://www.cs.ubc.ca/~murphyk/MLbook/)
* [Fast.ai](https://www.fast.ai/)
