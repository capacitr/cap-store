from django import template

register = template.Library()

from cap_store.models import Category 

@register.assignment_tag
def get_all_categories():
    return Category.objects.all() 


