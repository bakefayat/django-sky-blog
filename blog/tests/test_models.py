from django.test import TestCase
from datetime import datetime
import pytz
from config.settings import TIME_ZONE
from blog.models import Category, Blog, Comment
from django.urls import reverse


class TestCategory(TestCase):
    def setUp(self):
        self.category1 = Category.objects.create(title='first category', slug='first_category')
        self.category2 = Category.objects.create(slug='second_category', display=False)

    def test_shown_category_manager(self):
        """Test that ShownCategory manager worked properly"""
        count_of_shown_categories = Category.objects.shown().count()
        self.assertEqual(count_of_shown_categories, 1)
        self.assertEqual(self.category1.slug, 'first_category')

    def test_str_represent(self):
        """Test str of category model"""
        self.assertEqual(str(self.category1), 'first category')

    def test_get_absolute_url(self):
        """test get_absolute_url method of category"""
        url = reverse('accounts:cat_detail', args=[self.category1.slug])
        self.assertEqual(url, self.category1.get_absolute_url())


class TestComment(TestCase):
    def setUp(self):
        self.post = Blog.objects.create(title='post one',)
        self.comment1 = Comment.objects.create(body='comment one', post=self.post, display=True)
        self.comment2 = Comment.objects.create(body='comment two', post=self.post, display=True)
        self.comment3 = Comment.objects.create(body='comment three', post=self.post, display=False)

    def test_published_comment(self):
        """Test PublishedComment manager"""
        count_of_published_comments = Comment.objects.published().count()
        self.assertEqual(count_of_published_comments, 2)

    def test_str_represent(self):
        """Test str of comment model"""
        self.assertEqual(str(self.comment1), self.comment1.body)

    def test_get_absolute_url(self):
        """Test get_absolute_url method of Comment model"""
        url = reverse("blog:comment", args=[self.comment1.post.slug])
        self.assertEqual(self.comment1.get_absolute_url(), url)

    def test_jpublished(self):
        """Test jalali created time of comment"""
        time_zone = pytz.timezone(TIME_ZONE)
        self.comment1.created = datetime(year=2022, month=11, day=28, hour=23, minute=55, second=12, tzinfo=time_zone)
        self.assertEqual(self.comment1.jpublished(), '7 آذر 1401, ساعت 23:55')
