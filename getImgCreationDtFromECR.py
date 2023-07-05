import boto3
from datetime import datetime
import pdb

# Specify your AWS credentials

aws_access_key_id='ASIASYQ3HBXP6LTN64W5'
aws_secret_access_key='7Db2/r1boDK+DVd6z3Xovbq7kyWBW4otsqk9z5HB'
aws_session_token='IQoJb3JpZ2luX2VjELD//////////wEaCXVzLWVhc3QtMSJIMEYCIQDGUCpnz40s9IpnH50aH9ORlu4FC2FvrtABX63Xo7qP1wIhAOy/EHg/poF6/9NVsGR1MJ0+LjwCsSL2tN5koxZvF2UCKpUDCCkQABoMMTkwMTA5Mzg4MjU1IgwKrpa9QAYWhJ7yw8oq8gLNzxISHxp3p0nw3GNsgsOAWm6rzB/DJKYkdZPWiYMQa9zpkuntb5XpPcSD0KjFpcGT8PusNhs7JiErbUs04qKHSEPpv948yVQgHeTBfjK/KwetbudUmT6SM/cxELK0zW27ybIOuTA+XPH10UPIgs7LBuLMJZYP7u5hWii9Gj096HKpy6u98kMcWgvnjXYueHVdSuYbtykl70QM4FGXPt5zUvawMRWhYroqPFJYg7vU7281QDALHyNeqE51ZfB3yTYRaFFKaoaZLx+8vejMB+nxAshHKC30p1k49eXakTXxB9P8h+PbpOZL6+GRy3rekz03COSZeVYZ4MVPdMUidGmxsiEfmugC5XmBkIhcA5hLuTks9fZElBsLh7WdBbYLnz1uZJg8Wy1Pkj+O2B9bWihKtxMD/+Z/cNET/5BEBBYVdDdrg4tUMi5ej1CjBUsG4sXqUIVFC0HOI8RxpyVYMocsIsEgSsF7f1WG0dJoA8M0VDaVMJLBlKUGOqUBLwYOzdgDcglygdG7Byh3uD7NKtZtZYW3+DzdVsJhjIh6d8dl3SUuv3VAoZSySklrXM98xlW+Q1+H+i9RMSMfsgMT+LUPmwgCMOS+Frl8z6n1tEsrmVv2iZwq6tMp2cptr7abwCyqslB1ie9FHt/Z7NX1MLomBm5NZwg5R3fjHAWRissOeqtZWX6a9zu+YrYp6DjtLBPh7Z3OU0VKtZXAoMxRrIWw'
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
