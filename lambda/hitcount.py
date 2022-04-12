import json
import os
import boto3

ddb = boto3.resource('dynamodb')
table = ddb.Table(os.environ['HITS_TABLE_NAME'])
_lambda = boto3.client('lambda')

def handler(event, context):
    # print('request: {}'.format(json.dumps(event)))
    path = event['path']
    ip = event['requestContext']['identity']['sourceIp']
    httpMethod = event['httpMethod']

    globalKey = path + '_' + httpMethod + '_' + 'ALL'
    ipKey = path + '_' + httpMethod + '_' + ip

    table.update_item(
        Key={'path': globalKey},
        UpdateExpression='ADD hits :incr',
        ExpressionAttributeValues={':incr': 1}
    )

    table.update_item(
        Key={'path': ipKey},
        UpdateExpression='ADD hits :incr',
        ExpressionAttributeValues={':incr': 1}
    )

    resp = _lambda.invoke(
        FunctionName=os.environ['DOWNSTREAM_FUNCTION_NAME'],
        Payload=json.dumps(event),
    )

    body = resp['Payload'].read()

    # print('downstream response: {}'.format(body))
    return json.loads(body)
