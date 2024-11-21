def lambda_handler(event, context):
    params = event.get("queryStringParameters", {})
    try:
        a = float(params.get("a"))
        b = float(params.get("b"))
        operator = params.get("operator")
        if operator == "+":
            result = a + b
        elif operator == "-":
            result = a - b
        elif operator == "*":
            result = a * b
        elif operator == "/":
            if b == 0:
                raise ValueError("Division by zero.")
            result = a / b
        else:
            raise ValueError("Invalid operator.")
        return {"statusCode": 200, "body": f'{{"result": {result}}}'}
    except (ValueError, TypeError) as e:
        return {"statusCode": 400, "body": f'{{"error": "{str(e)}"}}'}
