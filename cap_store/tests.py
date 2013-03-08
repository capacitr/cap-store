"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.test.client import Client
from django.test import TestCase
from models import Recipe
from models import Product


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class AdminTest(TestCase):
    def test_import(self):
        pass

class ViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_recipe_view(self):
        recipe = Recipe()
        recipe.name = "test"
        recipe.description = "test"
        recipe.publish=True
        recipe.save()
        self.client.get(recipe.get_absolute_url())

    def test_product_view(self):
        product = Product()
        product.name = "test"
        product.slug = "test"
        product.description = "test"
        product.publish = True
        product.save()

        self.client.get(product.get_absolute_url())

class TemplateTagTest(TestCase):
    pass
