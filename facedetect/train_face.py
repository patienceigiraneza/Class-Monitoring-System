import cv2
import os
import numpy as np
from PIL import Image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "images")

face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()

x_train = []
y_labels = []
current_id = 0
labels_id = {}

for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith('png') or file.endswith('jpg'):
            path = os.path.join(root, file)
            label = os.path.basename(os.path.dirname(path)).replace(' ', "-").lower()
            print(label, path)
            if not label in labels_id:
                labels_id[label] = current_id
                current_id += 1
            id_ = label_ids[label]
            print(label_ids)

            # x_train.append(path)
            # x_labels.append(label)
            pil_image = Image.open(path).convert('L')
            image_array = np.array(pil_image, "uint8")
            faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.1, minNeighbors=5)

            for (x,y,w, h) in faces:
                roi = image.image_array[y:y+h, x:x+w]
                x_train.append(roi)
                y_train.appent(id_)
