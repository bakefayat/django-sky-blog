from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.generics import ListCreateAPIView
from .serializers import ArticleSerializer
from web.models import Blog
# Create your views here.


class ArticleListApiView(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = ArticleSerializer


class SimpleView(TemplateView):
    template_name = "registration/password_reset_done.html"
