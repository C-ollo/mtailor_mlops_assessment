import banana_dev as banana
import time
import base64

def test_server():
    api_key = ""
    model_key = ""
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

