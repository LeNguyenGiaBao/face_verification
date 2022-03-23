import insightface
from insightface.app import FaceAnalysis
import cv2 
import numpy as np
import glob 
import os 
from utils import *

model_name = 'buffalo_m'
app = FaceAnalysis(name=model_name, allowed_modules=['detection', 'recognition']) # enable detection model only
app.prepare(ctx_id=0, det_size=(640, 640))

# app = insightface.model_zoo.get_model('/home/giabao/.insightface/models/buffalo_l/w600k_r50.onnx')
# app.prepare(ctx_id=0)

dataset_path = '../data_verify/KomNET_dataset/*/'
# dataset_path = '../data_verify/KomNET_dataset/Social Media/original_training_sosmed/train/*/*.*'

# print(len(glob.glob(dataset_path)))
sim_list = []
for folder in glob.glob(dataset_path):
    paths = glob.glob(folder + '*.*')[:2]
    path1 = paths[0]
    path2 = paths[1]

    img1 = cv2.imread(path1)
    img2 = cv2.imread(path2)

    emb1 = app.get(img1)[0].embedding
    emb2 = app.get(img2)[0].embedding
    if emb1.shape == emb2.shape:
        sim = findCosineDistance(emb1, emb2)
        print(sim)

        sim_list.append(sim)
    
print(len(sim_list))
with open('sim_same_person.txt', 'w') as f:
    for sim in sim_list:
        f.write(str(sim)+'\n')
    # exit()
