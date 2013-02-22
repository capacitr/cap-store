# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Product'
#        db.create_table('store_product', (
#            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
#            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
#            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
#            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
#            ('brand', self.gf('django.db.models.fields.CharField')(max_length=255)),
#            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
#            ('image', self.gf('thumbnail_works.fields.EnhancedImageField')(max_length=100)),
#            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255)),
#            ('price', self.gf('django.db.models.fields.FloatField')(default=0)),
#            ('old_price', self.gf('django.db.models.fields.FloatField')(default=0)),
#            ('rating', self.gf('django.db.models.fields.IntegerField')(default=0)),
#            ('publish', self.gf('django.db.models.fields.BooleanField')(default=False)),
#        ))
#        db.send_create_signal('store', ['Product'])
#
#        # Adding M2M table for field site on 'Product'
#        db.create_table('store_product_site', (
#            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
#            ('product', models.ForeignKey(orm['store.product'], null=False)),
#            ('site', models.ForeignKey(orm['sites.site'], null=False))
#        ))
#        db.create_unique('store_product_site', ['product_id', 'site_id'])
#
        # Adding model 'Address'
        db.create_table('store_address', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('business', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('store', ['Address'])

        # Adding M2M table for field site on 'Address'
        db.create_table('store_address_site', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('address', models.ForeignKey(orm['store.address'], null=False)),
            ('site', models.ForeignKey(orm['sites.site'], null=False))
        ))
        db.create_unique('store_address_site', ['address_id', 'site_id'])

        # Adding model 'Card'
        db.create_table('store_card', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('card_number', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('exp_date', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('security_code', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('store', ['Card'])

        # Adding M2M table for field site on 'Card'
        db.create_table('store_card_site', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('card', models.ForeignKey(orm['store.card'], null=False)),
            ('site', models.ForeignKey(orm['sites.site'], null=False))
        ))
        db.create_unique('store_card_site', ['card_id', 'site_id'])

        # Adding model 'Customer'
        db.create_table('store_customer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=255)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('referral', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('preferred_method_of_contact', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('store', ['Customer'])

        # Adding M2M table for field site on 'Customer'
        db.create_table('store_customer_site', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('customer', models.ForeignKey(orm['store.customer'], null=False)),
            ('site', models.ForeignKey(orm['sites.site'], null=False))
        ))
        db.create_unique('store_customer_site', ['customer_id', 'site_id'])

        # Adding M2M table for field shipping_address on 'Customer'
        db.create_table('store_customer_shipping_address', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('customer', models.ForeignKey(orm['store.customer'], null=False)),
            ('address', models.ForeignKey(orm['store.address'], null=False))
        ))
        db.create_unique('store_customer_shipping_address', ['customer_id', 'address_id'])

        # Adding M2M table for field billing__address on 'Customer'
        db.create_table('store_customer_billing__address', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('customer', models.ForeignKey(orm['store.customer'], null=False)),
            ('address', models.ForeignKey(orm['store.address'], null=False))
        ))
        db.create_unique('store_customer_billing__address', ['customer_id', 'address_id'])

        # Adding M2M table for field card_info on 'Customer'
        db.create_table('store_customer_card_info', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('customer', models.ForeignKey(orm['store.customer'], null=False)),
            ('card', models.ForeignKey(orm['store.card'], null=False))
        ))
        db.create_unique('store_customer_card_info', ['customer_id', 'card_id'])

        # Adding model 'Order'
        db.create_table('store_order', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['store.Customer'])),
            ('salesperson', self.gf('django.db.models.fields.related.ForeignKey')(related_name='salesperson', to=orm['auth.User'])),
            ('garment_colors', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('total_quantity', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('type_of_garments', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('sizes', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('pick_up_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('ship_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('store', ['Order'])

        # Adding M2M table for field site on 'Order'
        db.create_table('store_order_site', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('order', models.ForeignKey(orm['store.order'], null=False)),
            ('site', models.ForeignKey(orm['sites.site'], null=False))
        ))
        db.create_unique('store_order_site', ['order_id', 'site_id'])

        # Adding model 'Garment'
        db.create_table('store_garment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('order', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['store.Order'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('upload', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('store', ['Garment'])

        # Adding model 'Invoice'
        db.create_table('store_invoice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('salesperson', self.gf('django.db.models.fields.related.ForeignKey')(related_name='invoices_salesperson', to=orm['auth.User'])),
            ('order', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['store.Order'])),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['store.Customer'])),
            ('po_number', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('turnaround', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ship_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('needed_by', self.gf('django.db.models.fields.DateTimeField')()),
            ('shipping_method', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('pay_terms', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('note', self.gf('django.db.models.fields.TextField')()),
            ('subtotal', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('discount', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('tax', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('shipping_handling', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('total', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('order_status', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('payment_status', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('store', ['Invoice'])

        # Adding M2M table for field site on 'Invoice'
        db.create_table('store_invoice_site', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('invoice', models.ForeignKey(orm['store.invoice'], null=False)),
            ('site', models.ForeignKey(orm['sites.site'], null=False))
        ))
        db.create_unique('store_invoice_site', ['invoice_id', 'site_id'])

        # Adding model 'LineItem'
        db.create_table('store_lineitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('invoice', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['store.Invoice'])),
            ('item_number', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('color', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('sizes', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('art_placement', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('art_dimension', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('price', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('total', self.gf('django.db.models.fields.FloatField')(default=0)),
        ))
        db.send_create_signal('store', ['LineItem'])

        # Adding model 'Queue'
        db.create_table('store_queue', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('assigned_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='assigner', to=orm['auth.User'])),
            ('assigned_to', self.gf('django.db.models.fields.related.ForeignKey')(related_name='assignee', to=orm['auth.User'])),
            ('order', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['store.Order'])),
        ))
        db.send_create_signal('store', ['Queue'])


    def backwards(self, orm):
        # Deleting model 'Product'
        db.delete_table('store_product')

        # Removing M2M table for field site on 'Product'
        db.delete_table('store_product_site')

        # Deleting model 'Address'
        db.delete_table('store_address')

        # Removing M2M table for field site on 'Address'
        db.delete_table('store_address_site')

        # Deleting model 'Card'
        db.delete_table('store_card')

        # Removing M2M table for field site on 'Card'
        db.delete_table('store_card_site')

        # Deleting model 'Customer'
        db.delete_table('store_customer')

        # Removing M2M table for field site on 'Customer'
        db.delete_table('store_customer_site')

        # Removing M2M table for field shipping_address on 'Customer'
        db.delete_table('store_customer_shipping_address')

        # Removing M2M table for field billing__address on 'Customer'
        db.delete_table('store_customer_billing__address')

        # Removing M2M table for field card_info on 'Customer'
        db.delete_table('store_customer_card_info')

        # Deleting model 'Order'
        db.delete_table('store_order')

        # Removing M2M table for field site on 'Order'
        db.delete_table('store_order_site')

        # Deleting model 'Garment'
        db.delete_table('store_garment')

        # Deleting model 'Invoice'
        db.delete_table('store_invoice')

        # Removing M2M table for field site on 'Invoice'
        db.delete_table('store_invoice_site')

        # Deleting model 'LineItem'
        db.delete_table('store_lineitem')

        # Deleting model 'Queue'
        db.delete_table('store_queue')


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
            'Meta': {'object_name': 'Address'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'business': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'site': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['sites.Site']", 'symmetrical': 'False'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'store.card': {
            'Meta': {'object_name': 'Card'},
            'card_number': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'exp_date': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'security_code': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'site': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['sites.Site']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'store.customer': {
            'Meta': {'object_name': 'Customer'},
            'billing__address': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'billing_address'", 'symmetrical': 'False', 'to': "orm['store.Address']"}),
            'card_info': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['store.Card']", 'symmetrical': 'False'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'preferred_method_of_contact': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'referral': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'shipping_address': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'shipping_address'", 'symmetrical': 'False', 'to': "orm['store.Address']"}),
            'site': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['sites.Site']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'store.garment': {
            'Meta': {'object_name': 'Garment'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['store.Order']"}),
            'upload': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        'store.invoice': {
            'Meta': {'object_name': 'Invoice'},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['store.Customer']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'discount': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'needed_by': ('django.db.models.fields.DateTimeField', [], {}),
            'note': ('django.db.models.fields.TextField', [], {}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['store.Order']"}),
            'order_status': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pay_terms': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'payment_status': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'po_number': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'salesperson': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'invoices_salesperson'", 'to': "orm['auth.User']"}),
            'ship_date': ('django.db.models.fields.DateTimeField', [], {}),
            'shipping_handling': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'shipping_method': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'site': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['sites.Site']", 'symmetrical': 'False'}),
            'subtotal': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'tax': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'total': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'turnaround': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'store.lineitem': {
            'Meta': {'object_name': 'LineItem'},
            'art_dimension': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'art_placement': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['store.Invoice']"}),
            'item_number': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'price': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sizes': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'total': ('django.db.models.fields.FloatField', [], {'default': '0'})
        },
        'store.order': {
            'Meta': {'object_name': 'Order'},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['store.Customer']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'garment_colors': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pick_up_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'salesperson': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'salesperson'", 'to': "orm['auth.User']"}),
            'ship_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['sites.Site']", 'symmetrical': 'False'}),
            'sizes': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'total_quantity': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type_of_garments': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'store.product': {
            'Meta': {'object_name': 'Product'},
            'brand': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('thumbnail_works.fields.EnhancedImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'old_price': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'price': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'publish': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rating': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'site': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'store'", 'symmetrical': 'False', 'to': "orm['sites.Site']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'store.queue': {
            'Meta': {'object_name': 'Queue'},
            'assigned_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'assigner'", 'to': "orm['auth.User']"}),
            'assigned_to': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'assignee'", 'to': "orm['auth.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['store.Order']"})
        }
    }

    complete_apps = ['store']
