# proyecto_deteccion

Base inicial del proyecto **PatternSight**, un sistema de inteligencia operacional predictiva orientado a aprender patrones desde video y sensores.

## Estado actual
Fase de documentación y scaffolding técnico inicial del MVP.

## Documentos incluidos
- `docs/product-v1.md` — documento de producto
- `docs/functional-architecture-v1.md` — arquitectura funcional inicial
- `docs/technical-architecture-v1.md` — arquitectura técnica inicial

## Estructura base del MVP
- `app/ingest/` — carga de video y sensores
- `app/vision/` — detección y tracking
- `app/sequence/` — construcción de secuencias
- `app/features/` — extracción de features
- `app/patterns/` — scoring de patrón y anomalía
- `app/scoring/` — generación de salidas
- `app/dashboard/` — dashboard inicial
- `main.py` — punto de entrada del pipeline

## Ejecutar
### 1. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 2. Correr pipeline
```bash
python main.py ruta/al/video.mp4 --imu ruta/opcional/al/imu.npy
```

### 3. Ver dashboard
```bash
streamlit run app/dashboard/app.py
```

## Secuencia de trabajo
1. documentación de producto
2. arquitectura funcional
3. arquitectura técnica
4. scaffolding MVP
5. implementación real de módulos
6. validación

## Idea central
PatternSight no busca solo analizar video cuadro por cuadro. Busca aprender secuencias, ciclos, drift, anomalías y comportamiento operativo para convertirlos en señales útiles de decisión.
