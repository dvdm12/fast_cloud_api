import json

def lambda_handler(event, context):
    # Extraer parámetros del cuerpo de la solicitud
    body = json.loads(event["body"])  # Convertir el body de texto JSON a un diccionario

    a = body.get("a")
    b = body.get("b")
    operator = body.get("operator")

    if not (a and b and operator):
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Missing parameters"})
        }

    # Realizar cálculo simple
    a, b = float(a), float(b)
    result = None
    if operator == "+":
        result = a + b
    elif operator == "-":
        result = a - b
    elif operator == "*":
        result = a * b
    elif operator == "/":
        result = a / b
    else:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Invalid operator"})
        }

    return {
        "statusCode": 200,
        "body": json.dumps({"result": result})
    }
