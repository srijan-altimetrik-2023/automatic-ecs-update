import boto3
from datetime import datetime
import pdb

# Specify your AWS credentials

aws_access_key_id=ASIASYQ3HBXPT3ZX45ER
aws_secret_access_key=5g7ZWGTKfd2iAC1BfHSs8PQLu/IDkOEM0Z5Ea42K
aws_session_token=IQoJb3JpZ2luX2VjELD//////////wEaCXVzLWVhc3QtMSJHMEUCIQCp5nH9r9B+idlYXGUvCmOO8Ms49NbvLT7BH6YhLLWYAwIgNlkaNQTao4J/Swr6Q/uxeIv2j3maWCeL/p/vQW5832MqlQMISBAAGgwxOTAxMDkzODgyNTUiDM+LaBTX4/QYy7i1IyryAiTdmSDF2WDFFed2T8kww0jYpnXBOY97gaKJ8wGWLgTgochb2Zod/DRW3fthjbiVcX148Kk1te4RJXpQiIH4QxE9CIQrEAJraSzoJ3iV9Lc52bVdNvNTMcN8NikB+98HqszJCxyO1dcz2X1D3vYXnFGAPQUdwhmo3LzDZ5jw50JSAP2VkW0oBrrg4LclFbgWs3oyWMGhob5mg8UJr6TN4jOjzjzNZDvzi35Le0qz7Cp0M+fete42Z9O+gknuWhWZSpUZbsvU1GCaSibLKJNzFqH3XU8i14OaSLVz2LlWj3xpmhb5JhccBAjcDX70qRnFFiwZpQ8FYEweWgJtQkxjY26UwH75bRWAtI0Func785Vs4JQaGq3XtMN05iN7qfCDabPPZRZX4Lea9W8uBw4T8dq6jcGA4zBNdAJHMU9NPzFVpZ28XO4vi/Rd+qZyyLHiOqlGMeL6qchaF3OPG/I4DCf3FEJ2ORAU4Pau3RJ8/zGETjsw3u6EpgY6pgFKBfTJBo9hDugPUMFVD6bztSDrKPXuJF4gS9RkXWkEmsyiR4BPTE/E7Bw+XH41l+Ru+sHSfRGPTunAcTs0v6Q1BhOOfgeKuyJ6pXpCn1XNv+ZTmwOOhkab1oMS7hcMKCgglU/nN+dTqS/Hea21yarkDk8T250RUf1GNQr+r3YyVppVfnSeMbqeo3fUwrT92uxJ7NMhkICdo9xGwIUA2bFKJkwV2e3s

region_name = 'ap-south-1'

# Specify the ECR repository details
repository_name = 'ami-nginx'
image_tag = 'latest'

# Create a session using your AWS credentials
session = boto3.Session(
            aws_access_key_id=aws_access_key_id,
                aws_secret_access_key=aws_secret_access_key,
                  aws_session_token=aws_session_token,
                    region_name=region_name
                    )

# Create an ECR client using the session
ecr_client = session.client('ecr')

# Get the repository URI
response = ecr_client.describe_repositories(repositoryNames=[repository_name])
repository_uri = response['repositories'][0]['repositoryUri']

# Pull the image
image_name = f'{repository_uri}:{image_tag}'
ecr_client.get_authorization_token()  # Ensures that the client is authorized to pull the image
ecr_client.batch_get_image(repositoryName=repository_name, imageIds=[{'imageTag': image_tag}])

# Get the image creation date
response = ecr_client.describe_images(repositoryName=repository_name, imageIds=[{'imageTag': image_tag}])
creation_timestamp = response['imageDetails'][0]['imagePushedAt']

creation_date = creation_timestamp.date()

# Print the image creation date
print(f"{creation_date}")
