from django import template
from blog.models import Category
from pages.models import Page
register = template.Library()


@register.inclusion_tag("core/navbar.html")
def navbar_cat():
    cat = {"categories": Category.objects.all().filter(display=True)}
    return cat


@register.inclusion_tag("core/nav-items.html")
def nav_items():
    navbar_items = {"items": Page.objects.published()}
    return navbar_items


@register.inclusion_tag("core/active.html")
def active(request, content, url_name, fa):
    context = {
        "request": request,
        "content": content,
        "url_name": url_name,
        "url": url_name,
        "fa": fa,
    }
    return context
