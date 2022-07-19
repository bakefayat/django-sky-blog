from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta


class TestModels(TestCase):
    def test_user_is_special(self):
        """
        test that user_is_special is okay
        user is_special is true if special_user field time further away from than current datetime
        """

        # 2 days later assigned to special_user datetime field.
        user = get_user_model().objects.create(
            username='ehsan',
            special_user=timezone.now() + timedelta(days=2)
        )

        # datetime assigned to special_user is earlier than happening of .
        user2 = get_user_model().objects.create(
            username='james',
            email='james@gmail.com',
            special_user=timezone.now()
        )
        self.assertTrue(user.is_specialuser())
        self.assertFalse(user2.is_specialuser())
