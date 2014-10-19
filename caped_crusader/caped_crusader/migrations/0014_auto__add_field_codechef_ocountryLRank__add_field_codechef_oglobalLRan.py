# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Codechef.ocountryLRank'
        db.add_column(u'caped_crusader_codechef', 'ocountryLRank',
                      self.gf('django.db.models.fields.IntegerField')(default=-1),
                      keep_default=False)

        # Adding field 'Codechef.oglobalLRank'
        db.add_column(u'caped_crusader_codechef', 'oglobalLRank',
                      self.gf('django.db.models.fields.IntegerField')(default=-1),
                      keep_default=False)

        # Adding field 'Codechef.ocountrySRank'
        db.add_column(u'caped_crusader_codechef', 'ocountrySRank',
                      self.gf('django.db.models.fields.IntegerField')(default=-1),
                      keep_default=False)

        # Adding field 'Codechef.oglobalSRank'
        db.add_column(u'caped_crusader_codechef', 'oglobalSRank',
                      self.gf('django.db.models.fields.IntegerField')(default=-1),
                      keep_default=False)

        # Adding field 'Codechef.ocountryLTRank'
        db.add_column(u'caped_crusader_codechef', 'ocountryLTRank',
                      self.gf('django.db.models.fields.IntegerField')(default=-1),
                      keep_default=False)

        # Adding field 'Codechef.oglobalLTRank'
        db.add_column(u'caped_crusader_codechef', 'oglobalLTRank',
                      self.gf('django.db.models.fields.IntegerField')(default=-1),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Codechef.ocountryLRank'
        db.delete_column(u'caped_crusader_codechef', 'ocountryLRank')

        # Deleting field 'Codechef.oglobalLRank'
        db.delete_column(u'caped_crusader_codechef', 'oglobalLRank')

        # Deleting field 'Codechef.ocountrySRank'
        db.delete_column(u'caped_crusader_codechef', 'ocountrySRank')

        # Deleting field 'Codechef.oglobalSRank'
        db.delete_column(u'caped_crusader_codechef', 'oglobalSRank')

        # Deleting field 'Codechef.ocountryLTRank'
        db.delete_column(u'caped_crusader_codechef', 'ocountryLTRank')

        # Deleting field 'Codechef.oglobalLTRank'
        db.delete_column(u'caped_crusader_codechef', 'oglobalLTRank')


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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'})
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