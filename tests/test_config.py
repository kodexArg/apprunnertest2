from django.test import TestCase
from django.conf import settings
from loguru import logger
import sys
import os

logger.remove()
logger.add(
    sys.stdout,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    level="INFO",
    colorize=True
)

class ConfigTests(TestCase):
    """Test suite for critical configuration settings.
    
    These tests verify that all required configuration settings are present
    and properly configured before the application starts.
    """

    def setUp(self):
        """Set up test environment for each test."""
        super().setUp()
        logger.info(f"Starting test: {self._testMethodName}")

    def test_secret_key(self):
        """Verify that SECRET_KEY is configured."""
        logger.info("Verifying SECRET_KEY configuration")
        self.assertTrue(hasattr(settings, 'SECRET_KEY'))
        self.assertTrue(settings.SECRET_KEY)
        logger.info("SECRET_KEY configuration verified")

    def test_database_config(self):
        """Verify that database configuration is present."""
        logger.info("Verifying database configuration")
        self.assertTrue(hasattr(settings, 'DATABASES'))
        self.assertIn('default', settings.DATABASES)
        
        db_config = settings.DATABASES['default']
        required_settings = ['ENGINE', 'NAME', 'USER', 'PASSWORD', 'HOST', 'PORT']
        
        for setting in required_settings:
            self.assertIn(setting, db_config)
            self.assertTrue(db_config[setting], f"Database setting {setting} is empty")
        logger.info("Database configuration verified")

    def test_aws_config(self):
        """Verify that AWS configuration is present."""
        logger.info("Verifying AWS configuration")
        required_settings = [
            'AWS_STORAGE_BUCKET_NAME',
            'AWS_S3_REGION_NAME',
            'AWS_S3_CUSTOM_DOMAIN',
        ]
        
        for setting in required_settings:
            self.assertTrue(
                hasattr(settings, setting),
                f"AWS setting {setting} is not present"
            )
            self.assertTrue(
                getattr(settings, setting),
                f"AWS setting {setting} is empty"
            )
        logger.info("AWS configuration verified")

    def test_security_settings(self):
        """Verify that security settings are properly configured."""
        logger.info("Verifying security settings")
        self.assertFalse(
            settings.DEBUG,
            "DEBUG must be disabled in production"
        )
        
        self.assertTrue(
            hasattr(settings, 'ALLOWED_HOSTS'),
            "ALLOWED_HOSTS is not configured"
        )
        self.assertTrue(
            isinstance(settings.ALLOWED_HOSTS, (list, tuple)),
            "ALLOWED_HOSTS must be a list or tuple"
        )
        self.assertTrue(
            len(settings.ALLOWED_HOSTS) > 0,
            "ALLOWED_HOSTS is empty"
        )
        logger.info("Security settings verified")

    def test_installed_apps(self):
        """Verify that all required apps are installed."""
        logger.info("Verifying installed apps")
        required_apps = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'storages',
            'core',
        ]
        
        for app in required_apps:
            self.assertIn(app, settings.INSTALLED_APPS)
        logger.info("Installed apps verified")

    def test_middleware(self):
        """Verify that all required middleware is configured."""
        logger.info("Verifying middleware configuration")
        required_middleware = [
            'django.middleware.security.SecurityMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
        ]
        
        for middleware in required_middleware:
            self.assertIn(middleware, settings.MIDDLEWARE)
        logger.info("Middleware configuration verified")

    def tearDown(self):
        """Clean up after each test."""
        super().tearDown()
        logger.info(f"Finishing test: {self._testMethodName}") 