# Auditoria integral del curs de Models d’Intel·ligència Artificial

**Data de revisió:** 6 d’octubre de 2026  
**Abast:** repositori complet, amb atenció a les pàgines d’entrada, unitats de les dues avaluacions, projecte integrador, presentacions Marp, continguts, activitats, rúbriques, recursos visuals, materials docents, fitxers generats i configuració de publicació.

## 1. Abast i mètode

He inventariat les unitats, inspeccionat els enllaços Markdown a notebooks, validat l’estructura de 61 notebooks locals enllaçats (cel·les, dependències declarades, cel·les executades guardades i sortides), cercat credencials literals i notebooks de solucions, inspeccionat la navegació i Jekyll, comparat fonts Marp amb continguts publicats i executat les comprovacions disponibles.

El curs conté dues avaluacions, deu blocs numerats (1–10, amb el bloc 1 dividit en 1.1 i 1.2), pàgines de continguts i activitats, recursos gràfics i un conjunt ampli de notebooks i fitxers multimèdia. Les àrees inclouen fonaments, cerca i CSP, jocs, sistemes basats en regles, PLN, visió, robòtica i un projecte integrador.

S’han revisat 61 notebooks locals enllaçats en l’estat inicial; quatre solucions s’han deslligat de les pàgines d’alumnat i ara queden 57 notebooks d’activitat o exemple enllaçats. No s’ha pogut executar cap notebook: els intents de llançar un kernel Jupyter en sis exemples autocontinguts han fallat amb `PermissionError: [Errno 1] Operation not permitted` en la inicialització de la interfície local. La inspecció estàtica no certifica que els models, les descàrregues o els exemples funcionen actualment. Tampoc no s’ha pogut compilar el lloc complet: falta la gem Ruby `csv-3.3.6`. Per tant, la publicació final i tots els enllaços externs resten pendents de comprovació.

No s’ha trobat un `AGENTS.md` aplicable dins d’aquest repositori. La carpeta `scripts/` està exclosa de Jekyll; el report i el prompt hi queden com a documents interns de revisió.

## 2. Valoració general

El curs té una estructura reconeixible que va dels fonaments a les tècniques i acaba amb un projecte; l’índex declara 90 hores, amb una distribució que suma correctament 90. Hi ha materials diversos i activitats pràctiques. La revisió ha corregit la navegació buida del segon trimestre, ha retirat diverses solucions dels enllaços públics i ha tret el capítol antic del lloc generat. Cal compilar i inspeccionar la web després dels canvis per confirmar les exclusions efectives.

La revisió detallada de vigència tècnica i reproductibilitat és desigual entre àrees. Diversos materials i exemples daten de tecnologies i versions anteriors; cal prioritzar una passada per notebooks, APIs, dependències i continguts de PLN, visió i robòtica abans de considerar l’auditoria tècnica tancada.

## 3. Inventari del curs

| Bloc | Materials principals localitzats | Estat d’aquesta revisió |
| --- | --- | --- |
| 1.1 Introducció i fonaments | Marp, HTML/PDF, continguts, treball pràctic 1 | Revisió de seqüència, activitat i missatges principals; cal actualitzar el resum d’actualitat i revisar totes les afirmacions tècniques amb fonts |
| 1.2 Ús responsable | Marp, HTML, continguts, exercicis, guia docent, crèdits d’imatges | S’ha tret la resposta dels continguts públics; PDF exclòs temporalment perquè no s’ha pogut regenerar |
| 2–5 | Conceptes previs, cerca, cerca local/CSP i jocs; presentacions, continguts i recursos | Inventari i revisió estructural; pendent execució completa d’exercicis i verificació tècnica de cada algoritme |
| 6 | Sistemes basats en regles i continguts | Inventari i revisió de navegació; pendent revisió línia a línia de teoria i exemples |
| 7 | PLN, continguts i notebooks enllaçats | Inventari i revisió de temes; pendent comprovació de compatibilitat de notebooks i models externs |
| 8 | Visió, continguts, notebooks, conjunts de dades i vídeos | Inventari; pendent execució de notebooks, comprovació de llicències i compatibilitat de llibreries |
| 9 | Robòtica, continguts i notebooks | Inventari; pendent execució dels entorns i comprovació de dependències i maquinari |
| 10 | Projecte integrador, proposta, dades i rúbrica | Inventari de fitxers; pendent contrast detallat entre dades, instruccions, hores i rúbrica |
| Materials generals | Índex, dues pàgines d’avaluació, llibre Markdown antic, presentacions extra | Revisió estructural; cal decidir si els materials antics i extras formen part del curs públic |

