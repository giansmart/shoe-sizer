import cv2
import numpy as np
import matplotlib.pyplot as plt
from ultralytics import YOLO


base_path = '../assets'
models_path = '../models'
image_path = f"{base_path}/magali_1_light.jpeg"

def get_best_detections(results):
    # Inicializar variables para guardar las mejores detecciones
    best_coin = None  # (x_center, y_center, score)
    best_foot = None  # (x_center, y_center, score)

    # Iterar sobre los resultados de las detecciones
    for box in results[0].boxes:
        # Extraer la clase, puntuación y coordenadas del cuadro delimitador
        cls = int(box.cls.numpy().item())  # Clase del objeto (0 para coin, 1 para foot, según data.yaml)
        conf = float(box.conf.numpy().item())  # Puntaje de confianza
        x1, y1, x2, y2 = box.xyxy.numpy()[0]  # Coordenadas del cuadro delimitador

        # Calcular el centro (x, y) del cuadro delimitador
        x_center = (x1 + x2) / 2
        y_center = (y1 + y2) / 2

        # Clasificar detecciones por clase
        if cls == 0:  # Clase "coin"
            if best_coin is None or conf > best_coin[2]:
                best_coin = (x_center, y_center, conf)  # Guardar mejor detección para "coin"
        elif cls == 1:  # Clase "foot"
            if best_foot is None or conf > best_foot[2]:
                best_foot = (x_center, y_center, conf)  # Guardar mejor detección para "foot"

    # Crear un diccionario con los resultados
    return {
        "coin": {"center": (best_coin[0], best_coin[1]), "score": best_coin[2]} if best_coin else None,
        "foot": {"center": (best_foot[0], best_foot[1]), "score": best_foot[2]} if best_foot else None
    }

def main():
    image = cv2.imread(image_path) # foot2
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    print('hello world')

if __name__ == "__main__":
    main()