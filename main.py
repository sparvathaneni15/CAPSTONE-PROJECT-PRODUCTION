import argparse
from aws_credentials import refresh_credentials
from sagemaker_training import train_model

def main():
    parser = argparse.ArgumentParser(description="Run SageMaker training with temporary AWS credentials.")
    
    parser.add_argument("--role", required=True, help="IAM role ARN for SageMaker.")
    parser.add_argument("--bucket", required=True, help="S3 bucket name.")
    parser.add_argument("--data-key", required=True, help="S3 key for training data.")
    
    args = parser.parse_args()
    
    # Refresh AWS credentials and initialize Boto3 session
    boto_session, expiration_time = refresh_credentials()
    
    # Train model using SageMaker
    train_model(boto_session, args.role, args.bucket, args.data_key)

if __name__ == "__main__":
    main()
