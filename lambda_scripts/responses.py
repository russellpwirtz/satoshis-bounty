def success(body):
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': body
    }

def error(code, body):
    return {
        'statusCode': code,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': body
    }

    