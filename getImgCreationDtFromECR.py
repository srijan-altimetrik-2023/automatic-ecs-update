import boto3
from datetime import datetime
import pdb

# Specify your AWS credentials

aws_access_key_id='ASIASYQ3HBXPU5QOSSGF'
aws_secret_access_key='DlJFi1FxcDJFfvnTicKmgIPZsVPwgD3xgzlBbEdL'
aws_session_token='IQoJb3JpZ2luX2VjELL//////////wEaCXVzLWVhc3QtMSJHMEUCIBr8Ev1JQMAQbl2Xt0xDtd8KMRRFm2aWC/fQFcpBhmvGAiEA/bF33i2ZJubqJncaYa9tuDTOW4TKMsY6dV+97ZhXgxoqlQMIKxAAGgwxOTAxMDkzODgyNTUiDOgmWN0+6BGRJ1sqXSryAhGqvEEBoTP11RQyhIpCNw2ptc4uyyuRTepm0+N25vfIN3mDTfKFC1ufKa59hFhZccRJURPg0wkwVNN1zJ/v9miOWgDRveFJyomF0tvrLzEG8rtcYZAPPpz2amMxunRQduC0hf0CGY23xhQuXFfesmDtaA14hKF+0W4bqrNGF04KOPdXdkJS1ZIpAdLinwD9xOKNkn8ax0E+p0xO85Dogj3ZdWqdaEW0WkOFKBR3hMKvv8BrkclmA7ZOW2alTzJ+pSLqWCXPWjxvAfy5FkY+cA03EDtAE8lAZkcJyviVgFSwRuHHo9L+PqtWK312g/3ImXUep43AM4SrMLF0lbibvjkgim4kwiZlzwLh6k0mca6KwtTKMuf4opw3N4oSUQE+d6TED07ysSh2avVc4y//FVUjEHf55BSIc7JLJwHx/bruMHAlzrhSJsWsXlJ6lpsku3aJRoYcb7pZEeD/VySYy1dGmJdP3YiD8juhEScW+IbYhFAwuO6UpQY6pgEv2zq2OPW5/6YXsUb/v+fMGAjyU8U7ZS28w65uOeTp3lHbfQPxlYx4yrJpED4Nf2zn4V9iteS9dZMyrr6BEY1xqRlU9f2ZZ899V+HCpb88T6dRIyYbV6SCkWZ03bR8SMJclA7Um3D+9nezvQ0fh9uJ41HBFHgoWBR1MzjLTiOZ6LBpEU3/T2iA867cTCIgtWgyVRwCMSUeZZ0wJZ8xkYUHDGrh4dyn'
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
