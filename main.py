from app.s3_manager import S3Manager
from app.sagemaker_manager import SageMakerManager

if __name__ == "__main__":
    s3_manager = S3Manager()
    sagemaker_manager = SageMakerManager()

    # Create S3 bucket example
    s3_manager.create_bucket("climate-prediction-data", "us-east-1")

    # Create SageMaker endpoint example
    sagemaker_manager.create_endpoint("climate-endpoint", "climate-endpoint-config")
