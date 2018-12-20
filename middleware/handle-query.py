import json
import boto3
from boto3.dynamodb.conditions import Key
import os

"""
responses = os.environ['RESPONSES']

ddb = boto3.resource('dynamodb')
response_table = ddb.Table('dev-responses')
"""

test_event = {"query": "whats the weather like"}

def lambda_handler(event, context):

    interrogatives = ['who','what','when','where','why','how','which','whose']
    keywords = ['watch','eat','weather','name','game','win','live','are','you']
    query = event['query']
    # terms = query.split(' ')
    score = []
    [score.append(x) for x in interrogatives if x in query]
    [score.append(x) for x in keywords if x in query]
    print(score)

    if 'what' and 'name' in score:
        response = "I'm Uncle Paul. It says my name all over the screen."
    elif 'where' and 'you' and 'live' in score:
        response = "I live in this computer now. I don't even have internet. Pretty cool, right?"
    elif 'what' and 'weather' in score:
        response = "Hey, Pop... Never mind, he's asleep."
    else:
        response = "You've got something on your shirt..."

    return {
        'statusCode': 200,
        'body': json.dumps(response)}
    

    
def test():
    print(lambda_handler(test_event, None))

test()

    
    




    