import os
import cv2
import matplotlib
import math
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import tensorflow_datasets as tfds

# Carga el conjunto de datos COCO
train_dataset , info = tfds.load(name="coco/2017", split="train",shuffle_files=True, with_info=True)
validation_dataset =tfds.load(name="coco/2017", split="validation",shuffle_files=False)
# Muestra información sobre el conjunto de datos
print(info)