## 4. Troballes prioritzades

### A-01 · Important — La llista d’unitats del segon trimestre faltava (corregit)

**Fitxer:** [`apunts/2.-segon_trimestre/2.-segon_trimestre.md`](/home/carles/Documentos/mia/apunts/2.-segon_trimestre/2.-segon_trimestre.md), secció «Temes».  
**Evidència:** la pàgina no tenia cap llista després del paràgraf d’introducció. S’han afegit enllaços ordenats als blocs 6–10.  
**Impacte:** abans no orientava l’alumnat cap a les unitats del trimestre.  
**Validació pendent:** la compilació Jekyll està bloquejada per la gem absent; cal confirmar les destinacions `{% link %}` en el build següent.

### A-02 · Important — Resposta incrustada en materials generats (corregit i regenerat)

**Fitxers:** Marp i continguts de 1.2, apartat de l’activitat de mètriques.  
**Evidència:** la versió original mostrava un gràfic amb els resultats de l’exercici. S’ha substituït per una explicació qualitativa sense valors de resposta; s’ha regenerat l’HTML. El PDF s’ha regenerat i torna a estar enllaçat; té 31 pàgines i no conté la resposta. El fitxer gràfic de resposta està exclòs de Jekyll i ja no s’enllaça des dels crèdits visuals.  
**Impacte:** la compilació final de Jekyll continua pendent; cal comprovar l’exclusió del gràfic en el web generat.  
**Validació:** text extret del PDF confirma que no hi apareixen el títol-resposta ni els valors calculats; HTML regenerat també sense el gràfic ni els resultats. La pàgina torna a oferir PDF i HTML actualitzats.

### A-03 · Important — Capítol antic potencialment publicable i inconsistent amb els continguts actuals (exclòs de Jekyll)

**Fitxer:** [`apunts/llibre.md`](/home/carles/Documentos/mia/apunts/llibre.md).  
**Evidència:** el front matter data el document en 2023 i conserva el marcador «El Teu Nom». El text descriu GPT-3 com a model que ha «revolucionat» el PLN, presenta la prova de Turing com un criteri per decidir si una màquina és intel·ligent i simplifica la IA general/forta com un únic objectiu. No apareix en la navegació principal, però és dins de `apunts/` i no figura entre les exclusions Jekyll.  
**Impacte:** encara que siga un material orfe, pot ser servit com a pàgina pública i contradir el material revisat més recent.  
**Acció aplicada:** `apunts/llibre.md` s’ha afegit a les exclusions de Jekyll; el fitxer es conserva en el repositori com a material històric fins que se’n decidisca el destí. El build complet queda pendent de validar.

### A-04 · Important — Dependències i execució dels notebooks requereixen una passada pràctica

**Àrees:** 61 notebooks locals enllaçats en l’estat inicial des de materials de les unitats 2–9 (57 després de retirar quatre enllaços a solucions).  
**Evidència:** s’han llegit i validat les estructures, les 701 cel·les de codi i les metadades. En els notebooks hi ha instruccions d’instal·lació `pip`, dependències remotes, crides a models preentrenats, dependències de GPU, sortides guardades i codi que descarrega dades. Sis notebooks sense cel·les d’instal·lació explícites s’han intentat executar; els kernels no han pogut iniciar-se en aquest sandbox (`PermissionError`). Alguns notebooks no fixen versions i d’altres acumulen sortides grans o dependents d’entorns externs.  
**Impacte:** les metadades i el codi no demostren que un notebook es puga executar avui ni que el resultat guardat siga reproduïble.  
**Recomanació:** fer una passada d’execució en un entorn docent net, fixar versions i dades, registrar requisits de GPU, xarxa i credencials, i marcar materials històrics o opcionals.

### A-05 · Important — Actualitzar i contextualitzar la secció de treball i IA (aplicat)

