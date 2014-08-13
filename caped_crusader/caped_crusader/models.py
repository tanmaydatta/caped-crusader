import settings
import datetime
import json
from operator import itemgetter
from django.contrib.auth.models import User
from django.db import models


class College(models.Model):
	collegeName = models.CharField(max_length=100)

	def __repr__(self):
		return '<college: %s>' % self.collegeName

class Codeforces(models.Model):
	handle = models.CharField(max_length=100)
	college = models.ForeignKey(College,null=True)
	name = models.CharField(max_length=200,null=True)
	def __repr__(self):
		return '<handle: %s>' % self.handle

class Topcoder(models.Model):
	handle = models.CharField(max_length=100)
	college = models.ForeignKey(College,null=True)
	coderId = models.CharField(max_length=100)
	def __repr__(self):
		return '<handle: %s>' % self.handle

class Codechef(models.Model):
	handle = models.CharField(max_length=100)
	college = models.ForeignKey(College,null=True)
	name = models.CharField(max_length=200,null=True)
	countryLRank = models.IntegerField(default=-1)
	globalLRank = models.IntegerField(default=-1)
	countrySRank = models.IntegerField(default=-1)
	globalSRank = models.IntegerField(default=-1)
	countryLTRank = models.IntegerField(default=-1)
	globalLTRank = models.IntegerField(default=-1)
	lRating = models.FloatField(default=-1.0)
	sRating = models.FloatField(default=-1.0)
	ltRating = models.FloatField(default=-1.0)

	def __repr__(self):
		return '<handle: %s>' % self.handle

class user(models.Model):
	Firstname = models.CharField(max_length=100)
	Lastname = models.CharField(max_length=200, null=True)
	Email = models.EmailField(default='test@test.com')
	Password = models.CharField(max_length=100)
	college = models.ForeignKey(College,default=1)
	codechef = models.CharField(max_length=100, null=True)
	codeforces = models.CharField(max_length=100, null=True)
	topcoder = models.CharField(max_length=100, null=True)
	spoj = models.CharField(max_length=100, null=True)