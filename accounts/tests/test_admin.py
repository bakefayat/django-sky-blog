from django.contrib.auth import get_user_model
from django.test import TestCase
from accounts.admin import UserAdminPanel
from accounts.models import User


class TestAdminSite(TestCase):

    def test_user_full_name(self):
        """test that user full name showed correctly"""
        get_user_model().objects.create_user(
                    username='ehsan', password='123', first_name='ehsan', last_name='ronaldo', email='sam@sample.com')
        get_user_model().objects.create_user(
                    username='ab', password='123', first_name='abraham', email='abraham@gmail.com')
        user_obj1 = User.objects.get(id=1)
        admin_function_result = UserAdminPanel.user_full_name(self, obj=user_obj1)
        self.assertEqual(admin_function_result, 'ehsan ronaldo')
        user_obj2 = User.objects.get(id=2)
        admin_function_result = UserAdminPanel.user_full_name(self, obj=user_obj2)
        self.assertEqual(admin_function_result, 'abraham')
