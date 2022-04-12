import json

def generateSeedPhrase(ip):
    print('generating seedphrase for ' + ip)
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': "{'seedphrase':'select, sell, seminar'}"
    }

def defaultResponse(ip):
    print('Unknown route for ' + ip)
    return {
        'statusCode': 404,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': "{'error': 'Unknown route'}"
    }

def route_request(path, ip):
    return {
        '/seedphrases/generate': generateSeedPhrase(ip),
    }.get(path, defaultResponse(ip))   


def handler(event_json, context):
    # print("Type:", type(event))
    # event_json = json.loads(event)

    ip = event_json['requestContext']['identity']['sourceIp']
    path = event_json['path']

    print("Type:", type(event_json))
    print("IP:", ip)
    print("path:", path)

    print('request: {}'.format(json.dumps(event_json)))

    return route_request(path, ip)

