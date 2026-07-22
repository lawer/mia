# TODO - Actualizacion de Modelos de IA

Documento de trabajo para adaptar el modulo `5071 - Modelos de Inteligencia Artificial` a una carga de 90 horas, manteniendo y actualizando el material existente.

## Fase 1 - Correcciones y actualizacion base

- [ ] Corregir las implementaciones didacticas de UCS y A* en `apunts/1.-primer_trimestre/3.-Búsqueda en espai d'estats/continguts.md`.
  - UCS debe conservar y actualizar el menor coste conocido de cada estado.
  - A* debe priorizar correctamente `f(n) = g(n) + h(n)`.
  - Incluir casos de prueba que comparen coste, nodos explorados y ruta encontrada.

- [ ] Corregir conceptos de sistemas basados en reglas en `apunts/2.-segon_trimestre/6.-Sistemes Basats en Regles/continguts.md`.
  - Definir el encadenamiento hacia atras como razonamiento deductivo dirigido por objetivos.
  - Eliminar la inferencia invalida `p -> q, q por tanto p`.
  - Diferenciar incertidumbre probabilistica, vaguedad y logica difusa.
  - Revisar las bibliotecas recomendadas y dejar solo alternativas mantenidas.

- [ ] Actualizar `apunts/2.-segon_trimestre/7.-NLP/continguts.md`.
  - Presentar HMM, RNN, LSTM y GRU como contexto historico, no como enfoque central.
  - Corregir que los LLM modernos relevantes son principalmente Transformers.
  - Corregir la descripcion de arquitecturas decoder-only.
  - Explicar cuando conviene TF-IDF, embeddings, clasificacion supervisada o un LLM.
  - Evitar presentar el preprocesado agresivo como requisito para Transformers.

- [ ] Actualizar la introduccion historica de IA en `apunts/1.-primer_trimestre/1.-Introducció/continguts.md`.
  - Sustituir afirmaciones no verificables sobre parametros de modelos.
  - Incorporar modelos fundacionales multimodales, modelos abiertos y ejecucion local.
  - Incorporar coste, latencia, privacidad y dependencia de proveedor como criterios tecnicos.


## Fase 2 - Consolidacion de materiales

- [ ] Anadir una tabla de seleccion de tecnica o modelo en la unidad de introduccion.
  - Reglas para decisiones estables y auditables.
  - Busqueda, CSP y optimizacion para planificacion y restricciones.
  - ML para prediccion basada en datos.
  - RAG para consulta de documentacion cambiante.
  - LLM para transformacion o generacion de lenguaje con controles.

- [ ] Crear una practica de sistema de decision explicable.
  - Reglas versionadas separadas de los datos y del motor de inferencia.
  - Traza de reglas activadas y explicacion de la conclusion.
  - Conflictos, datos incompletos y escalado a revision humana.

- [ ] Revisar la extension del bloque de busqueda y optimizacion.
  - Mantener formulacion de problemas, BFS/UCS/A*, CSP y una tecnica de busqueda local.
  - Pasar variantes avanzadas que no se reutilicen a material de ampliacion.

- [x] Inventariar las fuentes MARP del primer trimestre.
  - Creada `1-introduccio-marp.md`, con sus versiones HTML y PDF enlazadas desde `introduccio.md`.
  - `3.1-conceptes_previs.md` ya existia; no es necesario crear una fuente duplicada.
  - `3.2-busqueda-marp.md` cubre la unidad completa de busqueda, incluida la busqueda informada y las variantes de A*.

- [x] Corregir las rutas de recursos locales de las fuentes MARP existentes.
  - Actualizadas las rutas antiguas hacia `apunts/images/`.
  - El generador valida los recursos locales antes de renderizar cada presentacion.

- [x] Automatizar las presentaciones MARP y las paginas de contenidos.
  - `npm run build:marp` detecta las fuentes con `marp: true`, genera PDF, HTML y `continguts.md`.
  - El workflow de GitHub Pages ejecuta el proceso en cada push y publica desde `main`.
  - Vision por computador y robotica ya disponian de fuentes MARP; ahora se incluyen en la generacion automatica.

## Fase 3 - Nuevos contenidos y practicas

- [ ] Crear un bloque practico de IA responsable, privacidad y seguridad.
  - RGPD: minimizacion, finalidad, datos sensibles y conservacion.
  - Reglamento Europeo de IA: riesgo, transparencia, supervision humana y documentacion.
  - Sesgos, trazabilidad, explicabilidad y accesibilidad.
  - Seguridad por diseno y riesgos de LLM: prompt injection, fuga de datos y automatizacion no supervisada.

- [ ] Anadir una ficha de riesgos obligatoria a cada practica relevante.
  - Problema, usuarios afectados y limites del sistema.
  - Origen, licencia y datos personales del conjunto de datos.
  - Metricas, casos de fallo y mecanismo de supervision humana.
  - Riesgos de sesgo, privacidad y seguridad, con mitigaciones.

- [ ] Crear una practica de RAG con fuentes verificables.
  - Preparacion, segmentacion e indexacion de un corpus delimitado.
  - Embeddings y base vectorial local.
  - Recuperacion, reranking opcional y generacion con citas.
  - Abstencion cuando no exista evidencia suficiente.
  - Evaluacion separada de recuperacion y calidad/fidelidad de respuestas.
  - Pruebas de documentos maliciosos e instrucciones inyectadas.

## Vision y robotica

- [ ] Mantener la secuencia de control existente en `apunts/2.-segon_trimestre/9.-Robótica/`.
  - Control reactivo.
  - Logica difusa.
  - Generacion y balanceo de datos.
  - Control mediante red neuronal y comparacion de resultados.

- [ ] Anadir una introduccion practica al modelado de robots manipuladores.
  - Sistemas de coordenadas, grados de libertad y cinematica directa/inversa.
  - Planificacion de trayectorias y limites fisicos.
  - Simulacion como alternativa cuando no haya hardware.

- [ ] Incorporar seguridad funcional en las practicas roboticas.
  - Parada segura, limites de velocidad y zonas de exclusion.
  - Deteccion de incertidumbre y cesion de control a una persona.

## Proyecto integrador

- [ ] Disenar un proyecto final de 10 a 15 horas.
  - Caso propuesto: sistema de apoyo a la gestion de incidencias.
  - Reglas para priorizar y derivar casos.
  - Recuperacion documental para fundamentar respuestas.
  - LLM para redactar respuestas con citas y limites.
  - Pruebas normales, sin evidencia y adversarias.
  - Memoria tecnica con arquitectura, evaluacion y ficha de riesgos.

- [ ] Definir una rubrica comun para el proyecto.
  - Adecuacion del modelo elegido al problema.
  - Correccion y evaluacion tecnica.
  - Trazabilidad, seguridad, privacidad y gestion de sesgos.
  - Calidad de documentacion, demo y comunicacion de limites.

## Distribucion orientativa de 90 horas

| Bloque | Horas |
| --- | ---: |
| Fundamentos y seleccion de modelos | 10 |
| Busqueda, planificacion, optimizacion y CSP | 22 |
| Sistemas expertos, reglas y logica difusa | 15 |
| PLN, embeddings, Transformers y RAG | 20 |
| Vision y robotica | 13 |
| IA responsable y proyecto integrador | 10 |
