import boto3
import json
import os

def lambda_handler(event, context):
    dynamodb = boto3.resource("dynamodb", region_name=os.getenv("AWS_REGION"))
    table = dynamodb.Table(os.getenv("DYNAMODB_TABLE"))

    id = event.get("queryStringParameters", {}).get("id")
    if not id:
        return {"statusCode": 400, "body": '{"error": "The \'id\' parameter is required."}'}

    try:
        response = table.get_item(Key={"id": id})
        if "Item" in response:
            return {"statusCode": 200, "body": json.dumps(response["Item"])}
        else:
            return {"statusCode": 404, "body": '{"error": "Student not found."}'}
    except Exception as e:
        return {"statusCode": 500, "body": f'{{"error": "Unexpected error: {str(e)}"}}'}
