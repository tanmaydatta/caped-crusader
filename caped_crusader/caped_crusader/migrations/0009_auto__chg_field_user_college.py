# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'user.college'
        db.alter_column(u'caped_crusader_user', 'college_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['caped_crusader.College']))

    def backwards(self, orm):

        # Changing field 'user.college'
        db.alter_column(u'caped_crusader_user', 'college_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['caped_crusader.College'], null=True))

    models = {
        u'caped_crusader.college': {
            'Meta': {'object_name': 'College'},
            'collegeName': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'caped_crusader.user': {
            'Email': ('django.db.models.fields.EmailField', [], {'default': "'test@test.com'", 'max_length': '75'}),
            'Firstname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Lastname': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'Meta': {'object_name': 'user'},
            'Password': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'college': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'to': u"orm['caped_crusader.College']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['caped_crusader']