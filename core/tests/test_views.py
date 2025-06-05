from django.test import TestCase, Client
from django.urls import reverse
from loguru import logger
import sys
import os
from unittest.mock import patch

logger.remove()
logger.add(
    sys.stdout,
    format="[{level: <8}] {name}:{function}:{line} - {message}",
    level="INFO"
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
        self.assertEqual(response.content.decode(), "Hello World")
        logger.info("hello_world endpoint tested successfully")

    def test_health_check(self):
        """Verify that the health check endpoint returns 200 and correct message."""
        logger.info("Testing health check endpoint")
        response = self.client.get(reverse('health'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'status': 'ok', 'message': 'Health check successful'})
        logger.info("Health check endpoint tested successfully")

    def test_db_health_check_success(self):
        """Verify that the database health check endpoint returns 200 when database is accessible."""
        logger.info("Testing db_health_check endpoint with successful connection")
        response = self.client.get(reverse('db_health_check'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'status': 'ok', 'message': 'Database connection successful'})
        logger.info("db_health_check endpoint tested successfully")

    def test_db_health_check_failure(self):
        """Verify that the database health check endpoint returns 500 when database is inaccessible."""
        logger.info("Testing db_health_check endpoint with connection failure")
        with patch('django.db.connection.cursor') as mock_cursor:
            mock_cursor.side_effect = Exception("Simulated DB failure")
            response = self.client.get(reverse('db_health_check'))
            self.assertEqual(response.status_code, 500)
            self.assertEqual(response.json(), {'status': 'error', 'message': 'Database connection failed'})
        logger.info("db_health_check endpoint failure test completed")

    def tearDown(self):
        """Clean up after each test."""
        logger.info(f"Finishing test: {self._testMethodName}") 