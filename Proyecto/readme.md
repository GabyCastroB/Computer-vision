# 👁️‍🗨️ Computer Vision for Mobility Assistance of Visually Impaired People in Cities

This project was developed for the Machine Vision course at the National University of Colombia.
The main goal is to implement a system for the detection and classification of urban objects to support the mobility of people with visual impairments, using convolutional neural networks and image processing.  

---

## 📌 Summary  
The project consists of software based on YOLOv5 trained on an urban dataset (CARLA Dataset) to identify key objects in city environments:

- 🚦 Traffic lights (red, yellow, green)  
- 🚸 Crosswalks  
- 🚗 Vehicles  
- 🚲 Bicycles  
- 🏍️ Motorcycles  
- 🚷 Traffic signs (30 km/h, 60 km/h, 90 km/h) 
- 🚶 Pedestrians  

The system processes images, detects objects, and communicates the information in a way that can assist people with visual disabilities.

---

## 🎯 Scope  
- The model is designed for urban environments: streets, sidewalks, bridges, etc. 
- It focuses on objects that are critical for safe mobility.  
- It considers variations in lighting and time of day (day/night).

---

## ⚙️ Tools and Technologies 

- **Primary language**: Python 🐍  
- **Deep Learning frameworks**: [PyTorch](https://pytorch.org/) + [Ultralytics YOLOv5](https://github.com/ultralytics/yolov5)  
- **Execution environment**: Google Colab  
- **Experiment tracking**: Comet.ml  
- **Datasets**:  
  - [COCO](https://cocodataset.org) (initial reference)  
  - [CARLA Dataset](https://www.kaggle.com/datasets/) (final, optimized for traffic and signs)  

---

## 🗂️ Dataset  

- **CARLA Dataset** (103 MB)  
- 10 clases de objetos relevantes para movilidad en ciudad.  
- Includes detailed annotations with bounding boxes and semantic segmentation.  

Annotation example:  

```txt
[class_id] [x_center] [y_center] [width] [height]
3 0.512 0.624 0.214 0.198
```

## 🖼️ Visual example (image + bounding box)

Example of annotation and detection in the dataset:

![Dataset example](docs/img/dataset_example.png)

---

## 🛠️ Image Preprocessing

The following transformations were applied before training the model:

- Conversion to grayscale.  
- Resizing to 416×416 pixels.  
- Pixel normalization to the range [0, 1]. 
- Normalization of bounding boxes to YOLO format.  
- Application of a Gaussian filter for noise reduction.  

### Example:

|  Original image | Preprocessed image |
|-----------------|----------------------|
| ![original](docs/img/original.png) | ![Preprocessed](docs/img/preprocessed.png) |

---

## 🤖 Detection Algorithm 

YOLOv5 was chosen for its real-time speed and accuracy.

### Training parameters  

- 📷 **Training images**: 1600  
- 🧪 **Validation images**: 263  
- 📦 **Batch size**: 16  
- 🔁 **Epochs**: 80  
- 🏷️ **Clases**: 10  

---

### 🚀 Example training commands for Google Colab

```python
# Clonar repositorio de YOLOv5
!git clone https://github.com/ultralytics/yolov5  
%cd yolov5
```

# Install dependencies
```
!pip install -r requirements.txt
```
# Train the model
```
!python train.py --img 416 --batch 16 --epochs 80 --data data.yaml --weights yolov5s.pt
!git clone https://github.com/ultralytics/yolov5  
%cd yolov5
!pip install -r requirements.txt
```

# Training
```
!python train.py --img 416 --batch 16 --epochs 80 --data data.yaml --weights yolov5s.pt
```

## 📊 Evaluation Results 

### 🔹 Key metrics  

- **mAP@0.5** ≈ 0.80  
- **mAP@0.95** ≈ 0.65  
- **Precision** ≈ 0.98  
- **Recall** ≈ 0.38 *(affected by perspective and number of examples)*  

📌 Example confusion matrix:  

![Confusion matrix](docs/img/confusion_matrix.png)  

---

### 🔹 Training loss

- **Box loss, Obj loss y Cls loss** trend towards zero ✅  
- Good balance between precision and recall 

![Training results](docs/img/train_results.png)  

---

## 🔍 Prediction Results

The model showed very good precision in standard conditions:

|   Traffic sign & traffic light detection    |   Vehicle & pedestrian detection |
|---------------------------------------------|----------------------------------|
|  ![Prediction](docs/img/prediction1.png)    | ![Prediction2](docs/img/prediction2.png) |

⚠️ Detection performance decreases in extreme perspective changes (e.g., signs seen from the side).

📹 **Test videos (day and night):**  
- [Video 1](https://drive.google.com/file/d/1dYb0MZngtYF1aOs30iyHLgBVDCjSrcGb/view?usp=drive_link)  
- [Video 2](https://drive.google.com/file/d/1JtuEliXzeGDHh7GctchF1vozcavJTgXZ/view?usp=drive_link)  
- [Night Video](https://drive.google.com/file/d/1w4rRBnKMhH7vylNyhGoPzUjA0EoiaMLA/view?usp=drive_link)  

---

## ✅ Conclusions  

- Image preprocessing is essential to reduce input size and improve efficiency.  
- The model is accurate, but loses robustness under perspective variation.  
- Results indicate good overall performance, but improvements are needed:  
  - More data across different angles and lighting conditions.  
  - Tuning decision thresholds to balance precision and recall.

---

## 🔮 Future Work

- Expand the dataset with more conditions (weather, night, different perspectives).  
- Train with additional classes and more complex scenarios.  
- Implement continual learning so the system adapts to new data. 
- Integrate real-time audio output to provide direct assistance

---

## 👨‍💻 Authors  

- **Juan Nicolás Carvajal Useche**  
- **Gabriela María Castro Beltrán**  

📍 *Universidad Nacional de Colombia – Facultad de Ingeniería*  
👨‍🏫 *Profesor: Flavio Augusto Prieto Ortiz*  

---
