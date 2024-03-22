# Key Value Store

Engineered a key-value store using Kubernetes (k8s), FastAPI, and Huey as a REDIS queue that can scale reliably across multiple pods/deployments.

## Prerequisites

git, docker, minikube, kubectl

## Set up

```bash
# Clone the project
git clone https://github.com/mukul7661/camb.ai-backend-assessment
cd camb.ai-backend-assessment

# Build the docker iamge and push to Docker hub
docker build -t yourimage .
docker tag fastapi-huey-app:latest yourdockerhubusername/fastapi-huey-app:latest
docker push yourdockerhubusername/fastapi-huey-app:latest

# Now replace the image name in app-deployment.yaml
# Start minikube
minikube start

# Apply the services and deployments
kubectl apply -f app-deployment.yaml
kubectl apply -f app-service.yaml
kubectl apply -f redis-deployment.yaml
kubectl apply -f redis-service.yaml

# Forward the port to access traffic
kubectl port-forward service/fastapi-service 8000:80
```

## Usage

```bash

# Set the value in the store
curl -X POST http://localhost:8000/set/mykey -H "Content-Type: application/json" -d '{"value": "myvalue"}'

# Get the value from the store
curl -X GET http://localhost:8000/get/myKey

```
