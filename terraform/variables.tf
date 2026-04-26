variable "project_name" {
  description = "Project name prefix used for AWS resources."
  type        = string
  default     = "scalable-app"
}

variable "aws_region" {
  description = "AWS region for the EC2 instance."
  type        = string
  default     = "ap-south-1"
}

variable "instance_type" {
  description = "EC2 instance type."
  type        = string
  default     = "t3.medium"
}

variable "key_pair_name" {
  description = "Name for the AWS key pair."
  type        = string
}

variable "public_key_path" {
  description = "Path to the local SSH public key file."
  type        = string
}

variable "allowed_cidr" {
  description = "CIDR block allowed to access SSH and the Kubernetes API."
  type        = string
}
