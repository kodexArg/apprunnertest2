from django.apps import AppConfig
from django.conf import settings
import os


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        from django.contrib.auth.models import User
        
        if not User.objects.filter(username='admin').exists():
            # Obtener credenciales de la base de datos
            db_user = settings.DATABASES['default']['USER']
            db_password = settings.DATABASES['default']['PASSWORD']
            
            User.objects.create_superuser(
                username=db_user,
                email=f'{db_user}@example.com',
                password=db_password
            )
