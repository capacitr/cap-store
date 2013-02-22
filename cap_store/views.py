# Create your views here.
from django.shortcuts import render, render_to_response, get_object_or_404
from django.views.generic.simple import direct_to_template
from django.core.paginator import Paginator

from django.conf import settings

from store.models import Product, Category, Recipe

def paginate_product(req, page_number=None):
    p = Paginator(models.Product.objects.filter(site__pk__exact = settings.SITE_ID, publish=True), 5)
    page = p.page(page_number)
    products = page.object_list

    return direct_to_template(req, 'products_html.html', extra_context={'products': products})

def get_product_by_tag(req, tag_slug=None):

    products = None
    try:
        tag = get_object_or_404(models.Tag, slug=tag_slug)
        products = models.Product.objects.filter(site__pk__exact = settings.SITE_ID, tags__pk__in=[tag.pk])
    except models.Product.DoesNotExist:
        pass

    return direct_to_template(req, 'products.html', extra_context={'products': products})


def get_product(req, product_slug=None):
    p = get_object_or_404(models.Product, slug=product_slug)
    return direct_to_template(req, 'product.html', extra_context={'product': p})


def products_by_category(req, category_name=None):
    products = Product.objects.filter(category_one__category_slug=category_name).order_by('category_two__name')
    return render(req, 'products_by_category.html', {"products" : products })

def recipe(req, recipe_id=None):

    try:
        recipe_obj = Recipe.objects.get(pk=recipe_id)
        recipes = Recipe.objects.filter(category=recipe_obj.category)
    except Recipe.DoesNotExist:
        pass

    c = {
        'recipe' : recipe_obj,
        'recipes' : recipes
        }

    return render(req, 'recipe.html', c)

