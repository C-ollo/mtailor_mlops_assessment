Contained within this repository is a set of code that enables image classification through the use of a pre-trained PyTorch model on the ImageNet dataset. In order to increase deployment efficiency, the model has been converted to ONNX format.

To run this code, there are several steps that need to be followed:
1. Download the model weights from the provided link. https://www.dropbox.com/s/b7641ryzmkceoc9/pytorch_model_weights.pth?dl=0

2. Convert the dowloaded PyTorch model to an ONNX model.
The file `mtailormodel.onnx` will be created.
```
python convert_to_onnx.py
```

3. Test the converted ONNX model on the CPU by running the "test_onnx.py" script which contains sample images for verification purposes.

The model.py contains two classes - OnnxModel and Preprocessor - which provide functionality for loading and predicting with the ONNX model and pre-processing an input image, respectively, will be used in the tests.
```
pytest test_onnx.py
```


4. Deploy the ONNX model by forking the public template on Banana Dev, cloning it to your local machine, copying the contents of this repository, updating the DockerFile to include the necessary files, and creating a new app linked to your forked repository.
Query the deployed model using the "test_server.py" script which makes a call to the deployed instance of the model on Banana Dev and prints the name of the predicted class, along with the time taken to make the call. Please note that you will need to use the keys provided in Banana Dev.
```
ADD model.py .
ADD pytorch_model.py .
ADD pytorch_model_weights.onnx .
```
- Create a new app on Banana Dev and link it to your forked repository.
- Push to deploy.

5. Querying the deployed model.
- The test_server.py contains code to make a call to a deployed instance of the model on Banana Dev. It accepts the url of an image and prints the name of the predicted class. Additionally, it reports the time taken to make a call to the deployed model.
- NB: You'll need to use the keys provided in Banana Dev.
