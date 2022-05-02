import torch
import cv2 
import numpy as np
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.encoders import jsonable_encoder
import asyncio
import uvicorn
from typing import List
from model import load_model, get_emb
from distance import findEuclideanDistance

# Model
model_path = '/home/giabao/.insightface/models/buffalo_l/w600k_r50.onnx'
model = load_model(model_path)

# Fast API
app = FastAPI()

@app.get("/")
def index():
    return {"name" : "giabao"}

@app.post("/verify/")
async def detect(in_image_path: List[str] = Form(...), out_image_path: List[str] = Form(...)):
    in_emb = []
    out_emb = []
    try:
        for path in in_image_path:
            print(path)
            emb = get_emb(model, path)
            in_emb.append(emb)

        for path in out_image_path:
            print(path)
            emb = get_emb(model, path)
            out_emb.append(emb)

        in_emb = np.array(in_emb)
        out_emb = np.array(out_emb)

        euclidean = findEuclideanDistance(in_emb, out_emb)
        print(euclidean)
        return jsonable_encoder({
                "code": 200,
                'distance': str(euclidean),
                "msg": 'euclidean'
            })

    except Exception as e:
        print(e)
        return jsonable_encoder({
                "code": 201,
                "error_code": 0,
                "msg": str(e)
            })

if __name__ == "__main__":
    # Scale
    # x = 650
    # y = 250
    # w = 700
    # h = 700

    # Model
    # model = torch.hub.load('ultralytics/yolov5', 'custom', './weights/best.pt')  # or yolov5m, yolov5l, yolov5x, custom

    # run API
    uvicorn.run('app:app', host="0.0.0.0", port=8100, reload=True)