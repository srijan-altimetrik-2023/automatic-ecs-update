import boto3
from datetime import datetime
import pdb

# Specify your AWS credentials

aws_access_key_id='ASIASYQ3HBXPZUR3GLVE'
aws_secret_access_key='W7bAkK1F+skDwe+EkrfmVfMC3qKHv/jg5j8HPX5V'
aws_session_token='IQoJb3JpZ2luX2VjELH//////////wEaCXVzLWVhc3QtMSJGMEQCICPf+StCH6M40ab6qxntiStvjs2KvyiSbtZ8iL9pk0hxAiBzN9nIkfqL17g/y/5MGjWIPYzWnnsfU2lHaZMPynM3bCqVAwhKEAAaDDE5MDEwOTM4ODI1NSIM5kyIYUNsTGiXb7RWKvICTbrJS4xLetZA89Oa6zaiFDNftWdBhn4GvI6nr51Kx8nb75fKHwuYNgEUQKz/2Qv7j6/pS4xBO/wi8vh0JU01CTPdnlfyK7SF5vpTF0K5IezE/FJ4xGwr9g9HHUWiI5Mbwmxhgp9X61d+1PVmcoviSHzi50Z+tqxWbWeop/K/BRVmt+gvUvIhe835MEZQROZ/poZHsByA6xk9PFVDekWq0CgCMCJh7qUVSBeXOTpgE/LTwVfI0APRr4NZ8HoEQ5eRJaeJm6og/pYXwAW3TAFz4YvjEKgxOUQjvgKe5yKfSCKRRkmY29/xYjJl6FeSZm9SUIrjwyorzKseYoknULQAQ1JfEVJA5V3VfblTDEZNJGqMaC0WOcZyFfOhjdjc4Nxbt4oK+simTWqVdj2WEL+oB5DiLAQyUAu6PP8Q0ynCwFjVAH5KFvqvrn3yiULJsIbGGa0suvyZzkq1UFia+BJwSXJGaZa/FV+/6b+zRqJb2pvJJDD4mIWmBjqnAfEjGzIu1N1ErFfgvVz6k0MT4bZNoApHRikGaLYCr65vg+EUWjDmhqhmAKN2DA+GQB0OiH6FUuDzVuzyiMqGuvKwjBqw6ouYnY14en8F89R6R8u4ml2JSshKHNiq1aIUR2geb9LQoBFISPO7UewfFWJqmUs7KGM48cYpirmGE9m8+VJqQ4BYoEEU1SbydY0Z1Pmh2EAtAlZ5tK4j3T267GNlDDvE6L11'

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
