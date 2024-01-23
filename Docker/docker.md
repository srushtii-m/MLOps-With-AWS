## Dockerizing Linear Regression using PyTorch and Docker

Step 1: Clone the repository   
git clone https://github.com/srushtii-m/MLOps-With-AWS

Step 2: Build docker image  
cd MLOps-With-AWS/Docker  
docker build -t linear_regression_docker .  

Step 3: Run the Docker Container   
docker run linear_regression_docker