**Fitxer:** [`1-introduccio-marp.md`](/home/carles/Documentos/mia/apunts/1.-primer_trimestre/1.-Introducció/1-introduccio-marp.md#L341), diapositives «Situació actual» i «Món laboral».  
**Evidència inicial:** la situació actual es limitava a dir que els avenços són constants i que hi ha riscos; la diapositiva laboral enunciava conclusions sense data ni referència. S’ha actualitzat «Situació actual» amb criteris per interpretar capacitats segons tasca i context, i «Món laboral» amb dades i fonts de l’OIT (2025) i l’OCDE (2026). La presentació diferencia exposició potencial de prediccions de pèrdua de llocs, i relaciona l’impacte amb adopció, regulació i decisions organitzatives. Les fonts també figuren en les referències finals.  
**Fonts actuals:** l’[OIT, *Generative AI and jobs: A 2025 update*](https://www.ilo.org/publications/generative-ai-and-jobs-2025-update), 20 maig 2025, estima que una de cada quatre persones treballadores està en ocupacions amb algun grau d’exposició i assenyala que la transformació de les ocupacions és més probable que la seua desaparició; l’[OCDE, *The OECD AI exposure measure*](https://www.oecd.org/en/publications/the-oecd-ai-exposure-measure_f3da0f0a-en.html), 26 maig 2026, remarca que l’impacte real depén de l’adopció, regulació, canvi organitzatiu i decisions socials.  
**Validació:** font Marp, continguts, HTML i PDF actualitzats; el PDF manté 56 diapositives. La diapositiva laboral s’ha inspeccionat visualment i el text/cites hi caben sense solapar-se.

### A-06 · Menor — Citar la versió consolidada del Reglament d’IA

**Fitxers:** continguts i presentació de 1.2, secció «Marc normatiu».  
**Evidència:** el material enllaça la versió original del Reglament (UE) 2024/1689 a `.../oj/eng`, tot i que adverteix de consultar sempre el text vigent. EUR-Lex ofereix el text consolidat identificat com a `02024R1689-20260727`, amb canvis i disposicions d’aplicació que convé tindre presents en la consulta.  
**Font:** [EUR-Lex, text consolidat del Reglament (UE) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689).  
**Recomanació:** enllaçar explícitament a la vista consolidada i datar-la, mantenint l’avís que l’aplicació depén del cas i de les disposicions transitòries. No resumir terminis legals sense una nova comprovació jurídica.

### A-07 · Menor — Aclarir el paper dels materials extra i del llibre antic

**Fitxer:** [`index.md`](/home/carles/Documentos/mia/index.md).  
**Evidència:** «Scraping» i «Presentació Sagunt» apareixen en «Extras», sense explicar públic, objectiu ni relació amb les 90 hores.  
**Impacte:** no queda clar què és part avaluable i què és referència addicional.  
**Recomanació:** descriure breument a qui s’adrecen els materials extra i si formen part de l’avaluació.

### A-08 · Important — Clau d’API incrustada en un notebook (retirada; cal revocar-la)

**Fitxer:** `apunts/2.-segon_trimestre/8.-Reconeixement imatges/3_Deteccio_objectes.ipynb`, cel·la de connexió a Roboflow.  
**Evidència:** hi havia una clau literal com a argument de `Roboflow`. S’ha llevat del fitxer i el notebook ara llig `ROBOFLOW_API_KEY` de l’entorn; també s’ha afegit una instrucció explícita per guardar-la com a variable d’entorn i no escriure-la al notebook. No s’inclou el valor de la clau en aquest report.  
**Impacte:** una credencial inclosa en un repositori pot haver estat copiada o utilitzada per tercers; canviar el fitxer no invalida la clau ni les còpies ja publicades.  
**Acció necessària:** revocar i rotar la clau al compte Roboflow, i revisar l’activitat i l’historial Git. Cal documentar per a l’alumnat com configurar la variable d’entorn sense enganxar la clau al notebook.

### A-09 · Important — Quatre notebooks de solucions enllaçats des de pàgines públiques (enllaços retirats i fitxers exclosos de Jekyll)

**Àrees:** cerca en espai d’estats i cerca local/CSP.  
**Evidència:** en l’estat inicial hi havia quatre enllaços explícits a fitxers `*_solucionat*.ipynb`, inclosos enllaços «Open in Colab». S’han eliminat les files d’enllaç de les pàgines d’alumnat i afegit les quatre rutes a `exclude` de Jekyll. Els fitxers fonts es conserven en el repositori per a ús docent.  
**Impacte:** les solucions eren accessibles abans de completar els exercicis, en contra de la preferència docent establerta.  
**Validació pendent:** el build de Jekyll no s’ha completat en aquest entorn; cal comprovar la publicació quan es resolga la gem absent. L’exclusió del lloc estàtic no elimina el contingut de l’historial ni d’un repositori públic.

### A-10 · Menor — Metadades de format incompletes en dos notebooks (corregit)

**Fitxers:** `6.-Sistemes Basats en Regles/5.-preveure_valor_mercat.ipynb` i `7.-NLP/E1.-exercicis_representacio_text.ipynb`.  
**Evidència:** cinc cel·les de codi no tenien el camp requerit `execution_count`; la validació de `nbformat` fallava. S’ha afegit el valor nul correcte a les cinc cel·les; la validació estructural ara passa.

### A-11 · Menor — Tres rutes locals de notebook no coincidien amb la ubicació real (corregit)

**Fitxer:** `apunts/1.-primer_trimestre/4.-Búsqueda local i Satisfacció de restriccions/busqueda_espais_estats.md`.  
**Evidència:** els enllaços relatius ometien el directori `exercicis/`, mentre que els enllaços Colab apuntaven al directori correcte. S’han actualitzat els tres enllaços locals i ara resolen als fitxers existents.

### A-12 · Menor — 509 cel·les de 26 notebooks no tenen identificador estable

**Evidència:** la validació de `nbformat` passa, però avisa que 509 cel·les en 26 notebooks no tenen camp `id`. La versió actual del validador ho tolera; versions futures poden exigir-lo. No s’han reescrit tots els notebooks per no generar un canvi mecànic ampli durant aquesta auditoria.
**Recomanació:** afegir identificadors estables amb una normalització controlada quan es toque cada notebook o en una migració dedicada.

## 5. Revisió tècnica per àrea

- **Fonaments i agents:** el material 1.1 té una cronologia amb fonts associades i un treball pràctic que demana separar documentació i afirmacions promocionals. Les diapositives d’actualitat i treball s’han actualitzat amb fonts de 2025 i 2026 i amb una explicació dels límits d’una mètrica d’exposició. Completar comprovació de cada definició i exemple abans de donar aquesta àrea per auditada tècnicament.
- **Cerca, jocs i CSP:** les unitats estan presents i ordenades després del tema 1. Cal verificar formalment completesa/optimalitat dels algoritmes, heurístiques, pseudocodi i resultats dels exercicis amb execució independent.
- **Sistemes basats en regles:** hi ha una unitat dedicada; falta revisar exemples, tractament d’incertesa i límits de la lògica difusa contra referències actuals.
- **PLN:** els materials enllacen notebooks amb models i tasques diversos. Cal contrastar preprocessament, corpus, mètriques, versions i limitacions dels models, i distingir amb precisió embeddings, Transformers, generació i RAG.
- **Visió:** hi ha continguts de processament d’imatge, CNN, detecció, segmentació i generació. La revisió tècnica de codi, conjunts de dades, pesos preentrenats i llicències queda pendent d’execució.
- **Robòtica:** apareixen sensors, localització, control reactiu, xarxes neuronals i NEAT. Els notebooks no s’han pogut executar en aquest sandbox; cal validar l’execució en l’entorn previst, les assumpcions sobre maquinari i els límits de seguretat quan un model controla actuadors.
- **Projecte integrador:** hi ha fitxers de proposta, dades i rúbrica. Cal contrastar la mida i la llicència de les dades, que els resultats siguen reproduïbles i que els criteris de rúbrica siguen assolibles en les hores assignades.
- **IA responsable:** el NIST AI RMF, OWASP, RGPD i Reglament d’IA donen estructura al bloc. La font normativa hauria d’apuntar a la consolidació vigent; cal mantindre separades obligacions legals i marcs voluntaris.

## 6. Revisió didàctica i d’avaluació

La seqüència global és comprensible i l’índex reparteix les 90 hores en blocs que sumen correctament. El treball pràctic del tema 1 concreta el cas, exigeix fonts i limita la inferència; això dona una aplicació útil dels conceptes inicials. El bloc de responsabilitat afegeix una pràctica sobre paper amb dades sintètiques.

Cal completar la revisió de càrrega comparant cada calendari amb la durada real dels notebooks i projecte. En particular, les activitats que depenen de Colab necessiten una alternativa si falla la xarxa, la quota o la GPU. La llista d’unitats s’ha afegit a la pàgina del segon trimestre; falta confirmar-la en el build publicat. Per cada pràctica, recomane documentar prerequisits, temps, lliurables, criteris, dades i alternativa tècnica en un lloc únic.

La decisió curricular pendent és què fer amb `apunts/llibre.md` i amb els materials «Extras»: arxivar-los, actualitzar-los o incorporar-los explícitament. No convé afegir temes nous abans de saber quines unitats ja no s’executen o no encaixen en les 90 hores.

## 7. Publicació, privacitat, accessibilitat i llicències

- La configuració exclou `scripts`, `_solucionaris` i la guia docent de 1.2; és una mesura útil, però no detecta còpies de respostes en presentacions, gràfics o continguts web.
- S’han tret quatre enllaços directes a notebooks de solucions i s’han exclòs les rutes de Jekyll. S’ha retirat la resposta gràfica de 1.2 dels continguts web i l’HTML està regenerat; el PDF vell està exclòs fins a regenerar-lo. Cal confirmar-ho en el build publicat.
- En 1.2 hi ha fitxer de crèdits visuals i procedència; cal aplicar la mateixa traçabilitat a la resta del curs, inclosos conjunts de dades, vídeos, pesos de models i imatges de les presentacions antigues.
- No s’ha fet una prova automàtica completa de tots els enllaços, contrastos, text alternatiu i desbordaments de PDF/HTML.

## 8. Propostes de revisió ordenades

1. **Corregir la publicació i navegació:** completar els temes de segon trimestre; compilar i verificar Jekyll després dels canvis d’exclusió; decidir si es conserva el llibre de 2023 com a arxiu del repositori.
2. **Fer una passada de reproducció de notebooks:** en un entorn amb kernels autoritzats, triar una base per àrea, fixar versions, executar els 61 notebooks enllaçats des del principi, comprovar recursos remots i anotar alternatives sense GPU. Revocar la credencial exposada i documentar la variable `ROBOFLOW_API_KEY`.
3. **Auditar exercicis i avaluació:** comparar dades, solucions i rúbriques amb els objectius i hores dels blocs; revisar el projecte integrador com una seqüència de lliurables.
4. **Actualitzar afirmacions que canvien:** especialment treball i exposició a IA, models i APIs de PLN, models de visió i normativa. Citar fonts primàries amb data de consulta.
5. **Fer proves del lloc:** després d’instal·lar la dependència que falta, compilar Jekyll, verificar enllaços interns i recursos generats, i inspeccionar les pàgines resultants com a estudiant.

## 9. Canvis aplicats i validació

En aquesta passada s’ha ampliat el prompt per exigir auditoria de `.ipynb` i s’ha actualitzat aquest informe. També s’ha aplicat l’A-05 a la font Marp 1.1, els continguts i els fitxers HTML/PDF generats. S’ha afegit l’índex d’unitats 6–10, exclòs de Jekyll el llibre antic, corregit tres rutes locals, normalitzat metadades de cinc cel·les, eliminat els enllaços públics a quatre notebooks de solucions i exclòs les seues rutes de Jekyll. S’ha llevat la resposta numèrica de l’activitat 1.2 dels continguts i de la presentació; s’han regenerat HTML i PDF. La clau literal s’ha reemplaçat per una variable d’entorn; falta revocar-la al servei.

- Validació `nbformat` de tots els `.ipynb` del repositori: **passa** després de corregir les cinc cel·les incompletes; persisteix l’avís informatiu d’identificadors absents en 509 cel·les. Els 57 notebooks que continuen enllaçats a pàgines d’alumnat resolen a rutes existents després dels tres ajustos; s’han inspeccionat també els quatre notebooks de solucions deslligats.
- Intent d’executar sis notebooks amb Python estàndard: **no iniciat**; Jupyter falla abans d’executar cel·les amb `PermissionError: [Errno 1] Operation not permitted`.
- Marp HTML i PDF de 1.1 i 1.2: **regenerats**; els 56 fulls de 1.1 es conserven. PDF comprovat amb PyMuPDF: 31 pàgines; el títol-resposta, els valors calculats i la imatge-resposta no hi apareixen. La primera conversió local va fallar per permisos temporals; la conversió autoritzada posterior ha passat.
- `npm run test:marp`: **passa**, una prova, cap fallada.
- `git diff --check`: **passa**.
- `bundle exec jekyll build`: **no s’ha pogut completar**; Bundler retorna `Could not find csv-3.3.6 in locally installed gems (Bundler::GemNotFound)`.
- La configuració de Jekyll exclou `scripts/`, el llibre antic, els notebooks de solucions i el gràfic de respostes. La configuració YAML es valida, però la publicació resultant resta pendent del build Jekyll.
