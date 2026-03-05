import json
import csv
import boto3
import io
import logging
from validation import validate_row

# Logger configuration
logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3 = boto3.client("s3")


def lambda_handler(event, context):
    """
    Entry point for Lambda triggered by S3 event
    """

    logger.info("Lambda triggered with event: %s", json.dumps(event))

    try:
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']
    except KeyError as e:
        logger.error("Invalid event structure: %s", e)
        raise

    logger.info(f"Processing file from bucket: {bucket}, key: {key}")

    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        content = response['Body'].read().decode('utf-8')
    except Exception as e:
        logger.error("Failed to read file from S3: %s", str(e))
        raise

    csv_file = io.StringIO(content)
    reader = csv.DictReader(csv_file)

    valid_rows = []
    invalid_rows = []
    seen_ids = set()

    total_records = 0

    for row in reader:
        total_records += 1

        try:
            errors = validate_row(row, seen_ids)

            if errors:
                row["errors"] = errors
                invalid_rows.append(row)
            else:
                valid_rows.append(row)

        except Exception as e:
            logger.error("Unexpected error while validating row %s: %s", row, str(e))
            row["errors"] = ["Unexpected validation error"]
            invalid_rows.append(row)

    logger.info("Processing completed")
    logger.info("Total records: %s", total_records)
    logger.info("Valid records: %s", len(valid_rows))
    logger.info("Invalid records: %s", len(invalid_rows))

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "File processed successfully",
            "total_records": total_records,
            "valid_records": len(valid_rows),
            "invalid_records": len(invalid_rows)
        }),
    }