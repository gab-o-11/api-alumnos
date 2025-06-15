import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    path_params = event.get('pathParameters') or {}
    tenant_id = path_params.get('tenant_id')
    alumno_id = path_params.get('alumno_id')

    if not tenant_id or not alumno_id:
        return {
            'statusCode': 400,
            'body': 'Faltan tenant_id o alumno_id en la ruta'
        }

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')
    response = table.query(
        KeyConditionExpression=Key('tenant_id').eq(tenant_id) & Key('alumno_id').eq(alumno_id)
    )
    items = response.get('Items')
    if not items:
        return {
            'statusCode': 404,
            'body': 'Alumno no encontrado'
        }

    return {
        'statusCode': 200,
        'body': items[0]
    }
