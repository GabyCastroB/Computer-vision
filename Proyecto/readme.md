# 👁️‍🗨️ Visión por Computadora para la Movilidad de Personas Invidentes en Ciudades  

Este proyecto fue desarrollado en el curso **Visión de Máquina** de la Universidad Nacional de Colombia.  
El objetivo principal es implementar un sistema de **detección y clasificación de objetos urbanos** que apoye la movilidad de personas con discapacidad visual, usando **redes neuronales convolucionales** y **procesamiento de imágenes**.  

---

## 📌 Resumen  
El proyecto consiste en el desarrollo de un software basado en **YOLOv5** entrenado sobre un dataset urbano (CARLA Dataset), con el fin de identificar objetos clave en entornos de ciudad:  

- 🚦 Semáforos (rojo, amarillo, verde)  
- 🚸 Pasos peatonales  
- 🚗 Vehículos  
- 🚲 Bicicletas  
- 🏍️ Motocicletas  
- 🚷 Señales de tránsito (30km, 60km, 90km)  
- 🚶 Personas  

El sistema procesa imágenes, detecta los objetos y comunica la información de manera que sirva de apoyo a personas con discapacidad visual.

---

## 🎯 Alcance  
- El modelo está diseñado para **entornos urbanos**: calles, andenes, puentes, etc.  
- Se centra en objetos clave para la movilidad segura.  
- Considera variaciones de iluminación y horarios (día/noche).  

---

## ⚙️ Herramientas y Tecnologías  

- **Lenguaje principal**: Python 🐍  
- **Frameworks de Deep Learning**: [PyTorch](https://pytorch.org/) + [Ultralytics YOLOv5](https://github.com/ultralytics/yolov5)  
- **Entorno de ejecución**: Google Colab  
- **Gestión de experimentos**: Comet.ml  
- **Datasets**:  
  - [COCO](https://cocodataset.org) (referencia inicial)  
  - [CARLA Dataset](https://www.kaggle.com/datasets/) (final, optimizado para tráfico y señales)  

---

## 🗂️ Base de Datos  

- **CARLA Dataset** (103 MB)  
- 10 clases de objetos relevantes para movilidad en ciudad.  
- Incluye anotaciones detalladas con **bounding boxes** y segmentación semántica.  

Ejemplo de anotación:  

```txt
[class_id] [x_center] [y_center] [width] [height]
3 0.512 0.624 0.214 0.198

## 🖼️ Ejemplo visual (imagen + caja delimitadora)

Ejemplo de anotación y detección en el dataset:

![Ejemplo dataset](docs/img/dataset_example.png)

---

## 🛠️ Preprocesamiento de Imágenes  

Se aplicaron las siguientes transformaciones antes de entrenar el modelo:  

- Conversión a **escala de grises**.  
- Redimensionamiento a **416x416 píxeles**.  
- Normalización de píxeles en rango `[0,1]`.  
- Normalización de **bounding boxes** al formato YOLO.  
- Aplicación de **filtro Gaussiano** para reducción de ruido.  

### Ejemplo:

| Imagen original | Imagen preprocesada |
|-----------------|----------------------|
| ![original](docs/img/original.png) | ![preprocesada](docs/img/preprocessed.png) |

---

## 🤖 Algoritmo de Detección  

Se utilizó **YOLOv5** por su rapidez y precisión en tiempo real.  

### Parámetros de entrenamiento  

- 📷 **Imágenes de entrenamiento**: 1600  
- 🧪 **Imágenes de validación**: 263  
- 📦 **Batch size**: 16  
- 🔁 **Epochs**: 80  
- 🏷️ **Clases**: 10  

---

### 🚀 Ejemplo de entrenamiento en Google Colab  

```python
# Clonar repositorio de YOLOv5
!git clone https://github.com/ultralytics/yolov5  
%cd yolov5

# Instalar dependencias
!pip install -r requirements.txt

# Entrenamiento del modelo
!python train.py --img 416 --batch 16 --epochs 80 --data data.yaml --weights yolov5s.pt

!git clone https://github.com/ultralytics/yolov5  
%cd yolov5
!pip install -r requirements.txt

# Entrenamiento
!python train.py --img 416 --batch 16 --epochs 80 --data data.yaml --weights yolov5s.pt

## 📊 Evaluación de Resultados  

### 🔹 Métricas clave  

- **mAP@0.5** ≈ 0.80  
- **mAP@0.95** ≈ 0.65  
- **Precision** ≈ 0.98  
- **Recall** ≈ 0.38 *(afectado por la perspectiva y la cantidad de ejemplos)*  

📌 Ejemplo de matriz de confusión:  

![Matriz de confusión](docs/img/confusion_matrix.png)  

---

### 🔹 Pérdida durante el entrenamiento  

- **Box loss, Obj loss y Cls loss** tienden a **cero** ✅  
- Buen equilibrio entre **precisión y recall**  

![Resultados entrenamiento](docs/img/train_results.png)  

---

## 🔍 Resultados de Predicción  

El modelo mostró muy buena precisión en condiciones estándar:  

| Detección de señales de tránsito y semáforo | Detección de vehículos y peatones |
|---------------------------------------------|----------------------------------|
| ![predicción1](docs/img/prediction1.png)    | ![predicción2](docs/img/prediction2.png) |

⚠️ En casos de **cambios de perspectiva** (ej. señales vistas de lado), la detección disminuye.  

📹 **Videos de prueba (diurnos y nocturnos):**  
- [Video 1](https://drive.google.com/file/d/1dYb0MZngtYF1aOs30iyHLgBVDCjSrcGb/view?usp=drive_link)  
- [Video 2](https://drive.google.com/file/d/1JtuEliXzeGDHh7GctchF1vozcavJTgXZ/view?usp=drive_link)  
- [Video nocturno](https://drive.google.com/file/d/1w4rRBnKMhH7vylNyhGoPzUjA0EoiaMLA/view?usp=drive_link)  

---

## ✅ Conclusiones  

- El **preprocesamiento de imágenes** es clave para reducir el tamaño y mejorar la eficiencia.  
- El modelo es **preciso**, pero pierde robustez ante variaciones de perspectiva.  
- Los resultados sugieren un buen desempeño general, pero requieren:  
  - Más datos en diferentes ángulos e iluminación.  
  - Ajustar umbrales de decisión para balancear precisión y recall.  

---

## 🔮 Trabajo Futuro  

- Ampliar el dataset con más condiciones (**clima, noche, distintas perspectivas**).  
- Entrenar con más clases y escenarios complejos.  
- Implementar **aprendizaje continuo** para que el sistema se adapte con nuevos datos.  
- Integrar **salida auditiva en tiempo real** para asistencia directa.  

---

## 👨‍💻 Autores  

- **Juan Nicolás Carvajal Useche**  
- **Gabriela María Castro Beltrán**  

📍 *Universidad Nacional de Colombia – Facultad de Ingeniería*  
👨‍🏫 *Profesor: Flavio Augusto Prieto Ortiz*  

---
