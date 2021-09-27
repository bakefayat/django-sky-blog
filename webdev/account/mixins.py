from django.http import Http404
from django.shortcuts import get_object_or_404
from web.models import Blog
class FieldsMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser or request.user.is_staff:
            self.fields = [
                'title' , 'slug' , 'author' , 'description' , 'image' , 'published' , 'status' , 'category'
            ]
        elif request.user.is_author:
            self.fields = [
                'title' , 'slug' , 'description' , 'image' , 'category', 'published'
            ]
        else:
            raise Http404('no permision')
        return super().dispatch(request, *args, **kwargs)


class FormValidMixin():
    def form_valid(self, form):
        if self.request.user.is_superuser or self.request.user.is_staff:
            form.save()
        else:
            self.obj = form.save(commit=False)
            self.obj.author = self.request.user
            self.obj.status = 'w'
        return super().form_valid(form)


class UpdateAccessMixin:
    def dispatch(self, request, pk, *args, **kwargs):
        article = get_object_or_404(Blog, pk=pk)
        if request.user.is_superuser\
        or request.user.is_staff\
        or request.user == article.author:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("you can't access this.")


class DraftEditMixin:
    def dispatch(self, request, pk, *args, **kwargs):
        article = get_object_or_404(Blog, pk=pk)
        if article.status == 'p' and request.user.is_author:
            raise Http404("you can't edit published article.")
        else:
            return super().dispatch(request, pk, *args, **kwargs)


class DeleteArticleMixin:
    def dispatch(self, request, pk, *args, **kwargs):
        article = get_object_or_404(Blog, pk=pk)
        if request.user.is_superuser\
        or request.user.is_staff\
        or request.user.is_author and article.author == request.user:
            return super().dispatch(request, pk, *args, **kwargs)
        else:
            raise Http404('you have no permision to delete this article.')


class PreviewMixin:
    def dispatch(self, request, slug, *args, **kwargs):
        article = get_object_or_404(Blog, slug=slug)
        if request.user.is_superuser\
        or request.user.is_staff\
        or request.user == article.author:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("you can't access this.")

