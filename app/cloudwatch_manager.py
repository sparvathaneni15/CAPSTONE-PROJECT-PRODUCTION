import boto3
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CloudWatchManager:
    def __init__(self):
        self.cloudwatch_client = boto3.client('cloudwatch')

    def create_alarm(self, alarm_name, metric_name, namespace, threshold, comparison_operator, period, evaluation_periods):
        try:
            self.cloudwatch_client.put_metric_alarm(
                AlarmName=alarm_name,
                MetricName=metric_name,
                Namespace=namespace,
                Threshold=threshold,
                ComparisonOperator=comparison_operator,
                Period=period,
                EvaluationPeriods=evaluation_periods,
                ActionsEnabled=False  # Disable actions for simplicity
            )
            logger.info(f"CloudWatch alarm '{alarm_name}' created successfully.")
        except Exception as e:
            logger.error(f"Error creating CloudWatch alarm: {e}")
            raise

    def log_metric(self, namespace, metric_name, value):
        try:
            self.cloudwatch_client.put_metric_data(
                Namespace=namespace,
                MetricData=[
                    {
                        'MetricName': metric_name,
                        'Value': value
                    }
                ]
            )
            logger.info(f"Metric '{metric_name}' logged to CloudWatch under namespace '{namespace}'.")
        except Exception as e:
            logger.error(f"Error logging metric to CloudWatch: {e}")
            raise
