# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Codechef.college'
        db.add_column(u'caped_crusader_codechef', 'college',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['caped_crusader.College'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Codechef.college'
        db.delete_column(u'caped_crusader_codechef', 'college_id')


    models = {
        u'caped_crusader.codechef': {
            'Meta': {'object_name': 'Codechef'},
            'college': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['caped_crusader.College']", 'null': 'True'}),
            'handle': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
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
            'codechef': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'codeforces': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'college': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['caped_crusader.College']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'spoj': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'topcoder': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'})
        }
    }

    complete_apps = ['caped_crusader']