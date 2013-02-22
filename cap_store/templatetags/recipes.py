from django import template

register = template.Library()

from cap_store.models import Recipe

@register.assignment_tag
def get_all_recipes():
    return Recipe.objects.all() 



