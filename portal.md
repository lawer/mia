---
marp: true
size: 16:9
theme: lawer
class: default
_class: invert lead
paginate: true
_paginate: false
auto-scaling: true
---

<style scoped>
h1, p {
  color: #FFFFFF;
  text-shadow:
    0px 0px 3px #000000;
}


</style>

# Utilització de PortalEDU​

![bg opacity](image.png)

---

<!--
_class: invert lead
-->

<style scoped>
h1, h2, h3, h4, h5, h6, p {
  color: #FFFFFF;
  font-weight: 800;
  text-shadow:
    0px 0px 3px #000000;
}
</style>

## Introducció

---

### Què és PortalEDU?

- Plataforma oficial per webs de centre
- Basat ​en el gestor de continguts WordPress
- Permet crear i gestionar webs de centre educatius
- Moltes eines preinstal·lades
  - Constantament se n'afegeixen de noves
- No és extensible pero si es pot utilitzar de moltes maneres diferents.

---

### Accés

- https://portal.edu.gva.es/<nom_centre>/
- Cal tindre permís per administrar el web
- Els permisos els pot assignar l'equip directiu del centre.
- Més d'una persona pot administrar el web

---

<!--
_class: invert lead
-->

<style scoped>
h1, h2, h3, h4, h5, h6, p {
  color: #FFFFFF;
  font-weight: 800;
  text-shadow:
    0px 0px 3px #000000;
}
</style>

## Conceptes bàsics

---

<style scoped>section { font-size:33px; }</style>

### WordPress

- WordPress permet crear i gestionar continguts web sense necessitat de saber programar
- És fàcil d'utilitzar i gratuït.
- Problemes:
  - Vulnerable a atacs externs
  - Lent si no es gestiona bé
  - Errors de seguretat
  - Problemes de compatibilitat amb plugins o temes
- PortalEDU és una versió adaptada de WordPress que ens estalvia aquests problemes.

---

### Pàgines

- Formen la base del web
- Permeten crear contingut estàtic
  - El contingut estàtic és aquell que no canvia amb el temps.
- Exemples: Qui som, Contacte, etc.
- Quan estem creant l'estructura del web, és important pensar en les pàgines que volem crear i com les volem organitzar.
  - Una web ben estructurada és més fàcil de gestionar i d'utilitzar.

---

### Entrades

- S’utilitzen per a contingut dinàmic
  - Notícies, novetats, activitats del centre…
- Ordenades per data
- Es poden classificar amb categories i etiquetes
- Són ideals per a la part de “Actualitat” o “Blog” del centre
  - Exemple: Crònica d’una excursió escolar

---

<style scoped>section { font-size:30px; }</style>

### Categories i etiquetes

- Són dues maneres de classificar el contingut
- Les categories són més generals
  - Exemples: Activitats, Notícies, etc.
  - Permeten agrupar entrades relacionades
- Les etiquetes són més específiques
  - Exemples: Excursió, Esport, etc.
  - Permeten afegir més detalls a les entrades
- És important utilitzar categories i etiquetes per a facilitar la cerca i la navegació pel web
- No és obligatori utilitzar-les, però és recomanable
- No és recomanable utilitzar categories i etiquetes alhora

---

<style scoped>section { font-size:33px; }</style>

### Menús

- Serveixen per estructurar la navegació del web
  - Es molt important pensar en la navegació del web abans de crear-lo
- En PortalEDU sols hi ha un menú principal
- Es poden afegir:
  - Pàgines, enllaços personalitzats, categories d’entrades…
- L’ordre i la jerarquia són essencials per a una bona experiència d’usuari.
- No és recomanable afegir massa elements al menú ni afegir submenús.

---

<style scoped>section { font-size:32px; }</style>

### Edició de contingut (I)

- Es pot editar pàgines i entrades des del panell d’administració
- Editor visual de WordPress (Gutenberg):

  - Basat en blocs (text, imatge, vídeo, botó, etc.)
  - Permet afegir i editar contingut de manera senzilla.
  - Es poden afegir imatges, vídeos, documents, enllaços, etc.

- Alguns centres tenen disponible el plugin Elementor.
  - Permet crear dissenys més avançats i planificar el contingut de manera més visual.
  - No s'instal·larà a més centres i per això que ens centrarem en Gutenberg.

---

### Edició de contingut (II)

- **Procés d'edició**:

  - Accedir al panell d'administració
  - Seleccionar la pàgina o entrada que volem editar
  - Fer clic a "Editar"
  - Afegir o modificar el contingut
  - Fer clic a "Publicar" o "Actualitzar".

- **Important**: Revisar sempre abans de publicar, preferiblement en mode "Previsualització en una pestanya nova"

---

### Blocs fonamentals (I)

