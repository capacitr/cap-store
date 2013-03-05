from django.contrib import admin

import models

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'category_slug' :  ('name',)}
    list_display = ['name', 'image']

class CouponAdmin(admin.ModelAdmin):
    list_display = ['image']

class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'image', 'category', 'publish']
    list_editable = ['category', 'publish']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'category_one', 'category_two', 'publish']

admin.site.register(models.Recipe, RecipeAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Product, ProductAdmin)

