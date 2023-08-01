import boto3
from datetime import datetime
import pdb

# Specify your AWS credentials

aws_access_key_id='ASIASYQ3HBXP3AOLG7RQ'
aws_secret_access_key='pDm48vSdy924nlNkjpy/8tAgga8u1IYjvQAdevWc'
aws_session_token='IQoJb3JpZ2luX2VjED4aCXVzLWVhc3QtMSJHMEUCIQD7aR1EoCCIHHRK5FM7PGtumd+rqMa32z71fEZ7oLmR/wIgPEzb9k+ACCiwsB5fzavD/vhv+npSCjQB4hDySt0h+BIqngMI1///////////ARAAGgwxOTAxMDkzODgyNTUiDFYZDjMIQxUPy+zkkiryAmt6j+klroCmluRctchopzfiIYY/pqnJGwzzbGvO6u8Rk++ZLDowLlsxeEFWULf0gPwMymfUYVOZfPPBIHwh9TRYXm7Eg9EjEsFycP03IYVIYjL/5/UWPu6vqBA9DLr27bTVmfPxefjRmn7bfliaSvvM+FaPwnLhDh4WIMZeFtCmAgsZtKkmVOTe/DttEs4QBvJZiWKxCDntXGund5VslEfrqmFOh94CbgD5g9p1yeVr2DKvHhR2GETJDe1rKDv8oKi5jstnbbuGylRRkaZJ1zzUyHr0sozAeiAQ5zCmXE8m9ZWiH7R5qNJOwsddL52jeMwjQQpzUFl02tE1LfVgN9DVaKfT7NKXd+uusniH9baKylbqAd2un050o7S6OP/80aTLDdrr6h4nOaj1tJLxQ+BpeFF9AGWlbyhIQ4noQrXiJNcUmD/+o58cGoJDrLedTjUip/S44nE2UzTpwMGLnP6Dx6TrSDbUgSImmOI55FRvNfswr5ekpgY6pgHjUWHGdBTV+RR9UB6yTAg6z7+CMjcHDjhyw20MmQcE8WdlKS6KbCiJFbhuuqgFsaLWOyJ4Z12HuhNYNexMQ2LscWZPncMWAqZ5R8l+Hmb2ASXrobr0Ru0ySZSCbyQrJRZyvaHbTBLtEW1P2t0nqCXmV6XxRYhPhz+iDeJeqUl1YMHX5NhOj4EdUdqD2NKkG4SjVo0Q+HLN2pPNubJ1uX+jB56O1bNz'

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
