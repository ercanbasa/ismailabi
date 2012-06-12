# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Quote.is_active'
        db.add_column('quotes_quote', 'is_active', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Quote.is_active'
        db.delete_column('quotes_quote', 'is_active')


    models = {
        'quotes.quote': {
            'Meta': {'object_name': 'Quote'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'quote': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['quotes']
