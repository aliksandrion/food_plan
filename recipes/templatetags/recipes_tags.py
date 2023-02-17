from django import template
from recipes.models import Category
from django.core.cache import cache

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('recipes/list_categories.html')
def show_categories():
    categories = cache.get('categories')
    if not categories:
        categories = Category.objects.all()
        cache.set('categories', categories, 30)
    return {"categories": categories}
