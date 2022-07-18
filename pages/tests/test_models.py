from django.test import TestCase
from pages.models import Page


class PageManagerTest(TestCase):
    def test_published_pages(self):
        """Test that published page is working okay"""
        Page.objects.create(title="simple page", slug='simple_page', description='simple', status='pub')
        Page.objects.create(title="simple page2", slug='simple_page2', description='simple1', status='pub')
        Page.objects.create(title="simple page3", slug='simple_page3', description='simple3', status='dra')
        Page.objects.create(title="simple page4", slug='simple_page4', description='simple4', status='del')
        count_of_published_pages_by_filter = Page.objects.filter(status='pub').count()
        count_of_published_pages_by_manager = Page.objects.published().count()
        self.assertEqual(count_of_published_pages_by_filter, count_of_published_pages_by_manager)
