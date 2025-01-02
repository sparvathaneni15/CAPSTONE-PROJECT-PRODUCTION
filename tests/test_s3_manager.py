import unittest
from unittest.mock import patch, MagicMock
from app.s3_manager import S3Manager

class TestS3Manager(unittest.TestCase):
    @patch('boto3.client')
    def test_create_bucket(self, mock_boto_client):
        mock_s3 = MagicMock()
        mock_boto_client.return_value = mock_s3
        
        manager = S3Manager()
        manager.create_bucket('test-bucket', 'us-east-1')
        
        mock_s3.create_bucket.assert_called_once_with(
            Bucket='test-bucket',
            CreateBucketConfiguration={'LocationConstraint': 'us-east-1'}
        )
