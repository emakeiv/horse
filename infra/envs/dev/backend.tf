# terraform {
#   backend "s3" {
#     bucket         = "horse-tfstate"
#     key            = "dev/terraform.tfstate"
#     region         = "eu-north-1"
#     use_lockfile   = "horse-tf-locks"
#     encrypt        = true
#   }
# }
