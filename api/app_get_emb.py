import uvicorn
from fastapi import FastAPI, Form
from fastapi.encoders import jsonable_encoder
import numpy as np 
from model import load_model, get_emb


# Model
model_path = '/home/giabao/.insightface/models/buffalo_l/w600k_r50.onnx'
model = load_model(model_path)

# Fast API
app = FastAPI()

@app.post("/get_emb/")
async def get_emb_image(image_path: str = Form(...)):
    emb = get_emb(model, image_path)
    emb_string = str(emb.tolist())
    
    # convert to numpy
    # emb_converted = np.fromstring(emb_string[1:-1], sep=',')
    return jsonable_encoder({
            "code": 200,
            'emb': emb_string,
            "msg": 'euclidean'
        })

if __name__ == "__main__":
    # run API
    uvicorn.run('app_get_emb:app', host="0.0.0.0", port=8100, reload=True)