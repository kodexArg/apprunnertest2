from django.http import HttpResponse
import os
from django.db import connection
from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    return render(request, 'core/home.html')

def hello_world(request):
    return HttpResponse("Hello World")

def health(request):
    return JsonResponse({'status': 'ok', 'message': 'Health check successful'}, status=200)

def db_health_check(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            return JsonResponse({'status': 'ok', 'message': 'Database connection successful'}, status=200)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': 'Database connection failed'}, status=500)
