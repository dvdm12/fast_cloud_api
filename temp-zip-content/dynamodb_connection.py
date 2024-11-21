import boto3
import json


AWS_REGION = "us-east-1"
DYNAMODB_TABLE = "Students"


dynamodb = boto3.resource("dynamodb", region_name=AWS_REGION)
table = dynamodb.Table(DYNAMODB_TABLE)

def get_student_by_id(student_id):
    """
    Consulta un estudiante en DynamoDB por su ID.
    """
    try:
        response = table.get_item(Key={"id": student_id})
        return response.get("Item")
    except Exception as e:
        raise Exception(f"Error al obtener el estudiante: {str(e)}")

def validate_event(event):
    """
    Valida los parámetros del evento y extrae el 'id'.
    """
    student_id = event.get("queryStringParameters", {}).get("id")
    if not student_id:
        raise ValueError("El parámetro 'id' es obligatorio.")
    return student_id

def create_response(status_code, body):
    """
    Crea una respuesta con formato JSON.
    """
    return {
        "statusCode": status_code,
        "body": json.dumps(body),
        "headers": {"Content-Type": "application/json"}
    }

def lambda_handler(event, context):
    """
    Manejador principal de la función Lambda.
    """
    try:
        # Validar el evento y obtener el ID del estudiante
        student_id = validate_event(event)

        # Consultar el estudiante en DynamoDB
        student = get_student_by_id(student_id)

        if student:
            return create_response(200, student)
        else:
            return create_response(404, {"error": "Estudiante no encontrado."})

    except ValueError as ve:
        # Errores de validación
        return create_response(400, {"error": str(ve)})
    except Exception as e:
        # Errores inesperados
        return create_response(500, {"error": f"Error inesperado: {str(e)}"})
