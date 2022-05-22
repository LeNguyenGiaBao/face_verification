import numpy as np
from fastapi import FastAPI, Form
from fastapi.encoders import jsonable_encoder
import uvicorn
from typing import List
import numpy as np 
from distance import findEuclideanDistance, l2_normalize
from utils import revert_from_base64

# Fast API
app = FastAPI()

@app.get("/")
def index():
    return {"name" : "giabao"}

@app.post("/distance/")
async def distance(in_emb_list: List[str] = Form(...), out_emb_list: List[str] = Form(...)):

    # ------------------------------ LIST -----------------------------------
    in_emb = np.array([np.fromstring(i, sep=',') for i in in_emb_list])
    out_emb = np.array([np.fromstring(i, sep=',') for i in out_emb_list])

    if len(in_emb_list) == 1:
        in_emb = in_emb.reshape(-1, 512)
    if len(out_emb_list) == 1:
        out_emb = out_emb.reshape(-1, 512)

    
    # -------------------------------- BASE64 --------------------------------
    # in_emb = np.array([revert_from_base64(i) for i in in_emb_list])
    # out_emb = np.array([revert_from_base64(i) for i in out_emb_list])

    euclidean = findEuclideanDistance(in_emb, out_emb)
    return jsonable_encoder({
            "code": 200,
            "distance": str(euclidean),
            "msg": 'euclidean'
        })

if __name__ == "__main__":
    # run API
    uvicorn.run('app_get_distance:app', host="0.0.0.0", port=8300, reload=True)