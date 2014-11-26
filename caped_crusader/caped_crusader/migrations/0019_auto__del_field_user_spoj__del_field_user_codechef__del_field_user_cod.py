# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'user.spoj'
        db.delete_column(u'caped_crusader_user', 'spoj')

        # Deleting field 'user.codechef'
        db.delete_column(u'caped_crusader_user', 'codechef')

        # Deleting field 'user.codeforces'
        db.delete_column(u'caped_crusader_user', 'codeforces')

        # Deleting field 'user.topcoder'
        db.delete_column(u'caped_crusader_user', 'topcoder')


    def backwards(self, orm):
        # Adding field 'user.spoj'
        db.add_column(u'caped_crusader_user', 'spoj',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True),
                      keep_default=False)

        # Adding field 'user.codechef'
        db.add_column(u'caped_crusader_user', 'codechef',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True),
                      keep_default=False)

        # Adding field 'user.codeforces'
        db.add_column(u'caped_crusader_user', 'codeforces',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True),
                      keep_default=False)

        # Adding field 'user.topcoder'
        db.add_column(u'caped_crusader_user', 'topcoder',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True),
                      keep_default=False)


    models = {
        u'caped_crusader.codechef': {
            'Meta': {'object_name': 'Codechef'},
            'college': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['caped_crusader.College']", 'null': 'True'}),
            'countryLRank': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'countryLTRank': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'countrySRank': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'globalLRank': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'globalLTRank': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'globalSRank': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'handle': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'ocountryLRank': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'ocountryLTRank': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'ocountrySRank': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'oglobalLRank': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'oglobalLTRank': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'oglobalSRank': ('django.db.models.fields.IntegerField', [], {'default': '-1'})
        },
        u'caped_crusader.codeforces': {
            'Meta': {'object_name': 'Codeforces'},
            'college': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['caped_crusader.College']", 'null': 'True'}),
            'handle': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'orank': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'orating': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'rank': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'rating': ('django.db.models.fields.IntegerField', [], {'default': '-1'})
        },
        u'caped_crusader.college': {
            'Meta': {'object_name': 'College'},
            'collegeName': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'caped_crusader.topcoder': {
            'Meta': {'object_name': 'Topcoder'},
            'coderId': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'college': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['caped_crusader.College']", 'null': 'True'}),
            'handle': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orating': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'rank': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'rating': ('django.db.models.fields.IntegerField', [], {'default': '-1'})
        },
        u'caped_crusader.user': {
            'Email': ('django.db.models.fields.EmailField', [], {'default': "'test@test.com'", 'max_length': '75'}),
            'Firstname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Lastname': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'Meta': {'object_name': 'user'},
            'Password': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'college': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['caped_crusader.College']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['caped_crusader']