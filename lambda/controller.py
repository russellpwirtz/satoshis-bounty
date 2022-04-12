import json


def getSeedPhrase(ip):
    print('getting seedphrase for ' + ip)
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': '{"seedphrase":"select, sell, seminar, select, sell, seminar, select, sell, seminar, select, sell, seminar"}'
    }

# TODO: pass in json request body
def generateReport(ip):
    print('generating seedphrase report for ' + ip)
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': '{"results":[{"publicKey":"1GNgwA8JfG7Kc8akJ8opdNWJUihqUztfPe", "currencyAmount": "965.28794308", "currencySymbol": "BTC"}]}'
    }

def seedPhrases(httpMethod, ip):
    return {
        'GET': getSeedPhrase(ip),
        'POST': generateReport(ip)
    }.get(httpMethod, defaultResponse(ip))   


def defaultResponse(ip):
    print('Unknown route for ' + ip)
    return {
        'statusCode': 404,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': '{"error": "Unknown route"}'
    }

def route_request(path, httpMethod, ip):
    return {
        '/seedphrases': seedPhrases(httpMethod, ip),
    }.get(path, defaultResponse(ip))   


def handler(event, context):
    ip = event['requestContext']['identity']['sourceIp']
    path = event['path']
    httpMethod = event['httpMethod']

    print("IP:", ip)
    print("path:", path)
    print("httpMethod:", httpMethod)

    return route_request(path, httpMethod, ip)

