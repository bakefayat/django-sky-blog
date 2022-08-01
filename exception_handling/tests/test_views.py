from django.test import TestCase, Client


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_handler_404(self):
        self.client = Client()
        res = self.client.get('random_url_that_doesnt_exists')
        self.assertTemplateUsed(res, 'exception_handling/404.html')
