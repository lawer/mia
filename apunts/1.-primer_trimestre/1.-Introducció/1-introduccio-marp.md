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
  section p:has(a) { font-size: 16px; }
---

<!-- Transcripció del PDF original 1-introduccio.pdf: 55 diapositives.
Primera revisió conceptual: història, models, comparació humana/IA, racionalitat, regles, lògica difusa i cerca.
Es mantenen l’ordre i les 55 diapositives originals.
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

<<<<<<< HEAD
<!-- _class: lead -->

![bg](images/original/diapositiva-05.png)

# Una mica d'història
=======
- Com formular un problema perquè un sistema el puga resoldre.
- Diferents tècniques per construir agents intel·ligents.
- Avantatges, limitacions i costos de cada tècnica.
- Camps d'aplicació i impacte sobre les persones.
- Com triar entre famílies de tècniques i entendre'n les limitacions.
>>>>>>> 207e18b9b28f9ffea178f8a540286d47fe1a7e43

---

<!-- Diapositiva 6 del PDF original -->

<!-- _class: side -->

![bg right:45% fit](images/original/diapositiva-06.png)

## 1950: Alan Turing

- Turing publica *Computing Machinery and Intelligence*.
- Proposa substituir «poden pensar les màquines?» pel **joc d’imitació**, una prova del comportament observable.
- La prova avalua la capacitat de conversar de manera semblant a una persona.
- Superar-la no demostra, per si sol, consciència o comprensió.

