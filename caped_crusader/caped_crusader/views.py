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
import requests
import time
from bs4 import BeautifulSoup as bs
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

t = 0

def del_Id(requests):
	del requests.session['id']
	# print "true"
	response = HttpResponse(json.dumps({'status': 'done',}), mimetype="application/json")
	return response

def getDBObject(db_name):
    db = MySQLdb.connect(settings.MYSQL_HOST,settings.MYSQL_USERNAME,settings.MYSQL_PASSWORD,db_name)
    return db

def setId(requests):
	x = requests.GET['1']
	requests.session['id'] = x
	return HttpResponse(x)

def hello(requests):
	x = requests.GET['1']
	y = requests.session['id']
	response = HttpResponse(json.dumps({'id': x,'sessid': y}), mimetype="application/json")
	return response

@csrf_exempt
def addCfUser(requests):
	if requests.method == 'POST':
		college = requests.POST.get('college')
		handle = requests.POST.get('handle')
		response = []
		exists = Codeforces.objects.filter(handle=handle)
		if not exists:
			add_user = Codeforces.objects.create(handle=handle,college=College.objects.get(id=college))
			if add_user:
				response = HttpResponse(json.dumps({'status': 'success','handle': handle, 'college':college}), mimetype="application/json")
			else:
				response = HttpResponse(json.dumps({'status': 'failure','details': 'could not add user'}), mimetype="application/json")

		else:
			response = HttpResponse(json.dumps({'status': 'failure','details': 'user already exists'}), mimetype="application/json")

	else:
		response = HttpResponse(json.dumps({'status': 'failure','details': 'post request not received'}), mimetype="application/json")

	return response


@csrf_exempt
def updateCFUserlist(requests):
	# pdb.set_trace()
	if requests.method == 'POST':
		json_data = open("/var/www/html/caped-crusader/caped_crusader/caped_crusader/user-ratedList.json")
		data = json.load(json_data)
		length = len(data['result'])
		response = []
		for row in data['result']:
			try:
				college = row['organization']
				country = row['country']
			except:
				college = ""
			if college and country == 'India':
				response.append({'handle':row['handle'],'college':college})
		response = HttpResponse(json.dumps({'status': 'success','details': response}), mimetype="application/json")
	else:
		response = HttpResponse(json.dumps({'status': 'failure','details': 'post request not recieved'}), mimetype="application/json")
	return response

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
				response = { 'status':'failed', 'error':'problem adding college' }
		
		except ValidationError:	
			response = { 'status':'failed', 'error':'invalid email'}

	else:
		response = { 'status':'failed', 'error':'post request not recieved' }

	response = HttpResponse(json.dumps(response),
		mimetype = "application/json")

	return response


@csrf_exempt
def updateTCUserlist(requests):
	# pdb.set_trace()
	if requests.method == 'POST':
		json_data = open("/var/www/html/caped-crusader/caped_crusader/caped_crusader/topcoder.json")
		data = json.load(json_data)
		length = len(data['row'])
		response = []
		for row in data['row']:
			try:
				college = row['school']
				country = row['country_name']
				coderId = row['coder_id']
			except:
				college = ""
			if college and country == 'India':
				response.append({'handle':row['handle'],'college':college,'coderId':coderId})
		response = HttpResponse(json.dumps({'status': 'success','details': response}), mimetype="application/json")
	else:
		response = HttpResponse(json.dumps({'status': 'failure','details': 'post request not recieved'}), mimetype="application/json")
	return response



@csrf_exempt
def addTCUser(requests):
	if requests.method == 'POST':
		college = requests.POST.get('college')
		handle = requests.POST.get('handle')
		coderId = requests.POST.get('coderId')
		response = []
		exists = Topcoder.objects.filter(handle=handle)
		if not exists:
			add_user = Topcoder.objects.create(handle=handle,college=College.objects.get(id=college),coderId=coderId)
			if add_user:
				response = HttpResponse(json.dumps({'status': 'success','handle': handle, 'college':college}), mimetype="application/json")
			else:
				response = HttpResponse(json.dumps({'status': 'failure','details': 'could not add user'}), mimetype="application/json")

		else:
			response = HttpResponse(json.dumps({'status': 'failure','details': 'user already exists'}), mimetype="application/json")

	else:
		response = HttpResponse(json.dumps({'status': 'failure','details': 'post request not received'}), mimetype="application/json")

	return response


