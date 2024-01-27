# Using Custom script in Sagemaker

## Tensorflow script - custom-script-tensorflow.ipynb

- Load the sagemaker environment and MNIST data from S3 public repository
- The TensorFlow script (mnist-tf2.py), for training a neural network model on the MNIST dataset within the AWS SageMaker environment is loaded. 
- mnist-tf2.py: 
Model Definition: A simple neural network for digit classification is created and compiled with TensorFlow, incorporating layers for flattening, dense processing, dropout, and softmax activation.  
Data Loading: Custom functions load the MNIST training and testing data from specified directories.   
SageMaker Integration: The script utilizes argparse to handle SageMaker-specific directories and environment variables, ensuring smooth integration with the platform.   
Training and Saving: The model is trained on the MNIST dataset and, if on the primary node of a distributed setup, saved in TensorFlow's SavedModel format in a SageMaker-designated directory.  
- Creating a Training Job  
SageMaker TensorFlow Estimator: A TensorFlow estimator is created using the SageMaker Python SDK. This estimator is responsible for managing the training job in SageMaker.  
Training Job Configuration: Parameters like entry point (Python script), role, instance count, instance type, and TensorFlow version are configured.  
Starting Training Job: The fit method is called on the estimator with the training data URI, initiating the training job in SageMaker.  
- Deploying the Model
Endpoint Deployment: Once training is complete, the model is deployed to a SageMaker endpoint using the deploy method.  
Endpoint Configuration: The instance type and count for the endpoint are specified.  
- Making Predictions
Data Preparation: Test data is downloaded and prepared for making predictions.  
Invoking Endpoint: The deployed model endpoint is used to make predictions on the test data.  

## Pytorch script - custom-script-pytorch.ipynb

- Prepare the environment and data. MNIST data is downloaded using torchvision.datasets.
- Pytorch script mnist_pytorch.py:
Sagemaker session is created and the MNIST dataset is downloaded using Torchvision, and tensor conversion and normalization are applied and uploaded to S3 bucket.   
The script uses environment variables set by SageMaker, such as SM_MODEL_DIR for model artifacts and SM_CHANNEL_TRAINING for training data.    
- A PyTorch estimator object is configured with the training script, IAM role, instance count and type, Python version, and hyperparameters (epochs and backend).    
- The fit method of the estimator is called with the S3 data path, launching the training job on SageMaker's infrastructure.  
- Post-training, the model is deployed to a SageMaker endpoint using the estimator's deploy method.   
- A subset of the MNIST test images is selected randomly for model evaluation and the test data is sent to the deployed model endpoint for prediction.    

