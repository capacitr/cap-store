from django.conf.urls.defaults import patterns, include, url

import views

urlpatterns = patterns('',
    url(r'^p/(?P<page_number>[\d]+)/$', views.paginate_product, name='paginate_product'),
    url(r'^t/(?P<tag_slug>[\w-]+)/$', views.get_product_by_tag, name='store_product_by_tag'),
    url(r'^(?P<product_slug>[\w-]+)/$', views.get_product, name='store_product'),
    url(r'^category/(?P<category_name>[\w-]+)/$', views.products_by_category, name='product_by_category'),
    url(r'^recipe/(?P<recipe_id>\d+)/$', views.recipe, name='recipe'),
)
