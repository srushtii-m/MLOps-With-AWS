# Sagemaker Pipelines

## Training Pipeline

sagemaker-train-pipeline.ipynb: building a machine learning pipeline including data preprocessing, model training with hyperparameter tuning, model evaluation, and conditional model deployment based on performance metrics.   

## Inference Pipeline

sagemaker-inference-pipeline.ipynb: creating an inference pipeline and using batch transformation capabilities.

## Architecture of CI/CD Pipeline

### 1. Repository Creation in AWS CodeCommit     
- Store machine learning model source code and related files.    
- Manage model training and inference images.    

### 2. Utilizing Amazon S3:   
- Store raw data for preprocessing.     
- Save transformed datasets post-processing.    

### 3. Setting Up CI/CD Pipeline Assets:
- Use AWS CodeCommit and CodeBuild for pipeline automation components.     
- Test machine learning models locally to ensure functionality before deployment.      

### 4. Infrastructure Deployment using AWS CloudFormation:    
- Employ Infrastructure as Code (IaC) to deploy necessary resources for machine learning workflows.   

### 5. Automated Model Training with AWS SageMaker:     
- Facilitate automated model training processes using SageMaker.      

### 6. Managing MLOps Pipeline Deployment:    
- Deploy trained models to various environments like staging, development, or production.     
- Manage the transition of models between different environments.     

### 7. MLOps Pipeline Architecture:    
- Trigger the pipeline by uploading new or updated datasets or updating source code in AWS CodeCommit. 
- Implement AWS Lambda functions for initiating ETL processes and submitting AWS Glue jobs for data preprocessing and feature engineering.    
- Monitor the model training process in SageMaker using AWS CloudWatch events.    
- Incorporate training approval steps and conditional progression based on model training results.     
- Deploy the trained model using AWS CloudFormation and create a SageMaker endpoint for model serving.  
- Execute automated system tests using AWS Step Functions to evaluate model performance against predefined thresholds.     
- Proceed with deployment to production, implementing autoscaling policies and data capture for quality monitoring.     
- Complete the pipeline execution upon successful deployment to production.       