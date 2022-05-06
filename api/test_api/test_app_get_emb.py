import requests
import numpy as np 
import base64
import time 

url = "http://0.0.0.0:8100/get_emb/"

payload={'image_path': '/home/giabao/Documents/face/face_verification/data/processed_data/ninh_vao/3857309562_134850_PLATE_0_1_35,33,63,28,60,50,39,65,61,61.png'}
files=[

]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)
t1 = time.time()

response_json = response.json()
emb_str = response_json['emb']
emb_norm_bytes = str.encode(emb_str)
emb_norm_bytes = base64.b64decode(emb_norm_bytes)
emb_norm = np.frombuffer(emb_norm_bytes, dtype=np.float32)

t2 = time.time()
print(emb_norm.shape)
print(t2-t1)
