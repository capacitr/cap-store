from django import template

register = template.Library()

from store.models import Category 

@register.assignment_tag
def get_all_categories():
    return Category.objects.all() 


