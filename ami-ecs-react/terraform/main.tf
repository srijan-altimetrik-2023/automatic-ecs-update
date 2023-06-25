provider "aws" {
  region = "us-east-1"  # Replace with your desired AWS region
}

# Create ECS cluster
resource "aws_ecs_cluster" "srijan-ecs" {
  name = "srijan-ecs"
}

# Create ECS task definition
resource "aws_ecs_task_definition" "example_task_definition" {
  family                   = "example-task"
  container_definitions    = <<DEFINITION
[
  {
    "name": "example-container",
    "image": "${aws_ecr_repository.example_repository.repository_url}:latest",
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
  requires_compatibilities = ["FARGATE"]
  network_mode            = "awsvpc"
  execution_role_arn      = aws_iam_role.task_execution_role.arn
  task_role_arn           = aws_iam_role.task_role.arn
}

# Create ECR repository
resource "aws_ecr_repository" "example_repository" {
  name = "example-repo"
}

# Create IAM role for task execution
resource "aws_iam_role" "task_execution_role" {
  name = "example-task-execution-role"
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
}

# Attach policies to the task role (e.g., for accessing other AWS services)
resource "aws_iam_role_policy_attachment" "task_role_attachment" {
  role       = aws_iam_role.task_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly"
}

# Create ECS service
resource "aws_ecs_service" "example_service" {
  name            = "example-service"
  cluster         = aws_ecs_cluster.example_cluster.id
  task_definition = aws_ecs_task_definition.example_task_definition.arn
  desired_count   = 1

  deployment_minimum_healthy_percent = 100
  deployment_maximum_percent         = 200

  network_configuration {
    security_groups = [aws_security_group.example_security_group.id]
    subnets         = [aws_subnet.example_subnet.id

