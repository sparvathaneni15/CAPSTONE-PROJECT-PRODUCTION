import logging
import time
from datetime import datetime, timezone
import threading
from sagemaker.inputs import TrainingInput
from sagemaker.estimator import Estimator
from sagemaker import image_uris

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def monitor_and_refresh_token(refresh_function, expiration_time):
    """
    Monitor and refresh AWS temporary credentials before expiration.
    
    :param refresh_function: Function to refresh credentials.
    :param expiration_time: Current expiration time of the token.
    """
    while True:
        current_time = datetime.now(timezone.utc)
        if (expiration_time - current_time).total_seconds() < 300:
            logger.info("Refreshing temporary credentials...")
            _, expiration_time = refresh_function()
            logger.info(f"New token expiration time: {expiration_time}")
        
        time.sleep(60)

def train_model(boto_session, role, bucket, data_key):
    """
    Train a model using SageMaker.
    
    :param boto_session: Boto3 session with temporary credentials.
    :param role: IAM role ARN for SageMaker.
    :param bucket: S3 bucket name.
    :param data_key: S3 key for training data.
    """
    sagemaker_session = sagemaker.Session(boto_session=boto_session)
    
    # Define resources and input
    data_location = f"s3://{bucket}/{data_key}"
    output_path = f"s3://{bucket}/output/"
    
    train_input = TrainingInput(
        s3_data=data_location,
        content_type="text/csv"
    )
    
    image_uri = image_uris.retrieve(
        framework="xgboost",
        region=sagemaker_session.boto_region_name,
        version="1.5-1",
        image_scope="training"
    )
    
    estimator = Estimator(
        image_uri=image_uri,
        role=role,
        instance_count=3,
        instance_type="ml.m5.large",
        volume_size=100,
        output_path=output_path,
        hyperparameters={
            "n_estimators": 1150,
            "max_depth": 56,
            "learning_rate": 0.003,
            "colsample_bytree": 0.9,
            "subsample": 0.8,
            "min_child_weight": 1,
            "random_state": 42,
            "objective": "reg:squarederror",
            "tree_method": "hist",
            "device": "gpu" if "p" in "ml.m5.large" else "cpu",
        },
        sagemaker_session=sagemaker_session
    )
    
    # Start monitoring token expiration in a separate thread
    monitor_thread = threading.Thread(target=monitor_and_refresh_token, args=(refresh_credentials, expiration_time), daemon=True)
    monitor_thread.start()
    
    # Launch training job
    logger.info("Starting training job...")
    estimator.fit({"train": train_input})
