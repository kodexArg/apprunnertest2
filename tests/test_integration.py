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
    format="[{level: <8}] {name}:{function}:{line} - {message}",
    level="INFO"
)

class IntegrationTests(TestCase):
    """Test suite for external service integration tests. Verifies connectivity and functionality with AWS S3 and database."""

    @classmethod
    def setUpClass(cls):
        """Set up test environment for the entire test suite."""
        super().setUpClass()
        logger.info("Starting integration test suite")
    
    def setUp(self):
        """Set up test environment for each test."""
        super().setUp()
        logger.info(f"Starting test: {self._testMethodName}")

    def test_s3_connectivity(self):
        """Verifies actual connectivity to AWS S3 by attempting to list objects in the bucket."""
        logger.info("Testing S3 connectivity")
        try:
            s3_client = boto3.client(
                's3',
                region_name=settings.AWS_S3_REGION_NAME
            )
            # Try to list objects in the bucket
            response = s3_client.list_objects_v2(
                Bucket=settings.AWS_STORAGE_BUCKET_NAME,
                MaxKeys=1
            )
            self.assertIsNotNone(response)
            logger.info("S3 connectivity test successful")
        except ClientError as e:
            self.fail(f"S3 connectivity test failed: {str(e)}")

    def test_database_connectivity(self):
        """Verifies database connectivity by executing a simple SELECT query."""
        logger.info("Testing database connectivity")
        from django.db import connection
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
                result = cursor.fetchone()
                self.assertEqual(result[0], 1)
            logger.info("Database connectivity test successful")
        except Exception as e:
            self.fail(f"Database connectivity test failed: {str(e)}")

    def test_static_files_storage(self):
        """Verifies S3 static file storage by saving and retrieving a test file."""
        logger.info("Testing static files storage")
        from django.core.files.storage.storage import get_storage_class
        storage = get_storage_class('storages.backends.s3.S3Storage')()
        test_content = b"Test content for static file storage"
        test_filename = "test_static_file.txt"
        
        try:
            # Log storage configuration
            logger.info(f"Using bucket: {settings.AWS_STORAGE_BUCKET_NAME}")
            logger.info(f"Using region: {settings.AWS_S3_REGION_NAME}")
            
            # Try to save a file
            logger.info("Attempting to save file...")
            storage.save(test_filename, test_content)
            
            # Try to read it back
            logger.info("Attempting to read file...")
            with storage.open(test_filename) as f:
                content = f.read()
                self.assertEqual(content, test_content)
            
            # Clean up
            logger.info("Attempting to delete file...")
            storage.delete(test_filename)
            logger.info("Static files storage test successful")
        except Exception as e:
            logger.error(f"Storage test failed with error: {str(e)}")
            logger.error(f"Error type: {type(e).__name__}")
            if hasattr(e, 'response'):
                logger.error(f"AWS Response: {e.response}")
            self.fail(f"Static files storage test failed: {str(e)}")

    def tearDown(self):
        """Clean up after each test."""
        super().tearDown()
        logger.info(f"Finishing test: {self._testMethodName}")

    @classmethod
    def tearDownClass(cls):
        """Clean up after the entire test suite."""
        super().tearDownClass()
        logger.info("Finishing integration test suite") 