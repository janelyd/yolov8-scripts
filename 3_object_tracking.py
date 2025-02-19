# -*- coding: utf-8 -*-
"""3_object_tracking.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18cBciJLD_1O9exi_B1Eby-0G5kMOBTbh

# YOLOv8 Object tracking

## Ortam Hazırlıgı
"""

from google.colab import drive
drive.mount("/content/drive")

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/drive/MyDrive/yolov8/3_object_Tracking_counting

# Commented out IPython magic to ensure Python compatibility.
# %pip install ultralytics
import ultralytics
ultralytics.checks()

# object tracking: model egitiriz, goruntudeki resimleri bulur
# biz deteck edilen bu nesnelere id ekliyoruz.

"""## Test // Tracking

### Önceden eğitilmiş (pretrained) model ile nesne takibi
"""

!yolo track model=yolov8n.pt source="/content/drive/MyDrive/yolov8/3_object_Tracking_counting/data/test.mp4"

!yolo track model=yolov8n.pt source="data/test.mp4" tracker="bytetrack.yaml"
# tracker: takip modunu belirledik 1. boT track veya bytTrack var zaten
# tracker yazmadıgında default degeri boTrack

"""## Özgün model ile nesne takibi"""

# kendi modelimizi kullanmak istersek
# !yolo track model="custom_model_path" source=data/test.mp4 tracker="custom_tracker.yaml"