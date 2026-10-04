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

- [x] Integrar l'ús responsable dins del tema 1, després dels fonaments: `apunts/1.-primer_trimestre/0.-IA responsable/ia_responsable.md`.
  - El tema 1 queda en 6 hores: 3 hores d'introducció i 3 hores d'aplicació responsable.
  - La seqüència responsable inclou dos exercicis breus, un cas integrador i una rúbrica amb evidències observables.
  - Inclou consulta del RGPD i el Reglament Europeu d'IA en fonts oficials, sense convertir el material en assessorament jurídic.

- [x] Crear una ficha de analisis de riesgos reutilizable en las practicas relevantes.
  - Proposito, usuarios, personas afectadas, alternativas y limites.
  - Origen, licencia, minimizacion y datos personales.
  - Metricas, casos de fallo, sesgos y mitigaciones.
  - Supervision humana, comunicacion y condiciones para detener el uso.

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

- [x] Crear el proyecto final de 15 horas en `apunts/2.-segon_trimestre/10.-Projecte integrador/`.
  - Guía en cinco sesiones con reglas, RAG, borradores de respuesta y revisión humana.
  - Corpus y once incidencias sintéticas: casos bilingües, fuera del corpus, de riesgo, de inyección y documentos obsoletos.
  - Criterios técnicos de aceptación, entregables, memoria y defensa.
- [x] Definir una rúbrica común para el proyecto.
  - Adecuación del diseño, funcionamiento técnico y evaluación.
  - Responsabilidad, privacidad, seguridad, documentación y comunicación.

## Distribucion orientativa de 90 horas

| Bloque | Horas |
| --- | ---: |
| Tema 1: Introduccion y fundamentos de IA, con uso responsable | 6 |
| Busqueda, planificacion, optimizacion y CSP | 23 |
| Sistemas expertos, reglas y logica difusa | 14 |
| PLN, embeddings, Transformers y RAG | 22 |
| Vision y robotica | 10 |
| Proyecto integrador | 15 |
| **Total** | **90** |
