import boto3
from datetime import datetime
import pdb

# Specify your AWS credentials

aws_access_key_id='ASIASYQ3HBXPSVGJC23P'
aws_secret_access_key='RP6Adbk8ZhSpcFQq850rZc+oK2wsHY2DwSL80Bib'
aws_session_token='IQoJb3JpZ2luX2VjEIr//////////wEaCXVzLWVhc3QtMSJIMEYCIQCr3yoPg0qBaCzfQRKth/pu+2+Ek4JPn2C36QpbRLIV3gIhAKTwwmBd4ojCwJ8+1jcjKK1xOSO6nLqKZoJ4PqL5tMK9KqADCPL//////////wEQABoMMTkwMTA5Mzg4MjU1IgzOWtpkTcailxw3Pl0q9AJ37q33XonBtTXGQ3UnAtsKWBEJ8yQWB2iACploZ8dQnILxfAQdgozBFCBE1yM+9hKqn4DdJN9FhvfetqVyPzSPh1Ylx8VigD8dWiKINea7ShZ2KHBYn/ZrQiKvel0FO1yaS9EDr5YnFW0tKNLEH1mKvoE+an3W2RgMfnz7nuTraQyhUuPbPUm3VQZf4+ztYSKCyisGYqLlTpH3ik1AljGPZIavtBz9ibC/j1jRNxGTFGwFDvrR4e7iHW8hfHzBP3NtEK0XcQ+qqC4j/gzXnjDzLbIslBdKsMf2bdiGy1ZjT0t+1acXzJidarrSQTghhThHKV7e01bmWv0ah+1EupX4j6uP/R6wgUu5xE+tIhp2c7+xPyZjh9S9oy1OUv2xoVvy+RpzBI29Wrmtvnn3YuqId+lnCmZOPRFQy9oGMpiWWLKA4kr5fzVqW4/AQu3hthaE91Yv6/j0COaYTEpz7t+GF11LIRsl5l3L85kWIGN9vNa5FSUwrv+LpQY6pQEiYodBdsIF+16UGfU3XJ7VQ5pMZJIfogzvj8dTwZK5Qj1rn+PueqKza7luA9pZpgRBbcSn+q+6C5Ykqnxid46Imi3K5AoIKCEimbeUQpy/C4ZaPCdDBVaZV+JuQEChtzAgMsZ1irzAW1WMfpEl819UZA4W1HI4JPgP5sh7PPnWJH0Fhdgcvvu9lzXFmkMGkvpoaFdQSJ7EEypoqOvSZm0y3nXDPH0='

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
