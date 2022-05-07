import uvicorn
from fastapi import FastAPI, Form
from fastapi.encoders import jsonable_encoder
import numpy as np 
from model import load_model, get_emb
from distance import l2_normalize
import base64
import time 

# Model
model_path = '/home/giabao/.insightface/models/buffalo_l/w600k_r50.onnx'
model = load_model(model_path)

# Fast API
app = FastAPI()

@app.post("/get_emb/")
async def get_emb_image(image_path: str = Form(...)):
    emb = get_emb(model, image_path)
    emb_norm = l2_normalize(emb)


    # -------------------------------- BASE64 --------------------------------
    emb_norm_bytes = base64.b64encode(emb_norm)
    emb_norm_string = emb_norm_bytes.decode("utf-8")

    # # to revert
    # t1 = time.time()
    # emb_norm_bytes_2 = str.encode(emb_norm_string)
    # emb_norm_bytes_2 = base64.b64decode(emb_norm_bytes_2)
    # emb_norm_2 = np.frombuffer(emb_norm_bytes_2, dtype=np.float32)

    # print(emb_norm_2 == emb_norm)
    # print(time.time() - t1)  # time revert: 0.0009162s


    # ------------------------------ LIST -----------------------------------
    # emb_norm_string = str(emb_norm.tolist())

    # # to revert
    # emb_converted = np.fromstring(emb_string[1:-1], sep=',')


    return jsonable_encoder({
            "code": 200,
            'emb': emb_norm_string,
            "type": 'list'
        })

if __name__ == "__main__":
    # run API
    uvicorn.run('app_get_emb:app', host="0.0.0.0", port=8100, reload=True)