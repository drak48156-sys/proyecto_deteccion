# PatternSight - Documento de Producto v1

## Nombre del producto
PatternSight

## Categoría
Sistema de inteligencia operacional predictiva.

## Resumen ejecutivo
PatternSight es una plataforma que convierte video y datos de sensores en inteligencia operacional accionable. Su objetivo no es solo detectar objetos o contar eventos, sino aprender patrones de comportamiento operativo, identificar desviaciones, medir consistencia y anticipar degradación o anomalías en procesos repetitivos.

El producto está pensado para operaciones donde existe video disponible, pero donde esa información todavía no se transforma en diagnóstico, optimización o alerta temprana.

---

## Problema
Hoy muchas operaciones generan video constantemente, pero ese video queda como archivo pasivo o como monitoreo manual. Eso produce varios problemas:

- no se detectan patrones de pérdida de eficiencia con claridad
- no existe una lectura estructurada del comportamiento operativo
- es difícil comparar ciclos o sesiones
- las desviaciones se detectan tarde
- la supervisión depende demasiado de revisión manual
- se desaprovecha una fuente de datos valiosa ya existente

En contextos repetitivos, esto significa que hay comportamiento observable que sí puede medirse, pero no se está convirtiendo en decisión.

---

## Solución
PatternSight toma secuencias de video, y opcionalmente datos de sensores como IMU, para construir una representación del comportamiento operativo. A partir de eso:

- detecta fases del proceso
- segmenta ciclos o secuencias repetitivas
- calcula estabilidad y variabilidad
- identifica drift temporal
- detecta anomalías o comportamientos fuera de patrón
- genera métricas, alertas e insights accionables

PatternSight no se posiciona como un simple sistema de visión por computador. Se posiciona como una capa de inteligencia sobre procesos visibles.

---

## Qué hace realmente
### Entradas
- video monocular o estéreo
- sensores opcionales, como IMU
- metadata operacional opcional

### Procesamiento
- detección y tracking
- segmentación temporal
- extracción de features
- modelado de patrones
- scoring y diagnóstico

### Salidas
- score de consistencia
- score de anomalía
- drift temporal
- eventos relevantes detectados
- timeline operacional
- dashboard de análisis
- recomendaciones o alertas operativas

---

## Qué no promete todavía
Para evitar inflar el producto de forma poco defendible, PatternSight no debe prometer en su primera etapa:

- gemelo digital completo
- reconstrucción 3D total de alta precisión
- predicción universal para cualquier industria
- precisión perfecta de comportamiento futuro
- reemplazo de supervisión humana
- tonelaje exacto o métricas físicas no observables directamente

Estas capacidades podrían aparecer más adelante como capas avanzadas, pero no deben ser el centro del MVP.

---

## Cliente ideal inicial
El cliente ideal inicial está en entornos donde existe:

- operación repetitiva
- registro en video
- necesidad de comparar desempeño
- oportunidad de optimización
- interés en detectar desviaciones antes de que generen pérdidas mayores

### Sectores potenciales
- minería
- industria
- logística
- patios operativos
- construcción
- plantas con procesos repetitivos visibles

### Primer caso de uso recomendado
Operaciones repetitivas donde el ciclo puede observarse en video, segmentarse y compararse.

Ejemplos:
- carga y descarga
- movimiento repetitivo de maquinaria
- flujo visible de equipos o vehículos
- secuencias operativas con fases distinguibles

---

## Propuesta de valor
PatternSight convierte video en una capa de inteligencia operacional.

No solo muestra qué pasó. Ayuda a responder:
- cuál es el patrón operativo normal
- dónde empieza a degradarse
- qué secuencias se desvían
- qué sesiones son más consistentes
- qué señales anticipan pérdida de eficiencia o comportamiento anómalo

---

## Diferenciador
El diferenciador principal no es usar visión por computador. Tampoco es usar machine learning por sí solo.

El diferenciador es:

### Modelar comportamiento operativo
PatternSight no se queda en detectar objetos. Aprende secuencias, ciclos, regularidad, drift y desviaciones.

### Combinar visión y dinámica
Cuando haya sensores disponibles, puede combinar video con IMU u otras señales para mejorar lectura de movimiento y robustez del patrón.

### Orientarse a operación, no solo a observación
La meta no es contar cosas, sino convertir comportamiento observable en diagnóstico útil para decisión.

---

## MVP recomendado
### Objetivo del MVP
Demostrar que el sistema puede tomar video real, segmentar comportamiento repetitivo y devolver señales útiles sobre consistencia y anomalía.

### Alcance v1
- cargar video
- detectar/tracking básico
- segmentar secuencias o ciclos
- extraer features por ventana o ciclo
- generar score de consistencia
- generar score de anomalía
- mostrar resultados en un dashboard simple

### Salidas mínimas del MVP
- tabla por ciclo o ventana
- score de estabilidad
- score de anomalía
- timeline visual
- resumen textual con hallazgos

---

## Roadmap sugerido
### Fase 1 - MVP base
- ingesta de video
- tracking
- extracción de features
- scoring básico
- dashboard

### Fase 2 - Enriquecimiento temporal
- modelado de drift
- comparación entre sesiones
- alertas tempranas
- mejora de segmentación temporal

### Fase 3 - Integración de sensores
- uso de IMU
- sincronización video + sensores
- features mixtos
- mayor robustez del patrón

### Fase 4 - Inteligencia predictiva más fuerte
- predicción de secuencias
- clasificación de eventos
- anomalía avanzada
- probabilidad de degradación

### Fase 5 - Capa espacial / simulación
- reconstrucción espacial simple
- replay enriquecido
- vista 3D o semiespacial
- simulación como módulo avanzado

---

## Riesgos principales
- querer abarcar demasiadas industrias al inicio
- prometer 3D o predicción fuerte demasiado pronto
- no definir bien la unidad de análisis
- depender de datasets poco consistentes
- vender tecnología en vez de valor operacional

---

## Decisiones estratégicas actuales
- nombre preferido: PatternSight
- posicionamiento: sistema de inteligencia operacional predictiva
- primer foco: procesos repetitivos visibles en video
- prioridad: documentación, luego arquitectura, luego implementación
- enfoque técnico inicial: gratis y ejecutable con stack abierto

---

## Conclusión
PatternSight tiene potencial porque no parte de la idea genérica de “analizar video”, sino de una idea más fuerte: aprender patrones operativos desde secuencias observables y convertirlos en diagnóstico, anomalía y optimización.

Ese enfoque es más defendible, más escalable y más interesante como producto.
