from django import template

register = template.Library()

from cap_store.models import Category, Product

@register.assignment_tag
def get_all_categories():
    return Category.objects.all() 


@register.assignment_tag
def get_all_products():
    return Product.objects.filter(publish=True)
