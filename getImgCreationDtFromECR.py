import boto3
from datetime import datetime
import pdb

# Specify your AWS credentials

aws_access_key_id='ASIASYQ3HBXPUDZNHKAE'
aws_secret_access_key='cGrapGI/6yUFlfQhDGfxJllaRGH9fsFhomOXSC/w'
aws_session_token='IQoJb3JpZ2luX2VjEK3//////////wEaCXVzLWVhc3QtMSJHMEUCIDdckMGM+oTVTki/BpLdUHgp5przppT92DFiAaVLksIIAiEAmKZ67bhPGrpkllPYMes9tjyfkNwly4SFlcNvnEAfVKIqlgMIRhAAGgwxOTAxMDkzODgyNTUiDJcMADmbhVvoSn/O8SrzAhH63nALlS+uCsrkBpATymcesQrWYPSuM/5+QBn6PS3U5G+4VvT1zHc6Z/Tni7dcWhJdkBBqmmPU/H4d+F4vG0DHvXLo2ZZgqKn3A3F/TZxbTrUs4y+aEQ2rpRkOz3ui429bQ72z7UTTlt6x+5fA7jYACGzxo+WHu1ywbDDomw9lLjSezkK7ZEvnrTRBg7tfUoj3bHu60nSMwP0w6kHQXtVn9QwYR+VjGk1CCaoklB0FPxIfz/BfUQQ3mdQjUCWd2PnA8ZbI5qaeeI3iGXMXnpG+6+QDPGyv7Ryy8eKZKaiJaggqdfCUllYT+xStg+5pGd2b+zalmn2tLME3JCBW+NHyGIOcTup2s8ZlMoTDvElQo6CG51BGwelK3Pa4JdtqtLnv2LoQm2ZJONVBjyL7dyn/Fcy0sIzp9esncHucdN1oM68n3Gw0vWUzk1mO0YRl6oQWeuWX0mapjq3c6/INXt2w7gly7wWfWbUC0BOX7KcVN0ddMO6yhKYGOqYBBulHc+CHKKbveyWB0rv5MQ8BZOTn2qOC2wJpOtmKHnZFpwuRAJcul/nk1iDTPItK3Rvj7gNuJYJEJa8Ule14EsN5AXjnOuUk5T1wycnOEF23PsThelEBV9kq59oS8Zjbz60lpW2YjptiMPYhC4Nqm68XApbAwjKEoVe3gW1hSmvC+p2Sq0nbH4dnx7HVwG1BvLkuaB6Sw5qHMfmrGBCLn0f3RhFGMA=='
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
