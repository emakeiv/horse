
variable "aws_region" {
  type        = string
  default     = "eu-north-1"
}

variable "project" {
  type        = string
  default     = "horse"
}

variable "env" {
  type        = string
  default     = "dev"
}

variable "profile" {
  type        = string
  default     = "default"
}

variable "vpc_cidr" {
  type        = string
  default     = "10.0.0.0/16"
} 

variable "az_count" {
  type        = number
  default     = 2
}

variable "enable_nat" {
  type        = bool
  default     = false
}

variable "cluster_name" {
  type        = string
  default     = "horse-dev"
}

variable "node_desired" { 
  type        = number
  default     = 1   
}

variable "node_min"  { 
  type         = number
  default      = 1 
}

variable "node_max"  { 
  type         = number
  default      = 2 
}

variable "node_instance_types" {
  type    = list(string)
  default = ["t3.small"]
}