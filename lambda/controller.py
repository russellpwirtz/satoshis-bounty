import json
import os
import csv
import random

def get_word_list():
    file = open('seedphrase_word_list.txt')
    csvreader = csv.reader(file)
    words = []
    for row in csvreader:
        words.append(row[0])
    return words

def getSeedPhrase(ip):
    print('creating new seedphrase for ' + ip)

    words = get_word_list()
    print("word list: " + str(words))

    seedphrase = set()
    while (len(seedphrase) < 12):
        seedphrase.add(random.choice(words))

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': '{"seedphrase":"' + str(seedphrase) + '"}'
    }

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

def handler(event, context):
    ip = event['requestContext']['identity']['sourceIp']
    path = event['path']
    httpMethod = event['httpMethod']

    print("IP:", ip)
    print("path:", path)
    print("httpMethod:", httpMethod)

    return {
        '/seedphrases': seedPhrases(httpMethod, ip),
    }.get(path, defaultResponse(ip))   

