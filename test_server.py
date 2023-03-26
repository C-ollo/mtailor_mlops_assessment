import banana_dev as banana
import time
import base64

def test_server():
    api_key = "8eb2c606-b6d1-4a61-aefe-d45b354e0ae4"
    model_key = "15db684c-155a-4393-8fbc-e753e6348c7b"
    with open('n01440764_tench.jpeg', 'rb') as f:
        image_data = f.read()   
    image_data = base64.b64encode(image_data).decode('utf-8')
    model_inputs = {'input': image_data}    
    start = time.time()
    out = banana.run(api_key, model_key, model_inputs)
    stop = time.time()
    print(out)
    print(stop-start)
    return out, stop-start

test_server()



