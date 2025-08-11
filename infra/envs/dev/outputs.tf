
output "vpc_id"             { value = module.vpc.vpc_id }
output "public_subnet_ids"  { value = module.vpc.public_subnets }
output "ecr_repository_url" { value = aws_ecr_repository.horse.repository_url }
output "tfstate_bucket"     { value = module.tf_state_bucket.bucket }
output "mlflow_bucket"      { value = module.mlflow_bucket.bucket }