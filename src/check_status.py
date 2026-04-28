import json
import boto3
import os
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
TABLE_NAME = os.environ.get('TABLE_NAME')

def lambda_handler(event, context):
    print ("Received event:", json.dumps(event))

    try:
        table = dynamodb.Table(TABLE_NAME)
        # GET RequestId from path parameters

        if not request_Id:
            return {
                'statusCode': 400,
                'headers': { 'Access-Control-Allow-Origin': '*' },
                'body': json.dumps({'error': 'Missing requestId in path'})
            }
        


    except Exception as e:
        print (f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'headers': { 'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': str(e)})
        }