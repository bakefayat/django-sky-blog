from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
from pages.models import Page

class AdminSiteTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username='admin@bakefayat.com',
            password="pass123"
        )
        self.client.force_login(self.admin_user)

        self.page = Page.objects.create(title='simple page', description='its very simple page', slug='simple_page')

    def test_modules_listed(self):
        """test that pages listed on admin panel"""
        url = reverse('admin:pages_page_changelist')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, self.page.title)
        self.assertContains(res, self.page.description)

    def test_detail_module(self):
        """test that page details displayed correctly """
        url = reverse('admin:pages_page_change', args=[self.page.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, self.page.slug)

    def test_create_module(self):
        """Test that create page is ok"""
        url = reverse('admin:pages_page_add')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
