import boto3
from datetime import datetime
import pdb

# Specify your AWS credentials

aws_access_key_id='ASIASYQ3HBXPT3F2YTNY'
aws_secret_access_key='oGVh47UrpKdC0ZM+nSh1IuqI3p8ReU0oqNYcfvH7'
aws_session_token='IQoJb3JpZ2luX2VjEKH//////////wEaCXVzLWVhc3QtMSJHMEUCIE4Zz25i4K7v1bEth+srGiTCNaU85GvUPCRqs4hO5koNAiEA5LKRWv5fn9suT5Q8kN8iV1tO4t6vIaBc//8aLFWzTSMqlQMIGhAAGgwxOTAxMDkzODgyNTUiDDI7bBDIB+WaHjrb+yryAjCeOYt3SfP0RnvAGzttGjULgS3397ns3AUci482gLbknpf9N/82DNyrFfWqnWPO1NjV2DnccnumKNUVeIBt7SFKKXS13na0BaRXgYJW4AltkAFceytUkxUDH9g4Sn3OnztNzh2gJRPWgoB4weo4Yw2kd4NE/Qc/m229/AA8jguvlBEdTrYWi5TtpWPCTylFexOkymSWwA+iGlshT6pyWVqNewTY0D06WmqsXbz+yz5Ii8Ip+RY7XO/YNqKNrAFVq2KFTsBVdFNZVt/NxJUQrT1T54no33KV9USgjb3soegurqtE7B1fqJy20UBjokpufp0zHlQSxdI/IakWq77Q4qD/xO+Z1bx2vMpxUYhzPZsvhIyNXQ4kWfseoCFoO+Je1XohCoyg66AN58FyOmL360gXnpxgMQIiqLQymTFjcmivs8TmLJ3FgmUICSpUDdNROQRUHEQHRcDcb3CKJYWC3OV4eFtmXxaHNXqTGeE2f3myjG4wyZ6RpQY6pgHTKm5GGP2+x4P/yZao/3f5smLMzxD9TiUYfeO2n2zT8PBmiNiErTUGuJFMcJSvO1u0295WjkEzZhOxKRJvkkE0x24XlZ3Kf9MhpPtX5usngaWuwnCb9xEVtDh4q2T+p8CyLMb6TqHFY943FJSNpOnTbzwni7X1QkbTwCjSRV3e18HPxSafL1lQBUd4yt7ixKgAkmw174UWXuu6mnneTJo5yUKkEVkM'
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
