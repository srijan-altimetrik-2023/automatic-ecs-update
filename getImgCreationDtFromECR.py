import boto3
from datetime import datetime
import pdb

# Specify your AWS credentials

aws_access_key_id='ASIASYQ3HBXPZHGORU7N'
aws_secret_access_key='j629PE2nwgBz71KFnjXbZh2eZcOLw1WoG0aAAkUG'
aws_session_token='IQoJb3JpZ2luX2VjEG0aCXVzLWVhc3QtMSJHMEUCIQDtBC2qgrCvNZP00ACOiayzpA0XghlGxxt4Iz+Q+gBvYAIgOHT+er/v8f4DSB16CVYrMzj5LeZSXAiGq0prvCAZmBoqoAMI1v//////////ARAAGgwxOTAxMDkzODgyNTUiDFZfOeYl3co4k8pFcSr0Aj1FzXUuV5SENGiXAeYT/i1d2OYayXi7H4lGDnsRB6aPCb3gCZsl4d7zQIqyYRcalgsH71rqDRmOgZjigzoCmMF+2wBtkDycrLMcf5jJT1Kes6cBn3piHdRheAXTPik2pmh877HmWsGXN+cPqefrZ58/IEztNKXP7ssuHytXQ7TRiMipXrfn7UveUrQ8sDg51SCo8Qw7uraGZuqk/6eeRxLrr8pXH3UGo0wMId+8JWl8XhH9xBxGWeJLws/7duTLQS4X5nnOLQJ6LGc8IfonIWI814KAA5pZwRTVAgL+bVMEgI6UYbaBHvqBOT8SjsDga2tgmcgOjyh8Njp/gifLzB6aIy9KtZpGKgbHMPQOkAk6H8RMMq/QBrZw5dH95r6N0YszUJgq2xgiFNu+zxQq9z+xHMjwDqHciGwoaGzg7EerMSHfArrUwqE7MVOHgYPJx7FUR5ekNHIOD64Fg95IdW3IH4D16GJM4OilRMQDBi0LIyoAbDDJ2YWlBjqmAaKe9esF+JbjMtXyfn4MfsJqo3aBbay9Kb0LzPXgdsL6PEJ+Q0m6rRvkX83HQeZy0rVrTA01foUpuunSkuf1CzHVcvbyoofYyNVNwAve26k66Dd9CD3H2ZBbIYj1Q1R8p8ArunH0Y7Ot6RBgDIt7SUevReZ/aRG4apuQJKn64QAix7qQ1EGDeydPlQ+gnE4DRWmA+APnGzYLtQyV5ABLpBG8ti85zwE='
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
