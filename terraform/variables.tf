variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Project name"
  type        = string
  default     = "eks-kubernetes-status-api"
}

variable "cluster_name" {
  description = "EKS cluster name"
  type        = string
  default     = "status-api-eks-cluster"
}