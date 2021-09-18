from django.http import request
from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView, UpdateView
from web.models import Blog
from .mixins import FieldsMixin, FormValidMixin, UpdateAccessMixin
# Create your views here.

# @login_required
# def home(request):
#     return render(request, 'registration/admin.html')


class Home(LoginRequiredMixin, TemplateView):
    template_name = 'registration/admin.html'



class ArticleList(LoginRequiredMixin, ListView):
    template_name = 'registration/articleList.html'
    def get_queryset(self):
        if self.request.user.is_superuser:
            return(Blog.objects.all())
        else:
            return Blog.objects.filter(author=self.request.user)


class CreateArticle(LoginRequiredMixin, FormValidMixin, FieldsMixin, CreateView):
    model = Blog
    template_name = 'registration/articleCreate.html'


class UpdateArticle(LoginRequiredMixin, UpdateAccessMixin, FormValidMixin, FieldsMixin, UpdateView):
    model = Blog
    template_name = 'registration/articleCreate.html'
