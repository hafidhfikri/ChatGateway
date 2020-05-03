import requests as req
import json

def gateway(request):
    #set default response
    response = json.dumps({'fulfillmentMessages':[{'text':{'text':['Gateway Error']}}]})
    
    print(type(request))
    #get request payload
    #json_parse = request 

    #Get Parameter
    #param = json_parse.get('queryResult', {}).get('intent', {}).get('displayName')

    #print("param")

    #Route Case
    '''
    if param == 'IPSearchEngine':
        #ke routing
        response = json.dumps({'fulfillmentMessages':[{'text':{'text':['Mencari IP']}}]})
    elif param == 'ErrorList':
        #ke routing
        response = json.dumps({'fulfillmentMessages':[{'text':{'text':['Mencari Error']}}]})
    else:
        response = json.dumps({'fulfillmentMessages':[{'text':{'text':['Punten, Mamang teu paham yeuh....']}}]})
    '''
    return response