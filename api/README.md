# face_verification API

#### Update 22_05_03
- API work
- BUG: Call with Python Request: receive only one file
- TODO: Test on C#

### API for C#
```
var client = new RestClient("http://0.0.0.0:8100/verify/");
client.Timeout = -1;
var request = new RestRequest(Method.POST);
request.AlwaysMultipartFormData = true;
request.AddParameter("in_image_path", "/home/giabao/Documents/face/face_verification/data/processed_data/ninh_vao/3857309562_134850_PLATE_0_1_35,33,63,28,60,50,39,65,61,61.png");
request.AddParameter("in_image_path", "/home/giabao/Documents/face/face_verification/data/processed_data/ninh_vao/3857309562_134850_PLATE_1_1_34,33,59,27,58,48,41,63,59,58.png");
request.AddParameter("out_image_path", "/home/giabao/Documents/face/face_verification/data/processed_data/ninh_ra/0028802154_134931_PLATE_0_1_12,10,37,10,24,25,17,35,35,35.png");
request.AddParameter("out_image_path", "/home/giabao/Documents/face/face_verification/data/processed_data/ninh_ra/0028802154_134931_PLATE_1_1_12,10,37,10,24,25,17,35,35,35.png");
request.AddParameter("out_image_path", "/home/giabao/Documents/face/face_verification/data/processed_data/ninh_ra/0028802154_134931_PLATE_2_0_16,29,46,30,30,47,18,55,41,56.png");
IRestResponse response = client.Execute(request);
Console.WriteLine(response.Content);
```

### Result Format
- Success 
  ```
  {
      "code": 200,
      "distance": "0.93747157",
      "msg": "euclidean"
  }
  ```
  
  - Fail
  ```
  {
    "code": 201,   # error
    "error_code": 0,
    "msg": "error message"
  }
  ```
