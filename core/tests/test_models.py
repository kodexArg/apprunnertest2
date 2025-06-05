from django.test import TestCase
from django.contrib.auth import get_user_model
from loguru import logger
import sys

logger.remove()
logger.add(
    sys.stdout,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    level="INFO",
    colorize=True
)

class ModelTests(TestCase):
    """Test suite for core application models.
    
    This suite verifies the functionality of the core application's models,
    including user model and any custom models.
    """

    def setUp(self):
        """Set up test environment for each test."""
        super().setUp()
        logger.info(f"Starting test: {self._testMethodName}")

    def test_create_user(self):
        """Verify that a user can be created."""
        logger.info("Testing user creation")
        User = get_user_model()
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('testpass123'))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        logger.info("User creation test successful")

    def test_create_superuser(self):
        """Verify that a superuser can be created."""
        logger.info("Testing superuser creation")
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='adminpass123'
        )
        self.assertEqual(admin_user.username, 'admin')
        self.assertEqual(admin_user.email, 'admin@example.com')
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        logger.info("Superuser creation test successful")

    def test_user_str_representation(self):
        """Verify the string representation of a user."""
        logger.info("Testing user string representation")
        User = get_user_model()
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.assertEqual(str(user), 'testuser')
        logger.info("User string representation test successful")

    def tearDown(self):
        """Clean up after each test."""
        super().tearDown()
        logger.info(f"Finishing test: {self._testMethodName}") 