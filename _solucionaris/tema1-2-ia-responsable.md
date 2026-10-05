---
layout: default
title: Solucionari IA responsable
parent: 1.2 Ús responsable, segur i centrat en les persones
nav_exclude: true
---

# Solucionari i orientacions docents

Aquesta pàgina és accessible per enllaç; no té protecció d’accés. Mostrar les solucions després del treball en parelles. Les alternatives raonades són acceptables: s’avalua la coherència entre propòsit, risc, control i prova.

## Exercici 1

| Cas | Resposta orientativa | Risc i control |
| --- | --- | --- |
| Factura | Càlcul convencional amb quantitats i preus | Arrodoniment o entrada incorrecta; validar camps i provar casos coneguts |
| Ruta del robot | Cerca o optimització amb restriccions | Mapa desactualitzat; validar obstacles i disposar de parada segura |
| Suport tècnic | Regles de referència; aprenentatge supervisat si aporta una millora | Urgències no detectades; dades representatives, mètriques i revisió |
| Resposta documental | Cerca documental; generació amb recuperació si aporta valor | Font inventada o desactualitzada; comprovar citació i suport literal de les afirmacions |
| Beca | No assumir que és admissible decidir-la automàticament amb aquest enunciat | Impacte sobre drets; aclarir criteris, dades, marc aplicable i vies de revisió abans del disseny |

El cas de la beca no justifica una afirmació universal sobre la legalitat de qualsevol automatització. Un sistema de regles també pot ser IA simbòlica; el que importa és el mecanisme i com s’avalua. RAG no garanteix veracitat ni autorització per usar documents.

## Exercici 2: recomptes i mètriques

Positiu = urgent. Les etiquetes són sintètiques.

| Àmbit | VP | FN | FP | VN | N | Encert | Detecció | Taxa de FN |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Valencià | 3 | 2 | 1 | 4 | 10 | 70 % | 60 % | 40 % |
| Castellà | 5 | 0 | 1 | 4 | 10 | 90 % | 100 % | 0 % |
| Total | 8 | 2 | 2 | 8 | 20 | 80 % | 80 % | 20 % |

- Encert valencià: (3 + 4) / 10 = 0,70.
- Detecció valencià: 3 / (3 + 2) = 0,60.
- Taxa de FN valencià: 2 / (3 + 2) = 0,40.
- Encert total: (8 + 8) / 20 = 0,80.
- Detecció total: 8 / (8 + 2) = 0,80.

**Ampliació:** precisió positiva = VP / (VP + FP): 75 % en valencià, aproximadament 83,3 % en castellà i 80 % en total. Si no hi ha positius predits, aquesta mesura no està definida. La taxa de FP usa un altre denominador: FP / (FP + VN); no és la taxa de FN ni 1 menys la precisió positiva.

![Encert i detecció per idioma i en total](images/errors-per-idioma.svg)

### Interpretació esperada

La mitjana amaga una detecció d’urgències inferior en les peticions en valencià del conjunt. No permet afirmar que l’idioma siga la causa: podrien variar els tipus de petició, la dificultat o les etiquetes. Hi ha cinc urgències per idioma; un cas canvia la sensibilitat en 20 punts percentuals.

Comprovacions acceptables: ampliar la mostra amb casos representatius; comparar peticions equivalents traduïdes i revisades; revisar les etiquetes; controlar canal, tipus d’avaria i llargària; provar dades noves. El 100 % de detecció en castellà no demostra absència d’errors futurs.

La supervisió ha d’incloure una mostra de peticions marcades com a no urgents. Revisar només les alertes positives no detecta els FN. Si l’enunciat no dona puntuacions de confiança, no es pot calcular un llindar ni afirmar que el model està calibrat.

### Errors freqüents

- Dividir FN entre totes les peticions en lloc de les urgències reals.
- Confondre precisió positiva amb encert.
- Tractar 20 casos fabricats com una prova de discriminació causal.
- Proposar «més dades» sense precisar quines situacions cal cobrir.
- Considerar que l’humà revisarà sempre bé sense temps, formació o autoritat.

## Taller: exemple de disseny justificat

**Propòsit:** ajudar a preparar la cua, sense denegar servei. **Urgent:** interrupció d’un servei essencial sense alternativa. **Referència:** cua manual amb una regla d’escalat d’avaries generals.

| Risc | Control | Prova i resultat esperat | Responsable |
| --- | --- | --- | --- |
| No detectar avaria general | Derivació prioritària i revisió humana | T01 i T02 arriben a revisió prioritària | Responsable de suport |
| Petició ambigua | Demanar aclariment; no tancar | T04 genera una pregunta útil | Persona revisora |
| Extracció de peticions alienes | Permisos a la capa de dades; mínim privilegi | T05 no obté dades d’altres usuaris | Administració del sistema |
| Dades innecessàries | Separar contacte i contingut; revisar adjunts | T06 no envia secrets al model ni als registres | Responsable de dades |

**Criteri didàctic del pilot:** cap avaria general del conjunt de prova pot quedar sense revisió. **Aturada:** qualsevol accés no autoritzat o tancament automàtic suspén la funció afectada fins que s’investigue. No són llindars universals ni una garantia per a casos nous.

**Resultats:** pendents d’execució. L’alumnat dissenya proves, no certifica un sistema. Queden riscos residuals: error humà, nous tipus d’avaria, canvis en les dades i informació insuficient.

**Exemple de comunicació:** «Una eina proposa categoria i prioritat; el personal de suport les revisa. Pots demanar correcció pel mateix canal de la petició.» Cal adaptar-lo a l’ús real.

## Rúbrica operativa

Puntuar cada dimensió de 0 a 3. Nota sobre 10 = 10 × suma(pes × nivell / 3), amb pesos 0,25; 0,25; 0,30; 0,20.

| Dimensió | 3: assolit | 2: parcial | 1: inicial | 0: absent |
| --- | --- | --- | --- | --- |
| Problema, 25 % | Propòsit, afectats i alternativa comparables | Falta concretar un element | Propòsit genèric | No identifica el problema |
| Dades i riscos, 25 % | Dades mínimes i tres riscos contextualitzats | Riscos pertinents amb alguna llacuna | Llista genèrica sense context | No identifica riscos |
| Proves i controls, 30 % | Risc, control, prova i criteri vinculats | Relacions incompletes | Controls sense prova observable | No proposa proves |
| Supervisió, 20 % | Responsable, correcció, aturada i comunicació clars | Falta un mecanisme | «Revisió humana» sense concreció | No defineix supervisió |

No donar per executades proves que només s’han dissenyat. Prioritzar criteris observables sobre afirmacions com «és segur» o «és ètic».

## Eixida individual: respostes esperades

- Canviar noms per codis amb una clau és pseudonimitzar; no elimina la possibilitat de reidentificació.
- Un 80 % global pot amagar una detecció del 60 % en una part dels casos.
- Un control extern al model pot ser denegar a l’eina el permís de consultar peticions alienes o de tancar incidències.

Fonts de suport: [Comissió Europea](https://commission.europa.eu/law/law-topic/data-protection/data-protection-explained_en), [OWASP](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) i [Reglament d’IA](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng). Els càlculs provenen exclusivament de les dades sintètiques de la fitxa.
