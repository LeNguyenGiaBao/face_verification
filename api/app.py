import torch
import cv2 
import numpy as np
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.encoders import jsonable_encoder
import asyncio
import uvicorn
from typing import List
from model import load_model, get_emb
from distance import findEuclideanDistance, l2_normalize

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
            emb = get_emb(model, path)
            emb = l2_normalize(emb)
            in_emb.append(emb)

        for path in out_image_path:
            emb = get_emb(model, path)
            emb = l2_normalize(emb)
            out_emb.append(emb)

        in_emb = np.array(in_emb)
        out_emb = np.array(out_emb)

        euclidean = findEuclideanDistance(in_emb, out_emb)
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
    # run API
    uvicorn.run('app:app', host="0.0.0.0", port=8100, reload=True)