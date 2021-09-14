from django.http import request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic import TemplateView, CreateView
from web.models import Blog

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


class CreateArticle(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ['title' , 'slug' , 'author' , 'description' , 'image' , 'published' , 'status' , 'category']
    template_name = 'registration/articleCreate.html'

    def form_valid(self, form):
        if not(self.request.user.is_superuser):
            author = self.request.user
            status = 'd'
            form.instance.author = author
            form.instance.status = status
        return super().form_valid(form)