---
layout: default
title: Ficha de ejercicios 1.1 · Introducción a la IA
parent: 1. Introducción y fundamentos de la IA
nav_order: 2
nav_exclude: true
lang: es
---

# Ficha de ejercicios 1.1 · Introducción a la IA

**Duración orientativa: 50–60 minutos.** Trabaja individualmente o en pareja. Los casos son didácticos; no hace falta programar ni utilizar servicios externos. Anota las razones de tus decisiones: una etiqueta sin justificar no es suficiente.

## 1. Describe un agente: el robot aspirador

**Tiempo: 12 minutos.** Un robot aspirador recorre una casa, evita obstáculos, limpia y vuelve a la base cuando la batería está baja.

Completa la tabla con la información del caso. Si algún dato no está especificado, escribe «no indicado» en lugar de inventarlo.

| Componente | Descripción |
| --- | --- |
| Objetivo del agente | |
| Entorno | |
| Sensores: ¿qué puede percibir? | |
| Actuadores: ¿cómo puede actuar? | |
| Medida de rendimiento | |

1. Propón dos medidas de rendimiento que puedan entrar en conflicto, como el tiempo y el consumo de energía.
2. Describe una situación en la que una acción razonable con la información disponible tenga un resultado desfavorable.
3. Explica por qué «racional» no significa «siempre acierta».

## 2. Elige una técnica adecuada para la tarea

**Tiempo: 18 minutos.** Relaciona cada tarea con una técnica o combinación de técnicas. Puedes elegir entre cálculo o reglas, búsqueda, sistemas expertos, aprendizaje supervisado, no supervisado o por refuerzo, y generación de lenguaje con fuentes. Puedes repetir opciones.

| Tarea | Técnica probable | ¿Qué información necesita? | ¿Qué podría salir mal? |
| --- | --- | --- | --- |
| A. Calcular el importe de una compra a partir de precios y cantidades conocidos. | | | |
| B. Encontrar una ruta de coste mínimo en un mapa con calles cortadas. | | | |
| C. Clasificar mensajes como correo no deseado o legítimo a partir de ejemplos etiquetados. | | | |
| D. Agrupar peticiones similares cuando todavía no hay categorías asignadas. | | | |
| E. Aprender a jugar a un juego recibiendo una recompensa en cada partida. | | | |
| F. Redactar una respuesta a partir de un reglamento y señalar el fragmento que la justifica. | | | |
| G. Aplicar «si la temperatura supera el límite, activa la alarma» a una lectura de un sensor. | | | |

Después, elige dos filas y explica por qué una alternativa más sencilla o una combinación de técnicas podría ser mejor.

**Recuerda:** PLN, visión y robótica describen ámbitos o tipos de tarea; aprendizaje supervisado, búsqueda y reglas describen técnicas o mecanismos. Una aplicación puede combinar más de uno.

## 3. Compara decisiones con el rendimiento esperado

**Tiempo: 10 minutos.** Un robot puede llegar a una sala por una de dos rutas. Para simplificar, solo consideramos el tiempo total esperado.

| Ruta | Tiempo normal | Probabilidad de bloqueo | Tiempo adicional si se bloquea |
| --- | ---: | ---: | ---: |
| A | 8 min | 20 % | 20 min |
| B | 11 min | 2 % | 20 min |

Calcula el tiempo esperado de cada ruta con la fórmula «tiempo normal + probabilidad de bloqueo × tiempo adicional». ¿Qué ruta elegirías con este criterio?

1. Indica qué objetivo estás optimizando.
2. Di qué información podría cambiar la decisión (por ejemplo, consumo, seguridad o una restricción de paso).
3. Explica por qué esta elección no demuestra que el robot sea inteligente en cualquier otro sentido.

## 4. ¿Qué demuestra un hito?

**Tiempo: 10 minutos.** Para cada afirmación, escribe qué permite concluir el hito y qué no permite concluir. Si falta evidencia, especifica qué prueba adicional pedirías.

| Hito o ejemplo | Conclusión justificada | Conclusión que aún no está justificada |
| --- | --- | --- |
| Un programa gana una partida de ajedrez a una campeona. | | |
| Un sistema supera una prueba breve de conversación. | | |
| Un modelo clasifica imágenes con una tasa de acierto alta en un conjunto de prueba. | | |
| Un robot completa una tarea en un entorno controlado. | | |

## 5. Cierre breve: prepara el trabajo práctico

Elige una aplicación de IA que puedas documentar y completa este esquema en cinco líneas:

**Problema y usuario → entradas → técnica probable → salida o acción → resultado que buscaré en una fuente fiable.**

Antes de darla por buena, comprueba que sea una aplicación concreta y que las fuentes permitan distinguir los hechos de las afirmaciones promocionales. La [guía del trabajo práctico 1](treball-practic-1-es.md) explica el informe y los criterios de evaluación.

## Autoevaluación

Marca cada afirmación que ya puedes justificar con un ejemplo:

- [ ] Puedo describir un agente mediante su entorno, sensores, actuadores y una medida de rendimiento.
- [ ] Puedo distinguir una tarea de búsqueda, una regla y diferentes tipos de aprendizaje.
- [ ] Puedo explicar qué mide una prueba y qué no permite concluir.
- [ ] Puedo dar una razón por la que el sistema podría fallar en otro contexto.
