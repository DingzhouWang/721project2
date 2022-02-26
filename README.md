# 721project2

# Gradient Descent with GCP
## Introduction 
The web applciatoin can help us calculate the gradient descent. We should input our function, start point, and epsilon. The application utilizes Containers and Kubernetes, and use Cloud Run to deploy the service. \
Users can pull the container image from dockerhub or Container Registry and run in their local environment. \
And of course, the microservice has default input. 

<img width="841" alt="image" src="https://user-images.githubusercontent.com/31728012/155854194-8722f4b9-01ca-4b1e-824f-1cfc33cff1c0.png">


## How to run the app
1. Directly go to website [this link](34.111.205.68)
2. Run in local : `make` or `python3 app.py`
3. Pull image from Dockerhub : `docker pull dyzhou66/flask-ml:latest` and then `docker run -p 8080:8080 dyzhou66/flask-ml`

## Kubernetes
We can deploy this project to a Kubernetes cluster with:
```bash
kubectl apply -f https://raw.githubusercontent.com/DingzhouWang/721project2/master/kubernets-deployment.yaml

# or clone the repository

kubectl apply -f ./kubernetes-deployment.yaml
```

## Tech Used
Flask \
Docker \
Kubernetes \
Google Kubernetes Engine \
Google Container Registry \
Cloud Run
