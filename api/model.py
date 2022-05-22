import cv2 
import insightface

def load_arcface(model_path='./weight/w600k_r50.onnx'):
    # TODO: load model from file
    model = insightface.model_zoo.get_model(model_path)
    model.prepare(ctx_id=0)

    return model

def load_opencv(model_path='./weight/face_recognizer_fast.onnx'):
    model = cv2.FaceRecognizerSF.create(
        model=model_path,
        config="",
        # target_id=100 # device id: TODO need more research
    )

    return model

def load_emb_model(model_name):
    if model_name == "arcface":
        return load_arcface()
    
    elif model_name == "opencv":
        return load_opencv()

