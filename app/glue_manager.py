import boto3
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GlueManager:
    def __init__(self):
        self.glue_client = boto3.client('glue')

    def start_job(self, job_name, arguments=None):
        try:
            response = self.glue_client.start_job_run(
                JobName=job_name,
                Arguments=arguments or {}
            )
            job_run_id = response['JobRunId']
            logger.info(f"Glue job '{job_name}' started successfully with JobRunId: {job_run_id}.")
            return job_run_id
        except Exception as e:
            logger.error(f"Error starting Glue job '{job_name}': {e}")
            raise

    def get_job_status(self, job_name, job_run_id):
        try:
            response = self.glue_client.get_job_run(
                JobName=job_name,
                RunId=job_run_id
            )
            status = response['JobRun']['JobRunState']
            logger.info(f"Glue job '{job_name}' with JobRunId '{job_run_id}' is in state: {status}.")
            return status
        except Exception as e:
            logger.error(f"Error fetching status for Glue job '{job_name}': {e}")
            raise
