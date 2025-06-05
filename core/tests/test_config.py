"""
Tests de configuración para verificar el entorno de despliegue.
Estos tests se ejecutan durante el despliegue en AppRunner para asegurar
que todas las configuraciones necesarias están presentes y son correctas.
"""
from django.test import TestCase
from django.conf import settings
from loguru import logger
import sys
from datetime import datetime
import boto3
from botocore.exceptions import ClientError

# Configurar loguru para los tests
logger.remove()  # Remover el handler por defecto
logger.add(
    sys.stdout,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    level="INFO",
    colorize=True
)
logger.add(
    f"s3://{settings.AWS_STORAGE_BUCKET_NAME}/logs/tests_{datetime.now().strftime('%Y-%m-%d')}.log",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
    level="DEBUG",
    rotation="1 day",
    retention="30 days",
    compression="zip"
)

class EnvironmentConfigTests(TestCase):
    """
    Suite de pruebas para verificar la configuración del entorno.
    
    Estas pruebas verifican:
    - Variables de entorno requeridas
    - Configuración de la base de datos
    - Configuración de AWS S3
    - Configuración de seguridad
    """
    
    @classmethod
    def setUpClass(cls):
        """Configuración inicial para la clase de pruebas."""
        super().setUpClass()
        logger.info("Iniciando suite de pruebas de configuración del entorno")
    
    def setUp(self):
        """Configuración inicial para cada prueba."""
        super().setUp()
        logger.info(f"Iniciando prueba: {self._testMethodName}")
    
    def test_required_environment_variables(self):
        """
        Verifica que todas las variables de entorno requeridas estén presentes.
        
        Variables verificadas:
        - DB_HOST: Host de la base de datos
        - DB_PORT: Puerto de la base de datos
        - DB_NAME: Nombre de la base de datos
        - AWS_STORAGE_BUCKET_NAME: Nombre del bucket S3
        - AWS_S3_REGION_NAME: Región de AWS
        - AWS_S3_CUSTOM_DOMAIN: Dominio personalizado de CloudFront
        """
        logger.info("Verificando variables de entorno requeridas")
        required_vars = [
            'DB_HOST',
            'DB_PORT',
            'DB_NAME',
            'AWS_STORAGE_BUCKET_NAME',
            'AWS_S3_REGION_NAME',
            'AWS_S3_CUSTOM_DOMAIN',
        ]
        
        for var in required_vars:
            self.assertTrue(
                hasattr(settings, var),
                f"La variable de entorno {var} no está configurada"
            )
            self.assertTrue(
                getattr(settings, var),
                f"La variable de entorno {var} está vacía"
            )
        logger.info("Variables de entorno verificadas correctamente")

    def test_database_configuration(self):
        """
        Verifica la configuración de la base de datos.
        
        Configuraciones verificadas:
        - ENGINE: Motor de base de datos
        - NAME: Nombre de la base de datos
        - USER: Usuario de la base de datos
        - PASSWORD: Contraseña de la base de datos
        - HOST: Host de la base de datos
        - PORT: Puerto de la base de datos
        """
        logger.info("Verificando configuración de base de datos")
        self.assertTrue(hasattr(settings, 'DATABASES'))
        self.assertIn('default', settings.DATABASES)
        
        db_config = settings.DATABASES['default']
        required_db_settings = ['ENGINE', 'NAME', 'USER', 'PASSWORD', 'HOST', 'PORT']
        
        for setting in required_db_settings:
            self.assertIn(setting, db_config)
            self.assertTrue(db_config[setting], f"La configuración de base de datos {setting} está vacía")
        logger.info("Configuración de base de datos verificada correctamente")

    def test_aws_s3_configuration(self):
        """
        Verifica la configuración de AWS S3.
        
        Configuraciones verificadas:
        - AWS_STORAGE_BUCKET_NAME: Nombre del bucket S3
        - AWS_S3_REGION_NAME: Región de AWS
        - AWS_S3_CUSTOM_DOMAIN: Dominio personalizado de CloudFront
        - AWS_S3_OBJECT_PARAMETERS: Parámetros de objetos S3
        """
        logger.info("Verificando configuración de AWS S3")
        required_s3_settings = [
            'AWS_STORAGE_BUCKET_NAME',
            'AWS_S3_REGION_NAME',
            'AWS_S3_CUSTOM_DOMAIN',
            'AWS_S3_OBJECT_PARAMETERS',
        ]
        
        for setting in required_s3_settings:
            self.assertTrue(
                hasattr(settings, setting),
                f"La configuración de S3 {setting} no está presente"
            )
            self.assertTrue(
                getattr(settings, setting),
                f"La configuración de S3 {setting} está vacía"
            )
        logger.info("Configuración de AWS S3 verificada correctamente")

    def test_security_settings(self):
        """
        Verifica la configuración de seguridad.
        
        Configuraciones verificadas:
        - DEBUG: Modo de depuración (debe estar desactivado en producción)
        - ALLOWED_HOSTS: Hosts permitidos
        - Dominios de AWS en ALLOWED_HOSTS
        """
        logger.info("Verificando configuración de seguridad")
        # Verificar que DEBUG está desactivado en producción
        self.assertFalse(
            settings.DEBUG,
            "DEBUG debe estar desactivado en producción"
        )
        
        # Verificar ALLOWED_HOSTS
        self.assertTrue(
            hasattr(settings, 'ALLOWED_HOSTS'),
            "ALLOWED_HOSTS no está configurado"
        )
        self.assertTrue(
            isinstance(settings.ALLOWED_HOSTS, (list, tuple)),
            "ALLOWED_HOSTS debe ser una lista o tupla"
        )
        self.assertTrue(
            len(settings.ALLOWED_HOSTS) > 0,
            "ALLOWED_HOSTS está vacío"
        )
        
        # Verificar que los dominios de AWS están permitidos
        aws_domains = ['*.amazonaws.com', '*.apprunner.aws']
        for domain in aws_domains:
            self.assertIn(
                domain,
                settings.ALLOWED_HOSTS,
                f"El dominio {domain} debe estar en ALLOWED_HOSTS"
            )
        logger.info("Configuración de seguridad verificada correctamente")

    def tearDown(self):
        """Limpieza después de cada prueba."""
        super().tearDown()
        logger.info(f"Finalizando prueba: {self._testMethodName}")

    @classmethod
    def tearDownClass(cls):
        """Limpieza después de la suite de pruebas."""
        super().tearDownClass()
        logger.info("Finalizando suite de pruebas de configuración del entorno") 