Font: [Turing (1950)](https://www.cse.msu.edu/~cse841/papers/Turing.html).

---

<!-- Diapositiva 7 del PDF original -->

<!-- _class: side -->

![bg right:45% fit](images/original/diapositiva-07.png)

## El test

- En la versió habitual, una persona conversa per escrit amb **un humà i una màquina**, sense veure’ls.
- Ha d’identificar quin interlocutor és la màquina a partir de les respostes.
- El resultat depén de les preguntes, el temps i les condicions de la prova.
- Imitar una conversa humana no equival a demostrar totes les capacitats intel·lectuals humanes.

Font: [Turing (1950)](https://www.cse.msu.edu/~cse841/papers/Turing.html).

---

<!-- Diapositiva 8 del PDF original -->

## La pregunta de Turing

- **Pregunta inicial:** «Poden pensar les màquines?»
- **Dificultat:** no hi ha una definició única i operativa de «pensar».
- **Proposta:** estudiar si una màquina pot participar amb èxit en el joc d’imitació.
- **Abast:** és un criteri de comportament en una situació concreta, no una prova general de consciència.

Aquest resum és una paràfrasi de l’article, no una citació literal.

Font: [Turing (1950), apartats 1 i 6](https://www.cse.msu.edu/~cse841/papers/Turing.html).

---

<!-- Diapositiva 9 del PDF original -->

<!-- _class: side -->

![bg right:45% fit](images/original/diapositiva-09.png)

## 1955–1974: Els inicis

- **1955:** McCarthy i col·laboradors utilitzen el terme *intel·ligència artificial* en la proposta de Dartmouth.
- **1956:** se celebra la trobada de Dartmouth.
- **1958:** Rosenblatt publica el seu treball sobre el perceptró, un model que aprén a classificar.
- Les primeres demostracions generen expectatives que superen les capacitats dels sistemes de l’època.

Fonts: [Dartmouth (1955)](https://www-formal.stanford.edu/jmc/history/dartmouth/dartmouth.html), [Rosenblatt (1958)](https://www.cs.cmu.edu/~epxing/Class/10715/reading/Rosenblatt.perceptron.pdf).

---

<!-- Diapositiva 10 del PDF original -->

<!-- _class: side -->

![bg right:45% fit](images/original/diapositiva-10.png)

## 1974–1993: Expectatives i límits

- Els **hiverns de la IA** són períodes de desencantament i reducció del finançament.
- Als anys 80 creix l’ús comercial dels **sistemes experts**, amb antecedents com DENDRAL als anys 60.
- Recollir i mantenir el coneixement expert resulta costós.
- Les dificultats comercials no fan desaparèixer la recerca ni els sistemes basats en regles.

Font: [Història de DENDRAL i dels sistemes experts](https://softwarepreservation.computerhistory.org/AI/DENDRAL/).

---

<!-- Diapositiva 11 del PDF original -->

<!-- _class: side -->

![bg right:45% fit](images/original/diapositiva-11.png)

## 1997: Deep Blue

- Deep Blue, d’IBM, derrota el campió mundial Garri Kaspàrov en un matx d’escacs.
- Combina **cerca**, avaluació de posicions i maquinari especialitzat.
- Mostra que una màquina pot superar els millors humans en una tasca delimitada.
- Guanyar als escacs no demostra intel·ligència general.

Font: [IBM: Deep Blue](https://www.ibm.com/history/deep-blue).

---

<!-- Diapositiva 12 del PDF original -->

<!-- _class: side -->

![bg right:45% fit](images/original/diapositiva-12.png)

## 2002: Roomba

- iRobot llança Roomba el **2002** i contribueix a popularitzar els robots aspiradors domèstics.
- Combina sensors i accions per netejar el terra i reaccionar davant d’obstacles.
- L’autonomia no elimina el manteniment ni la preparació de l’entorn per part de l’usuari.
- Les funcions, com el retorn a la base o la creació de mapes, depenen del model i la generació.

Font: [Història d’iRobot](https://about.irobot.com/history).

---

<!-- Diapositiva 13 del PDF original -->

<!-- _class: side compact -->

![bg right:45% fit](images/original/diapositiva-13.png)

## 2004–2005: DARPA Grand Challenge

- El **2004**, 15 vehicles intenten recórrer autònomament una ruta desèrtica d’uns **229 km**.
- Cap vehicle completa el recorregut.
- El **2005**, cinc equips completen una nova ruta d’uns **212 km**.
- El repte impulsa la integració de percepció, planificació i control per a la conducció autònoma.

Fonts: [DARPA: 2004](https://www.darpa.mil/news/2014/grand-challenge-ten-years-later), [DARPA: 2005](https://www.darpa.mil/about/innovation-timeline/grand-challenge).

---

<!-- Diapositiva 14 del PDF original -->

<!-- _class: side -->

![bg right:45% fit](images/original/diapositiva-14.png)

## 2011: Watson

- Watson, d’IBM, guanya a **Ken Jennings i Brad Rutter** en una competició de *Jeopardy!*.
- Processa preguntes en llenguatge natural i busca possibles respostes.
- Combina evidències i estima la confiança de cada resposta.
- L’èxit en el concurs no implica que comprenga qualsevol situació com una persona.

Font: [IBM: Watson a Jeopardy!](https://www.ibm.com/history/watson-jeopardy).

---

<!-- Diapositiva 15 del PDF original -->

<!-- _class: side -->

![bg right:45% fit](images/original/diapositiva-15.png)

## 2016: AlphaGo

- AlphaGo derrota **Lee Sedol per 4–1** en un matx de Go.
- Combina **xarxes neuronals, aprenentatge per reforç i cerca**.
- El moviment 37 de la segona partida exemplifica una jugada sorprenent per als experts.
- Assolir un nivell superhumà no significa haver resolt matemàticament el joc.

Font: [Google DeepMind: AlphaGo](https://deepmind.google/research/alphago/).

---

<!-- Diapositiva 16 del PDF original -->

<!-- _class: side -->

![bg right:45% fit](images/original/diapositiva-16.png)

## 2017: AlphaGo Zero

- Parteix de les **regles del Go**, sense entrenar-se amb partides humanes.
- Aprén jugant contra si mateix mitjançant **aprenentatge per reforç**.
- Combina una xarxa neuronal amb cerca per seleccionar jugades.
- Després de tres dies d’entrenament, supera per **100–0** la versió d’AlphaGo que havia derrotat Lee Sedol.

Font: [Silver i Hassabis (2017)](https://deepmind.google/blog/alphago-zero-starting-from-scratch/).

---

<!-- Diapositiva 17 del PDF original -->

<!-- _class: side -->

![bg right:45% fit](images/original/diapositiva-17.png)

## 2020: GPT-3

- Model de llenguatge **autoregressiu** de la família GPT, basat en Transformers.
- La versió més gran presentada té **175.000 milions de paràmetres**.
- Genera text predient el token següent a partir del context.
- Pot fer tasques com traducció i resposta a preguntes amb instruccions i exemples dins del context, sense actualitzar els pesos.

Font: [Brown i col·laboradors (2020)](https://arxiv.org/abs/2005.14165).

---

<!-- Diapositiva 18 del PDF original -->

<!-- _class: side -->

![bg right:45% fit](images/original/diapositiva-18.png)

## 2021: DALL·E

- El primer DALL·E genera imatges a partir de descripcions textuals.
- Utilitza un Transformer que modela seqüències de tokens de text i d’imatge.
- El model té **12.000 milions de paràmetres**: aquesta xifra no és la mida d’una base de dades en GB.
- S’entrena amb parelles de text i imatge.

Font: [Ramesh i col·laboradors (2021)](https://arxiv.org/abs/2102.12092).

---

<!-- Diapositiva 19 del PDF original -->

<!-- _class: side -->

![bg right:45% fit](images/original/diapositiva-19.png)

## 2023: GPT-4

- L’informe de 2023 presenta un model basat en **Transformers** que accepta text i imatges i produeix **text**.
- Pot generar explicacions, resums i codi; això no equival a generar directament imatges o àudio.
- L’informe no publica el nombre de paràmetres.
- Pot produir errors i informació inventada, encara que la resposta semble convincent.

Font: [Informe tècnic de GPT-4 (2023)](https://arxiv.org/abs/2303.08774).

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

## Intel·ligència humana i artificial

| Aspecte | Persones | Sistemes d’IA |
| --- | --- | --- |
| Aprenentatge | Experiència, cos i interacció social | Dades, regles i interacció, segons el sistema |
| Adaptació | Transferència entre contextos | Variable; cal avaluar-la en cada tasca |
| Decisions | Raonament, emocions i biaixos | Objectius definits, aproximacions i biaixos |
| Limitacions | Errors i recursos limitats | Errors i dependència del disseny i les dades |

El rendiment observable no demostra, per si sol, consciència o experiència subjectiva.

---

<!-- Diapositiva 27 del PDF original -->

## IA estreta, IA general i IA forta

- **IA estreta:** especialitzada en tasques o dominis delimitats; pot superar el rendiment humà en aquests àmbits.
- **IA general (AGI):** capacitat d’aprendre i transferir coneixement entre una gran varietat de tasques. La definició i l’avaluació són objecte de debat.
- **IA forta, en sentit filosòfic:** tesi que un sistema computacional pot tenir comprensió o estats mentals reals.
- Són distincions diferents: amplitud de capacitats i naturalesa de la comprensió. No convé usar «general» i «forta» com a sinònims automàtics.

Font: [McCarthy sobre el debat de la IA forta](https://www-formal.stanford.edu/jmc/chinese.html).

---

<!-- Diapositiva 28 del PDF original -->

<!-- _class: lead -->

![bg](images/original/diapositiva-28.png)

# Racionalitat

---

<!-- Diapositiva 29 del PDF original -->


## Què és una decisió racional?

- Un agent racional selecciona l’acció amb **més utilitat o rendiment esperat**, segons la informació disponible.
- Cal considerar els possibles resultats, les seues probabilitats, els costos i les restriccions.
- **Exemple:** un robot pot triar una ruta més llarga si redueix prou el risc de col·lisió.
- Racionalitat no significa omniscència: una bona decisió pot tenir un resultat desfavorable.

Font: [Poole i Mackworth: utilitat esperada](https://artint.info/3e/html/ArtInt3e.Ch12.S1.html).

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

<<<<<<< HEAD
<!-- Diapositiva 36 del PDF original -->

## Definicions

- **Técnica**: Conjunt de procediments o recursos que s'han d'aplicar per a aconseguir un objectiu.
- **Tècniques de la IA**: Conjunt de tècniques, algorismes i mètodes que s'apliquen per a resoldre problemes d'IA.
- Combinant diferents paradigmes, podem obtenir **diferents tècniques**.
=======
## Seleccionar una tècnica

Relacionem el problema amb la família de tècniques: regles per a condicions estables, cerca per a rutes i plans, aprenentatge per a patrons en dades, i recuperació o RAG per a documentació. La idoneïtat i els riscos d'ús es treballen al bloc següent.
>>>>>>> 207e18b9b28f9ffea178f8a540286d47fe1a7e43

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

<<<<<<< HEAD
<!-- Diapositiva 39 del PDF original -->

## Sistemes experts (II)

### Sistemes basats en casos

- S'intenta resoldre un problema a partir de casos similars resolts anteriorment.
- Es recuperen casos similars i s'adapten a la nova situació.
- Una vegada solucionat el problema, el cas es guarda per a utilitzar-lo en el futur.
- D'aquesta forma, el sistema va aprenent a resoldre problemes més complexos.
- Camps d'aplicació: **Medicina**, **enginyeria**, **disseny**, etc.
=======
## Responsabilitat al llarg del mòdul

La tria tècnica té conseqüències per a les persones, les dades i l'organització. En el bloc següent aplicarem aquests criteris a biaixos, privacitat, verificació, supervisió i responsabilitat.
>>>>>>> 207e18b9b28f9ffea178f8a540286d47fe1a7e43

---

<!-- Diapositiva 40 del PDF original -->

## Sistemes experts (III)

### Sistemes basats en regles

- La base de coneixement conté **fets i regles**, sovint definits amb ajuda d’experts.
- El motor d’inferència aplica les regles per derivar **nous fets o conclusions**.
- **Exemple:** «si el sòl està sec, cal regar» + «el sòl està sec» → «cal regar».
- Inferir conclusions no és el mateix que aprendre o generar noves regles.
- Aplicacions: diagnòstic, control de processos i suport a decisions.

Font: [Poole i Mackworth: inferència amb clàusules definides](https://artint.info/2e/html2e/ArtInt2e.Ch5.S3.SS2.html).

---

<!-- Diapositiva 41 del PDF original -->

## Sistemes experts (IV)

### Sistemes basats en lògica difusa

- Representen conceptes graduals, com «temperatura alta» o «velocitat baixa».
- Un **grau de pertinença entre 0 i 1** indica fins a quin punt un valor encaixa en un conjunt difús.
- **Exemple:** 28 °C pot pertànyer a «calor» amb grau 0,7, segons la funció definida. No significa un 70 % de probabilitat que faça calor.
- Les regles s’activen gradualment i combinen els seus resultats.
- Aplicacions: control de temperatura, robòtica i altres sistemes de control.

Font: [Fuzzy sets, Scholarpedia](https://www.scholarpedia.org/article/Fuzzy_sets).

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

- Exploren estats i accions per trobar una solució.
- **Cerca no informada:** no utilitza una estimació heurística del cost restant.
  - Amplada, profunditat, profunditat limitada, aprofundiment iteratiu i **cost uniforme**.
- **Cerca informada:** utilitza una heurística per orientar l’exploració.
  - Cerca voraç i **A\***.
- Cost uniforme ordena pel cost acumulat; A* combina aquest cost amb l’estimació del cost restant.

Font: [Poole i Mackworth: cerca A*](https://artint.info/html1e/ArtInt_57.html).

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
