from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model

from api.permissions import IsSuperUser, IsSuperUserOrReadOnly, IsAuthorOrReadOnly

from blog.models import Blog


class TestPermissionsSuperUser(TestCase):
    def setUp(self):
        superuser = get_user_model().objects.create_superuser(username='james', email='james@james.com')
        factory = RequestFactory()
        self.request = factory.post('/')
        self.request.user = superuser

    def test_is_superuser(self):
        """Test IsSuperUser permission returned True as superuser"""
        permission_check = IsSuperUser()
        permission = permission_check.has_permission(self.request, None)
        self.assertTrue(permission)

    def test_is_superuser_or_read_only(self):
        """Test IsSuperUserOrReadOnly permission returned True as Safe Methods"""
        permission_check = IsSuperUserOrReadOnly()
        permission = permission_check.has_permission(self.request, None)
        self.assertTrue(permission)

    def test_is_author_or_read_only(self):
        """Test IsAuthorOrReadOnly permission returned True"""
        permission_check = IsAuthorOrReadOnly()
        author_user = get_user_model().objects.create(username='abraham', email='abraham@james.com')
        article = Blog.objects.create(author=author_user)
        permission = permission_check.has_object_permission(self.request, view=None, obj=article)
        self.assertTrue(permission)


class TestPermissionsNormalUser(TestCase):
    def setUp(self):
        normal_user = get_user_model().objects.create(username='abraham')
        factory = RequestFactory()
        self.request = factory.delete('/')
        self.request.user = normal_user
        self.safe_request = factory.get('/')
        self.safe_request.user = normal_user

    def test_is_superuser(self):
        """Test IsSuperUser permission returned False as normal user"""
        permission_check = IsSuperUser()
        permission = permission_check.has_permission(self.request, None)
        self.assertFalse(permission)

    def test_is_superuser_or_readonly(self):
        """Test IsSuperUserOrReadOnly permission returned True as Safe Methods"""
        permission_check = IsSuperUserOrReadOnly()
        permission = permission_check.has_permission(self.request, None)
        safe_permission = permission_check.has_permission(self.safe_request, None)

        self.assertFalse(permission)
        self.assertTrue(safe_permission)

    def test_is_author_or_read_only_by_non_author(self):
        """Test IsAuthorOrReadOnly permission by non author user"""
        author_user = get_user_model().objects.create(username='james', email='james@james.com')
        article = Blog.objects.create(author=author_user)
        permission_check = IsAuthorOrReadOnly()
        permission = permission_check.has_object_permission(self.request, view=None, obj=article)
        self.assertFalse(permission)

    def test_is_author_or_read_only_by_author(self):
        """Test IsAuthorOrReadOnly permission by author user"""
        article = Blog.objects.create(author=self.request.user)
        permission_check = IsAuthorOrReadOnly()
        permission = permission_check.has_object_permission(self.request, view=None, obj=article)
        self.assertTrue(permission)
