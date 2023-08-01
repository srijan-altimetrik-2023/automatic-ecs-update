import boto3
from datetime import datetime
import pdb

# Specify your AWS credentials

aws_access_key_id=ASIASYQ3HBXPS3QBLOF4
aws_secret_access_key=/Xszjd45cQQ4JhNwmskGQa1pClKA1/PLRRcM+Cxv
aws_session_token=IQoJb3JpZ2luX2VjEDcaCXVzLWVhc3QtMSJGMEQCIG2PVoRg26PjArZtVDEHtzDMStY2ZzT+eHuNYZBSFgKkAiARxVIMyCk2gAgoUXtSYPGeidu8ryCgNmnOFG9yTKoNAiqeAwjQ//////////8BEAAaDDE5MDEwOTM4ODI1NSIMd3GGRKWMaaYqXUWFKvIC01xr8uQl/6dukyadDmta+4d98nc8OO+EaMA/+NBN5cNuyXZWK88aJY/gC4udjDj0WJd1o3oglI0zV3OvcstM1vwBfOKVM277M162zMoSYdVItYgP5GBVwOZ96WLngG87SYA6ZzsGtLzvyDO2p2ofAks89dh8EWr8nhkUby3X9FCEvbpwwd+YoOw0kD9oWJsfYEBFYhVU+EjfIFgY9KTq9naW62DvWDg+neNXIxNxBvzwmLFIHtvKpGKJfs42+Da2c82GcBTKZLGiO1TR8dPLOmkHpGd5zToXvkEprtXaCAG8DHn8lPd8yrgjLYggVpEeW8GRdRfcQ0011usbmUs7xwpGWREIzu/1Y8PB0VSu/jPgQ0eJPkh7AYnPAhuHnPnuMb2AkdR99uonKD8yDA51LW4ZdoIdsPWzsBeuSj0BfmpVRRyE1FjsODi6URKZFlWBJ0xFKkyxaQ08yBMZCT6TqCMWFVXxnYF47+RbeM3Jzlu+EjDLz6KmBjqnAUqtt/+g6gfQ0PYn4yo++Y85tC+9rC794Nr7RoKsjHYoryvS22AvkvZQ2hcz/vrNbHsfiUtnXfFmId0vuz1OEQo3t5uHqk9NeCLOvMOvaW8VX44oDFje8RiOfGlg/ncgssdJkO/SZOSFT8JcJAIeKck3IAN03Nx6LGH7KPl4qZ0lT5XNC3AynXF7VB/Y6kIhqddNZd1xcIkJPP60rtLqX5AgYribK5XV

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
