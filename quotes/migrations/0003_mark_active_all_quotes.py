# encoding: utf-8
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
       orm['quotes.Quote'].objects.all().update(is_active=True)


    def backwards(self, orm):
        orm['quotes.Quote'].objects.all().update(is_active=False)


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
