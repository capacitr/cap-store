# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
#        db.create_table('store_category', (
#            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
#            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
#            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
#            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='store_category_user_related', to=orm['auth.User'])),
#            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='store_category_updated_by_related', to=orm['auth.User'])),
#            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
#            ('category_slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=255)),
#            ('image', self.gf('thumbnail_works.fields.EnhancedImageField')(max_length=100, blank=True)),
#            ('description', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
#        ))
        db.send_create_signal('store', ['Category'])

#        # Adding M2M table for field site on 'Category'
#        db.create_table('store_category_site', (
#            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
#            ('category', models.ForeignKey(orm['store.category'], null=False)),
#            ('site', models.ForeignKey(orm['sites.site'], null=False))
#        ))
#        db.create_unique('store_category_site', ['category_id', 'site_id'])
#
#        # Adding model 'Coupon'
#        db.create_table('store_coupon', (
#            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
#            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
#            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
#            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='store_coupon_user_related', to=orm['auth.User'])),
#            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='store_coupon_updated_by_related', to=orm['auth.User'])),
#            ('image', self.gf('thumbnail_works.fields.EnhancedImageField')(max_length=100)),
#        ))
#        db.send_create_signal('store', ['Coupon'])
#
#        # Adding M2M table for field site on 'Coupon'
#        db.create_table('store_coupon_site', (
#            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
#            ('coupon', models.ForeignKey(orm['store.coupon'], null=False)),
#            ('site', models.ForeignKey(orm['sites.site'], null=False))
#        ))
        db.create_unique('store_coupon_site', ['coupon_id', 'site_id'])

