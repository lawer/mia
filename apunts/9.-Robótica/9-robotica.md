---
marp: true
size: 16:9
theme: lawer
class: default
_class: invert lead
paginate: true
_paginate: false
auto-scaling: true
footer: Carles Gonzàlez
---

<style scoped>
h1, p {
  color: #FFFFFF;
  font-weight: bold;
  text-shadow:
    0px 0px 3px #000000;
}
</style>

# 9. Robòtica

Models d'intel·ligència artificial

![bg opacity](../images/community-jetracer_2020.jpg)

---

## Introducció

- La robòtica és una branca de la tecnologia que es dedica al disseny i construcció de robots.
- Els robots permeten als nostres models d'intel·ligència artificial interactuar amb el món real.
- La robòtica és una disciplina multidisciplinària que combina coneixements d'enginyeria, informàtica, matemàtiques, física, biologia, etc.

---

## Robots

- Un robot és un dispositiu programable que realitza tasques manipulant el seu entorn.
- Per fer-ho, els robots utilitzen actuadors per interactuar amb el món real.
- Els canvis podem ser físics (moure objectes) o digitals (enviar informació).

![bg right:40%](../images/robot.png)

---

### Sensors

- Els sensors són dispositius que permeten als robots percebre el seu entorn.
- Hi ha molts tipus de sensors. Els grups més importants son:
  - **Mesurar l'estat de l'entorn**: càmeres, radars, ultrasons, etc.
  - **Mesurar l'estat del robot**: acceleròmetres, giroscopis, encoders, etc.


![bg right:33%](../images/sensors.png)

---

### Operacions

- Per maximizar la seva eficiència, els robots han de ser capaços de prendre **decisions**.
- Les decisions poden ser simples (moure's cap a l'objectiu) o complexes (conduir un cotxe), sempre en l'objectiu de **realitzar una tasca**.
- Ho podem reduir a un problema d'**optimització**: aplicar les forces adequades per maximitzar l'objectiu.
- **Problema**: com fer-ho de manera eficient?

---

### Entorn

- En els problemes d'optimització que hem vist **fins ara** l'entorn era **virtual, observable i determinista**.
- En el **món real**, l'entorn és **no observable, no determinista i no estàtic**.
- Aixó fa que els problemes de robòtica siguin molt més complicats que els problemes d'optimització tradicionals.
- També es **dificulta l'aprenentatge**: el temps no es pot retrocedir per provar diferents accions ni es pot accelerar
  

---

### Intel·ligència artificial

- Tot el discutit fins ara ens poryta a que els robots **impliquen molts conceptes** dels vists durant el curs.
- Per alguns dels conceptes vistos trobarem en la robòtica una **aplicació pràctica** i real Per exemple, els robots autònoms utilitzen xarxes neuronals per processar la informació dels sensors i prendre decisions.
- Altres conceptes es veuran **ampliats**: per exemple, els algoritmes d'optimització han de ser adaptats per funcionar en entorns no deterministes.

---

## Hardware de robòtica

- Fins ara hem suposat que la forma de interactuar amb el món real era a través de la pantalla.
- Amb la robòtica, aquesta interacció es fa a través de **sensors i actuadors**.
- No podem solament programar el comportament del robot, sinó que també hem de dissenyar el **hardware** que ens permetrà interactuar amb el món real.
- La selecció dels sensors i actuadors determinarà el seu funcionament en les tasques que haurà de realitzar.

---

### Tipus de robots segons el seu hardware

- **Robots antropomòrfics**: robots que imiten la forma humana. També coneguts com a **robots humanoides**. Els més populars pero molt complexos i costosos.
- **Braços robòtics**: robots que poden moure objectes. També coneguts com a **robots manipuladors**. Són els més comuns, especialment en la indústria.
- **Robots mòbils**: robots que poden moure's pel seu entorn. Poden ser **terrestres, aquàtics o aeris**. Són els més comuns en la robòtica autònoma.

---

![bg left%](../images/antro.webp)

![bg center%](../images/arm.png)

![bg right%](../images/mobile.jpg)

---

### Tipus de sensors

- **Actius**: emeten una senyal i mesuren la resposta. Es solen utilitzar per mesurar distàncies. 
  - Radars, ultrasons. Econòmics i fàcils d'utilitzar.
- **Passius**: mesuren la radiació que rebreixen. 
  - Càmeres, micròfons. Més precisos però més cars i complexos.




