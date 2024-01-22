docker --version  
docker run hello-world  
docker pull busybox   
docker images   
docker run busybox   
docker run busybox echo "hello"  
docker ps   
docker ps -a    
docker run -it busybox sh   
docker rm <container_id>   

docker run -d -P --name gif learning/gif      
docker ps    
docker port gif   
docker stop gif   
docker run -p 8888:5000 learning/gif   
docker build -t gifv2 .   
docker run -p 8888:5000 gifv2    
docker login   
docker build -t yourusername/gif .  
docker push yourusername/gif  
