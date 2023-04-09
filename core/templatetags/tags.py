from django import template
from django.core.exceptions import ObjectDoesNotExist
from blog.models import Category, Blog
from extensions.utils import to_jalali
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


# list of categories
@register.inclusion_tag("core/navbar.html")
def navbar_cat():
    cat = {"categories": Category.objects.all().filter(display=True)}
    return cat


# list of top views
@register.inclusion_tag("core/top_posts.html")
def top_posts():
    top = {"popular_posts": Blog.objects.order_by('-hit_count_generic__hits')[:3]}
    return top


# list of pages
@register.inclusion_tag("core/nav-items.html")
def nav_items():
    navbar_items = {"items": Page.objects.published()}
    return navbar_items


# show font-icons and details in accounts app.
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


# show information of website.
@register.simple_tag()
def site_profile(item):
    current_site = Site.objects.get_current()
    try:
        profile = SiteProfile.objects.get(site=current_site)
        return profile.__getattribute__(item)
    except ObjectDoesNotExist:
        return 'جنگو آسمان'

# convert date to jalali
@register.simple_tag()
def jdate(date):
    return to_jalali(date)
