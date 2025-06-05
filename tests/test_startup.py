from django.test import TestCase
from django.conf import settings
from loguru import logger
import sys
from datetime import datetime
import boto3
from botocore.exceptions import ClientError

logger.remove()
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

class IntegrationTests(TestCase):
    """Test suite for system-wide integration tests.
    
    This suite verifies the integration between different components of the system,
    including environment configuration, database connectivity, AWS services,
    and security settings.
    """

    @classmethod
    def setUpClass(cls):
        """Set up test environment for the entire test suite."""
        super().setUpClass()
        logger.info("Starting integration test suite")
    
    def setUp(self):
        """Set up test environment for each test."""
        super().setUp()
        logger.info(f"Starting test: {self._testMethodName}")
    
    def test_environment_configuration(self):
        """Verify that all required environment variables are properly configured."""
        logger.info("Verifying environment configuration")
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
                f"Environment variable {var} is not configured"
            )
            self.assertTrue(
                getattr(settings, var),
                f"Environment variable {var} is empty"
            )
        logger.info("Environment configuration verified successfully")

    def test_database_integration(self):
        """Verify database configuration and connectivity settings."""
        logger.info("Verifying database integration")
        self.assertTrue(hasattr(settings, 'DATABASES'))
        self.assertIn('default', settings.DATABASES)
        
        db_config = settings.DATABASES['default']
        required_db_settings = ['ENGINE', 'NAME', 'USER', 'PASSWORD', 'HOST', 'PORT']
        
        for setting in required_db_settings:
            self.assertIn(setting, db_config)
            self.assertTrue(db_config[setting], f"Database setting {setting} is empty")
        logger.info("Database integration verified successfully")

    def test_aws_integration(self):
        """Verify AWS S3 configuration and connectivity settings."""
        logger.info("Verifying AWS integration")
        required_s3_settings = [
            'AWS_STORAGE_BUCKET_NAME',
            'AWS_S3_REGION_NAME',
            'AWS_S3_CUSTOM_DOMAIN',
            'AWS_S3_OBJECT_PARAMETERS',
        ]
        
        for setting in required_s3_settings:
            self.assertTrue(
                hasattr(settings, setting),
                f"S3 setting {setting} is not present"
            )
            self.assertTrue(
                getattr(settings, setting),
                f"S3 setting {setting} is empty"
            )
        logger.info("AWS integration verified successfully")

    def test_security_integration(self):
        """Verify security-related settings and configurations."""
        logger.info("Verifying security integration")
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
        
        aws_domains = ['*.amazonaws.com', '*.apprunner.aws']
        for domain in aws_domains:
            self.assertIn(
                domain,
                settings.ALLOWED_HOSTS,
                f"Domain {domain} must be in ALLOWED_HOSTS"
            )
        logger.info("Security integration verified successfully")

    def tearDown(self):
        """Clean up after each test."""
        super().tearDown()
        logger.info(f"Finishing test: {self._testMethodName}")

    @classmethod
    def tearDownClass(cls):
        """Clean up after the entire test suite."""
        super().tearDownClass()
        logger.info("Finishing integration test suite") 