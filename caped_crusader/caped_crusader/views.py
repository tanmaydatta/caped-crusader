import MySQLdb
import MySQLdb.cursors
import json
import time
import os
import hashlib
import urllib2
import re
from datetime import datetime
from operator import itemgetter
import logging
import urllib
import HTMLParser
import pprint
import random
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from django.http import * #(HttpResponse, HttpResponseRedirect)
from django.core.context_processors import csrf
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from django.shortcuts import render, redirect
from django.forms.models import model_to_dict
from django.core.mail import send_mail

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from phpserialize import serialize, unserialize

from caped_crusader.models import *

import settings

from hashlib import md5

from django.views.decorators.http import require_POST

import pdb
import requests


def getDBObject(db_name):
    db = MySQLdb.connect(settings.MYSQL_HOST,settings.MYSQL_USERNAME,settings.MYSQL_PASSWORD,db_name)
    return db

def hello(requests):
	return HttpResponse('hello')

def setCodechefDb(requests):
	if requests.method == 'GET':
		db_name="okrdx"
		db = getDBObject(db_name)
		cursor = db.cursor()
		data = []
		errors = []
		try:
			cursor.execute("SELECT * FROM detail")
			rows = cursor.fetchall()
			if rows:
				for row in rows:
					if row[11] < 167:
						exists = Codechef.objects.filter(handle=row[0])
						if not exists:
							add_user = Codechef.objects.create(handle=row[0],college=College.objects.get(id=row[11]))
							if add_user:
								data.append({'handle' : row[0],'college_id':row[11]})

			else:
				errors.append('Error Fetching Data.')
			db.close()
		except MySQLdb.Error, e:
			errors.append(str(e))

		if not errors:
			response = HttpResponse(json.dumps({'status': 'success','details': data}), mimetype="application/json")

		else:
			response = HttpResponse(json.dumps({'status': 'failure','errors': errors}), mimetype="application/json")

	else:
		response = HttpResponse(json.dumps({'status': 'failure','errors': 'get request not recieved'}), mimetype="application/json")

	return response



@csrf_exempt
def addCollege(requests):
	# pdb.set_trace()
	if requests.method == 'POST':
		college = requests.POST.get('college')

		try:
			add_college = College.objects.create(collegeName=college)

			if add_college:
				response = { 'status':'success' }
			else:
				response = { 'status':'failed', 'error':'problem with creating client' }
		
		except ValidationError:	
			response = { 'status':'failed', 'error':'invalid email'}

	else:
		response = { 'status':'failed', 'error':'post request not recieved' }

	response = HttpResponse(json.dumps(response),
		mimetype = "application/json")

	return response