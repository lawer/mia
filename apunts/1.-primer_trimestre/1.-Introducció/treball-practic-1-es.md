---
layout: default
title: "Trabajo práctico 1: análisis de una aplicación de IA"
parent: 1. Introducción y fundamentos de la IA
nav_order: 1
nav_exclude: true
lang: es
---

# Trabajo práctico 1: análisis de una aplicación de IA

## Propósito

Elige una aplicación real de inteligencia artificial y explica **qué problema resuelve, cómo funciona a grandes rasgos y qué técnicas estudiadas en el tema 1.1 reconoces en ella**. Termina valorando qué permite hacer, cuáles son los límites de las pruebas disponibles y qué información necesitarías todavía.

Con este trabajo cierras la primera parte del tema 1: aplicarás los conceptos de agentes, técnicas y ámbitos de uso a un caso concreto. En la sección 1.2 estudiarás con más detalle a las personas afectadas, los riesgos y los controles.

## Elección del caso

Puede ser una aplicación comercial, un servicio público o un prototipo de investigación. Elige un caso con suficiente información pública sobre la tarea y su funcionamiento; no hace falta que sea una aplicación creada por un equipo de I+D, pero sí necesitas encontrar al menos una fuente técnica o primaria fiable.

Ejemplos: un sistema de recomendación, un asistente de texto, una herramienta de traducción, un sistema de diagnóstico asistido, un detector de objetos, un robot o un agente que resuelve problemas mediante búsqueda. Puedes proponer otro caso si encuentras documentación que permita verificar cómo funciona.

**Alcance:** analiza una aplicación concreta y una tarea principal. No intentes explicar una empresa entera, una familia completa de modelos o «la IA en medicina» en general. No hace falta programar ni crear una cuenta en ningún servicio.

## Informe

Extensión orientativa: **4–6 páginas**, sin contar portada, bibliografía y anexos. Trabaja individualmente o en pareja, según la organización de la clase. Incluye estos apartados:

### 1. Identificación y resumen

- Nombre de la aplicación, organización o equipo responsable, año aproximado y fuentes consultadas.
- ¿Qué problema aborda y quién la utiliza?
- Resume en 100–150 palabras qué hace, qué técnica principal emplea y cuál es el resultado que has encontrado más relevante.

### 2. ¿Cómo funciona?

Describe el sistema como una aplicación concreta, no como una «caja mágica»:

| Elemento | Pregunta orientativa |
| --- | --- |
| Objetivo | ¿Qué intenta conseguir y cómo se podría medir si lo logra? |
| Entradas | ¿Qué información recibe: texto, imágenes, datos, acciones o estado del entorno? |
| Mecanismo | ¿Qué técnica transforma las entradas en una predicción, respuesta o acción? |
| Salida o acción | ¿Qué produce? ¿Se lo presenta a una persona o actúa sobre el entorno? |
| Contexto de uso | ¿En qué condiciones y con qué límites se utiliza? |

No todas las fuentes publican todos estos detalles. Cuando corresponda, indica **«no documentado en las fuentes consultadas»**; no rellenes los vacíos con suposiciones.

### 3. Relación con los conceptos del tema 1.1

Identifica la técnica o familia de técnicas y justifícala con evidencias de las fuentes. Según el caso, puedes hablar de reglas, búsqueda, optimización, aprendizaje supervisado, no supervisado o por refuerzo, redes neuronales, generación de lenguaje, visión o robótica. Explica solo las que sean pertinentes.

Distingue entre **técnica** y **ámbito de aplicación**: por ejemplo, PLN describe un ámbito, mientras que un modelo supervisado o un transformer describe mecanismos o arquitecturas que pueden utilizarse en él. Una misma aplicación puede combinar varias técnicas.

### 4. ¿Qué pruebas hay?

- ¿Qué resultados, ejemplos o métricas publica la fuente?
- ¿Con qué tarea, datos y condiciones se obtuvieron?
- ¿Hay una comparación con una alternativa o una referencia humana?
- ¿Qué **no** demuestran esos resultados? Señala al menos una limitación de las pruebas.

Separa los resultados medidos de las afirmaciones promocionales. Si no hay una evaluación pública, explícalo en lugar de atribuir al sistema una eficacia no comprobada.

### 5. Alcance y valoración final

En un párrafo o una tabla breve, resume:

- un beneficio concreto que respalden las fuentes;
- una limitación o situación en la que la técnica podría fallar;
- una pregunta importante que no puedas resolver con la información disponible;
- tu conclusión: **dónde parece útil y dónde no tienes pruebas suficientes para recomendarla**.

No hace falta realizar aquí una auditoría legal o ética completa. Reserva la pregunta «¿quién podría sufrir las consecuencias y qué controles hacen falta?» para el bloque 1.2.

### 6. Bibliografía y trazabilidad

Incluye al menos **tres fuentes**, citadas también en el cuerpo del informe:

1. Una **fuente primaria o técnica**: artículo original, documentación técnica, informe del equipo desarrollador o publicación del grupo de investigación.
2. Una fuente **académica o independiente** que aporte contexto, verificación o una perspectiva distinta.
3. Otra fuente fiable que haga falta para entender el ámbito o comprobar una afirmación concreta.

Para cada fuente, anota la autoría o entidad, el título, la fecha, el enlace y la fecha de consulta. Un buscador —Google Scholar, por ejemplo— sirve para encontrar publicaciones, pero no sustituye la referencia al artículo. Da prioridad a publicaciones, universidades, organismos públicos y documentación técnica identificable; no uses una publicación en redes sociales como única prueba de una afirmación.

## Exposición breve

Prepara una explicación de **3 minutos** con una sola diapositiva o esquema: problema → entradas → técnica → salida → evidencia y límite. El resto del grupo debe poder entender qué hace la aplicación sin leer el informe.

## Criterios de evaluación

| Criterio | Peso |
| --- | ---: |
| Problema, tarea y contexto bien delimitados | 20 % |
| Explicación del funcionamiento y conexión correcta con los conceptos del tema 1.1 | 30 % |
| Calidad, diversidad y cita de las fuentes | 20 % |
| Interpretación de los resultados y de sus limitaciones | 20 % |
| Claridad del informe y de la exposición | 10 % |

Se valora especialmente distinguir entre lo que confirma la documentación y lo que todavía es incierto. No se puntúa la complejidad técnica del sistema elegido: es preferible analizar bien una aplicación sencilla que describir una compleja solo con frases promocionales.

## Pregunta de transición al tema 1.2

Después de explicar cómo funciona, deja abierta esta pregunta: **si se empezara a utilizar la aplicación con personas reales, quién podría verse afectado, qué error sería más grave y quién debería poder revisarlo?** La retomaremos en el bloque siguiente.
