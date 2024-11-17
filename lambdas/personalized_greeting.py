def lambda_handler(event, context):
    name = event.get("queryStringParameters", {}).get("name")
    if not name:
        return {
            "statusCode": 400,
            "body": '{"error": "The \'name\' parameter is required."}'
        }
    return {
        "statusCode": 200,
        "body": f'{{"message": "Hello, {name}!"}}'
    }
