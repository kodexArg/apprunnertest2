from django.urls import path
from .views import health, db_health_check, home

urlpatterns = [
    path('health/', health, name='health'),
    path('health/db/', db_health_check, name='db_health_check'),
    path('home/', home, name='home'),
] 