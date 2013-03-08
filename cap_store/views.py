from django.shortcuts import render, get_object_or_404
from cap_store.models import Product, Recipe

def get_product(request, product_slug=None):
    p = get_object_or_404(Product, slug=product_slug)
    return render(request, 'product.html', {'product': p})

def get_recipe(req, recipe_id=None):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(req, 'recipe.html', {'recipe' : recipe})
