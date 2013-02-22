from django.db import models

from thumbnail_works.fields import EnhancedImageField
from django.contrib.auth.models import User

from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^thumbnail_works\.fields\.EnhancedImageField"])



SCORE_CHOICES = zip( range(1,6), range(1,6) )

CONTACT_CHOICES = (
    ('phone', 'phone'),
    ('email', 'email'),
    )

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
    

class Product(models.Model):

    brand = models.CharField(max_length=255)

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

    ingredients = models.TextField()
    nutritionals = models.TextField()
    nutritional_image = models.ImageField(upload_to='uploads', blank=True)
    @property
    def rating_list(self):
        return range(1,6)

    publish = models.BooleanField(default=False)

    @models.permalink
    def get_absolute_url(self):
        return ('get_product', None, {'slug' : self.slug} )

class Address(models.Model):

    name = models.CharField(max_length=255)
    business = models.CharField(max_length=255)

    phone = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)

    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
#    latitude = models.CharField(max_length=255)
#    longitude = models.CharField(max_length=255)

    def __unicode__(self):
        return "%s - %s" % (self.name, self.address)

    class Meta:
        verbose_name_plural = "Addresses"
        unique_together = ('address', 'zip_code',)


class Card(models.Model):
    card_number = models.CharField(max_length=255, unique=True)
    exp_date = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    security_code = models.CharField(max_length=255)

    def __unicode__(self):
        return "%s - %s" % (self.card_number[-4:], self.exp_date)


class Customer(models.Model):
    name = models.CharField(max_length=255)
    business_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255)

    phone = models.CharField(max_length=255)

    shipping_address = models.ManyToManyField(Address, related_name="shipping_address")
    card_info = models.ManyToManyField(Card)

    referral = models.CharField(max_length=255)

    preferred_method_of_contact = models.CharField(max_length=255, choices=CONTACT_CHOICES)

    def __unicode__(self):
        return "%s - %s - %s" % (self.name, self.email, self.phone)

class Order(models.Model):
    customer = models.ForeignKey(Customer, null=True)
    salesperson = models.ForeignKey(User, related_name="salesperson", null=True, blank=True)

    garment_colors = models.CharField(max_length=255)
    total_quantity = models.CharField(max_length=255)
    type_of_garments = models.CharField(max_length=255)
    sizes = models.CharField(max_length=255)

    pick_up_date = models.DateTimeField(blank=True, null=True)
    ship_date = models.DateTimeField(blank=True, null=True)

    description = models.TextField()

    def __unicode__(self):
        return "%s - %s" % (self.customer, self.salesperson,)

class Garment(models.Model):
    order = models.ForeignKey(Order)
    name = models.CharField(max_length=255)

ORDER_STATUSES = (
    ('draft', 'Draft'),
    ('ready-for-print', 'Ready for Print'),
    ('waiting-for-approval', 'Waiting for Approval'),
    ('completed', 'Completed')
    )

PAYMENT_STATUSES = (
    ('paid','Paid'),
    ('unpaid', 'Unpaid'),
    ('po', 'PO'),
    ('partial-payment', 'partial-payment')
    )

class Invoice(models.Model):

    salesperson = models.ForeignKey(User, related_name="invoices_salesperson", null=True)

    order = models.ForeignKey(Order, null=True)
    invoice_number = models.CharField(max_length=255)

    customer = models.ForeignKey(Customer, null=True)
    
    po_number = models.CharField(max_length=255)
    turnaround = models.CharField(max_length=255)

    ship_date = models.CharField(max_length=255)
    needed_by = models.CharField(max_length=255)

    shipping_method = models.CharField(max_length=255)
    pay_terms = models.CharField(max_length=255)

    note = models.TextField()

    subtotal = models.FloatField(default=0)
    discount = models.FloatField(default=0)
    tax_discount = models.FloatField(default=0)
    tax = models.FloatField(default=0)
    shipping_handling = models.FloatField(default=0)
    total = models.FloatField(default=0)

    order_status = models.CharField(max_length=255, choices=ORDER_STATUSES)
    payment_status = models.CharField(max_length=255, choices=PAYMENT_STATUSES)

    def __unicode__(self):
        return "%s - %s" % (self.invoice_number, self.customer)

class LineItem(models.Model):

    invoice = models.ForeignKey(Invoice)
    
    item_number = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    sizes = models.CharField(max_length=255)

    art_placement = models.CharField(max_length=255)
    art_dimension = models.CharField(max_length=255)
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    total = models.FloatField(default=0)


class Coupon(models.Model):
    image = EnhancedImageField(
        upload_to = 'uploads',
        process_source = dict(
            size='897x449', sharpen=True, upscale=True, format='JPEG'),
        thumbnails = {
            'avatar': dict(size='697x349'),
        }

    )
class Recipe(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()

    image = EnhancedImageField(
        upload_to = 'uploads',
        process_source = dict(
            size='120x90', sharpen=True, upscale=True, format='JPEG'),
        thumbnails = {
            'avatar': dict(size='120x90'),
        }
    )

    ingredients = models.TextField(blank=True)
    directions = models.TextField(blank=True)

    category = models.ForeignKey('store.Category', null=True, on_delete=models.SET_NULL)

    publish = models.BooleanField(default=False)

    @models.permalink
    def get_absolute_url(self):
        return ('recipe', (), {
            'recipe_id' : self.pk 
        })

    class Meta:
        ordering = ['category__name']

