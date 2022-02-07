from django import template
from ..models import Category

register = template.Library()


@register.inclusion_tag("blog/navbar.html")
def navbar_cat():
    cat = {"categories": Category.objects.all().filter(display=True)}
    return cat


@register.inclusion_tag("accounts/active.html")
def active(request, content, url_name, fa):
    context = {
        "request": request,
        "content": content,
        "url_name": url_name,
        "url": url_name,
        "fa": fa,
    }
    return context
