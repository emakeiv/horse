locals {

  azs = slice(data.aws_availability_zones.available.names, 0, var.az_count)
  
  # derive /24 public subnets deterministically from the VPC CIDR
  # (e.g., 10.0.100.0/24, 10.0.101.0/24 for i=0,1)
  public_subnets = [for i, _ in local.azs : cidrsubnet(var.vpc_cidr, 8, 100 + i)]

  acct           = data.aws_caller_identity.me.account_id
  acct_id        = data.aws_caller_identity.me.account_id
  tf_bucket_name = "${var.project}-tfstate-${local.acct}-${var.aws_region}"
  ml_bucket_name = "${var.project}-mlflow-${local.acct}-${var.env}"

}