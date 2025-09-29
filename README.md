# Computer-vision
This repository contains a collection of Python-based computer vision projects and scripts, developed to explore various fundamental and applied concepts in the field. 🤖
## Interpolation 📝
This repository contains a computer vision project focused on image interpolation. Through a practical workshop, various interpolation techniques for image scaling are explored and applied, with the implementation provided in a Jupyter Notebook (Tarea1.ipynb).
### Interpolation Techniques :computer:
#### Nearest-Neighbor Interpolation
* Concept: This simple technique estimates the value of an unknown pixel by taking the value of the closest known pixel in the original image.
* Characteristics: Fast, but can produce blocky, jagged results with a pixelated look.
#### Bilinear Interpolation
* Concept: Uses a combination of linear interpolation in two directions (horizontal and vertical) to estimate the value of the new pixel from the four nearest surrounding pixels.
* Characteristics: Produces smoother results than nearest-neighbor and is more accurate, though it requires more computation.
### Other Techniques (mentioned)
* Bicubic Interpolation: More advanced, it considers 16 neighboring pixels to produce even smoother interpolation.
* B-splines: Uses segments of polynomial curves for a very smooth approximation of data.
## Colors 🌈
This repository contains a computer vision project focused on color space transformations. Through a series of experiments in a Jupyter Notebook (Tarea-2-Colores.ipynb), various color models are explored, including RGB, HSV, LAB, and YUV, using images related to urban mobility.
### Color Space Transformations
#### BGR to RGB
* Concept: Explores the simple channel swapping between the BGR format (common in OpenCV) and the more standard RGB format.
#### BGR to HSV
* Concept: Demonstrates the conversion from BGR to the HSV (Hue, Saturation, Value) model, which is based on human perception. This is particularly useful for color-based segmentation and manipulation.
#### RGB to YUV
* Concept: Shows the conversion from RGB to YUV, a color model used in video systems that separates luminance (brightness) from chrominance (color).
#### BGR to LAB
* Concept: Explains the conversion to the LAB color space, a perceptual model based on how humans see color. It separates lightness (L) from the green-magenta (a) and blue-yellow (b) components.
## Filters 🖼️
This repository contains a computer vision project focused on the application and evaluation of different filters for noise reduction, specifically multiplicative speckle noise. 
### Techniques Explored 🔬
#### Multiplicative Noise (Speckle)
* Generation: A function is implemented to add multiplicative noise to images with a controllable intensity, simulating the speckle noise found in radar images, ultrasounds, and other technologies.
* Evaluation: The effect of the noise is demonstrated on both real and synthetic images, showing how noise intensity affects visual perception. 
#### Lee Filter
* Implementation: The Lee filter is applied, a mathematical method designed to reduce speckle noise while preserving edges and textures.
* Evaluation: The filter is applied to the noisy images to demonstrate its effectiveness in removing noise
## Morphology 📝
This repository contains a computer vision project focused on morphological operations, specifically exploring directional dilation and thinning. The project, developed by Gabriela Castro and Juan Carvajal, is implemented in a Jupyter Notebook (Tarea4.ipynb).
### Key Features 🔑
* Directional Dilation: Implementation of an algorithm to dilate objects directionally, based on the relative position and distance of other nearby objects.
* Thinning: Code that implements the thinning operation, used to reduce objects to a single-pixel-wide line skeleton.
* Structuring Elements: Definition of specific structuring elements (kernels) for each direction, used in the directional dilation.
* Property Calculation: Functions to calculate the centroid and area of detected objects, key information for the directional dilation algorithm.
## Segmentacion 🔪
This repository contains a computer vision project focused on image segmentation, exploring techniques for delineating and identifying objects within images. 
### Key Features 🔑
#### Active Contours (Snakes):
Implementation of the Snake algorithm to segment objects based on an initial contour that iteratively adjusts to the object's boundaries by minimizing an energy function.
Demonstrates how internal (smoothness) and external (image gradient) energy terms influence the final segmentation.
#### SLIC (Simple Linear Iterative Clustering):
Exploration of the SLIC superpixel algorithm, which groups similar pixels into perceptually meaningful regions.
Used for efficiently segmenting images into superpixels based on color and proximity.
## Project Structure 📁
### 👁️‍🗨️ Computer Vision for Mobility of Visually Impaired Persons in Cities
This project was developed for the Machine Vision course at the National University of Colombia. The main objective is to implement a detection and classification system for urban objects to support the mobility of visually impaired persons, using convolutional neural networks and image processing.
####🗂️ Database
* CARLA Dataset (103 MB)
* 10 classes of objects relevant to urban mobility.
* Includes detailed annotations with bounding boxes and semantic segmentation.
#### ✅ Conclusions
* Image preprocessing is key to reducing size and improving efficiency.
* The model is accurate but loses robustness with perspective variations.
* Results suggest good overall performance, but require:
* More data with different angles and lighting.
* Fine-tuning decision thresholds to balance precision and recall.
## Requirements ✅
To run these notebooks, you will need to have Python and the necessary libraries installed.
