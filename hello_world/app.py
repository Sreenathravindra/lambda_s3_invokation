import json
import csv
# import requests


def lambda_handler(event, context):


    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']



    with open("raw_orders.csv", "r") as file:
        reader = csv.DictReader(file)

    for row in reader:
        print(row)

    print(bucket)
    print(key)


    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }
