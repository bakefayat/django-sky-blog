from django.http import request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from web.models import Blog

# Create your views here.

# @login_required
# def home(request):
#     return render(request, 'registration/admin.html')


class Home(LoginRequiredMixin, TemplateView):
    template_name = 'registration/admin.html'



class ArticleList(LoginRequiredMixin, ListView):
    template_name = 'registration/articleList.html'
    queryset = Blog.objects.all()


class home_blog(LoginRequiredMixin, ListView):
    queryset = Blog.objects.published()
    paginate_by = 2
    template_name = 'blog/articleList.html'
