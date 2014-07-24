# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'user'
        db.create_table(u'caped_crusader_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Firstname', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('Lastname', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('Email', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('Password', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'caped_crusader', ['user'])

        # Adding model 'College'
        db.create_table(u'caped_crusader_college', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('collegeName', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'caped_crusader', ['College'])


    def backwards(self, orm):
        # Deleting model 'user'
        db.delete_table(u'caped_crusader_user')

        # Deleting model 'College'
        db.delete_table(u'caped_crusader_college')


    models = {
        u'caped_crusader.college': {
            'Meta': {'object_name': 'College'},
            'collegeName': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'caped_crusader.user': {
            'Email': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'Firstname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Lastname': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'Meta': {'object_name': 'user'},
            'Password': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['caped_crusader']