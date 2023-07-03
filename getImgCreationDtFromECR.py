import boto3
from datetime import datetime
import pdb

# Specify your AWS credentials

aws_access_key_id='ASIASYQ3HBXPSUFGER6R'
aws_secret_access_key='WfvbRgenamd9rcrW/uzVlZVMZ5W8MV8+mb9QzJWY'
aws_session_token='IQoJb3JpZ2luX2VjEIv//////////wEaCXVzLWVhc3QtMSJHMEUCIFh8yp10EDTYQDM+zRlHplttjj5VclBWRcYw08egGSNsAiEAtkZJ3dzGsTC5cng9Oo83UpVGAL6uIWq41X6iC3xj7agqngMI9P//////////ARAAGgwxOTAxMDkzODgyNTUiDDIktDnealOx0heALCryAk3jB7C83q7WD5hot5DUmyjZCeGqAesxgjb1aoR5LfShj1ihaA4JMZ0FLhNDaXjWkm8BYu3K/7mhgF8zd/MiWad6ic7J1vVTcx7lY9w7aIPPgzVHn7vDED+d+hl+OZ8kK3T4DTf63BbjzPLjkGulogFvjurf4Z47Lbw9mcZ/DiEinWsLB31tdoH3k29TfPXbVFVz9Gtb1WT3huyw2n9ch0HtfTPsq9N3ueuJRa6UJJ+sppQa1dIZ6q5IaX+YOPyqJiKwvpokDbVfn8T5WwbMtRoIyrRzS6SAe9Z+fVKpFrNxIHmzjA+DbZNfrAJTzvOebUizizuxFZSawpOwIl1bpSKvVXzeQ6vxJxoKyjPrV3ZWRsGM4r13i/RotsoEBRPuRu0YhAPx7AZEbmuR7NS8zyhmqYZSj6GnW3PtqqNN18k7dm9qcEwGY1rpbdBy9UU5BQ4kYCiQxBnrBQX8KpaAblSTw/8SRDNKBj+fuDchB3JP/8Yw/qiMpQY6pgFR4WfPdLQ6u+Ae2co377pe+4F8u17a87N7BH3PzCDo8Mvn6byw/TIbaxIas9DY8rhIvKvnkNK6XM4bydGmLeNKdZmegCV2A8OMxySwJX0xY3RSDA+Yggegs7RRPrYn//3ZQn4WJg9QytW4goF8NYsUvnGiAx0aCSjGcRXQnXRjTzBwEOQa2qCS4Hfzlwjb5I8aN/brWq3GjMPXoy5n10b96SrO8521'

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
