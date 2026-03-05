import json
import csv
import boto3
import io

s3 = boto3.client("s3")

def lambda_handler(event, context):

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    print(f"Processing file from bucket: {bucket}, key: {key}")

    response = s3.get_object(Bucket=bucket, Key=key)
    content = response['Body'].read().decode('utf-8')

    csv_file = io.StringIO(content)
    reader = csv.DictReader(csv_file)

    for row in reader:
        print(row)


    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "File processed successfully"
        }),
    }