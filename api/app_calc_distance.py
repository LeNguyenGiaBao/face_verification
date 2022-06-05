import numpy as np
from fastapi import FastAPI, Form
from fastapi.encoders import jsonable_encoder
import uvicorn
from typing import List
import numpy as np 
from distance import findEuclideanDistance, l2_normalize

# config
FACE_EMB_MODEL = "opencv"  # or "insightface"
ENCODE_TYPE = "string"  # or "base64"
MEASURE = "euclidean"

# Fast API
app = FastAPI()

@app.get("/")
def index():
    return {"name" : "giabao"}

@app.post("/distance/")
async def distance(in_emb_list: List[str] = Form(""), out_emb_list: List[str] = Form("")):
    try:
        if ENCODE_TYPE == "string": 
            if FACE_EMB_MODEL == "opencv":
                in_emb = np.array([np.fromstring(i, sep=',') for i in in_emb_list])
                out_emb = np.array([np.fromstring(i, sep=',') for i in out_emb_list])

                if len(in_emb_list) == 1:
                    in_emb = in_emb.reshape(-1, 128)
                if len(out_emb_list) == 1:
                    out_emb = out_emb.reshape(-1, 128)
        if MEASURE == 'euclidean': 
            distance = findEuclideanDistance(in_emb, out_emb)

        return jsonable_encoder({
            "code": 200,
            "distance": str(distance),
            "measure": MEASURE,
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
    uvicorn.run('app_calc_distance:app', host="127.0.0.1", port=8200, reload=True)