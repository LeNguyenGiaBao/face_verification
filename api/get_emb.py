import cv2 
from get_landmark import get_landmark

def get_emb(model_name, model, img_path):
    img = cv2.imread(img_path)

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