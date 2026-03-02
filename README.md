## Serverless S3 Event Processing using AWS SAM
# Project Overview
This project demonstrates an event-driven serverless architecture where files uploaded to Amazon S3 automatically trigger an AWS Lambda function. The Lambda function processes the file metadata and logs the results into CloudWatch.

The entire infrastructure is provisioned using AWS SAM (Serverless Application Model), enabling Infrastructure as Code (IaC).

## Architecture

S3 → Lambda → CloudWatch Logs

## Problem Statement

Modern applications require automated, scalable processing of incoming files without managing servers.

This project implements a serverless solution that:

 - Automatically reacts to file uploads

 - Processes data using AWS Lambda

 - Enables local testing via SAM CLI

 - Deploys infrastructure using CloudFormation

## Tech Stack

 - AWS Lambda
 - Amazon S3
 - Amazon API Gateway
 - AWS SAM
 - AWS CloudFormation
 - Python
 - Docker

## Features

✔ Event-driven architecture
✔ Fully serverless deployment
✔ Infrastructure as Code (IaC)
✔ Local testing using SAM CLI
✔ API Gateway integration
✔ CloudWatch log monitoring

## Deployment
Build the application:
 sam build --use-container
Deploy the application:
 sam deploy --guided
Run locally:
sam local start-api

## Project Structure

new_proj/
│
├── hello_world/        # Lambda function code
├── events/             # Test event JSON files
├── tests/              # Unit and integration tests
├── template.yaml       # Infrastructure definition (SAM)

## Key Learnings

- Understanding AWS SAM template structure
- Handling S3 event notifications
- Configuring IAM roles securely
- Local testing with Docker containers
- Debugging Lambda logs using CloudWatch

## Future Enhancements (Data Engineer Upgrade)

- Add CSV validation logic
- Store processed data in DynamoDB
- Move valid/invalid records to separate S3 buckets
- Add Step Functions for workflow orchestration
- Integrate with AWS Glue for ETL
