from django.http import HttpResponse
import os
from django.db import connection
from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    return render(request, 'core/home.html')

def health(request):
    return JsonResponse({'status': 'ok'}, status=200)

def db_health_check(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            return JsonResponse({'status': 'ok'}, status=200)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