- **Paràgraf**: Per escriure text normal
- **Encapçalament (Títol)**: Per organitzar el contingut en seccions (H2, H3…)
- **Imatge**: Inserir una imatge des del dispositiu o la biblioteca
- **Galeria**: Mostrar diverses imatges en format mosaic
- **Enllaç**: Afegir hipervincles a text o botons
- **Botó**: Crear crides a l'acció (ex: "Contacta amb nosaltres")

---

### Blocs fonamentals (II)

- **Llista**: Crear llistes numerades o amb punts
- **Columnes**: Organitzar el contingut en columnes
- **Taula**: Crear taules per mostrar dades
- **Fitxer**: Afegir PDF o altres documents descarregables
- **PDF Embedder**: El block fitxer permet incrustar un PDF en el contingut però no hi ha garanties de que es vegi correctament en tots els navegadors. Per això, per veure sense descarregar, utilitzarem el bloc PDF Embedder.
- **Àudio** i **Vídeo**: Inserir àudios i vídeos propis o d'altres plataformes.

---

### Blocs Avançats

- **HTML**: Inserir codi HTML personalitzat
- **Carrusel d'Entrades**: Mostrar entrades recents en format de carrusel
- **Visor lliscant d'Entrades**: Semblant al carrusel, però amb un disseny que ocupa tota l'amplada de la pantalla.
- **Acordió**: Bloc que permet incrustar contingut desplegable.
- **Bucle de consulta**: Permet mostrar contingut dinàmic en funció de la consulta realitzada (ex: últimes entrades, entrades d'una categoria específica, etc.)

---

### Ginys

- Permeten afegir contingut dinàmic a la barra lateral del web
- Es poden afegir a qualsevol pàgina o entrada
- Permeten mostrar informació addicional com:
  - Últimes entrades
  - Categories
  - Etiquetes
  - Calendari
  - Enllaços a xarxes socials
- Es poden afegir ginys personalitzats i de tercers.

---

<style scoped>section { font-size:30px; }</style>

### Publicació i revisions (I)

- **Opcions abans de publicar:**

  - Guardar com esborrany
  - Vista prèvia
  - Publicar

- **Altres opcions:**

  - Programar data de publicació
  - Fer privada o protegida amb contrasenya
  - Assignar autor/a
  - Assignar categories i etiquetes

- **Consell:** Revisa sempre abans de publicar i comprova el resultat

---

<style scoped>section { font-size:32px; }</style>

### Publicació i revisions (II)

- **Revisions:**
  - Permet veure les versions anteriors d'una pàgina o entrada
  - Permet comparar dues versions, veure les diferències i restaurar una versió anterior si és necessari
  - És important revisar les revisions abans de publicar canvis importants
- **Imatge destacada**: És la imatge principal associada a una entrada.
  - Es mostra en llistats d’articles, portades o ginys amb últimes entrades, xarxes socials...
  - Dona una aparença més atractiva i visual al contingut

---

<style scoped>section { font-size:31px; }</style>

### Elements multimèdia (I)

- **Imatges:**

  - Es poden afegir imatges des del dispositiu o la biblioteca de mitjans.
  - Es poden redimensionar i retallar les imatges abans d'inserir-les.
  - Es recomana utilitzar imatges d'alta qualitat i optimitzades per a la web.

- **Vídeos:**
  - Es poden incrustar vídeos propis de Teams (grup documentar) i de plataformes com YouTube o Vimeo.
  - Es poden pujar vídeos propis, però és recomanable utilitzar plataformes externes per a evitar problemes de càrrega i espai.

---

<style scoped>section { font-size:30px; }</style>

### Elements multimèdia (II)

- **Biblioteca de mitjans:**
  - Permet gestionar totes les imatges, vídeos i documents pujat al web.
  - Permet organitzar els fitxers en carpetes i categories.
  - Permet cercar fitxers per nom, tipus o data de càrrega.
  - Es recomanable pujar primer els fitxers a la biblioteca i després inserir-los a les pàgines o entrades.
    - PortalEDU no detecta si la imatge s'ha pujar anteriorment, per lo que es molt fàcil duplicar fitxers que, si s'esborren, produiran errors.
- El tamany màxim de pujada és de 30MB per fitxer i el espai total és de 2GB.

---

<!--
_class: invert lead
-->

<style scoped>
h1, h2, h3, h4, h5, h6, p {
  color: #FFFFFF;
  font-weight: 800;
  text-shadow:
    0px 0px 3px #000000;
}
</style>

## Conceptes avançats

---

### Grup documentar

- En OneDrive no podem configurar els fitxers o carpetes de manera que siguen totalment públiques (per seguretat).
- Els fitxers i carpetes que compartim amb el team Documentar, però, si es poden configurar com a públics.
- En teams tenim espai il·limitat, per lo que el proost es pujar els fitxers (especialemnt els vídeos i imatges grans) al team Documentar, compartir-los i després incrustar-los.
- Una avantatge és que Teams té un reproductor de vídeos optimitzat per a vídeos grans.
