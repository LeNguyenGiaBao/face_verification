# face_verification API

## WORKFLOW
- Moto get in park:
    - Get image
    - Save image
    - When free: get and save embeding from [api](https://github.com/LeNguyenGiaBao/face_verification/blob/master/api/app_get_emb.py)
    - Assume that we have 10 images -> 10 embbeding 

- Moto get out park:
    - Get image
    - Get embbeding
    - Calculate with embeddings from IN (Assume 10 IN vs. 1 OUT)
    - Get distance and check threshold
    - Continue until accepted

- Advantage:
    - When OUT: Dont need enough images to calculate.


#### Update 22_05_05
- API for get embbeding only
- add sample data
- TODO: make API for calculate distance


#### Update 22_05_03
- API work
- BUG: Call with Python Request: receive only one file
- TODO: Test on C#
