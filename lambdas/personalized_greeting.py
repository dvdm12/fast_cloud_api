import json


def lambda_handler(event, context):
    # Extraer parámetros del cuerpo de la solicitud
    body = json.loads(event["body"])  # Convertir el body de texto JSON a un diccionario

    # Obtener el parámetro 'name'
    name = body.get("name")

    # Validar que el parámetro 'name' esté presente
    if not name:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "The 'name' parameter is required."})
        }

    # Responder con un mensaje personalizado
    return {
        "statusCode": 200,
        "body": json.dumps({"message": f"Hello, {name}!"})
    }
