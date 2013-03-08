from django.db import models

from thumbnail_works.fields import EnhancedImageField
from django.utils import simplejson

from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^thumbnail_works\.fields\.EnhancedImageField"])


SCORE_CHOICES = zip( range(1,6), range(1,6) )

class Category(models.Model):
    name = models.CharField(max_length=255)
    category_slug = models.SlugField(max_length=255, unique=True)

    image = EnhancedImageField(
        upload_to = 'uploads',
        process_source = dict(
            size='280x108', sharpen=True, upscale=True, format='JPEG'),
        thumbnails = {
            'avatar': dict(size='280x108'),
        },
        blank=True
    )

    description = models.TextField(default="", blank=True)

    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        verbose_name_plural = 'categories'

class Order(models.Model):
    pass

class Product(models.Model):
    brand = models.CharField(max_length=255, blank=True)

    name = models.CharField(max_length=255)

    image = EnhancedImageField(
        upload_to = 'uploads',
        process_source = dict(
            size='1000x1000', sharpen=True, upscale=False, format='JPEG'),
        thumbnails = {
            'avatar': dict(size='697x349'),
            'product1': dict(size='405x238'),
        }
        )

    category_one = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, related_name='parent_category', blank=True)
    category_two = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, related_name='child_category', blank=True)

    description = models.TextField(blank=True)

    slug = models.SlugField(max_length=255)

    price = models.FloatField(default=0)
    old_price = models.FloatField(default=0)

    rating = models.IntegerField(choices=SCORE_CHOICES, default=0)

    attributes = models.TextField(blank=True)

    @property
    def attributes_dict(self):
        return simplejson.loads(self.attributes)

    @property
    def rating_list(self):
        return range(1,6)

    publish = models.BooleanField(default=False)

    @models.permalink
    def get_absolute_url(self):
        return ('get_product', (), {'product_slug' : self.slug} )

class Image(models.Model):
    product = models.ForeignKey('Product')
    image = models.ImageField(upload_to="images")
