import uvicorn
from fastapi import FastAPI, Form
from fastapi.encoders import jsonable_encoder
import numpy as np 

from model import load_emb_model
from get_emb import get_emb
from distance import l2_normalize
import base64
import time 

# config
FACE_EMB_MODEL = "opencv"  # or "insightface"
ENCODE_TYPE = "string"  # or "base64"

# load model
model = load_emb_model(FACE_EMB_MODEL)

# Fast API
app = FastAPI()

@app.get("/")
def index():
    return {"name" : "giabao"}

@app.post("/get_emb/")
async def get_emb_image(image_path: str = Form(...)):
    try:
        emb = get_emb(FACE_EMB_MODEL, model, image_path)
        emb_norm = l2_normalize(emb)

        if ENCODE_TYPE == 'string':
            emb_norm_string = str(emb_norm.tolist())[1:-1]

            return jsonable_encoder({
                "code": 200,
                "emb": emb_norm_string,
                "model": FACE_EMB_MODEL,
                "encode_type": ENCODE_TYPE
            })

        elif ENCODE_TYPE == 'base64':
            emb_norm_bytes = base64.b64encode(emb_norm)
            emb_norm_string = emb_norm_bytes.decode("utf-8")

            return jsonable_encoder({
                "code": 200,
                "emb": emb_norm_string,
                "model": FACE_EMB_MODEL,
                "encode_type": ENCODE_TYPE
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
    uvicorn.run('app_get_emb:app', host="0.0.0.0", port=8100, reload=True)