from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from blog.models import Blog
from extensions.utils import(
    check_author_staff_superuser, 
    check_staff_superuser,
    check_owner_staff_superuser,
    )


class FieldsMixin:
    def dispatch(self, request, *args, **kwargs):
        self.fields = [
            "title",
            "slug",
            "status",
            "description",
            "image",
            "category",
            "is_special",
            "published",
        ]
        if check_staff_superuser(request):
            self.fields.append("author")
        return super().dispatch(request, *args, **kwargs)


class FormValidMixin:
    def form_valid(self, form):
        if check_staff_superuser(self.request):
            form.save()
        else:
            self.obj = form.save(commit=False)
            self.obj.author = self.request.user
            if not self.obj.status == "w":
                self.obj.status = "d"
        return super().form_valid(form)


class UpdateAccessMixin:
    def dispatch(self, request, pk, *args, **kwargs):
        article = get_object_or_404(Blog, pk=pk)
        check_owner_staff_superuser(request, article)
        return super().dispatch(request, *args, **kwargs)


class DraftEditMixin:
    def dispatch(self, request, pk, *args, **kwargs):
        article = get_object_or_404(Blog, pk=pk)
        if article.status == "p" and request.user.is_author:
            raise Http404("you can't edit published article.")
        else:
            return super().dispatch(request, pk, *args, **kwargs)


class DeleteArticleMixin:
    def dispatch(self, request, pk, *args, **kwargs):
        article = get_object_or_404(Blog, pk=pk)
        check_owner_staff_superuser(request, article)
        return super().dispatch(request, pk, *args, **kwargs)


class PreviewMixin:
    def dispatch(self, request, slug, *args, **kwargs):
        article = get_object_or_404(Blog, slug=slug)
        check_owner_staff_superuser(request, article)
        return super().dispatch(request, *args, **kwargs)


class AuthorsMixin:
    def dispatch(self, request, *args, **kwargs):
        if check_author_staff_superuser(request):
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect("accounts:profile")


class ArticleActionMixin:
    @property
    def success_message(self):
        return NotImplemented

    def form_valid(self, form):
        messages.info(self.request, self.success_message)
        return super().form_valid(form)
