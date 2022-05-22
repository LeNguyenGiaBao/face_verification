import cv2 
import requests
import glob 
import os

url = "http://0.0.0.0:8000/detect/"

data_path = '../data/original_data/ninh_ra/'
dest_data_path = data_path.replace('original_data', 'processed_data')
if not os.path.exists(dest_data_path):
    os.mkdir(dest_data_path)

for path in glob.glob(data_path + '*.png'):
    file_name = os.path.split(path)[1]
    payload={'name_cam': ''}
    files=[
    ('image',(file_name,open(path,'rb'),'image/png'))
    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    response = response.json()

    print(response)
    if response['code'] == 200 and response['data']<2:
        box = response['box1'].split(',')
        x,y,w,h = box
        x = int(x)
        y = int(y)
        w = int(w)
        h = int(h)
        landmark = response['landmark1']
        mask = str(response['data'])

        img = cv2.imread(path)
        face = img[y:y+h, x:x+w, :]

        new_file_name = file_name.replace('.png', '_'+mask+'_'+landmark+'.png')
        new_file_path = os.path.join(dest_data_path, new_file_name)

        cv2.imwrite(new_file_path, face)
