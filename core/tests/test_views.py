from django.test import TestCase, Client
from django.urls import reverse
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

class CoreViewsTests(TestCase):
    """Test suite for core application views.
    
    This suite verifies the functionality of the core application's views,
    including the hello world endpoint and database health check endpoint.
    """

    def setUp(self):
        """Set up test client and logging for each test."""
        self.client = Client()
        logger.info(f"Starting test: {self._testMethodName}")

    def test_hello_world(self):
        """Verify that the hello world endpoint returns a 200 status code and contains expected text."""
        logger.info("Testing hello_world endpoint")
        response = self.client.get(reverse('hello_world'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('Hello World', response.content.decode())
        logger.info("hello_world endpoint tested successfully")

    def test_db_health_check_success(self):
        """Verify that the database health check endpoint returns 200 when database is accessible."""
        logger.info("Testing db_health_check endpoint with successful connection")
        response = self.client.get(reverse('db_health_check'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('successful', response.content.decode())
        logger.info("db_health_check endpoint tested successfully")

    def test_db_health_check_failure(self):
        """Verify that the database health check endpoint returns 500 when database is inaccessible."""
        logger.info("Testing db_health_check endpoint with connection failure")
        os.environ['DB_HOST'] = 'invalid_host'
        response = self.client.get(reverse('db_health_check'))
        self.assertEqual(response.status_code, 500)
        self.assertIn('failed', response.content.decode().lower())
        logger.info("db_health_check endpoint failure test completed")

    def tearDown(self):
        """Clean up after each test."""
        logger.info(f"Finishing test: {self._testMethodName}") 