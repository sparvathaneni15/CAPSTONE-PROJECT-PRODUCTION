import unittest
from scripts.aws_credentials import get_temporary_credentials

class TestAWSCredentials(unittest.TestCase):
    
    def test_get_temporary_credentials(self):
        creds = get_temporary_credentials(duration_seconds=900)  # Test with a short duration
        
        self.assertIn('AccessKeyId', creds)
        self.assertIn('SecretAccessKey', creds)
        self.assertIn('SessionToken', creds)
