from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from datetime import datetime

def keyboard(request):
    
    return JsonResponse({
        'type':'buttons',
        'buttons':['name','now']
    })
 
@csrf_exempt
def answer(request):

    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    datacontent = received_json_data['content']
 
    if datacontent == 'name':
        myName = "Cho Chan Bong"
 
        return JsonResponse({
                'message': {
                    'text': myName
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['name','now']
                }
 
            })
 
    elif datacontent == 'now':
        dateNow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
 
        return JsonResponse({
                'message': {
                    'text': dateNow
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['name','now']
                }
 
            })