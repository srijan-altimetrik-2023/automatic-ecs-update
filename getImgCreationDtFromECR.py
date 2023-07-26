import boto3
from datetime import datetime
import pdb

# Specify your AWS credentials

aws_access_key_id='ASIASYQ3HBXPUUH3KSOW'
aws_secret_access_key='m5J+q5sjRVKVpOb75Xc95YPfmJoNrEXvoHqFLYa2'
aws_session_token='IQoJb3JpZ2luX2VjEKj//////////wEaCXVzLWVhc3QtMSJIMEYCIQC4bxmM510m0ZY4bqaXnxYw7bm5Zn0oBZqNJxNsEfI3RgIhALXgUq9Rt7AdquhEivuBo2srIMaG8+MQUks7cYekU+6YKpYDCEEQABoMMTkwMTA5Mzg4MjU1IgzjP+I07m0iWCeIB/Mq8wLBIyLkP0LZcjtZqAO6fwtBqTenY07Yq2MdNRE7BaOztmWeMWv7IijK5KYC9InBbO8e906WbBR5yqjRdHIuAm4z9RKcRZjh1U2XE63VW7w5TMMBEjDfk2T/Mt7EVMnYBB/o71XGbwlZhsPlP/jh3phJH2FGnP8e14RFhY43nVv2EZDHmkiUJf+vYW2N90HoWiQ8x1Gi6qZAuVeg60UPSIkLqnO1IupCacwmW44N+XwIT4HR8mU+8lqEOwjFT1I7rZF3U9NtzsHQlnBkMMdtIcV/r3IIuOSCfgt85ZvfGhJ1gKn9z8j5O3ve5rT1vyTREk4gF9aDtPgwDKpySwC14fj2QPrthSiZeebby/q0ggU/ZxpRSxFS3RLYIRsVBXSEFkOEOpxsS+aAqw453Xfc44UKEZc1tO/57Z1zvZu0l9TTMQS2tc4zVCkbC9urNBKcqYv65F/YC25MP+3adY1RAyq17JWtCg3yt3APPgxX10+l3E6MoTD9k4OmBjqlAYlhdP1HB/rR3VDiAihyIGPJyVpIXegw4sMDxxTIg5CIPEQY6eyxv+BCUMEEvJa4C6322GQ/Kyu0OrYOtczwEp8k7HLWeAosax/oJgQ4Pz0uSzR0wdlptZTRUmAiQtk9OGv/2u22uWZd8FOY2tYv7CeMqK7b6EVZFY72maxmBMbtRJvfN1YKnnHoviVFjtkuL3GqzYH63Do+YAkIg5IZiVbSDnT3mA=='
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
