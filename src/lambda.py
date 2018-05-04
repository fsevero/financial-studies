import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
table = dynamodb.Table('datasetc')

def lambda_handler(event, context):
    document_number = event['document']

    try:
        response  = table.get_item(
            Key={'Document': document_number}
        )
    except ClientError as e:
        raise Exception(e.response['Error']['Message'])

    if 'Item' not in response:
        raise Exception('Document not found')

    return response['Item']