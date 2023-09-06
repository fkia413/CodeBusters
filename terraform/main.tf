terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 2.0"
    }
  }
}

# configure AWS provider
provider "aws" {
  region                  = "eu-west-2"
  shared_credentials_file = "~/.aws/credentials"
}

# create a new resource - testing for now
resource "aws_instance" "EC2" {
  ami           = var.ami-id
  instance_type = var.instance-type
}
