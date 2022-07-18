from django.test import TestCase
from core.models import SiteProfile
from django.contrib.sites.models import Site


class SiteProfileTest(TestCase):
    def test_self_str(self):
        """test that __str__ function is working fine"""
        simple_site = SiteProfile.objects.create(title='Test Category', description="this is simple")
        self.assertEqual(str(simple_site), 'Test Category')
