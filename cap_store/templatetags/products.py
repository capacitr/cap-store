from django import template
from django.core.paginator import Paginator

register = template.Library()

from cap_store.models import Category, Product

@register.assignment_tag
def get_all_categories():
    return Category.objects.all() 

@register.assignment_tag
def get_all_products(page=None, num=None):
    products = Product.objects.filter(publish=True)
    if page:
        p = Paginator(products, num if num else 5)
        return p.page(page)
    return products

@register.assignment_tag
def get_products_by_tag(tag_slug=None):
    products = Product.objects.filter(tag__tag__in=[tag_slug], publish=True)
    return products
