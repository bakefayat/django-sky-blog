from django import template
from ..models import Category
register = template.Library()

@register.simple_tag()
def title():
    return 'ورزش 4'


@register.inclusion_tag('blog/navbar.html')
def navbar_cat():
    cat = {'categories': Category.objects.all().filter(display=True)}
    return cat