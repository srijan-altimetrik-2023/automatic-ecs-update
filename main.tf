terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "4.45.0"
    }
  }
}



# Define the provider and region
provider "aws" {
  region = "ap-south-1"
}

# Create an ECS cluster
resource "aws_ecs_cluster" "ecs_cluster" {
  name = "my-ecs-cluster"
}

# Create an EC2 instance
resource "aws_instance" "ecs_instance" {
  instance_type = "t2.micro"
  ami           = "ami-057752b3f1d6c4d6c"  # Replace with the desired EC2 instance AMI ID
  subnet_id     = "subnet-0f149076385f14b45"  # Replace with the desired subnet ID

  tags = {
      Environment = "Prod"
      Application = "Testing"
      Project = "CloudOps"
      Owner = "mnageti@altimetrik.com"
      Name = "tf_ec2"
  }

  # Attach the ECS cluster instance to the cluster
  user_data = <<-EOF
              #!/bin/bash
              echo ECS_CLUSTER=${aws_ecs_cluster.ecs_cluster.name} >> /etc/ecs/ecs.config
              EOF

  # Attach a security group to the instance
  vpc_security_group_ids = ["sg-0b2b80b19887446b4"]  # Replace with the desired security group ID
}


(* 

provider "aws" {
  region = "ap-south-1" 
}

resource "aws_instance" "instance" {
  ami = "ami-057752b3f1d6c4d6c"
  instance_type = "t2.micro"
  tags = {
      Environment = "Prod"
      Application = "Testing"
      Project = "CloudOps"
      Owner = "mnageti@altimetrik.com"
      Name = "tf_ec2"
  }
volume_tags = {
  Environment = "Prod"
      Application = "Testing"
      Project = "CloudOps"
      Owner = "mnageti@altimetrik.com"
      Name = "tf_ebs"
}
  lifecycle {
    create_before_destroy = true
  }
} *)
