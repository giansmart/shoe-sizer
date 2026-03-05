# Shoe Sizer

Python-based tool for shoe size estimation, using an interactive web interface built with Gradio.

## Description

Shoe Sizer allows users to easily get shoe size recommendations. The project uses Gradio for the frontend, facilitating interaction with the processing logic in Python.

## Installation

The project uses Python 3.12.

1. Activate the virtual environment:
   ```bash
   source .venv/bin/activate
   ```

2. Install dependencies (if necessary):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To start the application:

```bash
python app.py
# Note: Replace 'app.py' with the name of your main script if different.
```

## Arquitectura

### Flujo de Datos
Este diagrama muestra cómo viajan los datos desde el usuario hasta obtener la predicción.

```mermaid
flowchart LR
    U[Usuario] -->|Imagen o medidas| G[Interfaz Gradio]
    G -->|Procesamiento| M[Logica del modelo]
    M -->|Calculo| P[Prediccion de talla]
    P -->|Resultado| G
```

### Arquitectura del Pipeline
Pipeline observado en los notebooks de `experiments` para estimar talla desde imagen.

```mermaid
flowchart TD
    I[Imagen de pie con moneda]

    subgraph V["Vision Pipeline"]
        direction TD
        D[YOLO deteccion coin y foot]
        P[Puntos de referencia centros]
        G[SAM segmentacion guiada]
        B[Bounding boxes desde mascaras]
    end

    subgraph FEA["Feature Engineering"]
        direction TD
        F[Features width height coin_width coin_height foot_width]
        C[Calibracion con diametro moneda 25.5 mm]
    end

    subgraph ML["Modelado y Salida"]
        direction TD
        M[Modelo de regresion XGBoost]
        O[Prediccion size_cm]
        E[Conversion a talla EU]
    end

    I --> D
    B --> F
    C --> M
    M --> O
    O --> E

    classDef input fill:#e8f1ff,stroke:#2563eb,stroke-width:2px,color:#0f172a;
    classDef vision fill:#ecfeff,stroke:#0891b2,stroke-width:1.5px,color:#0f172a;
    classDef feat fill:#f0fdf4,stroke:#16a34a,stroke-width:1.5px,color:#0f172a;
    classDef model fill:#fff7ed,stroke:#ea580c,stroke-width:1.5px,color:#0f172a;
    classDef output fill:#fef2f2,stroke:#dc2626,stroke-width:2px,color:#0f172a;

    class I input;
    class D,P,G,B vision;
    class F,C feat;
    class M model;
    class O,E output;
```
