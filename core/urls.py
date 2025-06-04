from django.urls import path
from .views import hello_world, db_health_check

urlpatterns = [
    path('', hello_world),
    path('health/db/', db_health_check),
] 