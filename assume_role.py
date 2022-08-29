import boto3
from botocore.exceptions import ClientError

current_account_session = boto3.Session()
sts_client = current_account_session.client('sts')
role_name = ''



assumed_role_object = sts_client.assume_role(
    RoleArn= f'arn:aws:iam::{aws_account_id}:role/{role_name}',
    RoleSessionName= f'{role_name}-Session'
)

assumed_role_credentials = assumed_role_object['Credentials']

assumed_role_session = boto3.Session(
    aws_access_key_id = assumed_role_credentials['AccessKeyId'],
    aws_secret_access_key = assumed_role_credentials['SecretAccessKey'],
    aws_session_token = assumed_role_credentials['SessionToken']
)


ec2 = boto3.resource('ec2', 'ap-southeast-2')
ec2_snapshots = ec2.snapshots.filter(OwnerIds=[self])
for snapshot in ec2_snapshots:
    print(ec2_cnt, snapshot)
    ec2_cnt += 1
    