def get_cc_rank(request,contest,get_handle):
	# pdb.set_trace()
	cc = "http://www.codechef.com/rankings/"+contest
	page = requests.get(cc)

	page = page.text
	x = page.find("<table>")
	y = page.find("</table>",x)
	table = page[x:y]
	table = bs(table)
	trs = table.find_all("tr")
	flag = 0
	for tr in trs:
		tds = tr.find_all("td")
		if tds:
			handle = tds[1].find("a").text
			if handle == get_handle:
				flag = 1
				rank = tds[0].find(text=True)
				break;

	if flag == 1:
		response = HttpResponse(json.dumps({'status': 'success','handle': get_handle,'rank':rank}), mimetype="application/json")

	else:
		response = HttpResponse(json.dumps({'status': 'failure','details': 'handle not found'}), mimetype="application/json")
	return response


def ccTable(request,contest):
	db_name="okrdx"
	db = getDBObject(db_name)
	cursor = db.cursor()
	errors = []
	url = "http://www.codechef.com/rankings/"+contest
	try:
		sql = "CREATE TABLE " + contest + " (handle varchar(100) NOT NULL,score DOUBLE, college_id INT)"
		cursor.execute(sql)
		db.close()
	except MySQLdb.Error, e:
		errors.append(str(e))

	if not errors:
		response = HttpResponse(json.dumps({'status': 'success'}), mimetype="application/json")

	else:
		response = HttpResponse(json.dumps({'status': 'failure','errors': errors}), mimetype="application/json")

	return response


def fillCCTable(request,contest):
	# pdb.set_trace()
	allUsers = Codechef.objects.all()
	db_name="okrdx"
	db = getDBObject(db_name)
	cursor = db.cursor()
	errors = []
	try:
		for user in allUsers:
			sql = "INSERT INTO "+contest+" (handle, college_id ) VALUES (%s,%s)" 
			# print sql
			cursor.execute(sql,( user.handle, user.college.id ))
		db.commit()

	except MySQLdb.Error, e:
		errors.append(str(e))

	if not errors:
		response = HttpResponse(json.dumps({'status': 'success'}), mimetype="application/json")

	else:
		response = HttpResponse(json.dumps({'status': 'failure','errors': errors}), mimetype="application/json")

	return response

def updateCCRank(request,contest,run):
	# pdb.set_trace()
	try:
		global t 
		t = int (0)
		while True:
			if t >= int(run):
				response = HttpResponse(json.dumps({'status': 'success'}), mimetype="application/json")
				break
			print t
			print run
			ts = time.time()
			cc = "http://www.codechef.com/rankings/"+contest
			page = requests.get(cc)
			db_name="okrdx"
			db = getDBObject(db_name)
			cursor = db.cursor()
			errors = []
			page = page.text
			x = page.find("<table>")
			y = page.find("</table>",x)
			table = page[x:y]
			table = bs(table)
			trs = table.find_all("tr")
			try:
				for tr in trs:
					tds = tr.find_all("td")
					if tds:
						handle = tds[1].find("a").text
						score = tds[len(tds)-1].text
						sql = "SELECT * FROM "+contest+" WHERE handle = '{0}'".format(handle)
						cursor.execute(sql)
						row = cursor.fetchall()
						if row:
							sql = "UPDATE "+contest+" SET score = '{0}' WHERE handle = '{1}'".format(score,handle)
							cursor.execute(sql)
				db.commit()
				te = time.time()
				t = t + int(te - ts)
				print t

			except MySQLdb.Error, e:
				errors.append(str(e))

			if not errors:
				response = HttpResponse(json.dumps({'status': 'success'}), mimetype="application/json")

			else:
				response = HttpResponse(json.dumps({'status': 'failure','errors': errors}), mimetype="application/json")
			print "one iteration complete"

	except:
		response = HttpResponse(json.dumps({'status': 'session id deleted'}), mimetype="application/json")

	return response