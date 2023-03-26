# This file is used to verify your http server acts as expected
# Run it with `python3 test.py``

import requests
import base64
with open('n01440764_tench.jpeg', 'rb') as f:
        image_data = f.read()   
image_data = base64.b64encode(image_data).decode('utf-8')
model_inputs = {'input': image_data}    

res = requests.post('http://localhost:8000/', json = model_inputs)

print(res.json())