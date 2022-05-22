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

# img_vao = cv2.imread('./data/matvao_3444605152_134536_PLATE_6.png')
# img_ra = cv2.imread('./data/matra_3857309562_134850_PLATE_9.png')


# print(img_vao.shape)
# print(img_ra.shape)

# emb1 = app.get(img_vao)
# emb2 = app.get(img_ra)

# emb1 = emb1[0].embedding
# emb2 = emb2[0].embedding

# emb1 = l2_normalize(emb1)
# emb2 = l2_normalize(emb2)

# dis = findEuclideanDistance(emb1, emb2)
# print(dis)

ninh_vao = glob.glob('./data/ninh_vao/*.png')
ninh_ra = glob.glob('./data/ninh_ra/*.png')
thay_ra = glob.glob('./data/thay_ra/*.png')

print(len(ninh_vao))
print(len(ninh_ra))
print(len(thay_ra))

emb_ninh_vao = []
emb_ninh_ra = []
emb_thay_ra = []

for i in ninh_vao:
    img = cv2.imread(i)
    face = app.get(img)
    
    if face != []:
        emb = face[0].embedding
        emb_norm = l2_normalize(emb)
        emb_ninh_vao.append([i, emb_norm])

for i in ninh_ra:
    img = cv2.imread(i)
    face = app.get(img)
    
    if face != []:
        emb = face[0].embedding
        emb_norm = l2_normalize(emb)
        emb_ninh_ra.append([i, emb_norm])

for i in thay_ra:
    img = cv2.imread(i)
    face = app.get(img)
    
    if face != []:
        emb = face[0].embedding
        emb_norm = l2_normalize(emb)
        emb_thay_ra.append([i, emb_norm])

print(len(emb_ninh_vao))
print(len(emb_ninh_ra))
print(len(emb_thay_ra))

same = open('./data/ninh_vao_ra_cosine.csv', 'w')
for i in emb_ninh_vao:
    for j in emb_ninh_ra:
        dis = findCosineDistance(i[1], j[1])
        same.write('{},{},{}\n'.format(i[0], j[0], dis))

diff = open('./data/ninh_vao_thay_ra_cosine.csv', 'w')
for i in emb_ninh_vao:
    for j in emb_thay_ra:
        dis = findCosineDistance(i[1], j[1])
        diff.write('{},{},{}\n'.format(i[0], j[0], dis))