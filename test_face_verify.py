from turtle import back
import insightface
from insightface.app import FaceAnalysis
import cv2 
import numpy as np
import glob 
import os 

model_name = 'buffalo_m'
app = FaceAnalysis(name=model_name, allowed_modules=['detection', 'recognition']) # enable detection model only
app.prepare(ctx_id=0, det_size=(640, 640))

dataset_path = '../data_verify/KomNET_dataset/Social Media/resize 224x224_sosmed/train/*/*.*'
for path in glob.glob(dataset_path):
    # extension = path.split('.')[-1]
    # if extension == "jpg" or extension == "png" or extension == "jpeg":
    background = np.zeros((500,500,3))
    print(path)
    img = cv2.imread(path)
    print(img.shape)
    background[100:324, 100:324, :] = img
    cv2.imwrite('test.jpg', background)
    print(app.get(background))
    exit()
