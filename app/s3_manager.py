import boto3
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class S3Manager:
    def __init__(self):
        self.s3_client = boto3.client('s3')

    def create_bucket(self, bucket_name, region):
        try:
            self.s3_client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': region}
            )
            logger.info(f"S3 bucket '{bucket_name}' created successfully in region '{region}'.")
        except Exception as e:
            logger.error(f"Error creating S3 bucket: {e}")
            raise

    def upload_data(self, local_path, bucket_name, s3_path):
        try:
            self.s3_client.upload_file(local_path, bucket_name, s3_path)
            logger.info(f"Data uploaded to S3: {bucket_name}/{s3_path}")
        except Exception as e:
            logger.error(f"Error uploading data to S3: {e}")
            raise
