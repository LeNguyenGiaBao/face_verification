import requests
import time 
import glob 
import os

url = "http://0.0.0.0:8100/get_emb/"

num_files = len(glob.glob('../../data/processed_data_arcface/*/*.png'))
t1 = time.time()
for path in glob.glob('../../data/processed_data_arcface/*/*.*'):
    abs_path = os.path.abspath(path)
    payload={'image_path': '/home/giabao/Documents/face/face_verification/data/processed_data_arcface/ninh_ra/0028802154_134931_PLATE_0_1_12,10,37,10,24,25,17,35,35,35.png'}
    files=[]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)

t2 = time.time()
print("Total time", t2-t1)
print("Num files", num_files)
print("Time per file", (t2-t1)/num_files)

#Total time 1.3814163208007812
# Num files 25
# Time per file 0.05525665283203125