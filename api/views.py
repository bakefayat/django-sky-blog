from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import ArticleSerializer, UserSerializer
from .permissions import IsSuperUserOrReadOnly, IsAuthorOrReadOnly, IsSuperUser
from web.models import Blog
from account.models import User
# Create your views here.


class ArticleListApiView(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsSuperUserOrReadOnly,)


class ArticleDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = "slug"
    permission_classes = (IsAuthorOrReadOnly,)


class UserListApiView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permision_classes = (IsSuperUserOrReadOnly,)


class UserDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permision_classes = (IsSuperUser,)