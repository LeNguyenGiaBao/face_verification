import cv2 
import numpy as np 
import time 

def get_emb(model, img_path):
    t1 = time.time()
    img = cv2.imread(img_path)

    # generate bbox, assume that bbox is size of image
    h, w, d = img.shape
    bbox = [2, 2, w-1, h-1]
    bbox = np.array(bbox)

    emb = model.get(img)
    t2 = time.time()
    print(t2-t1)
    return emb