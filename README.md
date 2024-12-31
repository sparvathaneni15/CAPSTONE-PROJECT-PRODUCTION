# SageMaker Training with Temporary AWS Credentials

This repository contains Python scripts to train a machine learning model on AWS SageMaker using temporary AWS credentials. The code is modular, production-ready, and includes logging and unit testing capabilities.

## Prerequisites

Before running the code, ensure you have the following:

1. **Python Environment**:
   - Python 3.7 or higher installed.
   - Install required dependencies using `pip install -r requirements.txt`.

2. **AWS Configuration**:
   - An AWS account with the necessary permissions to run SageMaker training jobs.
   - An IAM role ARN with SageMaker execution permissions.
   - An S3 bucket to store training data and outputs.

3. **Training Data**:
   - A CSV file uploaded to your S3 bucket. Update the `--data-key` parameter with its path.

4. **Dependencies**:
   - Install the following Python libraries if not already installed:
     - `boto3`
     - `sagemaker`

## File Structure

```
.
├── aws_credentials.py       # Handles temporary AWS credentials
├── sagemaker_training.py    # Defines SageMaker training logic
├── main.py                  # CLI entry point for running the code
├── test_aws_credentials.py  # Unit tests for AWS credential functions
├── requirements.txt         # Python dependencies
└── README.md                # Documentation
```

## How to Run

### Step 1: Install Dependencies

Run the following command to install required Python libraries:

```bash
pip install -r requirements.txt
```

### Step 2: Prepare Your Environment

Ensure your AWS environment is set up:
- Create an S3 bucket and upload your training data (e.g., `train.csv`).
- Note down your IAM role ARN and S3 bucket name.

### Step 3: Run the Code

Use the `main.py` script to execute the training job. The script accepts command-line arguments for configuration.

```bash
python main.py --role <IAM_ROLE_ARN> --bucket <S3_BUCKET_NAME> --data-key <S3_DATA_KEY>
```

#### Example:

```bash
python main.py --role arn:aws:iam::123456789012:role/SageMakerRole \
               --bucket my-sagemaker-bucket \
               --data-key datasets/train.csv
```

### Step 4: Monitor Training

The script automatically refreshes temporary AWS credentials during long-running jobs. Logs will provide updates on token refreshes and job status.

### Step 5: Output Location

The trained model artifacts will be saved in the specified S3 bucket under the `output/` folder.

## Testing

Unit tests are included for AWS credential functions. To run tests:

```bash
python -m unittest test_aws_credentials.py
```

## Logging

Logs are written to the console for monitoring purposes. You can modify logging levels in the `sagemaker_training.py` file by changing:

```python
logging.basicConfig(level=logging.INFO)
```

## Notes

- Ensure your IAM role has sufficient permissions for SageMaker and S3 operations.
- For large datasets, consider using SageMaker's distributed training capabilities by adjusting instance types and counts in `sagemaker_training.py`.

---

This `README.md` provides clear instructions for setting up, running, and testing the code.

Sources
[1] image.jpg https://pplx-res.cloudinary.com/image/upload/v1735656608/user_uploads/vxBgDTOyrTJxHfN/image.jpg
