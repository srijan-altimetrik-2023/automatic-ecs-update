terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "4.45.0"
    }
  }
}
provider "aws" {
  region = "ap-south-1"
}

# Create ECS cluster
resource "aws_ecs_cluster" "srijan-ecs" {
  name = "srijan-ecs"
  tags = {
      Environment = "Prod"
      Application = "Testing"
      Project = "CloudOps"
      Owner = "mnageti@altimetrik.com"
      Name = "tf_ecs"
  }
}

# Create ECS task definition
resource "aws_ecs_task_definition" "example_task_definition" {
  family                   = "example-task"
  container_definitions    = <<DEFINITION
[
  {
    "name": "example-container",
    "image": "${aws_ecr_repository.ami-automate-latest.repository_url}:latest",
    "portMappings": [
      {
        "containerPort": 80,
        "hostPort": 80,
        "protocol": "tcp"
      }
    ],
    "cpu": 256,
    "memoryReservation": 512
  }
]
DEFINITION
  network_mode            = "awsvpc"
  execution_role_arn      = aws_iam_role.task_execution_role.arn
  task_role_arn           = aws_iam_role.task_role.arn
  tags = {
      Environment = "Prod"
      Application = "Testing"
      Project = "CloudOps"
      Owner = "mnageti@altimetrik.com"
      Name = "tf_ecs_task"
  }
}

# Create ECR repository
resource "aws_ecr_repository" "ami-automate-latest" {
  name = "ami-automate-latest"
  tags = {
      Environment = "Prod"
      Application = "Testing"
      Project = "CloudOps"
      Owner = "mnageti@altimetrik.com"
      Name = "tf_ecr"
  }
}

# Create IAM role for task execution
resource "aws_iam_role" "task_execution_role" {
  name = "task-execution-role"
  assume_role_policy = <<POLICY
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "ecs-tasks.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
POLICY
 tags = {
      Environment = "Prod"
      Application = "Testing"
      Project = "CloudOps"
      Owner = "mnageti@altimetrik.com"
      Name = "tf_iam"
  }
}

# Attach policies to the task execution role (e.g., for logging)
resource "aws_iam_role_policy_attachment" "task_execution_role_attachment" {
  role       = aws_iam_role.task_execution_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
}

# Create IAM role for task
resource "aws_iam_role" "task_role" {
  name = "example-task-role"
  assume_role_policy = <<POLICY
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "ecs-tasks.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
POLICY
 tags = {
      Environment = "Prod"
      Application = "Testing"
      Project = "CloudOps"
      Owner = "mnageti@altimetrik.com"
      Name = "tf_iam_role"
  }
}

# Attach policies to the task role (e.g., for accessing other AWS services)
resource "aws_iam_role_policy_attachment" "task_role_attachment" {
  role       = aws_iam_role.task_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly"
}

resource "aws_default_vpc" "default_vpc" {
  tags = {
      Environment = "Prod"
      Application = "Testing"
      Project = "CloudOps"
      Owner = "mnageti@altimetrik.com"
      Name = "tf_vpc"
  }
}

# Providing a reference to our default subnets
resource "aws_default_subnet" "default_subnet" {
  availability_zone = "ap-south-1a"
  tags = {
      Environment = "Prod"
      Application = "Testing"
      Project = "CloudOps"
      Owner = "mnageti@altimetrik.com"
      Name = "tf_subnet"
  }
}

resource "aws_security_group" "service_security_group" {
  ingress {
    from_port = 0
    to_port   = 0
    protocol  = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0 # Allowing any incoming port
    to_port     = 0 # Allowing any outgoing port
    protocol    = "-1" # Allowing any outgoing protocol
    cidr_blocks = ["0.0.0.0/0"] # Allowing traffic out to all IP addresses
  }
}

# Create ECS service
resource "aws_ecs_service" "example_service" {
  name            = "example-service"
  cluster         = aws_ecs_cluster.srijan-ecs.id
  task_definition = aws_ecs_task_definition.example_task_definition.arn
  desired_count   = 2
  deployment_minimum_healthy_percent = 100
  deployment_maximum_percent         = 200

  network_configuration {
    subnets = ["${aws_default_subnet.default_subnet.id}"]
    security_groups  = ["${aws_security_group.service_security_group.id}"]
 }
 tags = {
      Environment = "Prod"
      Application = "Testing"
      Project = "CloudOps"
      Owner = "mnageti@altimetrik.com"
      Name = "tf_ecs_service"
  }
}

resource "aws_iam_instance_profile" "test_profile" {
  name  = "test_profile"
  role = "${aws_iam_role.ec2_role.name}"
}

resource "aws_iam_role" "ec2_role" {
  name = "ec2-role"
  assume_role_policy = "${data.aws_iam_policy_document.assume-role-policy.json}"
}

resource "aws_instance" "my-test-instance" {
  ami             = "ami-057752b3f1d6c4d6c"
  instance_type   = "t2.micro"
  iam_instance_profile = "${aws_iam_instance_profile.test_profile.name}"

  tags = {
    Environment = "Prod"
      Application = "Testing"
      Project = "CloudOps"
      Owner = "mnageti@altimetrik.com"
      Name = "tf_ec2_service"
  }
  volume_tags = {
      Environment = "Prod"
      Application = "Testing"
      Project = "CloudOps"
      Owner = "mnageti@altimetrik.com"
      Name = "tf_ebs"
}
}
data "aws_iam_policy_document" "assume-role-policy" {
  statement {
    actions = ["sts:AssumeRole"]

    principals {
      type        = "Service"
      identifiers = ["ec2.amazonaws.com"]
    }
  }
}
