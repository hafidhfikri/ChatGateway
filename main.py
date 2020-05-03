import requests as req
import json

def gateway(request):
    #set default response
    response = json.dumps({'fulfillmentMessages':[{'text':{'text':['Mashoookkk']}}]})
    
    #get request payload
    #json_parse = request.get_json() 

    #Get Parameter
    #param = json_parse.get('queryResult', {}).get('intent', {}).get('displayName')

    #Route Case

    #return json.dumps({'fulfillmentMessages':[{'text':{'text':[param]}}]})
    return response