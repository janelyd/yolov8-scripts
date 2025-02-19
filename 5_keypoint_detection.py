# -*- coding: utf-8 -*-
"""5_keypoint_detection.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1d_b9ClL7wkaaBAV5knk2cYn9aNuiBx8U

# YOLOv8 Keypoint Detection

## Ortam Hazırlıgı
"""

from google.colab import drive
drive.mount('/content/drive')

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/drive/MyDrive/yolov8/5_keypoint_detection

# Commented out IPython magic to ensure Python compatibility.
# %pip install ultralytics

import ultralytics
ultralytics.checks()

"""## Test işlemleri | Prediction | Inference

"""

# 1. cli ile:
!yolo pose predict model=yolov8n-pose.pt source='/content/drive/MyDrive/yolov8/5_keypoint_detection/naimabi.jpg'  # predict with official model

import cv2
import imutils
from google.colab.patches import cv2_imshow

img_path = "/content/drive/MyDrive/yolov8/5_keypoint_detection/runs/pose/predict3/naimabi.jpg"

img = cv2.imread(img_path)
img = imutils.resize(img, width=450)

cv2_imshow(img)

"""## Aynı işlem ama Python ile

"""

import cv2
import imutils
import numpy as np
from ultralytics import YOLO
from google.colab.patches import cv2_imshow

img_path = "/content/drive/MyDrive/yolov8/5_keypoint_detection/naimabi.jpg"
model_path = "yolov8n-pose.pt"



img = cv2.imread(img_path)
model = YOLO(model_path)

results = model(img_path)[0] # bizim için anlamlı olanı depolardı 0. index

# eklem koordinalarını görme:
# result içindeki keypointlere erişmemiz lazım bunun için
for result in results:
  points = np.array(result.keypoints.xy.cpu(),dtype="int")
 # print(points)
  for point in points:
    for p in point:
      cv2.circle(img,(p[0],p[1]), 3 , (0,255,0),1)





# plotted_img = results.plot()

cv2_imshow(img)

"""## Eğitim // Training

### COCO8 veriseti ile eğitim
"""

!yolo pose train data=coco8-pose.yaml model=yolov8n-pose.pt epochs=20 imgsz=640 batch=8 workers=8 name=yolov8_pose_detection device=0
# transfer learning için model