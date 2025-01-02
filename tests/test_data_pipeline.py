import unittest
from unittest.mock import patch, MagicMock
from app.data_pipeline import DataPipeline

class TestDataPipeline(unittest.TestCase):
    @patch('app.s3_manager.S3Manager')
    def test_execute_pipeline(self, mock_s3_manager_class):
        # Mock S3Manager methods
        mock_s3_manager = MagicMock()
        mock_s3_manager_class.return_value = mock_s3_manager

        # Create instance of DataPipeline and execute pipeline
        pipeline = DataPipeline()
        pipeline.execute_pipeline("local/raw_data.csv", "local/processed_data.csv", "test-bucket")

        # Assert upload_data was called twice (for raw and processed data)
        self.assertEqual(mock_s3_manager.upload_data.call_count, 2)
        
        # Assert correct arguments were passed to upload_data
        mock_s3_manager.upload_data.assert_any_call("local/raw_data.csv", "test-bucket", "raw_data/")
        mock_s3_manager.upload_data.assert_any_call("local/processed_data.csv", "test-bucket", "processed_data/")
