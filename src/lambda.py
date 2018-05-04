import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
table = dynamodb.Table('datasetc')

def lambda_handler(event, context):
    document_number = event['document']

    response  = table.get_item(
        Key={'Document': document_number}
    )

    if 'Item' not in response:
        raise Exception('Document not found')

    return response['Item']