import settings
import datetime
import json
from operator import itemgetter
from django.contrib.auth.models import User
from django.db import models

class user(models.Model):
	Firstname = models.CharField(max_length=100)
	Lastname = models.CharField(max_length=200, null=True)
	Email = models.CharField(max_length=100, null=True)
	Password = models.CharField(max_length=100)

	def __repr__(self):
		return '<client: %s>' % self.Firstname
