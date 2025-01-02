import boto3
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SageMakerManager:
    def __init__(self):
        self.sagemaker_client = boto3.client('sagemaker')

    def create_endpoint(self, endpoint_name, config_name):
        try:
            self.sagemaker_client.create_endpoint(
                EndpointName=endpoint_name,
                EndpointConfigName=config_name
            )
            logger.info(f"SageMaker endpoint '{endpoint_name}' created successfully.")
        except Exception as e:
            logger.error(f"Error creating SageMaker endpoint: {e}")
            raise

    def enable_logging(self, endpoint_name, log_group_name):
        try:
            self.sagemaker_client.update_endpoint(
                EndpointName=endpoint_name,
                EnableCloudWatchLogging=True,
                ResourceConfig={'LogGroupName': log_group_name}
            )
            logger.info(f"CloudWatch logging enabled for endpoint '{endpoint_name}'.")
        except Exception as e:
            logger.error(f"Error enabling logging: {e}")
            raise
