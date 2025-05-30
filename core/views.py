from django.http import HttpResponse
import os

def hello_world(request):
    ping_value = os.environ.get('PING', 'NO_SECRET')
    return HttpResponse(f'Hello World - PING: {ping_value}')
