import seedphrase
import responses

def get_seedphrase(ip):
    return responses.success('{"seedphrase":"' + (" ". join(seedphrase.generate_seedphrase(seedphrase.get_word_list()))) + '"}')

# def generate_report(ip):
#     print('generating seedphrase report for ' + ip)
#     return responses.success('{"results":[{"publicKey":"1GNgwA8JfG7Kc8akJ8opdNWJUihqUztfPe", "currencyAmount": "965.28794308", "currencySymbol": "BTC"}]}')

def unknown_route(ip):
    print('Unknown route for ' + ip)
    return responses.error(404, '{"error": "Unknown route"}')

def seedphrases(httpMethod, ip):
    return {
        'GET': get_seedphrase(ip),
        # 'POST': generate_report(ip)
    }.get(httpMethod, unknown_route(ip))   

def handler(event, context):
    ip = event['requestContext']['identity']['sourceIp']
    path = event['path']
    httpMethod = event['httpMethod']

    return {
        '/seedphrases': seedphrases(httpMethod, ip),
    }.get(path, unknown_route(ip))   

