from django import template

register = template.Library()

from store.models import Recipe

@register.assignment_tag
def get_all_recipes():
    return Recipe.objects.all() 



