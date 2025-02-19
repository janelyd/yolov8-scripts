
# YOLOv8 Görüntü Sınıflandırma

# Drive'a bağlanma
from google.colab import drive
drive.mount("/content/drive")

!pwd
# %cd /content/drive/MyDrive/yolov8/1_image_classificaiton

# Ultralytics'i indir
# %pip install ultralytics

import ultralytics
ultralytics.checks()

# Sınıflandırma / Prediction

# Komutları kullanarak sınıflandırma işlemi
# Resim sınıflandırma / Test / Imagenet
!yolo classify predict model=yolov8l-cls.pt  source="https://upload.wikimedia.org/wikipedia/commons/1/18/Dog_Breeds.jpg" save=True
"""model=yolov8l-cls.pt: Kullanılacak modeli belirtir.
Burada "YOLOv8 large" sınıflandırma modeli kullanılıyor."""

# Sonuçları inceleme
import cv2
import imutils
from google.colab.patches import cv2_imshow
img_path = "/content/drive/MyDrive/yolov8/1_image_classificaiton/runs/classify/predict/Dog_Breeds.jpg"
#linkten aldıgımız görüntüyü okuma
img = cv2.imread(img_path)
# yeniden boyutlandırma
img = imutils.resize(img, width=640)
cv2_imshow(img)

#  AYnı işlemleri python kodu ile yazma
import numpy as np
from ultralytics import YOLO

img_path = "/content/drive/MyDrive/yolov8/1_image_classificaiton/runs/classify/predict/Dog_Breeds.jpg"
model_path = "/content/drive/MyDrive/yolov8/1_image_classificaiton/yolov8l-cls.pt"

model = YOLO(model_path) # modeli yükle
results = model(img_path) # resmi yğkle ve sınıflandır

# sınıflara ve sınıflara dair olasılıklara results üzerinden erişcez
class_dict = results[0].names # classlara dair sözlük, isim
probs = results[0].probs.data.tolist() # olasılıklara erişmek için

print("Sınıflar", class_dict)
print("Olasılıklar", probs)

# en yuksek olasılıga sahip sınıfı bulma
print("Sonuc", class_dict[np.argmax(probs)])


# ödev: cv2.putText() ile sonuçları resim üzerine yazdır

# //////////////////////////////////////////////////////////

image = cv2.imread(img_path)

# Window name in which image is displayed
window_name = 'Image'

# font
font = cv2.FONT_HERSHEY_SIMPLEX

# org
org = (320, 100)

# fontScale
fontScale = 3

# Blue color in BGR
color = (255, 0, 0)

# Line thickness of 2 px
thickness = 2

# Using cv2.putText() method
image = cv2.putText(image, 'Kopkee', org, font,
                   fontScale, color, thickness, cv2.LINE_AA)

# Displaying the image
cv2_imshow(image)

"""## Eğitim / Training"""

# ZIP biçiminde oldugu için dosyaları ayıklama
!unzip data/covid_classification.zip -d ./data

# Eğitim
# transfer öğrenme için model
# worker: aynı anda paralel olarak kaç birimin çalışacağı
# batch: görüntülerin kaçarlı olarak eğitime sokulacagı
# device=0: CUDA yı kullanmak için, artık egitim işlemi gpu uzerinden gerçekleşicek
# name: işlemlerin kaydolucağı dosyanın adı
!yolo classify train model= yolov8l-cls.pt data=data/covid_classification imgsz=224 workers=8 batch=16 device=0 epochs=25 name="yolov8_classification"

# eğitim yarıda kesilirse ne yapcagız?
# diyelim ki 10.adımda kesildi eğitim. son ağırlık last.pt'de kayıtlı olacak
!yolo classify train model= /content/drive/MyDrive/yolov8/1_image_classificaiton/runs/classify/yolov8_classification2/weights/last.pt resume=True

"""## COVID Sınıflandırma | Prediction"""

# bir modeli kullanarak sınıflandırma işlemi 2 yöntemi var
# 1. command line

# yolov8_classificaiton2 içindeki weights'ten best olanı seçtik
# inference'a gidip tüm resimleri tarayıp detection'ı yapıp kaydedecek
!yolo classify predict model= /content/drive/MyDrive/yolov8/1_image_classificaiton/runs/classify/yolov8_classification2/weights/best.pt source="/content/drive/MyDrive/yolov8/1_image_classificaiton/inference" save=True

# 2. python kodlarıyla

import numpy as np
from ultralytics import YOLO

# img_path olarak rastgele 1 tane görüntü seçtim inference'dan
img_path = "/content/drive/MyDrive/yolov8/1_image_classificaiton/inference/Normal-6.png"
# modelimin yolu en son train ettigim best.pt
model_path = "/content/drive/MyDrive/yolov8/1_image_classificaiton/runs/classify/yolov8_classification2/weights/best.pt"

model = YOLO(model_path) # modeli yükle
results = model(img_path) # resmi yğkle ve sınıflandır

# sınıflara ve sınıflara dair olasılıklara results üzerinden erişcez
class_dict = results[0].names # classlara dair sözlük, isim
probs = results[0].probs.data.tolist() # olasılıklara erişmek için

print("Sınıflar", class_dict)
print("Olasılıklar", probs)


# en yuksek olasılıga sahip sınıfı bulma
print("Sonuc", class_dict[np.argmax(probs)])

# ////////////////// cv2 putText ile
# name'de probs'u en yuksek çıkan SINIFI atadık
name = class_dict[np.argmax(probs)]

# max_prob'a direkt en yuksek çıkan olasılıgın SAYI DEGERINI atadık
max_prob= np.max(probs) * 100

print(name + " " + "%" + str(max_prob))

# yukarıdaki ifadeyi bir text degiskenine atayıp, resmin uzerine yazmak için çağırıcam
text = name + " " + "%" + str(max_prob)

#cv2.putText ile resim uzerine class ve olasılıkk bilgisini yazma:
image = cv2.imread(img_path)

# Window name in which image is displayed
window_name = 'Image'

# font
font = cv2.FONT_HERSHEY_SIMPLEX

# org
org = (50, 50)

# fontScale
fontScale = 1

# Blue color in BGR
color = (255, 100, 50)

# Line thickness of 2 px
thickness = 2

# Using cv2.putText() method
image = cv2.putText(image, text, org, font,
                   fontScale, color, thickness, cv2.LINE_AA)

# Displaying the image
cv2_imshow(image)
