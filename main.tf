# Define the provider and region
terraform {
  backend "s3" {
    bucket     = "ami-automate-s3"
    key        = "state_updates.txt"
    region = "ap-south-1"
    access_key = "ASIASYQ3HBXP7LFULTGE"
    secret_key = format("AK_%s", filebase64sha256("/D12fL/mAdAFI8HG9nKiJ5gekFiBKjagkOqRDnMe"))
  }
}

provider "aws" {
  region = "ap-south-1"
}

# Create an EC2 instance
resource "aws_instance" "instance_updated" {
  ami = "ami-057752b3f1d6c4d6c"
  instance_type = "t2.micro"
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
}

