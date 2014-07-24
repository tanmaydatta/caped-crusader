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

class user(models.Model):
	Firstname = models.CharField(max_length=100)
	Lastname = models.CharField(max_length=200, null=True)
	Email = models.EmailField(default='test@test.com')
	Password = models.CharField(max_length=100)
	college = models.ForeignKey(College,default=1)
	codechef = models.CharField(max_length=100, null=True)
	hackerrank = models.CharField(max_length=100, null=True)
	codeforces = models.CharField(max_length=100, null=True)
	topcoder = models.CharField(max_length=100, null=True)
	spoj = models.CharField(max_length=100, null=True)