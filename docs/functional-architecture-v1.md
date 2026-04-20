# PatternSight - Arquitectura Funcional v1

## Objetivo de esta arquitectura
Definir cómo se comporta el sistema desde el punto de vista funcional, antes de entrar a implementación técnica detallada.

La meta es ordenar el flujo de valor del producto: qué entra, qué transforma, qué aprende y qué entrega.

---

## Principio del sistema
PatternSight no analiza frames aislados como unidad principal.
La unidad importante del sistema debe ser una secuencia observable:
- ciclo
- ventana temporal
- evento compuesto
- tramo operativo

Eso permite modelar comportamiento, no solo apariencia.

---

## Flujo funcional general
1. ingesta
2. percepción visual
3. estructuración temporal
4. extracción de features
5. modelado de patrón
6. scoring y diagnóstico
7. visualización y salida

---

## Capa 1 - Ingesta
### Función
Recibir y normalizar entradas del sistema.

### Entradas posibles
- video monocular
- video estéreo
- IMU opcional
- metadata opcional

### Salida funcional
- fuente visual validada
- timestamps base
- datos listos para preprocesar

### Preguntas críticas
- hay sincronía entre fuentes
- hay suficiente calidad visual
- la duración es utilizable
- hay tramo operativo relevante

---

## Capa 2 - Percepción visual
### Función
Detectar elementos y movimiento observable del entorno.

### Capacidades base
- detección de objetos relevantes
- tracking
- localización relativa
- estimación de trayectorias visibles
- estado o fase observable si aplica

### Salida funcional
- objetos seguidos en el tiempo
- eventos visibles base
- trazas de movimiento

---

## Capa 3 - Estructuración temporal
### Función
Convertir flujo continuo en unidades operativas analizables.

### Capacidades base
- segmentar ventanas temporales
- detectar inicio/fin de secuencia
- agrupar microeventos en ciclo o patrón
- alinear video y sensores cuando existan

### Salida funcional
- secuencias estructuradas
- ciclos detectados
- ventanas comparables

### Esta capa es crítica
Aquí se define si el sistema realmente entiende comportamiento o solo acumula detecciones.

---

## Capa 4 - Extracción de features
### Función
Traducir secuencias en señales medibles.

### Features potenciales
- duración de ciclo
- variabilidad temporal
- velocidad relativa
- dirección y trayectorias
- permanencia por zona
- aceleración o jerk si hay sensores
- regularidad del patrón
- densidad de eventos
- relación entre objetos

### Salida funcional
- vectores o tablas por secuencia
- representación estructurada del comportamiento

---

## Capa 5 - Modelado de patrón
### Función
Aprender o definir qué se considera comportamiento estable, variable o anómalo.

### Capacidades iniciales
- baseline de comportamiento
- comparación entre secuencias
- detección de desviación
- drift temporal
- similitud entre ciclos

### Capacidades futuras
- predicción del siguiente estado
- clasificación automática de comportamiento
- recomendación basada en patrón observado

### Salida funcional
- patrón esperado
- secuencias fuera de norma
- drift o deterioro

---

## Capa 6 - Scoring y diagnóstico
### Función
Volver el análisis interpretable para uso operativo.

### Salidas clave
- score de consistencia
- score de anomalía
- drift temporal
- eventos relevantes
- comparación entre sesiones

### Resultado deseado
No solo mostrar datos, sino decir:
- qué cambió
- cuándo cambió
- qué tan importante es
- qué parte del patrón se degradó

---

## Capa 7 - Visualización y entrega
### Función
Presentar la información de forma accionable.

### Salidas posibles
- dashboard
- timeline operacional
- heatmaps o trazas
- tabla por ciclo o secuencia
- resumen ejecutivo
- alertas
- exportación de datos

### Regla
La visualización debe explicar el patrón, no distraer del patrón.

---

## Módulos funcionales del MVP
### Módulo A - Video Input
Carga y validación de video.

### Módulo B - Detection & Tracking
Objetos y trayectorias.

### Módulo C - Sequence Builder
Conversión de flujo a secuencias.

### Módulo D - Feature Engine
Extracción de señales cuantificables.

### Módulo E - Pattern Engine
Consistencia, anomalía y drift.

### Módulo F - Insight Layer
Interpretación y resumen.

### Módulo G - Dashboard
Entrega visual al usuario.

---

## Unidad de análisis recomendada
### No usar como unidad principal
- frame aislado

### Sí usar como unidad principal
- ciclo
- secuencia
- evento compuesto
- ventana temporal con contexto

Esto es central para la identidad del producto.

---

## Qué se puede medir de forma defendible en v1
- frecuencia de ciclo
- duración media y variabilidad
- estabilidad del movimiento
- repetición de secuencias
- desviaciones respecto al patrón base
- anomalías operativas visibles
- drift temporal simple

---

## Qué se deja para después
- simulación 3D avanzada
- predicción compleja de largo horizonte
- modelos profundos más caros
- soporte universal multiindustria
- gemelo digital completo

---

## Stack funcional viable con herramientas gratuitas
### Percepción
- OpenCV
- YOLO
- trackers abiertos

### Análisis
- NumPy
- Pandas
- scikit-learn
- PyTorch más adelante

### Visualización
- Streamlit o dashboard web ligero
- Plotly

### Datos
- archivos locales
- SQLite o PostgreSQL local si hace falta

---

## Criterio de éxito de la v1
La v1 funciona si logra esto:
- tomar video real
- estructurarlo en secuencias útiles
- generar métricas consistentes
- detectar al menos señales simples de desviación
- explicar hallazgos de forma clara

---

## Conclusión
La arquitectura funcional de PatternSight depende de una decisión clave: tratar el comportamiento como secuencia, no el video como colección de frames. Si esa base se respeta, el producto puede crecer desde una analítica útil hasta una capa predictiva y espacial mucho más fuerte.
