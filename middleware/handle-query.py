import json
import boto3
from boto3.dynamodb.conditions import Key
import os

responses = os.environ['RESPONSES']

ddb = boto3.resource('dynamodb')
response_table = ddb.Table(responses)

def lambda_handler(event, context):

    keywords = ['watch','eat','weather']

    
    query = event['query']

    terms = query.split(' ')

    for word in terms:
        if word in keywords:
            


    
    




    