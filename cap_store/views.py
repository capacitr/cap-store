from django.shortcuts import render, get_object_or_404
from cap_store.models import Product, Recipe

def get_product(request, product_slug=None):
    p = get_object_or_404(Product, slug=product_slug)
    return render(request, 'product.html', {'product': p})

def products_by_category(req, category_name=None):
    products = Product.objects.filter(category_one__category_slug=category_name).order_by('category_two__name')
    return render(req, 'products_by_category.html', {"products" : products })

def get_recipe(req, recipe_id=None):
    recipe= get_object_or_404(Recipe, pk=recipe_id)

    c = {
        'recipe' : recipe,
        }

    return render(req, 'recipe.html', c)
