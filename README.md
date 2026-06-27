# EKS Kubernetes Status API

This project demonstrates how to deploy a containerized Python Flask API to Amazon EKS using Docker, Amazon ECR, Kubernetes manifests, Terraform, and AWS Load Balancer Controller.

## Project Overview

The application is a simple Status API built with Python Flask. It is containerized with Docker, pushed to Amazon ECR, and deployed to an Amazon EKS Kubernetes cluster.

The infrastructure is created using Terraform, and the application is deployed using Kubernetes manifests including Deployment, Service, and Ingress.

## Architecture

User
→ AWS Application Load Balancer
→ Kubernetes Ingress
→ Kubernetes Service
→ Kubernetes Pods
→ Docker Container
→ Flask Status API

## Technologies Used

* Python Flask
* Docker
* Amazon ECR
* Amazon EKS
* Kubernetes
* Kubernetes Deployment
* Kubernetes Service
* Kubernetes Ingress
* AWS Load Balancer Controller
* Application Load Balancer
* Terraform
* AWS IAM
* Helm
* eksctl

## API Endpoints

### Home

```http
GET /
```

Returns a basic success message.

### Health Check

```http
GET /health
```

Used to verify that the application is healthy.

### Status

```http
GET /status
```

Returns service status information.

Example response:

```json
{
  "environment": "dev",
  "managed_by": "Kubernetes",
  "platform": "Amazon EKS",
  "service": "eks-kubernetes-status-api",
  "status": "running",
  "version": "1.0.0"
}
```

## Deployment Flow

1. Build the Flask application.
2. Create a Docker image.
3. Test the container locally.
4. Create an Amazon ECR repository.
5. Push the Docker image to Amazon ECR.
6. Create EKS infrastructure using Terraform.
7. Connect local kubectl to the EKS cluster.
8. Deploy the application using Kubernetes manifests.
9. Expose the application using Ingress and AWS Load Balancer Controller.
10. Test the public Application Load Balancer endpoint.

## Terraform Infrastructure

Terraform creates the following AWS resources:

* VPC
* Public subnets
* Private subnets
* NAT Gateway
* EKS Cluster
* EKS Managed Node Group
* IAM roles
* Security groups

## Kubernetes Resources

The application is deployed using:

* Deployment
* Service
* Ingress

The Deployment runs two replicas of the Flask API. The Service routes traffic to the pods. The Ingress exposes the application through an AWS Application Load Balancer.

## Local Docker Test

```bash
docker build -t eks-kubernetes-status-api .

docker run -p 5001:5000 eks-kubernetes-status-api
```

Test locally:

```bash
curl http://localhost:5001/status
```

## Deploy Infrastructure

```bash
cd terraform

terraform init
terraform fmt
terraform validate
terraform plan
terraform apply
```

## Connect kubectl to EKS

```bash
aws eks update-kubeconfig \
  --region us-east-1 \
  --name status-api-eks-cluster
```

Check nodes:

```bash
kubectl get nodes
```

## Deploy Application to Kubernetes

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/ingress.yaml
```

Check resources:

```bash
kubectl get pods
kubectl get svc
kubectl get ingress
```

## Cost Management

This project is designed as a portfolio and learning project. The infrastructure can be deployed on demand using Terraform and destroyed after testing to avoid unnecessary AWS costs.

Destroy infrastructure:

```bash
cd terraform
terraform destroy
```

## What I Learned

* How to containerize a Flask application with Docker
* How to push Docker images to Amazon ECR
* How to create an EKS cluster using Terraform
* How Kubernetes Deployments manage pods
* How Kubernetes Services route traffic to pods
* How Ingress exposes applications externally
* How AWS Load Balancer Controller creates an ALB from Kubernetes Ingress
* How to deploy and test a containerized application on Amazon EKS
