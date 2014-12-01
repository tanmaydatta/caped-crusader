# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'contactUs'
        db.create_table(u'caped_crusader_contactus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('Phone', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('Email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('Message', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'caped_crusader', ['contactUs'])

        # Deleting field 'Codeforces.id'
        db.delete_column(u'caped_crusader_codeforces', u'id')


        # Changing field 'Codeforces.handle'
        db.alter_column(u'caped_crusader_codeforces', 'handle', self.gf('django.db.models.fields.CharField')(max_length=100, primary_key=True))
        # Adding unique constraint on 'Codeforces', fields ['handle']
        db.create_unique(u'caped_crusader_codeforces', ['handle'])


    def backwards(self, orm):
        # Removing unique constraint on 'Codeforces', fields ['handle']
        db.delete_unique(u'caped_crusader_codeforces', ['handle'])

        # Deleting model 'contactUs'
        db.delete_table(u'caped_crusader_contactus')


        # User chose to not deal with backwards NULL issues for 'Codeforces.id'
        raise RuntimeError("Cannot reverse this migration. 'Codeforces.id' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Codeforces.id'
        db.add_column(u'caped_crusader_codeforces', u'id',
                      self.gf('django.db.models.fields.AutoField')(primary_key=True),
                      keep_default=False)


        # Changing field 'Codeforces.handle'
        db.alter_column(u'caped_crusader_codeforces', 'handle', self.gf('django.db.models.fields.CharField')(max_length=100))

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
            'handle': ('django.db.models.fields.CharField', [], {'max_length': '100', 'primary_key': 'True'}),
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
        u'caped_crusader.contactus': {
            'Email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'Message': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Meta': {'object_name': 'contactUs'},
            'Name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Phone': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
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
            'Email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'Firstname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Lastname': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'Meta': {'object_name': 'user'},
            'Password': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Username': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['caped_crusader']