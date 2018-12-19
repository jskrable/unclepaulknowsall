import json
import boto3
from boto3.dynamodb.conditions import Key
import os

responses = os.environ['RESPONSES']

ddb = boto3.resource('dynamodb')
response_table = ddb.Table(responses)

def lambda_handler(event, context):
    
    query = event['query']
    terms = query.split(' ')
    keywords = ['watch','eat','weather']

    