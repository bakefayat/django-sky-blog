from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
from django.shortcuts import get_list_or_404, render, get_object_or_404
from .models import Blog, Category
from django.contrib.auth.models import User


class ArticleList(ListView):
    queryset = Blog.objects.published()
    template_name = 'blog/articleList.html'
    paginate_by = 2


class ArticleDetail(DetailView):
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Blog.objects.published(), slug=slug)
    template_name = 'blog/articleDetail.html'


class CategoryList(ListView):
    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.shown(), slug=slug)
        return category.articles.published()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context


    template_name = 'blog/categoryList.html'
    paginate_by = 2



class UserList(ListView):
    def get_queryset(self):
        global user
        username = self.kwargs.get('slug')
        user = get_object_or_404(User, username=username)
        return user.articles.all()
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = user
        return context

    
    template_name = 'blog/userList.html'
    paginate_by = 2
