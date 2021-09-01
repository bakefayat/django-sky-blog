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
        user = get_object_or_404(User.objects.all(), username=username)
        return user.articles.all()
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = user
        return context

    
    template_name = 'blog/userList.html'
    paginate_by = 2


def blog(request, page=1):
    article_list = Blog.objects.all().filter(status='p')
    pagination = Paginator(article_list, 2)
    articles = pagination.get_page(page)
    context = {'articles': articles}
    return render(request, 'blog/index.html', context)


def single(request, slug):
    single= get_object_or_404(Blog, slug=slug, status='p')
    context = {'article': single}
    return render(request, 'blog/single.html', context)


# def category(request, slug, page=1):
#     category = get_object_or_404(Category, slug=slug)
#     articles_list = category.articles.published()
#     pagination = Paginator(articles_list, 1)
#     articles = pagination.get_page(page)
#     context = {
#         'articles': articles,
#         'category': category,
#         }
#     return render(request, 'blog/category.html', context)
