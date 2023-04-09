from django.test import TestCase

from accounts.models import User
from accounts.forms import ProfileForm

class ProfileFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='password')
    
    def test_init_method(self):
        form = ProfileForm(user=self.user)
        self.assertTrue(form.fields["username"].disabled)
        self.assertTrue(form.fields["is_author"].disabled)
        self.assertTrue(form.fields["special_user"].disabled)
