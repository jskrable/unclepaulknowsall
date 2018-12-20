import json
import boto3
from boto3.dynamodb.conditions import Key
import os

"""
responses = os.environ['RESPONSES']

ddb = boto3.resource('dynamodb')
response_table = ddb.Table('dev-responses')
"""

test_event = {"query": "weather"}

def lambda_handler(event, context):

    interrogatives = ['who','what','when','where','why','how','which','whose']
    #keywords = ['watch','eat','weather']
    query = event['query']
    terms = query.split(' ')

    if 'what' and 'your' and 'name' in query:
        response = "I'm Uncle Paul. It says my name all over the screen."
    elif 'where' and 'are' and 'you' in query:
        response = "I live in this computer now. I don't even have internet. Pretty cool, right?"
    else:
        response = "You've got something on your shirt..."
        

    return {
        'statusCode': 200,
        'body': json.dumps(response)}
    

    
def test():
    print(lambda_handler(test_event, None))

test()

    
    




    