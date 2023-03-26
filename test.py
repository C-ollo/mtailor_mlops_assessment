# This file is used to verify your http server acts as expected
# Run it with `python3 test.py``

import requests
import base64
import banana_dev as banana

api_key = "8eb2c606-b6d1-4a61-aefe-d45b354e0ae4"
model_key = "15db684c-155a-4393-8fbc-e753e6348c7b"
with open('n01440764_tench.jpeg', 'rb') as f:
        image_data = f.read()   
image_data = base64.b64encode(image_data).decode('utf-8')
model_inputs = {'input': image_data}    

res = requests.post('https://api.banana.dev/', json = model_inputs)

print(res.json())

out = banana.run(api_key,model_key,model_inputs)
print(out)