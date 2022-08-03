from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token


class TestViews(TestCase):
    def test_revoke_token(self):
        """Test RevokeTokenApiView"""
        user = get_user_model().objects.create_superuser(username='james', email='james@james.com')
        token = Token.objects.create(user=user)
        client = APIClient()
        # set token to header.
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        url = reverse('api:token')
        res = client.delete(url)
        self.assertEqual(res.status_code, 204)
