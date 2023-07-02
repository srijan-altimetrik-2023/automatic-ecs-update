terraform {
backend "s3" {
    bucket     = "ami-automate-s3"
    key        = "state.txt"
    region = "ap-south-1"
  }

}
provider "aws" {
  region = "ap-south-1"
  default_tags {
    tags = {
      Environment = "Prod"
      Application = "Testing"
      Project = "CloudOps"
      Owner = "mnageti@altimetrik.com"
    }
  }
}
