---
layout: default
title: Guía del proyecto final
parent: 10. Proyecto integrador
nav_exclude: true
lang: es
---

# Guía del proyecto final

## Reto

El servicio de soporte de un centro recibe peticiones sobre cuentas, red, impresoras y equipamiento de aula. El equipo construirá un **asistente de apoyo a la toma de decisiones** que:

1. clasifique y derive una incidencia mediante reglas explícitas;
2. recupere información de un corpus cerrado de documentos;
3. prepare un borrador de respuesta con referencias a las fuentes;
4. se abstenga cuando no encuentre pruebas suficientes y solicite revisión humana.

El asistente no diagnostica a personas, no pide contraseñas, no ejecuta acciones, no modifica tickets ni envía respuestas. La decisión y cualquier comunicación final corresponden a una persona.

## Requisitos funcionales

### 1. Clasificación y derivación

- Definid categorías útiles para el caso, por ejemplo **cuentas**, **red**, **impresión**, **equipamiento de aula** y **fuera de alcance**.
- Separad la categoría, la prioridad sugerida y la necesidad de revisión humana.
- Mantened las reglas en un lugar identificable y explicad por qué se activa cada una.
- Tratad los indicios de riesgo físico, seguridad o incidencia compartida como motivos de revisión urgente; no presentéis una hipótesis como un hecho confirmado.
- Si faltan datos o hay indicios contradictorios, derivad el caso a una persona.

### 2. Recuperación aumentada por generación (RAG)

- Indexad solo los documentos de prueba de la página de datos.
- Recuperad fragmentos pertinentes y mostrad el identificador y el título del documento.
- Si la consulta no está cubierta por el corpus, indicad que no hay pruebas y no improviséis instrucciones.
- Separad la calidad de la recuperación de la calidad de la respuesta: encontrar el documento correcto no garantiza que el resumen sea fiel.

### 3. Borrador de respuesta

- Generad un borrador breve en el idioma de la incidencia cuando sea posible.
- Cada afirmación operativa debe estar respaldada por fragmentos citados.
- No reveléis ni repitáis credenciales, datos personales innecesarios o instrucciones maliciosas incluidas en un ticket.
- Mostrad siempre el aviso **«Borrador pendiente de revisión humana»**.
- Podéis utilizar un LLM, un modelo local o una plantilla controlada. Si no hay un entorno autorizado, sustituid la generación por una respuesta simulada; no hace falta enviar datos a un servicio externo.

## Plan de trabajo: 15 horas

| Sesión | Horas | Tareas | Evidencia |
| --- | ---: | --- | --- |
| 1. Definir el sistema | 3 | Delimitar propósito y límites; identificar a las personas usuarias y afectadas; completar la ficha de riesgos; acordar arquitectura y pruebas de aceptación. | Diagrama y ficha de riesgos inicial |
| 2. Reglas de triaje | 3 | Definir categorías, derivaciones y reglas; implementar una traza que explique cada resultado; probar casos con información incompleta. | Reglas versionadas y pruebas |
| 3. Recuperar fuentes | 3 | Preparar el corpus, segmentar e indexar y recuperar fragmentos; mostrar citas; añadir abstención para consultas sin respaldo. | Búsqueda reproducible y medida de recuperación |
| 4. Redactar y poner a prueba | 3 | Conectar una plantilla o LLM; limitar el uso a las pruebas disponibles; probar inyección de instrucciones, datos sensibles y casos fuera de alcance. | Borradores y resultados de pruebas |
| 5. Integrar y defender | 3 | Ejecutar el conjunto completo de pruebas; corregir errores; documentar decisiones; hacer una demostración y una defensa breve. | Prototipo, memoria y presentación |

Las sesiones son una propuesta de distribución. Se pueden adaptar sin cambiar el total de 15 horas ni las entregas esenciales.

## Criterios técnicos de aceptación

- Las reglas devuelven categoría, derivación y un motivo trazable.
- En las incidencias cubiertas, el sistema recupera al menos un fragmento pertinente entre los tres primeros resultados en **8 de las 9** incidencias con respaldo documental.
- Las respuestas incluyen identificadores de fuentes y no afirman haber resuelto una incidencia.
- Las consultas fuera del corpus se abstienen en lugar de inventar una solución.
- Los casos de seguridad o riesgo físico llegan a revisión humana.
- Los casos equivalentes en valenciano y castellano reciben una categoría y una derivación equivalentes.
- Ninguna credencial de prueba se repite en la respuesta, y las instrucciones maliciosas dentro de un ticket no alteran las reglas del sistema.
- La aplicación no tiene ninguna herramienta que envíe mensajes o modifique sistemas externos.

Los umbrales son criterios para este conjunto sintético y pequeño; no demuestran que el sistema generalice a un servicio real.

## Entregas

1. **Prototipo o demostración reproducible** con reglas, recuperación de fuentes, borrador de respuesta y revisión humana.
2. **Diagrama de arquitectura** y breve justificación de las técnicas seleccionadas.
3. **Conjunto de pruebas** con resultados, errores detectados y acciones correctivas.
4. **Memoria técnica** de 3–5 páginas con propósito, datos, arquitectura, métricas, limitaciones y riesgos.
5. **Demostración de 5–7 minutos** que muestre un caso ordinario, uno con pruebas insuficientes y uno adversario o de alto riesgo.
6. **Ficha de riesgos final**, adaptada al prototipo construido.

## Memoria y defensa

La memoria debe explicar qué resuelve el sistema y qué no, por qué se eligieron reglas/RAG/generación u otras alternativas más sencillas, de dónde proceden los datos, qué muestran las pruebas y quién tiene la última palabra. Incluid al menos un error detectado durante las pruebas y el cambio realizado para reducir el riesgo.
