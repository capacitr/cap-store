from django import template

register = template.Library()

from cap_store.models import Recipe

@register.assignment_tag
def get_all_recipes(category=None):
    if category:
        return Recipe.objects.filter(publish=True, category__name=category)
    return Recipe.objects.filter(publish=True) 

