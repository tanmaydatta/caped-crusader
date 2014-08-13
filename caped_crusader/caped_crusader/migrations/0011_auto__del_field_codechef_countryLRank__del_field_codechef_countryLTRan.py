# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Codechef.countryLRank'
        db.delete_column(u'caped_crusader_codechef', 'countryLRank')

        # Deleting field 'Codechef.countryLTRank'
        db.delete_column(u'caped_crusader_codechef', 'countryLTRank')

        # Deleting field 'Codechef.globalSRank'
        db.delete_column(u'caped_crusader_codechef', 'globalSRank')

        # Deleting field 'Codechef.globalLRank'
        db.delete_column(u'caped_crusader_codechef', 'globalLRank')

        # Deleting field 'Codechef.countrySRank'
        db.delete_column(u'caped_crusader_codechef', 'countrySRank')

        # Deleting field 'Codechef.lRating'
        db.delete_column(u'caped_crusader_codechef', 'lRating')

        # Deleting field 'Codechef.ltRating'
        db.delete_column(u'caped_crusader_codechef', 'ltRating')

        # Deleting field 'Codechef.globalLTRank'
        db.delete_column(u'caped_crusader_codechef', 'globalLTRank')

        # Deleting field 'Codechef.sRating'
        db.delete_column(u'caped_crusader_codechef', 'sRating')


    def backwards(self, orm):
        # Adding field 'Codechef.countryLRank'
        db.add_column(u'caped_crusader_codechef', 'countryLRank',
                      self.gf('django.db.models.fields.IntegerField')(default=-1),
                      keep_default=False)

        # Adding field 'Codechef.countryLTRank'
        db.add_column(u'caped_crusader_codechef', 'countryLTRank',
                      self.gf('django.db.models.fields.IntegerField')(default=-1),
                      keep_default=False)

        # Adding field 'Codechef.globalSRank'
        db.add_column(u'caped_crusader_codechef', 'globalSRank',
                      self.gf('django.db.models.fields.IntegerField')(default=-1),
                      keep_default=False)

        # Adding field 'Codechef.globalLRank'
        db.add_column(u'caped_crusader_codechef', 'globalLRank',
                      self.gf('django.db.models.fields.IntegerField')(default=-1),
                      keep_default=False)

        # Adding field 'Codechef.countrySRank'
        db.add_column(u'caped_crusader_codechef', 'countrySRank',
                      self.gf('django.db.models.fields.IntegerField')(default=-1),
                      keep_default=False)

        # Adding field 'Codechef.lRating'
        db.add_column(u'caped_crusader_codechef', 'lRating',
                      self.gf('django.db.models.fields.FloatField')(default=-1.0),
                      keep_default=False)

        # Adding field 'Codechef.ltRating'
        db.add_column(u'caped_crusader_codechef', 'ltRating',
                      self.gf('django.db.models.fields.FloatField')(default=-1.0),
                      keep_default=False)

        # Adding field 'Codechef.globalLTRank'
        db.add_column(u'caped_crusader_codechef', 'globalLTRank',
                      self.gf('django.db.models.fields.IntegerField')(default=-1),
                      keep_default=False)

        # Adding field 'Codechef.sRating'
        db.add_column(u'caped_crusader_codechef', 'sRating',
                      self.gf('django.db.models.fields.FloatField')(default=-1.0),
                      keep_default=False)


    models = {
        u'caped_crusader.codechef': {
            'Meta': {'object_name': 'Codechef'},
            'college': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['caped_crusader.College']", 'null': 'True'}),
            'handle': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'})
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