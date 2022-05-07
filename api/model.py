import insightface
from insightface.app import FaceAnalysis
from insightface.app.common import Face 
import cv2
import os 
import numpy as np 
import time 
import matplotlib.pyplot as plt
from path_processing import process_path

# '/home/giabao/.insightface/models/buffalo_l/w600k_r50.onnx'
def load_model(model_path):
    model = insightface.model_zoo.get_model(model_path)
    model.prepare(ctx_id=0)

    return model

def get_emb(model, img_path):
    t1 = time.time()
    img = cv2.imread(img_path)

    # generate bbox, assume that bbox is size of image
    h, w, d = img.shape
    bbox = [2, 2, w-1, h-1]
    bbox = np.array(bbox)

    # load landmark
    landmark = process_path(img_path)
    face = Face(bbox=bbox, kps=landmark, det_score=1)  # det_score dont affect to emb

    emb = model.get(img, face)
    t2 = time.time()
    print(t2-t1)
    return emb


if __name__=="__main__":
    model = load_model('/home/giabao/.insightface/models/buffalo_l/w600k_r50.onnx')
    img_path = '/home/giabao/Documents/face/face_verification/data/processed_data/ninh_ra/0028802154_134931_PLATE_0_1_337,10,362,10,349,25,342,35,360,35.png'
    img_path2 = '/home/giabao/Documents/face/face_verification/data/processed_data/thay_ra/3444605152_134536_PLATE_1_1_239,124,275,122,257,143,246,158,270,157.png'

    emb = get_emb(model, img_path)
    emb2 = get_emb(model, img_path2)
    print(emb==emb2)

    # img2 = cv2.imread('/home/giabao/Documents/face/face_verification/data/original_data/ninh_ra/0028802154_134931_PLATE_0.png')
    # t3 = time.time()
    # face_detect = model_face_detect.get(img2)  
    # t4 = time.time()
