from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating new user with email successful"""
        email = 'padmaraju.pinnam@gmail.com'
        username = 'nani'
        password = '6gvRdrK'
        user = get_user_model().objects.create_user(
            username=username,
            email=email,
            password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_invalid_email(self):
        """Test new users email validation"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None,
                password='123', username='test')

    def test_create_super_user(self):
        """Test creating new super user"""
        super_user = get_user_model().objects.create_superuser(
            email='test1@gmail.com',
            password='test',
            username='test'
        )
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
