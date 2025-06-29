import boto3

def lambda_handler(event, context):
    tenant_id = event.get('tenant_id')
    alumno_id = event.get('alumno_id')

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')
    response = table.delete_item(
        Key={
            'tenant_id': tenant_id,
            'alumno_id': alumno_id
        }
    )
    return {
        'statusCode': 200,
        'response': response
    }
