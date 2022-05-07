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

#### Update 22_05_06
- API get embedding: return base64 (length decrease 10k -> 2k7)
- TODO: Make API for input file

#### Update 22_05_05
- API for get embbeding only
- add sample data
- TODO: make API for calculate distance


#### Update 22_05_03
- API work
- BUG: Call with Python Request: receive only one file
- TODO: Test on C#


### API

#### API Get Embbedding
Use: ```python app_get_emb.py```  
Url: ```http://127.0.0.1:8100/get_emb/```  
C#: 
```
var client = new RestClient("http://0.0.0.0:8100/get_emb/");
client.Timeout = -1;
var request = new RestRequest(Method.POST);
request.AlwaysMultipartFormData = true;
request.AddParameter("image_path", "/home/giabao/Documents/face/face_verification/data/processed_data/ninh_vao/3857309562_134850_PLATE_0_1_35,33,63,28,60,50,39,65,61,61.png");
IRestResponse response = client.Execute(request);
Console.WriteLine(response.Content);
```  

Input: path of image that crop and has landmark in file name  
Output:
```
{
    "code": 200,
    "emb": "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",
    "msg": "success"
}
```

Test in Python: ```python test_api/test_app_get_emb.py```
