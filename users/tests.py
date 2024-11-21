from django.test import TestCase
from .models import CustomUser

class CustomUserModelTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='password123',
            role='student',
            study_level='L2',
            subscription_valid=True,
            first_name='Test',
            last_name='User',
            mobile_number='1234567890'
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.role, 'student')
        self.assertTrue(self.user.subscription_valid)
        self.assertEqual(self.user.study_level, 'L2')

    def test_user_email(self):
        self.assertEqual(self.user.email, 'testuser@example.com')
