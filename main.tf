# Define the provider and region
terraform {
  backend "s3" {
    bucket     = "ami-automate-s3"
    key        = "state.txt"
    region = "ap-south-1"
    access_key = "AKIASYQ3HBXP4WF6HPY5"
    secret_key = "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"
  }
}
provider "aws" {
  region = "ap-south-1"
}



# Create an EC2 instance
resource "aws_instance" "instance" {
  ami = "ami-057752b3f1d6c4d6c"
  instance_type = "t2.micro"
  subnet_id = "subnet-04be86837ecdfbbc0"
  tags = {
      Environment = "Prod"
      Application = "Testing"
      Project = "CloudOps"
      Owner = "pawkumar@altimetrik.com"
      Name = "SCP_test"
  }
  volume_tags = {
      Environment = "Prod"
      Application = "Testing"
      Project = "CloudOps"
      Owner = "pawkumar@altimetrik.com"
      Name = "SCP_test"
  }
  vpc_security_group_ids = ["sg-01e24941edc06d626"]
}

