import boto3
from datetime import datetime
import pdb

# Specify your AWS credentials

aws_access_key_id='ASIASYQ3HBXP36OIVPP2'
aws_secret_access_key='GcXmYF8L5/y/Zt38XFy3NK1ih71pDm4YAeLUU6jK'
aws_session_token='IQoJb3JpZ2luX2VjEK///////////wEaCXVzLWVhc3QtMSJGMEQCIBEFgMRjKASbps3ObX9XlabfCuHOQuF5feOcvANTUdnjAiBYSjj190+lAUc8prbcNI2x14SnXO6Gobvn0znJgVBa0CqWAwhHEAAaDDE5MDEwOTM4ODI1NSIM/bWgFbFmUdm42iVXKvMC+T+EB3A/nPLgAD7vW3m8PdgBYWOEs7wEFbcFO/XnCgOEjFKdaxX6B2FAwIt2baerdgXfhLnAIGG1KmkBmeMZLjE7nxEVA0MkmufExkOdXwwUO9FvbUcVWccqJZMJpVMkIFkI2oPa2TZoXO5QtWc3pyvggvyOdSn4X3eqlAhdH05GmtMsOnW7x2ZXa4u6RGxc6L1BDM58lko3nACNSgNaFXCl4aJ9S4eAezmcg15YFOcaa0ODQR8Kkxsdd1S8PzKB3ehq0ZkGNtzZn6wMvfccDmvO0gUEbzDWWmAj3Gr5N+0Z0GaqogvWEwvVNIwLpae/nyhTYlLBw4L3Hapv2Qr6rS4qyDjEDLAtYx927WivyNaY23I79KHj9mjTnwpwi8ZxLK3dITq6L/ZYTyZ4zKj/kzsGNzxmC6ij/LMLw4pI/VGhv5IPlM3WZhaVA0nL/NEbG5DcZcRPgP077Gj6vvjCnxQLOcVkeQHY4UhoWKHpF7dEE0QwidGEpgY6pwG4dPA5PtNtENA6pstnoQ2j2Ke6ZBROsfjAiI9qpdclKAEIQzDrTCmHjPeqNSWAvidck/ZYOxQW2SF/UDC4WEr2hPivkl7NrVTmfqhJjM6N0dUDyG9jzFFWgf/XbgjO0E/INVydZGyuC6vIfU3CYxengKHC2qVnFy2J2EL37+o/6qMbKuvv4ezyhS8ONcL/sDKGdlZgehKEaG3vDLnHQF5+7xn09YGH4A=='
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
