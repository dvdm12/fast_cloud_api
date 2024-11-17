import json

def lambda_handler(event, context):
    try:
        body = json.loads(event["body"])
        text = body.get("text", "")
        word_count = len(text.split())
        char_count = len(text)
        uppercase_text = text.upper()
        return {
            "statusCode": 200,
            "body": json.dumps({
                "word_count": word_count,
                "char_count": char_count,
                "uppercase_text": uppercase_text
            })
        }
    except KeyError:
        return {"statusCode": 400, "body": '{"error": "The body must include a \'text\' field."}'}
