terraform {
  backend "s3" {
    bucket       = "horse-tfstate-961341508903-eu-north-1"
    key          = "envs/dev/terraform.tfstate"
    region       = "eu-north-1"
    use_lockfile = true
  }
}

