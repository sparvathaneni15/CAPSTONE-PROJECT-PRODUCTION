import unittest
from unittest.mock import patch, MagicMock
from app.sagemaker_manager import SageMakerManager

class TestSageMakerManager(unittest.TestCase):
    @patch('boto3.client')
    def test_create_endpoint(self, mock_boto_client):
        # Mock SageMaker client and its methods
        mock_sagemaker = MagicMock()
        mock_boto_client.return_value = mock_sagemaker
        
        manager = SageMakerManager()
        manager.create_endpoint("test-endpoint", "test-config")

        # Assert that create_endpoint was called with correct parameters
        mock_sagemaker.create_endpoint.assert_called_once_with(
            EndpointName="test-endpoint",
            EndpointConfigName="test-config"
        )

    @patch('boto3.client')
    def test_enable_logging(self, mock_boto_client):
        # Mock SageMaker client and its methods
        mock_sagemaker = MagicMock()
        mock_boto_client.return_value = mock_sagemaker
        
        manager = SageMakerManager()
        manager.enable_logging("test-endpoint", "test-log-group")

        # Assert that update_endpoint was called with correct parameters for enabling logging
        mock_sagemaker.update_endpoint.assert_called_once_with(
            EndpointName="test-endpoint",
            EnableCloudWatchLogging=True,
            ResourceConfig={'LogGroupName': "test-log-group"}
        )
