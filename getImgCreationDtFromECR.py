import boto3
from datetime import datetime
import pdb

# Specify your AWS credentials

aws_access_key_id='ASIASYQ3HBXPXILQ63AF'
aws_secret_access_key='y19TMNT132fHPnkDjdvvg6k9qgE7pH6LSQc8MD2w'
aws_session_token='IQoJb3JpZ2luX2VjEMb//////////wEaCXVzLWVhc3QtMSJGMEQCIDj6KyEnJOnr58jdFcedn2KYEitPNinRN1FRn1bMDdApAiBDDad4sJ7I8fdzO9Qjyhp+KkuOmBwCvcNNXBzGdO1cgCqVAwheEAAaDDE5MDEwOTM4ODI1NSIM82wsr81p9TjqDUTTKvICFucqc64U88SzlnRaummyPEGTN3Ui0HrvarpMrIXQuMzsMmutIz4HK0PV85+MAhkojLA4QrG0jamxQXO3UTOdzIJ54Sjlvid+2iRT/kZk9CGWPR68hBouQ0ODEd+5WG3zOX06zyLQG+5I8P1B0WPlxSwqHs4NxxNcVFckv3VCIst7zzxW4+qKY4m21+I0YaOBY2eIS8nWa5JA0v28pO6QZmze/mYfjfN7vSnuLMRPxQAwGE9yioeflwS23jl4KFszWyaxECRWvl4oUxy7nEeC369GGQ6jb5PXjKXavkzOeQ9pqQwXICsw/BjRdgzzABF4MBWxnL0jIvxNXZRCzK30O2kSrqYnUnrK+gE+w6QrwlcUQsd8edh95pXWO8cUQDeVpgY/paeFtY8jX6SMSwy92oYdWKLi6GQc29ZusMfGF2TP7MFhZZwHUh2IimRN6+Se2yt+sXGVuNPlF8FDnd9K2tJ3QS15hyFounU/Lx1ibKk1azCe2YmmBjqnAY4A4HG/cx4YtnV/z2OGvQ1KDuOFN0Bl+MT4MZUiQ21jHd03rFZ7VPT0CCUw2GLpOOOzUEI8hnGW8LJsmRka2NJNf1UCShYOb5FSQdGkamqXG+hzBwzWSfsWUlUwQflwCmG7tKydJGvj2QafD4gtRwY0KQ1n6dHNTqBCXIXERB8YIKUP7G1wifKXQ4H90u0WwsFl0crsWgKtvqjyxWMc4zhjprA2f5EM'

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
