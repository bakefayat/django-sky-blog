from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import ArticleSerializer
from .permissions import IsSuperUserOrReadOnly, IsAuthorOrReadOnly
from web.models import Blog
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
