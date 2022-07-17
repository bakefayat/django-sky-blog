from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from modules.models import Module


class AdminSiteTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username='admin@bakefayat.com',
            password="pass123"
        )
        self.client.force_login(self.admin_user)

        self.module = Module.objects.create(title='simple module', body='its very simple module',
                                                  position='top', order='1', display='True')

    def test_modules_listed(self):
        """test that modules listed on admin panel"""
        url = reverse('admin:modules_module_changelist')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, self.module.title)
        self.assertContains(res, self.module.order)
        self.assertContains(res, self.module.position)
        self.assertContains(res, self.module.display)

    def test_detail_module(self):
        """test that module details displayed correctly """
        url = reverse('admin:modules_module_change', args=[self.module.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, self.module.body)

    def test_create_module(self):
        """Test that create module page is ok"""
        url = reverse('admin:modules_module_add')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
