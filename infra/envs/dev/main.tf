provider "aws" {
  region = var.aws_region
  profile = var.aws_profile
}

resource "aws_ecr_repository" "horse" {
  name                 = var.project
  image_tag_mutability = "MUTABLE"
  image_scanning_configuration { scan_on_push = true }
  tags = { Project = var.project, Env = var.env }
}

module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "5.5.0"

  name = "${var.project}-${var.env}-vpc"
  cidr = var.vpc_cidr

  azs             = local.azs
  private_subnets = []                                
  public_subnets  = [for i, _ in local.azs : "10.0.${i + 101}.0/24"]

  enable_nat_gateway = false                           
  single_nat_gateway = false
  enable_dns_support   = true
  enable_dns_hostnames = true

  map_public_ip_on_launch = true

  public_subnet_tags = {
    "kubernetes.io/role/elb"                     = "1"
    "kubernetes.io/cluster/${var.cluster_name}"  = "shared"
  }

  tags = { Project = var.project, Env = var.env }
}


module "tf_state_bucket" {
  source      = "./modules/s3"
  bucket_name = local.tf_bucket_name
  purpose     = "tfstate"
  tags        = { Project = var.project, Env = var.env }
}

module "mlflow_bucket" {
  source      = "./modules/s3"
  bucket_name = local.ml_bucket_name
  purpose     = "mlflow"
  tags        = { Project = var.project, Env = var.env }
}