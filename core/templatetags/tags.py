from django import template
from blog.models import Category
from pages.models import Page
from modules.models import Module
from core.models import SiteProfile
from django.contrib.sites.models import Site
register = template.Library()


# widgets
@register.inclusion_tag("core/widget.html")
def widget(position):
    cat = {"modules": Module.objects.filter(display=True, position=position)}
    return cat


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


@register.simple_tag()
def site_profile(item):
    current_site = Site.objects.get_current()
    profile = SiteProfile.objects.get(site=current_site)
    return profile.__getattribute__(item)