#        # Adding field 'Address.date_updated'
#        db.add_column('store_address', 'date_updated',
#                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2012, 8, 30, 0, 0), blank=True),
#                      keep_default=False)
#
#        # Adding field 'Address.updated_by'
#        db.add_column('store_address', 'updated_by',
#                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='store_address_updated_by_related', to=orm['auth.User']),
#                      keep_default=False)

        # Adding field 'Address.latitude'
        db.add_column('store_address', 'latitude',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'Address.longitude'
        db.add_column('store_address', 'longitude',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)
#
#        # Adding field 'Invoice.date_updated'
#        db.add_column('store_invoice', 'date_updated',
#                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2012, 8, 30, 0, 0), blank=True),
#                      keep_default=False)
#
#        # Adding field 'Invoice.updated_by'
#        db.add_column('store_invoice', 'updated_by',
#                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='store_invoice_updated_by_related', to=orm['auth.User']),
#                      keep_default=False)
#
#        # Adding field 'LineItem.date_updated'
#        db.add_column('store_lineitem', 'date_updated',
#                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2012, 8, 30, 0, 0), blank=True),
#                      keep_default=False)
#
#        # Adding field 'LineItem.user'
#        db.add_column('store_lineitem', 'user',
#                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='store_lineitem_user_related', to=orm['auth.User']),
#                      keep_default=False)
#
#        # Adding field 'LineItem.updated_by'
#        db.add_column('store_lineitem', 'updated_by',
#                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='store_lineitem_updated_by_related', to=orm['auth.User']),
#                      keep_default=False)
#
#        # Adding M2M table for field site on 'LineItem'
#        db.create_table('store_lineitem_site', (
#            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
#            ('lineitem', models.ForeignKey(orm['store.lineitem'], null=False)),
#            ('site', models.ForeignKey(orm['sites.site'], null=False))
#        ))
#        db.create_unique('store_lineitem_site', ['lineitem_id', 'site_id'])
#
#        # Adding field 'Card.date_updated'
#        db.add_column('store_card', 'date_updated',
#                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2012, 8, 30, 0, 0), blank=True),
#                      keep_default=False)
#
#        # Adding field 'Card.updated_by'
#        db.add_column('store_card', 'updated_by',
#                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='store_card_updated_by_related', to=orm['auth.User']),
#                      keep_default=False)
#
#        # Adding field 'Garment.date_updated'
#        db.add_column('store_garment', 'date_updated',
#                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2012, 8, 30, 0, 0), blank=True),
#                      keep_default=False)
#
#        # Adding field 'Garment.user'
#        db.add_column('store_garment', 'user',
#                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='store_garment_user_related', to=orm['auth.User']),
#                      keep_default=False)
#
#        # Adding field 'Garment.updated_by'
#        db.add_column('store_garment', 'updated_by',
#                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='store_garment_updated_by_related', to=orm['auth.User']),
#                      keep_default=False)
#
#        # Adding M2M table for field site on 'Garment'
#        db.create_table('store_garment_site', (
#            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
#            ('garment', models.ForeignKey(orm['store.garment'], null=False)),
#            ('site', models.ForeignKey(orm['sites.site'], null=False))
#        ))
#        db.create_unique('store_garment_site', ['garment_id', 'site_id'])
#
#
#        # Renaming column for 'Garment.upload' to match new field type.
#        db.rename_column('store_garment', 'upload', 'upload_id')
#        # Changing field 'Garment.upload'
#        db.alter_column('store_garment', 'upload_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['uploader.File']))
#        # Adding index on 'Garment', fields ['upload']
#        db.create_index('store_garment', ['upload_id'])
#
#        # Adding field 'Queue.date_updated'
#        db.add_column('store_queue', 'date_updated',
#                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2012, 8, 30, 0, 0), blank=True),
#                      keep_default=False)
#
#        # Adding field 'Queue.user'
#        db.add_column('store_queue', 'user',
#                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='store_queue_user_related', to=orm['auth.User']),
#                      keep_default=False)
#
#        # Adding field 'Queue.updated_by'
#        db.add_column('store_queue', 'updated_by',
#                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='store_queue_updated_by_related', to=orm['auth.User']),
#                      keep_default=False)
#
#        # Adding M2M table for field site on 'Queue'
#        db.create_table('store_queue_site', (
#            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
#            ('queue', models.ForeignKey(orm['store.queue'], null=False)),
#            ('site', models.ForeignKey(orm['sites.site'], null=False))
#        ))
#        db.create_unique('store_queue_site', ['queue_id', 'site_id'])
#
#        # Adding field 'Order.date_updated'
#        db.add_column('store_order', 'date_updated',
#                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2012, 8, 30, 0, 0), blank=True),
#                      keep_default=False)
#
#        # Adding field 'Order.updated_by'
#        db.add_column('store_order', 'updated_by',
#                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='store_order_updated_by_related', to=orm['auth.User']),
#                      keep_default=False)
#
#        # Adding field 'Product.updated_by'
#        db.add_column('store_product', 'updated_by',
#                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='store_product_updated_by_related', to=orm['auth.User']),
#                      keep_default=False)
#
#        # Adding field 'Product.category_one'
#        db.add_column('store_product', 'category_one',
#                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='parent_category', null=True, on_delete=models.SET_NULL, to=orm['store.Category']),
#                      keep_default=False)
#
#        # Adding field 'Product.category_two'
#        db.add_column('store_product', 'category_two',
#                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='child_category', null=True, on_delete=models.SET_NULL, to=orm['store.Category']),
#                      keep_default=False)
#
#        # Adding field 'Product.description'
#        db.add_column('store_product', 'description',
#                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
#                      keep_default=False)
#
#        # Adding field 'Product.ingredients'
#        db.add_column('store_product', 'ingredients',
#                      self.gf('django.db.models.fields.TextField')(default=''),
#                      keep_default=False)
#
#        # Adding field 'Product.nutritionals'
#        db.add_column('store_product', 'nutritionals',
#                      self.gf('django.db.models.fields.TextField')(default=''),
#                      keep_default=False)
#
#        # Adding field 'Product.nutritional_image'
#        db.add_column('store_product', 'nutritional_image',
#                      self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100),
#                      keep_default=False)
#
#        # Adding field 'Customer.date_updated'
#        db.add_column('store_customer', 'date_updated',
#                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2012, 8, 30, 0, 0), blank=True),
#                      keep_default=False)
#
#        # Adding field 'Customer.updated_by'
#        db.add_column('store_customer', 'updated_by',
#                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='store_customer_updated_by_related', to=orm['auth.User']),
#                      keep_default=False)


    def backwards(self, orm):
        # Removing index on 'Garment', fields ['upload']
        db.delete_index('store_garment', ['upload_id'])

        # Deleting model 'Category'
        db.delete_table('store_category')

        # Removing M2M table for field site on 'Category'
        db.delete_table('store_category_site')

        # Deleting model 'Coupon'
        db.delete_table('store_coupon')

        # Removing M2M table for field site on 'Coupon'
        db.delete_table('store_coupon_site')

        # Deleting field 'Address.date_updated'
        db.delete_column('store_address', 'date_updated')

        # Deleting field 'Address.updated_by'
        db.delete_column('store_address', 'updated_by_id')

        # Deleting field 'Address.latitude'
        db.delete_column('store_address', 'latitude')

        # Deleting field 'Address.longitude'
        db.delete_column('store_address', 'longitude')

        # Deleting field 'Invoice.date_updated'
        db.delete_column('store_invoice', 'date_updated')

        # Deleting field 'Invoice.updated_by'
        db.delete_column('store_invoice', 'updated_by_id')

        # Deleting field 'LineItem.date_updated'
        db.delete_column('store_lineitem', 'date_updated')

        # Deleting field 'LineItem.user'
        db.delete_column('store_lineitem', 'user_id')

        # Deleting field 'LineItem.updated_by'
        db.delete_column('store_lineitem', 'updated_by_id')

        # Removing M2M table for field site on 'LineItem'
        db.delete_table('store_lineitem_site')

        # Deleting field 'Card.date_updated'
        db.delete_column('store_card', 'date_updated')

        # Deleting field 'Card.updated_by'
        db.delete_column('store_card', 'updated_by_id')

        # Deleting field 'Garment.date_updated'
        db.delete_column('store_garment', 'date_updated')

        # Deleting field 'Garment.user'
        db.delete_column('store_garment', 'user_id')

        # Deleting field 'Garment.updated_by'
        db.delete_column('store_garment', 'updated_by_id')

        # Removing M2M table for field site on 'Garment'
        db.delete_table('store_garment_site')


        # Renaming column for 'Garment.upload' to match new field type.
        db.rename_column('store_garment', 'upload_id', 'upload')
        # Changing field 'Garment.upload'
        db.alter_column('store_garment', 'upload', self.gf('django.db.models.fields.files.FileField')(max_length=100))
        # Deleting field 'Queue.date_updated'
        db.delete_column('store_queue', 'date_updated')

        # Deleting field 'Queue.user'
        db.delete_column('store_queue', 'user_id')

        # Deleting field 'Queue.updated_by'
        db.delete_column('store_queue', 'updated_by_id')

        # Removing M2M table for field site on 'Queue'
        db.delete_table('store_queue_site')

        # Deleting field 'Order.date_updated'
        db.delete_column('store_order', 'date_updated')

        # Deleting field 'Order.updated_by'
        db.delete_column('store_order', 'updated_by_id')

        # Deleting field 'Product.updated_by'
        db.delete_column('store_product', 'updated_by_id')

        # Deleting field 'Product.category_one'
        db.delete_column('store_product', 'category_one_id')

        # Deleting field 'Product.category_two'
        db.delete_column('store_product', 'category_two_id')

        # Deleting field 'Product.description'
        db.delete_column('store_product', 'description')

        # Deleting field 'Product.ingredients'
        db.delete_column('store_product', 'ingredients')

        # Deleting field 'Product.nutritionals'
        db.delete_column('store_product', 'nutritionals')

        # Deleting field 'Product.nutritional_image'
        db.delete_column('store_product', 'nutritional_image')

        # Deleting field 'Customer.date_updated'
        db.delete_column('store_customer', 'date_updated')

        # Deleting field 'Customer.updated_by'
        db.delete_column('store_customer', 'updated_by_id')


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
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'site': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'store_address_site_related'", 'symmetrical': 'False', 'to': "orm['sites.Site']"}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'store_address_updated_by_related'", 'to': "orm['auth.User']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'store_address_user_related'", 'to': "orm['auth.User']"}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'store.card': {
            'Meta': {'object_name': 'Card'},
            'card_number': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
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
            'site': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'store_invoice_site_related'", 'symmetrical': 'False', 'to': "orm['sites.Site']"}),
            'subtotal': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'tax': ('django.db.models.fields.FloatField', [], {'default': '0'}),
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
        'store.queue': {
            'Meta': {'object_name': 'Queue'},
            'assigned_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'assigner'", 'to': "orm['auth.User']"}),
            'assigned_to': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'assignee'", 'to': "orm['auth.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['store.Order']"}),
            'site': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'store_queue_site_related'", 'symmetrical': 'False', 'to': "orm['sites.Site']"}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'store_queue_updated_by_related'", 'to': "orm['auth.User']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'store_queue_user_related'", 'to': "orm['auth.User']"})
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
