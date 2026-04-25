# proyecto_deteccion

Base inicial del proyecto **PatternSight**, un sistema de inteligencia operacional predictiva orientado a aprender patrones desde video y sensores.

## Estado actual
Fase de documentación, scaffolding técnico e interfaz interactiva inicial del MVP.

## Documentos incluidos
- `docs/product-v1.md` — documento de producto
- `docs/functional-architecture-v1.md` — arquitectura funcional inicial
- `docs/technical-architecture-v1.md` — arquitectura técnica inicial
- `docs/propuesta-monitoreo-tanque-v1.md` — propuesta detallada del frente de detección de fugas en tanque

## Estructura base del MVP
- `app/ingest/` — carga de video y sensores
- `app/vision/` — detección y tracking
- `app/sequence/` — construcción de secuencias
- `app/features/` — extracción de features
- `app/patterns/` — scoring de patrón y anomalía
- `app/scoring/` — generación de salidas
- `app/dashboard/` — dashboard inicial con upload de video
- `main.py` — punto de entrada del pipeline
- `prototypes/tank_sim_python/` — prototipo Python para simulación de tanque, anomalías y alertas

## Ejecutar
### 1. Crear entorno virtual e instalar dependencias
```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

### 2. Correr pipeline
```bash
.venv/bin/python main.py ruta/al/video.mp4 --imu ruta/opcional/al/imu.npy
```

### 3. Ver dashboard interactivo
```bash
.venv/bin/streamlit run app/dashboard/app.py
```

En esa interfaz podrás subir videos y ver:
- metadata
- señal de movimiento
- secuencias estimadas
- scores iniciales

### 4. Ejemplo validado
```bash
.venv/bin/python main.py /data/.openclaw/workspace/hackathon/inbound_videos/left_13Deu2vxds0QTg3gdnvA3JhHo5k9KXZqK.mp4 --sample-stride 15
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

## Frente actual
Además del frente de video, este repo pasa a ser el repositorio principal del trabajo de detección de fugas y simulación de tanque. Aquí se subirá la propuesta, prototipos Python, evolución de lógica de detección y siguientes iteraciones del sistema.
