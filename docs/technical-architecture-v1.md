# PatternSight - Arquitectura Técnica v1

## Objetivo
Traducir la arquitectura funcional a una estructura técnica ejecutable para un MVP.

---

## Stack técnico recomendado
### Lenguaje principal
- Python

### Percepción visual
- OpenCV
- YOLOv8 o equivalente open source
- tracker abierto, por ejemplo ByteTrack

### Procesamiento y análisis
- NumPy
- Pandas
- scikit-learn
- SciPy

### Modelado futuro
- PyTorch

### Dashboard inicial
- Streamlit

### Persistencia simple
- archivos locales JSON/CSV/Parquet
- SQLite si hace falta una capa mínima de base de datos

---

## Estructura de carpetas sugerida
```text
proyecto_deteccion/
  docs/
  data/
    raw/
    processed/
    interim/
  outputs/
  app/
    ingest/
    vision/
    sequence/
    features/
    patterns/
    scoring/
    dashboard/
  scripts/
  tests/
```

---

## Módulos técnicos

## 1. ingest
### Responsabilidad
- cargar videos
- validar formato
- leer sensores opcionales
- normalizar rutas y metadata

### Salidas
- objeto de sesión o dataset cargado

---

## 2. vision
### Responsabilidad
- detección
- tracking
- extracción de trayectorias

### Salidas
- objetos detectados
- tracks por frame o tramo

---

## 3. sequence
### Responsabilidad
- convertir tracks en secuencias
- detectar inicios/finales de ciclo
- crear ventanas de análisis

### Salidas
- secuencias estructuradas
- ciclos comparables

---

## 4. features
### Responsabilidad
- calcular métricas por secuencia
- duración
- variabilidad
- desplazamiento
- densidad de eventos
- suavidad si hay IMU

### Salidas
- tabla de features

---

## 5. patterns
### Responsabilidad
- baseline
- similitud entre secuencias
- anomalía simple
- drift temporal

### Salidas
- score de patrón
- score de anomalía
- drift

---

## 6. scoring
### Responsabilidad
- convertir señales en métricas interpretables
- generar resumen ejecutivo

### Salidas
- json
- tablas
- resumen textual

---

## 7. dashboard
### Responsabilidad
- exponer resultados en interfaz simple
- timeline
- scores
- tablas
- gráficos de evolución

---

## Pipeline MVP
1. cargar video
2. detectar y trackear
3. estructurar secuencias
4. extraer features
5. calcular consistencia y anomalía
6. visualizar resultados

---

## Inputs esperados del MVP
- un video de prueba
- opcionalmente IMU en formato estructurado

## Outputs esperados del MVP
- `outputs/report.json`
- `outputs/summary.md`
- visualización en dashboard
- tabla por secuencia

---

## Criterio de éxito técnico de v1
- correr sobre un video real
- producir secuencias válidas
- generar métricas consistentes
- mostrar una anomalía o drift simple de ejemplo
- exponer resultados en dashboard simple

---

## Riesgos técnicos actuales
- segmentación de secuencias mal definida
- tracking inestable en escenas complejas
- features poco informativas
- confusión entre microevento y ciclo completo

---

## Recomendación
No arrancar por red neuronal compleja. Primero consolidar:
- percepción
- secuencias
- features
- scoring interpretable

Luego sí introducir modelado temporal más fuerte.
