Contained within this repository is a set of code that enables image classification through the use of a pre-trained PyTorch model on the ImageNet dataset. In order to increase deployment efficiency, the model has been converted to ONNX format.

To run this code, there are several steps that need to be followed:

Download the model weights from the provided link.
Create and activate a virtual environment before installing the necessary requirements.
Convert the downloaded PyTorch model to an ONNX model by running the "convert_to_onnx.py" file, which will generate the "pytorch_model_weights.onnx" file.
Test the converted ONNX model on the CPU by running the "test_onnx.py" script which contains sample images for verification purposes.
Deploy the ONNX model by forking the public template on Banana Dev, cloning it to your local machine, copying the contents of this repository, updating the DockerFile to include the necessary files, and creating a new app linked to your forked repository.
Query the deployed model using the "test_server.py" script which makes a call to the deployed instance of the model on Banana Dev and prints the name of the predicted class, along with the time taken to make the call. Please note that you will need to use the keys provided in Banana Dev.