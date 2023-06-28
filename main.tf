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

resource "aws_vpc" "my_vpc" {
  cidr_block = "10.0.0.0/16"
}

# Create an ECS cluster
resource "aws_ecs_cluster" "my_cluster" {
  name = "my-cluster"
}

# Create an EC2 instance
resource "aws_instance" "my_instance" {
  instance_type = "t2.micro"
  ami           = "ami-0f5ee92e2d63afc18"  # Replace with the desired EC2 instance AMI ID
  subnet_id     = aws_vpc.my_vpc.id  # Replace with the desired subnet ID

  tags = {
      Environment = "Prod"
      Application = "Testing"
      Project = "CloudOps"
      Owner = "mnageti@altimetrik.com"
      Name = "tf_ec2"
  }

  # Attach the ECS cluster instance to the cluster
}
resource "aws_ecs_task_definition" "my_task_definition" {
  family                   = "my-task-family"
  container_definitions    = <<EOF
  [
    {
      "name": "my-container",
      "image": "nginx",
      "cpu": 256,
      "memory": 512,
      "portMappings": [
        {
          "containerPort": 80,
          "hostPort": 80
        }
      ]
    }
  ]
  EOF
}
resource "aws_ecs_service" "my_service" {
  name            = "my-service"
  cluster         = aws_ecs_cluster.my_cluster.id
  task_definition = aws_ecs_task_definition.my_task_definition.arn
  desired_count   = 1
  
  # Other service configuration options
}
