terraform {
  required_version = ">= 1.2.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.6"
    }
  }

  backend "s3" {
    bucket = "ajcurley"
    key    = "infrastructure/upwork/aprecisioncompany.tfstate"
    region = "us-east-1"
  }
}

provider "aws" {
  region  = "us-east-1"
  profile = "ci"
}

locals {
  project = "aprecisioncompany"
  env     = "dev"
}
