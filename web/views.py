from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from .models import Blog, Category
from core.mixins import SearchActionMixin
from account.models import User


class ArticleListView(ListView):
    queryset = Blog.objects.published()
    template_name = "blog/article_list.html"
    paginate_by = 2
    

class SearchListView(SearchActionMixin, ListView):
    model = Blog
    template_name = "blog/search_list.html"
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context


class ArticleDetailView(DetailView):
    def get_object(self):
        slug = self.kwargs.get("slug")
        return get_object_or_404(Blog.objects.published(), slug=slug)

    template_name = "blog/article_detail.html"


class CategoryListView(ListView):
    def get_queryset(self):
        global category
        slug = self.kwargs.get("slug")
        category = get_object_or_404(Category.objects.shown(), slug=slug)
        return category.articles.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = category
        return context

    template_name = "blog/category_list.html"
    paginate_by = 2


class UserListView(ListView):
    def get_queryset(self):
        global user
        username = self.kwargs.get("slug")
        user = get_object_or_404(User, username=username)
        return user.articles.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = user
        return context

    template_name = "blog/user_list.html"
    paginate_by = 2
