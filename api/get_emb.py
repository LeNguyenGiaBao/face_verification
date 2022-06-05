import cv2 
import base64
import numpy as np 
from get_landmark import get_landmark

def get_emb(model_name, model, image):
    contents = base64.b64decode(image)
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    cv2.imwrite('test.jpg', img)
    # landmark = get_landmark(img_path)
    # img_height, img_width = img.shape[0], img.shape[1]

    if model_name == "opencv":
        # TODO here: apply alignCrop function (hard)
        emb = model.feature(img)[0]

        return emb
    
    elif model_name == "arcface":
        # TODO: add arcface emb
        pass

if __name__=="__main__":
    from model import load_emb_model

    model_name = "opencv"
    model = load_emb_model(model_name)

    emb = get_emb(model_name, model, '/home/giabao/Documents/face/face_verification/api_opencv/noface.png')
    print(emb)