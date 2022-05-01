import insightface
from insightface.app import FaceAnalysis
from insightface.app.common import Face 
import cv2
import os 
import numpy as np 
import time 

model = insightface.model_zoo.get_model('/home/giabao/.insightface/models/buffalo_l/w600k_r50.onnx')
model.prepare(ctx_id=0)

model_name = 'buffalo_m'
model_face_detect = FaceAnalysis(name=model_name, allowed_modules=['detection', 'recognition']) # enable detection model only
model_face_detect.prepare(ctx_id=0, det_size=(640, 640))

if __name__=="__main__":
    img_path = '../data/processed_data/ninh_vao/3857309562_134850_PLATE_0_1_330,90,358,85,355,107,334,122,356,118.png'
    file_name_extension = os.path.split(img_path)[1]
    file_name = os.path.splitext(file_name_extension)[0]
    file_name_components = file_name.split('_')
    landmark = file_name_components[-1].split(',')
    landmark = list(map(int, landmark))
    landmark = np.array(landmark)
    landmark = landmark.reshape((5, 2))
    print(landmark)

    img = cv2.imread(img_path)
    h, w, d = img.shape
    bbox = [0, 0, w-1, h-1]
    bbox = np.array(bbox)
    t1 = time.time()
    face = Face(bbox=bbox, kps=landmark, det_score=1.0)
    emb = model.get(img, face)
    t2 = time.time()
    print(emb.shape, t2-t1)

    img2 = cv2.imread('/home/giabao/Documents/face/face_verification/data/original_data/ninh_vao/3857309562_134850_PLATE_0.png')
    t3 = time.time()
    face_detect = model_face_detect.get(img2)  
    t4 = time.time()

    print(t4-t3)
    print(face_detect)
    print(face_detect[0]['embedding']-emb)
