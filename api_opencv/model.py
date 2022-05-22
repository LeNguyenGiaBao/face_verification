import cv2 

# cv2 check GPU
# print(cv2.cuda.getCudaEnabledDeviceCount())

def load_detect_model(detect_model_path):
    # https://docs.opencv.org/4.x/df/d20/classcv_1_1FaceDetectorYN.html
    detector = cv2.FaceDetectorYN.create(
        model=detect_model_path,
        config="",
        input_size=(320, 320),
        score_threshold=0.9,
        nms_threshold=0.3,
        top_k=5000
    )

    return detector 

def load_emb_model(emb_model_path):
    recognizer = cv2.FaceRecognizerSF.create(
        model=emb_model_path,
        config="",
        # target_id=100
    )

    return recognizer

if __name__=="__main__":
    # recognizer = load_emb_model("./weight/face_recognizer_fast.onnx")

    # print(recognizer)

    detector = load_detect_model("./weight/yunet.onnx")

    img = cv2.imread('../data/multi_face.jpg')
    # img = cv2.imread('noface.png')
    h, w, _ = img.shape 

    detector.setInputSize((w, h))
    success, faces1 = detector.detect(img)
    print(success)
    print(faces1)  # (4, 15)
    # print(faces1[0])
    face_detect = sorted(faces1, key=lambda x:(x[2]*x[3]), reverse=True)
    print(face_detect)


    x, y, w, h = faces1[0][:4].astype(int)
    face = img[y:y+h, x:x+w]
    cv2.imwrite('test.jpg', face)