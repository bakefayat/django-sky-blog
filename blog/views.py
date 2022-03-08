from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.shortcuts import get_object_or_404

from .forms import CommentForm
from .mixins import CommentFormValidMixin
from .models import Blog, Category
from core.mixins import SearchActionMixin
from accounts.models import User


class ArticleListView(ListView):
    queryset = Blog.objects.published().select_related("author")
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


class ArticleDetailView(CreateView, CommentFormValidMixin, DetailView):
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        slug = self.kwargs.get("slug")
        # get id of the post -> required for post field on Comment model.
        post = get_object_or_404(Blog.objects.published(), slug=slug).id
        kwargs["post"] = post
        return kwargs

    def get_object(self):
        slug = self.kwargs.get("slug")
        return get_object_or_404(Blog.objects.published(), slug=slug)

    template_name = "blog/article_detail.html"
    form_class = CommentForm


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


# show success message
class CommentDetailView(TemplateView):

    template_name = "blog/comment_submit.html"
    model = Blog
