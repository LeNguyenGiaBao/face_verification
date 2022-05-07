import numpy as np
from fastapi import FastAPI, Form
from fastapi.encoders import jsonable_encoder
import uvicorn
from typing import List
import numpy as np 
from distance import findEuclideanDistance, l2_normalize


# Fast API
app = FastAPI()

@app.get("/")
def index():
    return {"name" : "giabao"}

@app.post("/distance/")
async def detect(in_emb_list: List[str] = Form(...), out_emb_list: List[str] = Form(...)):
    in_emb_array = np.fromstring(in_emb_list[0], sep=',')
    out_emb_array = np.fromstring(out_emb_list[0], sep=',')

    in_emb = in_emb_array.reshape(-1, 512)
    out_emb = out_emb_array.reshape(-1, 512)

    euclidean = findEuclideanDistance(in_emb, out_emb)
    return jsonable_encoder({
            "code": 200,
            "distance": str(euclidean),
            "msg": 'euclidean'
        })

if __name__ == "__main__":
    # run API
    uvicorn.run('app_get_distance:app', host="0.0.0.0", port=8200, reload=True)