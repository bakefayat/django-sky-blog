from django.http import request
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView
from web.models import Blog
from .mixins import DeleteArticleMixin, FieldsMixin, FormValidMixin, UpdateAccessMixin, DraftEditMixin, DeleteArticleMixin, PreviewMixin

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


class UpdateArticle(DraftEditMixin, LoginRequiredMixin, UpdateAccessMixin, FormValidMixin, FieldsMixin, UpdateView):
    model = Blog
    template_name = 'registration/articleUpdate.html'


class DeleteArticle(DeleteArticleMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('account:list')
    template_name = 'registration/articleDelete.html'


class PreviewArticle(PreviewMixin, DetailView):
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Blog, slug=slug)
    template_name = 'blog/articleDetail.html'
