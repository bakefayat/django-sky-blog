from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from .models import Page


class PageDetailView(DetailView):
    template_name = "pages/detail.html"
    model = Page

    def get_object(self):
        slug = self.kwargs.get("slug")
        return get_object_or_404(Page.objects.published(), slug=slug)

