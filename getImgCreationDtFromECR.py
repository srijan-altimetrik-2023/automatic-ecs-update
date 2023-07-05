import boto3
from datetime import datetime
import pdb

# Specify your AWS credentials

aws_access_key_id='ASIASYQ3HBXP4PEG5JHD'
aws_secret_access_key='gpk8lphYuZq7qg4ebyNjP5pi5ie+B1VCSL6rnS8V'
aws_session_token='IQoJb3JpZ2luX2VjELL//////////wEaCXVzLWVhc3QtMSJHMEUCIQDjX85KECtFgcx9HjTmTanF2sDwFYnj4WzW8iXWPeJaQQIgSxmMTiSy298NXZ6mqB6MlzeuOJy5QmifEK+6Fn3Oqs8qlQMIKhAAGgwxOTAxMDkzODgyNTUiDHvfeNVqVkvDLoxt6yryAtYAKr12njqIXgKYtnKlP1sTSXl/VNcnxnwUoG1mUEPf6tpac9++K8xWp9jgLp9bmNDT5aq7j62YJIJ0vvJURiMY3bG1sgCG2rmlhTMTIHyvV7GeqheLOaNIb+/1zxBRZu+/fTI8hZNDrr42eIf/lXx091coWT8TxDxnfbs3jiW1L9HhS8wkd/EWxVG1pUOgpv+UY9UIqkbUXfEAp5gdJghxS7gnz70k8HhXwiy0VvIhPplTXT/a3gRx0g6oc88fvE/rZvFrQBOCS86sKU6vphTEBW9NyHZhIwsSar09SziVDAsFOIIQYlvhLOIqZjRRrJ7vJqWm5csVZkVa2M0Zjbl0HT3pdVjMLkui7aH9fT+nH5VclUTGz3uQaEFKPBgd0DIZ1C/kavimX74Q84T+FMYRBxaxzMv+ESLcHHLqQoQVMNNOZYcoIuuSYfcV+YOn7dC30KJnfpvIfzKQBQbY5ggin3ra1aJAwgDaYlxwUn9OdnEw1uuUpQY6pgFfQUWMHXBJXQuto3A3VXnQhQco5DZ2KTiW9nkur8fTrWKmPUCuEVRHhdxamSqKc83Q7X77/1+kPQ243Cr/OUUMLCIjyoNOdsPLH/qvai+w5/TeOtpGvoN7ibIuN09EutqAjyZLql8zQ8NixE9MiN1qrPzrwYjMVa0zMiL3/L1m5rM8ULErSEoj4YXA67Uf8GdCRbwS5n5IHXFLq04vpjFC6w5nZY8b'
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
