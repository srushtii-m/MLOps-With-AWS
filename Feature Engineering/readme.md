# SageMaker Feature Model Building

Using Sagemaker to preprocess and perform feature engineering.

## Dataset
[Moro et al., 2014] S. Moro, P. Cortez and P. Rita. A df-Driven Approach to Predict the Success of Bank Telemarketing. Decision Support Systems, Elsevier, 62:22-31, June 2014

## Overview
- This repository contains a Jupyter notebook that demonstrates using Amazon SageMaker Processing for data preprocessing in machine learning workflow.   
- SageMaker Processing is used for handling large-scale data processing tasks. The processed data can be retrieved from and saved back to an S3 bucket.  

## Feature engineering with sagemaker processing
I am using a pre-built Scikit-Learn container from SageMaker, which includes common functions and libraries.     
A custom Python script (feature_engineering_script.py) is employed for data processing.

### feature_engineering_script : 
1. Argument parsing:    
- The script uses argparse to define and parse command-line arguments.     
- Specific arguments include filepath (the input data directory), filename (the name of the dataset file), outputpath (the directory for saving processed data), and categorical_features (a list of categorical feature names in the dataset).    

2. Data Preprocessing Steps:
- The script reads the dataset from the specified input path using pandas.
- Dropping columns based on previous eda
- One-hot encoding categorical features
- Randomly splitting the dataset into training (70%), validation (20%), and testing (10%) sets.   

3. Data Storage:
- The processed datasets (training, validation, and test) are saved back to the specified output paths in a CSV format. This is in line with SageMaker's expectations for input data in training jobs.  

4. Integration with SageMaker:
- The script is designed to work within the SageMaker environment, adhering to its directory structure (/opt/ml/processing/input/ for inputs and /opt/ml/processing/output/ for outputs).  
- This structure is essential for SageMaker processing jobs, which automatically load input data from and save output data to these directories in an Amazon S3 bucket.

## Steps followed in feature-engineering-with-sagemaker-processing file:

1. Setting Up the Processing Job:   
- The input and output directories are set to opt/ml/processing/input and opt/ml/processing/output, respectively, as per SageMaker's requirements.
- The processed data is automatically loaded from and saved back to an S3 bucket upon job completion.

2. Importing and Preparing the Dataset:  
The dataset is imported and transformed using SageMaker Processing.

3. Instantiating the Sklearn Processor:  
- A SklearnProcessor object is created, specifying instance types and counts for the job.

4. Specifying Inputs and Outputs:  
- Inputs and outputs for the processing job are specified, including source and destination paths, input modes, and data distribution types.  
- This setup ensures data parallelization across multiple instances if used.  

5. Feature Engineering Script Details:
- The script uses an argument parser to easily run on different environments (cloud or local).  
- It performs preprocessing tasks such as encoding categorical features and splitting the dataset.  
- Outputs are saved in specified CSV formats in designated S3 paths.  

6. Executing the Processing Job:   
- The processing job is executed, and its status can be monitored via the SageMaker console.
- Once completed, the outputs are verified in the respective S3 bucket paths.   

