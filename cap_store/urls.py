from django.conf.urls.defaults import patterns, url

import views

urlpatterns = patterns('',
    url(r'^(?P<product_slug>[\w-]+)/$', views.get_product, name='get_product'),
    url(r'^recipe/(?P<recipe_id>\d+)/$', views.get_recipe, name='get_recipe'),
)
