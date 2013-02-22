# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Card', fields ['card_number']
        db.create_unique('store_card', ['card_number'])


    def backwards(self, orm):
        # Removing unique constraint on 'Card', fields ['card_number']
        db.delete_unique('store_card', ['card_number'])


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'store.address': {
            'Meta': {'unique_together': "(('address', 'zip_code'),)", 'object_name': 'Address'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'business': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'site': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'store_address_site_related'", 'symmetrical': 'False', 'to': "orm['sites.Site']"}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'store_address_updated_by_related'", 'to': "orm['auth.User']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'store_address_user_related'", 'to': "orm['auth.User']"}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'store.card': {
            'Meta': {'object_name': 'Card'},
            'card_number': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'exp_date': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'security_code': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'site': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'store_card_site_related'", 'symmetrical': 'False', 'to': "orm['sites.Site']"}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'store_card_updated_by_related'", 'to': "orm['auth.User']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'store_card_user_related'", 'to': "orm['auth.User']"}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'store.category': {
            'Meta': {'object_name': 'Category'},
            'category_slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('thumbnail_works.fields.EnhancedImageField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'site': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'store_category_site_related'", 'symmetrical': 'False', 'to': "orm['sites.Site']"}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'store_category_updated_by_related'", 'to': "orm['auth.User']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'store_category_user_related'", 'to': "orm['auth.User']"})
        },
        'store.coupon': {
            'Meta': {'object_name': 'Coupon'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('thumbnail_works.fields.EnhancedImageField', [], {'max_length': '100'}),
            'site': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'store_coupon_site_related'", 'symmetrical': 'False', 'to': "orm['sites.Site']"}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'store_coupon_updated_by_related'", 'to': "orm['auth.User']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'store_coupon_user_related'", 'to': "orm['auth.User']"})
        },
        'store.customer': {
            'Meta': {'object_name': 'Customer'},
            'billing__address': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'billing_address'", 'symmetrical': 'False', 'to': "orm['store.Address']"}),
            'business_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'card_info': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['store.Card']", 'symmetrical': 'False'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'preferred_method_of_contact': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'referral': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'shipping_address': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'shipping_address'", 'symmetrical': 'False', 'to': "orm['store.Address']"}),
            'site': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'store_customer_site_related'", 'symmetrical': 'False', 'to': "orm['sites.Site']"}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'store_customer_updated_by_related'", 'to': "orm['auth.User']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'store_customer_user_related'", 'to': "orm['auth.User']"})
        },
        'store.garment': {
            'Meta': {'object_name': 'Garment'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['store.Order']"}),
            'site': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'store_garment_site_related'", 'symmetrical': 'False', 'to': "orm['sites.Site']"}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'store_garment_updated_by_related'", 'to': "orm['auth.User']"}),
            'upload': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['uploader.File']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'store_garment_user_related'", 'to': "orm['auth.User']"})
        },
        'store.invoice': {
            'Meta': {'object_name': 'Invoice'},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['store.Customer']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'discount': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice_number': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'needed_by': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'note': ('django.db.models.fields.TextField', [], {}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['store.Order']"}),
            'order_status': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pay_terms': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'payment_status': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'po_number': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'salesperson': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'invoices_salesperson'", 'to': "orm['auth.User']"}),
            'ship_date': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'shipping_handling': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'shipping_method': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'site': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'store_invoice_site_related'", 'symmetrical': 'False', 'to': "orm['sites.Site']"}),
            'subtotal': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'tax': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'tax_discount': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'total': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'turnaround': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'store_invoice_updated_by_related'", 'to': "orm['auth.User']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'store_invoice_user_related'", 'to': "orm['auth.User']"})
        },
        'store.lineitem': {
            'Meta': {'object_name': 'LineItem'},
            'art_dimension': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'art_placement': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['store.Invoice']"}),
            'item_number': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'price': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'row_color': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'site': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'store_lineitem_site_related'", 'symmetrical': 'False', 'to': "orm['sites.Site']"}),
            'sizes': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'total': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'store_lineitem_updated_by_related'", 'to': "orm['auth.User']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'store_lineitem_user_related'", 'to': "orm['auth.User']"})
        },
        'store.order': {
            'Meta': {'object_name': 'Order'},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['store.Customer']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'garment_colors': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pick_up_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'salesperson': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'salesperson'", 'to': "orm['auth.User']"}),
            'ship_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'store_order_site_related'", 'symmetrical': 'False', 'to': "orm['sites.Site']"}),
            'sizes': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'total_quantity': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type_of_garments': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'store_order_updated_by_related'", 'to': "orm['auth.User']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'store_order_user_related'", 'to': "orm['auth.User']"})
        },
        'store.product': {
            'Meta': {'object_name': 'Product'},
            'brand': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'category_one': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'parent_category'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['store.Category']"}),
            'category_two': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'child_category'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['store.Category']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('thumbnail_works.fields.EnhancedImageField', [], {'max_length': '100'}),
            'ingredients': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nutritional_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'nutritionals': ('django.db.models.fields.TextField', [], {}),
            'old_price': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'price': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'publish': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rating': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'site': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'store_product_site_related'", 'symmetrical': 'False', 'to': "orm['sites.Site']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'store_product_updated_by_related'", 'to': "orm['auth.User']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'store_product_user_related'", 'to': "orm['auth.User']"})
        },
        'uploader.file': {
            'Meta': {'object_name': 'File'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'file_type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'uploader_file_site_related'", 'symmetrical': 'False', 'to': "orm['sites.Site']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'uploader_file_updated_by_related'", 'to': "orm['auth.User']"}),
            'upload': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'uploader_file_user_related'", 'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['store']