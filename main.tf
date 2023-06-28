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
  region = "us-east-1"
}

resource "aws_vpc" "my_vpc" {
  cidr_block = "10.0.0.0/16"
  tags = {
        Environment = "Prod"
        Application = "Testing"
        Project = "CloudOps"
        Owner = "mnageti@altimetrik.com"
        Name = "tf_my_vpc"
    }
}

# Create an ECS cluster
resource "aws_ecs_cluster" "my_cluster" {
  name = "my-cluster"
  tags = {
        Environment = "Prod"
        Application = "Testing"
        Project = "CloudOps"
        Owner = "mnageti@altimetrik.com"
        Name = "tf_my_cluster"
    }
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
  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_ecs_task_definition" "my_task_definition" {
  family                   = "my-task-family"
 tags = {
      Environment = "Prod"
      Application = "Testing"
      Project = "CloudOps"
      Owner = "mnageti@altimetrik.com"
      Name = "tf_my_task_definition"
  }
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
   tags = {
      Environment = "Prod"
      Application = "Testing"
      Project = "CloudOps"
      Owner = "mnageti@altimetrik.com"
      Name = "tf_my_service"
  }
  
  # Other service configuration options
}
