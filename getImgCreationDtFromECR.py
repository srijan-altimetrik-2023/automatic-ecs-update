import boto3
from datetime import datetime
import pdb

# Specify your AWS credentials

aws_access_key_id='ASIASYQ3HBXPQZACN7IB'
aws_secret_access_key='3CdFdc/vCBzXFC9/lsy6Tq0VlxRandctJOWIE0q1'
aws_session_token='IQoJb3JpZ2luX2VjEMj//////////wEaCXVzLWVhc3QtMSJHMEUCICt4JGLHGshvAZcPt28Jqb2CgnYcGNbDrdVyF7d0pizOAiEAhSqfY5E0698uqPCA4ZIAPXwzr85UsAnFgckL2M1TCMYqlQMIYBAAGgwxOTAxMDkzODgyNTUiDPtCABowOZjIbn3FcCryAuhMO4Yfq0dN/M+3OropUdWNiz9WIPoH8XyMh9NXB6epwRVm/fzMngT2UTiGHt3E69CZQjAs8qIs3VxptJlmqcFRejnzwo6d95NZQbz/wyNqbADjGmg9M3qZqlghUukZSmmyazKbL6bph82BZNJ5t9wvQ8kU0/B9ghNk4zgYZQNIieWdpzomn40ZHmaVHvHJou1BGD1fJ+h0jluCeW7bG4A4Q9qjzv61p5iyDX6Qxbx5kEgue7uQ8yg0YvsTVWlbyQgQdlxGJFZlI867UInCcQjkXeNBs/aPAsIwGU9RvSLC7wvKvTcD2aWdzXNLcwdtinNTEANCzd01UPLKJ6uiQ53ZbJV8de+Te+GPL6YgS27bFVeBuPTk9XwXxrDNgwfDh2X73PDdRUmXnfNVj2zNZ7p7olPpZ1L1H11aYFzB+jrRzNAi/0XO6QsRT7M68Es48luFV7H8H4U/NvHx3gAL+2CbBllqLKm4eI5j9leaAjAEB9UwtZOKpgY6pgEP44JefW+UeTzblSiSj+0BORKbj1gXKn7YV6oOoXyGpGnftnM46vGrAiPRgbimbPyRf6WtTrabknLDsBRD+aXSVXlzPtzIYtMtE/4swSG+AHNmK5rHUQfNuhF7qHmaMfNuL5L+z5uBeJV6Mtr94iyGrcZgA7SrKRClIPvwEOdjLJcKI+4a9+k2t8Bsp9R9GwX2gs3iRPl1/uIMDgnYyjreCb/Xx8kg'

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
