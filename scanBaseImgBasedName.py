import boto3
import pdb

def fetch_ami_with_tag(tag_key, tag_value, ami_name):
     # Create a session using your AWS credentials
    session = boto3.Session(
              aws_access_key_id='ASIASYQ3HBXPQACNZC7T',
              aws_secret_access_key='YQS5vM5hkdgo3EO53/zUeTHYozAhZ6XUsDPTT27n',
              aws_session_token='IQoJb3JpZ2luX2VjEEQaCXVzLWVhc3QtMSJHMEUCIH0bvmsip0IjaSPCHZlMoKBNQNLyi/S/Gaq/758KXkksAiEAkLA7XR9CFi+eUJp26adcFzmuRn/ChABn32bf9vlrlhQqngMIrP//////////ARAAGgwxOTAxMDkzODgyNTUiDBS2C0WVJxR3rlX87SryAhAjshT5n7K7GoI3vStd5y5aV4sgkb9bMjxOk0DWRXE6z/ZJvfL/EGFMDMzzIRMLdA2V4TDMZrLKRUNYjJ69PcWlaxPZzQvc9JesFi5PW5A/rA6V1Zh4PIV7Su8Xa5kS6tfIpcvnOOkpbfedULpMjH0u7jjeWrfyBRjlkYRohseRxFyeEqk+SYwVwuyPtThU6ec5JHHbND6U+upDqQvtCaRBrivF0oREdNvBHhpCZa+I81Awg/f7fPws1dYfSqi/y1/3cCnAV0Su1qXkYuwwvHYnYihs2vW8AozA8NoubKSYVo/mpbtLmqPUG/xmFaRdMuEAAShhEm+GlFgbU+QikCveKE/DDZ7VmMA2T1DZ15Py6V8te641y4E7JT6uKXRQRlvOTSt5MYmF1Ogb9buvU2cSf9D6s1CVQ/YnEQy/MDLyJKG7nu0Psl5vjXyDGI9XiGimALsnTq5rF15URIC0GKywPx3YqUd+zMMUsWMLkMdvTV8wms/8pAY6pgF746U88TRkuOrs0O4VfsEFCxuU9BjviSSVpAG3lxM/3MLlRiCTQ+VE465MyN36UFUSIasW8gzQRjZrxAL6svjcMFJ/kww0Y4ieD5+0URyEqcrduNeWPLSVlYCMYfZXw50puIiCLKNgITZx2Rt6M+MKKVDO1djYXcPzjU4qcEQxS+yv2wJMiyAHATYSiAeU1A8S5NOYI5vmrrKaTDZPagq5iav54MKZ',
              region_name='ap-south-1'  # Replace with your desired region
                                                                                                                                                                                      )



     # Create a client for the EC2 service
    ec2_client = session.client('ec2')

    response = ec2_client.describe_images(
                     Filters=[
                                     {
                                       'Name': 'Name',
                                        'Values': [ami_name]
                                      }
                              ]
                         )
    pdb.set_trace()
     # Iterate through the response and print AMI details
    for image in response['Images']:
            ami_id = image['ImageId']
            creation_date = image['CreationDate']
            print(f"AMI ID: {ami_id}, Creation Date: {creation_date}")


# Replace 'your_tag_key' and 'your_tag_value' with your specific tag details
fetch_ami_with_tag('version', 'latest', 'test-ami')
