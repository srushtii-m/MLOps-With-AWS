## Model Building

1. SageMaker Environment Setup    
- Retrieve Sagemaker execution role (ARN) and set up default S3 bucket and prefixes for storing data.
- Establish paths for training, validation and test data, where the processed data are stored in S3.  

2. Specify XGBoost Container
- Retrieve the image URI for the XGBoost container in the current AWS region.   

3. Instantiate estimator for Training
- XGBoost estimator is instantiated with specified parameters including the container URI, execution role, instance count and type, and output path for model artifacts.   
- Hyperparameters for the XGBoost model are set, such as max_depth, eta, and objective.    
- The fit method is called to start the training job, with the training and validation dataset locations provided.   

4. Monitoring and Completing the Training Job    
- After initiating the training job, its status can be monitored through the SageMaker console under the training jobs section.   
- The training job must complete before proceeding to the next steps, like model evaluation or deployment.

5.  Model Training Completion  
- The training job, using an ML.m4.xlarge EC2 instance, is confirmed to be completed in SageMaker. 
- The training is executed using the XGBoost algorithm.   

6. Model Deployment
- The model is deployed using SageMaker's deploy method.  
- The deployment is done on an instance of type ML.m4.xlarge.
- It creates a real-time HTTPS endpoint for the model.   
- The status of the endpoint can be monitored in the SageMaker console under "Endpoint Configuration".  

7. Model Prediction and Evaluation
- After deployment, the model's endpoint is used for making predictions.
- Test data (previously processed and stored in S3) is loaded into a DataFrame.  
- A custom function loops through the test data, sending mini-batches to the SageMaker endpoint for prediction.  
- Predictions are collected and converted from CSV output to an array format.   
- The performance of the model is evaluated using a confusion matrix.

## Model Deployment with end point configuration

1. Creating a SageMaker Model
- Setup model name and environment variables. 
- Using create_model method of the SageMaker client is used, specifying details like the container image (XGBoost in this case), model data location, environment variables, and the execution role.

2. Set up endpoint configuration  
- Define endpoint configuration name. 
- The create_endpoint_config method is used to create an endpoint configuration, specifying details such as the model name, instance type, and concurrency settings.  

3. Deploy the model
- An endpoint is created using the create_endpoint method, which initiates the deployment process of the model to a SageMaker endpoint.  

4. Invoking the endpoint
- The deployed model is tested by sending a payload to the endpoint using the invoke_endpoint method. This simulates how one would use the model for making predictions.   
- The responses from the endpoint are decoded to interpret the model's predictions.   


## Model Tuning

- Ranges for various hyperparameters like eta, min_child_weight, alpha, and max_depth are defined. SageMaker's hyperparameter tuning searches within these ranges.  
- Tuner Object Creation: A hyperparameter tuner object is created using the SageMaker estimator, the chosen metric (validation AUC), hyperparameter ranges, and configurations for the number of jobs and parallel executions.
- Once the tuning job is complete, the best performing job can be identified in the SageMaker console.  
- The best model from the hyperparameter tuning job is deployed using an ML instance. 
- An endpoint is created for the model, enabling it to be used for making predictions.