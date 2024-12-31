import os
import boto3
from datetime import datetime, timezone

def get_temporary_credentials(duration_seconds=3600):
    """
    Obtain temporary security credentials using AWS STS.
    
    :param duration_seconds: Duration for which the credentials are valid (default: 1 hour).
    :return: Temporary credentials as a dictionary.
    """
    sts_client = boto3.client('sts')
    response = sts_client.get_session_token(DurationSeconds=duration_seconds)
    
    # Extract credentials
    credentials = response['Credentials']
    return {
        'AccessKeyId': credentials['AccessKeyId'],
        'SecretAccessKey': credentials['SecretAccessKey'],
        'SessionToken': credentials['SessionToken'],
        'Expiration': credentials['Expiration']
    }

def refresh_credentials():
    temp_creds = get_temporary_credentials(duration_seconds=3600)
    
    # Update environment variables
    os.environ['AWS_ACCESS_KEY_ID'] = temp_creds['AccessKeyId']
    os.environ['AWS_SECRET_ACCESS_KEY'] = temp_creds['SecretAccessKey']
    os.environ['AWS_SESSION_TOKEN'] = temp_creds['SessionToken']
    
    # Update boto3 session
    boto_session = boto3.Session(
        aws_access_key_id=temp_creds['AccessKeyId'],
        aws_secret_access_key=temp_creds['SecretAccessKey'],
        aws_session_token=temp_creds['SessionToken'],
        region_name="us-east-1"
    )
    
    return boto_session, temp_creds['Expiration']
