from django.http import HttpResponse
import os
from django.db import connection

def hello_world(request):
    ping_value = os.environ.get('PING', 'NO_SECRET')
    return HttpResponse(f'Hello World - PING: {ping_value}')

def db_health_check(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            return HttpResponse("Database connection successful", status=200)
    except Exception as e:
        return HttpResponse(f"Database connection failed: {str(e)}", status=500)
