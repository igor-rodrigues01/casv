# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserEmail'
        db.create_table('register_user_useremail', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal('register_user', ['UserEmail'])


    def backwards(self, orm):
        # Deleting model 'UserEmail'
        db.delete_table('register_user_useremail')


    models = {
        'register_user.useremail': {
            'Meta': {'object_name': 'UserEmail'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['register_user']