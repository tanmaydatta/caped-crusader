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

url = "http://localhost:8000/"

def testCCauth(requests):
	cc = "http://www.codechef.com/contests"
	page = urllib2.urlopen(cc)
	page = bs(page)
	x = page.find_all('div', {'id': 'custom-login'})
	return HttpResponse(x)

def del_Id(requests):
	del requests.session['id']
	# print "true"
	response = HttpResponse(json.dumps({'status': 'done',}), mimetype="application/json")
	return response

def getDBObject(db_name):
    db = MySQLdb.connect(settings.MYSQL_HOST,settings.MYSQL_USERNAME,settings.MYSQL_PASSWORD,db_name)
    return db

@csrf_exempt
def setId(requests):
	pdb.set_trace()
	x = requests.GET['1']
	requests.session['id'] = x
	return HttpResponse(json.dumps({'sessid': x}), mimetype="application/json")

@csrf_exempt
def checkCollege(requests):
	# pdb.set_trace()
	errors = []
	try:
		if requests.POST.get('college'):
			flag = 0
			colleges = College.objects.all()
			for college in colleges:
				if requests.POST.get('college') == college.collegeName:
					flag = 1
					break
			if flag == 0:
				errors.append('Incorrect college name entered!')
	except:
		error.append('Error fetching data!')
	if not errors:
		response = HttpResponse(json.dumps({'status': 'success','details': requests.POST.get('college')}), mimetype="application/json")
	else :
		response = HttpResponse(json.dumps({'status': 'failure', 'errors': errors}), mimetype="application/json")

	return response

@csrf_exempt
def hello(requests):
	# pdb.set_trace()
	try:
		y = requests.session['id']
		response = HttpResponse(json.dumps({'sessid': y}), mimetype="application/json")
	except:
		response = HttpResponse(json.dumps({'sessid': 'null'}), mimetype="application/json")
	return response



def getCFCollege(handle,college_id):
	cc = "http://codeforces.com/api/user.info?handles="+str(handle)
	# print cc
	page = urllib2.urlopen(cc).read()
	page = json.loads(page)
	tags = []
	errors = []
	if page['status'] == 'OK':
		try:
			college = page['result'][0]['organization']
		except:
			college = ""
		if college:
			db_name="okrdx"
			db = getDBObject(db_name)
			cursor = db.cursor()
			# print college
			try:
				sql = "SELECT * FROM collegeTags WHERE id = '{0}'".format(str(college_id))
				cursor.execute(sql)
				rows = cursor.fetchall()
				if rows:
					for row in rows:
						x = row[1]
						x = [x.strip() for x in x.split(',')]
						tags = x;
						break
				else:
					errors.append('Error Fetching Data.')
				db.close()
			except MySQLdb.Error, e:
				errors.append(str(e))

			if not errors:
				flag = 0
				for tag in tags:
					temp = college.find(tag)
					if temp > -1:
						flag = 1
						break

				if flag == 1:
					response = json.dumps({'status': 'success'})

				else:
					response = json.dumps({'status': 'failure','errors':'college did not match'})

			else:
				response = json.dumps({'status': 'failure','errors':errors})
		else:
			response = json.dumps({'status': 'failure','errors':'college did not match'})

	else:
		response = json.dumps({'status': 'failure','errors':'incorrect handle'})

	return response


@csrf_exempt
def addCfUser(requests):
	if requests.method == 'POST':
		college = requests.POST.get('college')
		handle = requests.POST.get('handle')
		college = getCFCollege(handle,college)
		college1 = json.loads(college)
		response = []
		if college1['status'] == 'success':
			college = requests.POST.get('college')
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
			response = HttpResponse(college, mimetype="application/json")

	else:
		response = HttpResponse(json.dumps({'status': 'failure','details': 'post request not received'}), mimetype="application/json")

	return response


@csrf_exempt
def getallColleges(requests):
	# pdb.set_trace()
	if requests.method == 'POST':
		response = []
		allCollege = College.objects.all()
		for college in allCollege:
			response.append(college.collegeName);
		response = HttpResponse(json.dumps({'status': 'success','details': response}), mimetype="application/json")
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

@csrf_exempt
def getCCContestRank(requests,contest):
	# pdb.set_trace()
	if requests.method == 'POST':
		response = []
		errors = []
		data = []
		db_name="okrdx"
		db = getDBObject(db_name)
		cursor = db.cursor()
		flag = 0
		college = College.objects.filter(collegeName=requests.POST.get('college'))
		# print college[0].id
		contest = contest.upper()
		try:
			cursor.execute("SELECT * FROM "+str(contest)+" WHERE college_id = "+str(college[0].id)+" ORDER BY score DESC , handle ASC")
			rows = cursor.fetchall()
			if rows:
				for row in rows:
					name = Codechef.objects.filter(handle=row[0])
					try:
						name = name[0].name
						data.append({'handle' : row[0],'score':row[1],'name' : name})
					except:
						name = ""
					
			else:
				errors.append('Error Fetching Data.')
		except MySQLdb.Error, e:
			errors.append(str(e))
		if not errors:
			response = HttpResponse(json.dumps({'status': 'success','details': data}), mimetype="application/json")
		else:
			response = HttpResponse(json.dumps({'status': 'failure','errors': errors}), mimetype="application/json")
	else:
		response = HttpResponse(json.dumps({'status': 'failure','details': 'post request not received'}), mimetype="application/json")
	return response

@csrf_exempt
def ccContestRanks(requests,contest):
	# pdb.set_trace()
	if requests.method == 'POST':
		response = []
		errors = []
		data = []
		college = College.objects.filter(collegeName=requests.POST.get('college'))
		# print college[0].id
		users = Codechef.objects.filter(college=college[0].id)
		# users.sort(key=operator.attrgetter('globalLRank'))
		if contest == 'long':
			users = users.order_by('globalLRank')
		elif contest == 'lunchtime':
			users = users.order_by('globalLTRank')
		else :
			users = users.order_by('globalSRank')
		try:
			for user in users:
				name = user.name
				handle = user.handle
				if contest == 'long':
					grank = user.globalLRank
					crank = user.countryLRank
					grankchange = user.globalLRank - user.oglobalLRank
				elif contest == 'lunchtime':
					grank = user.globalLTRank
					crank = user.countryLTRank
					grankchange = user.globalLTRank - user.oglobalLTRank
				else :
					grank = user.globalSRank
					crank = user.countrySRank
					grankchange = user.globalSRank - user.oglobalSRank
				if grank > 0:
					data.append({'handle' : handle,'rank':grank,'crank':crank,'name' : name,'rankchange':grankchange})
			
			users = users.order_by('name')

			for user in users:
				name = user.name
				handle = user.handle
				if contest == 'long':
					grank = user.globalLRank
					crank = user.countryLRank
					grankchange = user.globalLRank - user.oglobalLRank
				elif contest == 'lunchtime':
					grank = user.globalLTRank
					crank = user.countryLTRank
					grankchange = user.globalLTRank - user.oglobalLTRank
				else :
					grank = user.globalSRank
					crank = user.countrySRank
					grankchange = user.globalSRank - user.oglobalSRank
				if grank < 0:
					data.append({'handle' : handle,'rank':grank,'crank':crank,'name' : name,'rankchange':grankchange})
					
		except :
			errors.append("error fetching data")
		if not errors:
			response = HttpResponse(json.dumps({'status': 'success','details': data}), mimetype="application/json")
		else:
			response = HttpResponse(json.dumps({'status': 'failure','errors': errors}), mimetype="application/json")
	else:
		response = HttpResponse(json.dumps({'status': 'failure','details': 'post request not received'}), mimetype="application/json")
	return response


@csrf_exempt
def getCCContests(requests):
	# pdb.set_trace()
	if requests.method == 'POST':
		response = []
		errors = []
		data = []
		db_name="okrdx"
		db = getDBObject(db_name)
		cursor = db.cursor()
		cursor.execute("SHOW TABLES FROM okrdx")
		rows = cursor.fetchall()
		if rows:
			for row in rows:
				if row[0] != 'collegeTags' and row[0] != 'detail':
					data.append(row[0])
		else:
			errors.append('Error Fetching Data.')
		if not errors:
			response = HttpResponse(json.dumps({'status': 'success','details': data}), mimetype="application/json")
		else:
			response = HttpResponse(json.dumps({'status': 'failure','errors': errors}), mimetype="application/json")
	else:
		response = HttpResponse(json.dumps({'status': 'failure','details': 'post request not received'}), mimetype="application/json")
	return response

def correctCCCollegeId(requests):
	pdb.set_trace()
	response = []
	errors = []
	data = []
	db_name="okrdx"
	db = getDBObject(db_name)
	cursor = db.cursor()
	cursor.execute("SHOW TABLES FROM okrdx")
	rows = cursor.fetchall()
	t = 0
	# for row in rows:
	row = rows[7]
	print row[0]
	if row[0] == 'AUG14':
		cursor.execute("SELECT * FROM "+row[0])
		rows1 = cursor.fetchall()
		for row1 in rows1:
			try:
				try:
					user = Codechef.objects.filter(handle=row1[0])
					college = user[0].college.id
				except:
					college = row1[2]
				# if row1[0] == 'nitish_iitr':
				# print college
				# print row1[2]
				if row1[2] != college:
					# print row[0]
					sql = "UPDATE "+row[0]+" SET college_id = "+str(college)+" WHERE handle LIKE '"+row1[0]+"'"
					print sql
					try:
						cursor.execute(sql)
						row2 = cursor.fetchall()
						print row2
					except MySQLdb.Error, e:
						errors.append(str(e))
			except MySQLdb.Error, e:
				errors.append(str(e))
				
		# print t+1
		# t = t+1
		db.commit()
	if not errors:
		response = HttpResponse(json.dumps({'status': 'success','details': data}), mimetype="application/json")
	else :
		response = HttpResponse(json.dumps({'status': 'failure','details': errors}), mimetype="application/json")
	return response
def setCodechefDb(requests):
	if requests.method == 'GET':
		db_name="okrdx"
		db = getDBObject(db_name)
		cursor = db.cursor()
		data = []
		errors = []
		i=0
		try:
			cursor.execute("SELECT * FROM detail")
			rows = cursor.fetchall()
			if rows:
				for row in rows:
					if row[11] == 3:
						exists = Codechef.objects.filter(handle=row[0])
						if not exists:
							add_user = Codechef.objects.create(handle=row[0],college=College.objects.get(id=row[11]))
							if add_user:
								data.append({'handle' : row[0],'college_id':row[11]})
								i = i+1

			else:
				errors.append('Error Fetching Data.')
			db.close()
		except MySQLdb.Error, e:
			errors.append(str(e))

		if not errors:
			response = HttpResponse(json.dumps({'status': 'success','details': data,'count':i}), mimetype="application/json")

		else:
			response = HttpResponse(json.dumps({'status': 'failure','errors': errors}), mimetype="application/json")

	else:
		response = HttpResponse(json.dumps({'status': 'failure','errors': 'get request not recieved'}), mimetype="application/json")

	return response


@csrf_exempt
def addCollege(requests):
	# pdb.set_trace()
	try:
		if requests.method == 'GET':
			college = requests.GET.get('college')
			college = college.replace(',','')
			college = college.replace('  ',' ')
			college = college.lower()
			tags = []
			errors = []
			db_name="okrdx"
			db = getDBObject(db_name)
			cursor = db.cursor()

			try:
				exist = College.objects.filter(collegeName=college)
				flag = 0
				try:
					sql = "SELECT * FROM collegeTags "
					cursor.execute(sql)
					rows = cursor.fetchall()
					if rows:
						for row in rows:
							flag = 0
							x = row[1]
							x = [x.strip() for x in x.split(',')]
							tags = x
							for tag in tags:
								temp = college.find(tag.lower())
								if temp > -1:
									flag = 1
									break	
							if flag == 1:
								break					
					else:
						errors.append('Error Fetching Data.')
					db.close()
				except MySQLdb.Error, e:
					errors.append(str(e))

				if not exist and flag == 0:
					add_college = College.objects.create(collegeName=college)

					if add_college:
						response = { 'status':'success' }
					else:
						response = { 'status':'failed', 'error':'problem adding college' }
				else:
					response = { 'status':'failed', 'error':'already exists in database'}
			
			except ValidationError:	
				response = { 'status':'failed', 'error':'error in database'}

		else:
			response = { 'status':'failed', 'error':'post request not recieved' }

		response = HttpResponse(json.dumps(response),
			mimetype = "application/json")
	except:
		response = { 'status':'failed', 'error':'request data not recieved' }
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

def getTCCollege(handle,college_id):
	cc = "http://api.topcoder.com/v2/users/search?handle="+str(handle)+"&caseSensitive=true"
	# print cc
	page = requests.get(cc)
	page = page.text
	page=json.loads(page)
	if page['users']:
		userid = str(page['users'][0]['userId'])
		cc = "http://community.topcoder.com/tc?module=MemberProfile&cr="+userid
		page = requests.get(cc)
		page = page.text
		page = bs(page)
		tables = page.find_all('table', {'class': 'profileTable'})
		tds = tables[0].find_all('td')
		ul = tds[len(tds)-1]
		lis = ul.find_all('li')
		college = lis[2].find_all('span')[0].text
		college = college.replace(',','')
		college = college.replace('  ',' ')
		college = college.lower()
		tags = []
		errors = []
		db_name="okrdx"
		db = getDBObject(db_name)
		cursor = db.cursor()
		# print college
		try:
			sql = "SELECT * FROM collegeTags WHERE id = '{0}'".format(str(college_id))
			cursor.execute(sql)
			rows = cursor.fetchall()
			if rows:
				for row in rows:
					x = row[1]
					x = [x.strip() for x in x.split(',')]
					tags = x;
					break
			else:
				errors.append('Error Fetching Data.')
			db.close()
		except MySQLdb.Error, e:
			errors.append(str(e))

		if not errors:
			flag = 0
			for tag in tags:
				temp = college.find(tag)
				if temp > -1:
					flag = 1
					break

			if flag == 1:
				response = json.dumps({'status': 'success','userid':userid})

			else:
				response = json.dumps({'status': 'failure','errors':'college did not match'})

		else:
			response = json.dumps({'status': 'failure','errors':errors})
	else:
		response = json.dumps({'status': 'failure','errors':'incorrect handle'})
	return response

@csrf_exempt
def addTCUser(requests):
	if requests.method == 'POST':
		college = requests.POST.get('college')
		handle = requests.POST.get('handle')
		college = getTCCollege(handle,college)
		college1 = json.loads(college)
		if college1['status'] == 'success':
			coderId = college1('userid')
			college = requests.POST.get('college')
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
			response = HttpResponse(college, mimetype="application/json")

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
		sql = "CREATE TABLE " + contest + " (handle varchar(100) NOT NULL UNIQUE,score DOUBLE, college_id INT)"
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

def updateCCcontestRank(request,contest,run):
	# pdb.set_trace()
	try:
		global t 
		t = int (0)
		i = 0
		while True:
			if t >= int(run):
				response = HttpResponse(json.dumps({'status': 'success','iterations':i}), mimetype="application/json")
				break
			# print t
			# print run
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
				# print t

			except MySQLdb.Error, e:
				errors.append(str(e))

			if not errors:
				response = HttpResponse(json.dumps({'status': 'success','iterations':i+1}), mimetype="application/json")

			else:
				response = HttpResponse(json.dumps({'status': 'failure','errors': errors}), mimetype="application/json")
			# print i+1," iteration(s) complete"
			i = i +1

	except:
		response = HttpResponse(json.dumps({'status': 'session id deleted'}), mimetype="application/json")

	return response

def collegeTags():
	db_name="okrdx"
	db = getDBObject(db_name)
	cursor = db.cursor()
	tags = []
	errors = []
	try:
		cursor.execute("SELECT * FROM collegeTags")
		rows = cursor.fetchall()
		if rows:
			for row in rows:
				if row[0] < 167:
					x = row[1]
					x = [x.strip() for x in x.split(',')]
					tags.append(x)

		else:
			errors.append('Error Fetching Data.')
		db.close()
	except MySQLdb.Error, e:
		errors.append(str(e))

	if not errors:
		response = tags
	else:
		response = ""
	return response

def syncCCCollege(request):
	pdb.set_trace()
	allObjects = Codechef.objects.all()
	db_name="okrdx"
	db = getDBObject(db_name)
	cursor = db.cursor()
	sql = "SELECT * FROM collegeTags"
	cursor.execute(sql)
	rows = cursor.fetchall()
	for row in allObjects:
		if row.college.id != 28 and row.college.id !=166 and row.college.id !=4 and row.college.id !=5 and row.college.id !=15 and row.college.id !=23 and row.college.id !=24 and row.college.id !=57 and row.college.id !=78 and row.college.id !=90 and row.college.id !=93 and row.college.id !=102:
			print row.handle
			cc = "http://www.codechef.com/users/"+str(row.handle)		
			page = requests.get(cc)
			page = page.text
			page = bs(page)
			x = page.find_all('table', {'cellpadding': '0','cellspacing':'0','border':'0'})
			table = x[1]
			trs = table.find_all("tr")
			tds = trs[9].find_all("td")
			try:
				college = tds[1].text
				college = college.replace(',','')
				college = college.replace('  ',' ')
				college = college.lower()
				tds = trs[8].find_all("td")
				student = tds[1].text
				tds = trs[1].find_all("td")
				name = tds[1].text
				print college 
			except:
				college = ""
			if college and student == "Student":
				for row1 in rows:
					flag = 0
					x = row1[1]
					x = [x for x in x.split(',')]
					for tag in x:
						temp = college.find(tag.lower())
						if temp > -1:
							print tag + " hello"
							flag = 1
							cid = row1[0]
							row.college = College.objects.get(id=cid)
							row.name = name
							row.save()
							break
					if flag == 1:
						break
				if flag == 0:
					row.name = "none"
					row.save()
				print row.id
			else:
				row.name = "none1"
				row.save()
			print row.handle
	return HttpResponse(True)



def getCCCollege(handle,college_id):
	# pdb.set_trace()
	cc = "http://www.codechef.com/users/"+str(handle)
	# print cc
	page = requests.get(cc)
	page = page.text
	page = bs(page)
	x = page.find_all('table', {'cellpadding': '0','cellspacing':'0','border':'0'})
	if not x:
		response = json.dumps({'status': 'failure','errors':'incorrect handle'})
	else:
		table = x[1]
		trs = table.find_all("tr")
		tds = trs[8].find_all("td")
		college = tds[1].text
		table = x[0]
		trs = table.find_all("tr")
		tds = trs[0].find_all("td")
		div = tds[0].find_all('div', {'class': 'user-name-box'})
		name = div[0].text
		tags = []
		errors = []
		db_name="okrdx"
		db = getDBObject(db_name)
		cursor = db.cursor()
		# print name
		# user-name-box
		try:
			sql = "SELECT * FROM collegeTags WHERE id = '{0}'".format(str(college_id))
			cursor.execute(sql)
			rows = cursor.fetchall()
			if rows:
				for row in rows:
					x = row[1]
					x = [x.strip() for x in x.split(',')]
					tags = x;
					break
			else:
				errors.append('Error Fetching Data.')
			db.close()
		except MySQLdb.Error, e:
			errors.append(str(e))

		if not errors:
			flag = 0
			for tag in tags:
				temp = college.find(tag)
				if temp > -1:
					flag = 1
					break

			if flag == 1:
				response = json.dumps({'status': 'success','name':name})

			else:
				response = json.dumps({'status': 'failure','errors':'college did not match'})

		else:
			response = json.dumps({'status': 'failure','errors':errors})

	return response

def addCCUser(requests):
	# pdb.set_trace()
	if requests.method == 'POST':
		handle = requests.POST.get('handle')
		college = requests.POST.get('college')
		college = getCCCollege(handle,college)
		college1 = json.loads(college)
		if college1['status'] == 'success':
			name = college1['name']
			college = requests.POST.get('college')
			response = []
			exists = Codechef.objects.filter(handle=handle)
			if not exists:
				add_user = Codechef.objects.create(handle=handle,college=College.objects.get(id=college),name=name)
				if add_user:
					cc = url + "updateCCRank/" + handle + "/"		
					page = urllib2.urlopen(cc).read()
					page = json.loads(page)
					if page['status'] == 'success':
						response = HttpResponse(json.dumps({'status': 'success','handle': handle, 'college':college}), mimetype="application/json")
					else:
						response = HttpResponse(json.dumps({'status': 'failure','details': 'could not update rank'}), mimetype="application/json")
				else:
					response = HttpResponse(json.dumps({'status': 'failure','details': 'could not add user'}), mimetype="application/json")

			else:
				response = HttpResponse(json.dumps({'status': 'failure','details': 'user already exists'}), mimetype="application/json")
		else:
			response = HttpResponse(college, mimetype="application/json")

	else:
		response = HttpResponse(json.dumps({'status': 'failure','details': 'post request not received'}), mimetype="application/json")

	return response

def updateCCNames(request):
	# pdb.set_trace()
	try:
		i = 0
		allObjects = Codechef.objects.all()
		for row in allObjects:
			if not row.name:
				cc = "http://www.codechef.com/users/"+str(row.handle)		
				page = requests.get(cc)
				page = page.text
				page = bs(page)
				x = page.find_all('table', {'cellpadding': '0','cellspacing':'0','border':'0'})
				table = x[1]
				trs = table.find_all("tr")
				tds = trs[1].find_all("td")
				name = tds[1].text
				row.name = name
				row.save()
				print row.name
			print i+1
			i = i+1
		response = json.dumps({'status': 'success'})
	except:
		response = json.dumps({'status': 'failure'})
	return response

def SyncTCColleges(request):
	pdb.set_trace()
	db_name="okrdx"
	db = getDBObject(db_name)
	cursor = db.cursor()
	sql = "SELECT * FROM collegeTags"
	cursor.execute(sql)
	rows = cursor.fetchall()
	i = 0
	try:
		allObjects = Topcoder.objects.all()
		for row in allObjects:
			if row.college.id == 5:
				print row.handle
				cc = "http://community.topcoder.com/tc?module=MemberProfile&cr="+str(row.coderId)
				page = requests.get(cc)
				page = page.text
				page = bs(page)
				tables = page.find_all('table', {'class': 'profileTable'})
				tds = tables[0].find_all('td')
				ul = tds[len(tds)-1]
				lis = ul.find_all('li')
				try:
					college = lis[2].find_all('span')[0].text
					college = college.lower()
					school = lis[2].find_all('strong')[0].text
					print college 
				except:
					college = ""
				if college and school == 'School':
					flag = 0
					for row1 in rows:
						flag = 0
						x = row1[1]
						x = [x for x in x.split(',')]
						for tag in x:
							temp = college.find(tag.lower())
							if temp > -1:
								print tag + " hello"
								flag = 1
								cid = row1[0]
								row.college = College.objects.get(id=cid)
								row.save()
								break
						if flag == 1:
							break
					if flag == 0:
						row.delete()
				else:
					row.delete()
				print row.id
				response = json.dumps({'status': 'success'})
	except:
		response = json.dumps({'status': 'failure'})
	return HttpResponse(response)


def updateSyncCFNames(request):
	pdb.set_trace()
	db_name="okrdx"
	db = getDBObject(db_name)
	cursor = db.cursor()
	sql = "SELECT * FROM collegeTags"
	cursor.execute(sql)
	rows = cursor.fetchall()
	try:
		i = 0
		allObjects = Codeforces.objects.all()
		for row in allObjects:
			# if not row.name:
			print row.handle
			cc = "http://codeforces.com/api/user.info?handles="+str(row.handle)		
			page = urllib2.urlopen(cc).read()
			page = json.loads(page)
			try:
				college = page['result'][0]['organization']
				college = college.replace(',','')
				college = college.replace('  ',' ')
				college = college.lower()
				print college
			except:
				college = ""
			try:
				fname = page['result'][0]['firstName']
			except:
				fname = ""
			try:
				lname = page['result'][0]['lastName']
			except:
				lname = ""
			name = fname + " " + lname
			row.name = name
			row.save()
			# print row.name
			if college:
				for row1 in rows:
					flag = 0
					x = row1[1]
					x = [x.strip() for x in x.split(',')]
					for tag in x:
						temp = college.find(tag.lower())
						if temp > -1:
							print tag
							flag = 1
							cid = row1[0]
							row.college = College.objects.get(id=cid)
							row.save()
							break
					if flag == 1:
						break
			print row.id
		response = json.dumps({'status': 'success'})
	except:
		response = json.dumps({'status': 'failure'})
	return HttpResponse(response)



def updateCCRank(request,handle):
	# pdb.set_trace()
	try:
		errors = []
		users = Codechef.objects.all()
		try:
			for user in users:
				if handle == '1':
					condition = user.id > 0	
				else:
					condition = user.handle == handle
				if condition:
					# pdb.set_trace()
					# print user.handle
					cc = "http://www.codechef.com/users/"+str(user.handle)
					page = urllib2.urlopen(cc).read()
					page = bs(page)
					tables = page.find_all("table",{'class':'rating-table'})
					trs = tables[0].find_all("tr")
					tds = trs[1].find_all("td")
					Long = tds[1].find_all("hx")
					glrank = Long[0].text
					if glrank.replace('.','',1).isdigit():
						user.globalLRank = int(glrank)
						clrank = Long[1].text
						lrating =float(''.join(ele for ele in tds[2].text if ele.isdigit() or ele == '.'))
						if clrank.replace('.','',1).isdigit():
							user.countryLRank = int(clrank)
						user.lRating = float(lrating)
					tds = trs[2].find_all("td")
					Short = tds[1].find_all("hx")
					gsrank = Short[0].text
					if gsrank.replace('.','',1).isdigit():
						user.globalSRank = int(gsrank)
						csrank = Short[1].text
						srating =float(''.join(ele for ele in tds[2].text if ele.isdigit() or ele == '.'))
						user.sRating = float(srating)
						if csrank.replace('.','',1).isdigit():
							user.countrySRank = int(csrank)

					tds = trs[3].find_all("td")
					Lunch = tds[1].find_all("hx")
					gltrank = Lunch[0].text
					if gltrank.replace('.','',1).isdigit():
						user.globalLTRank = int(gltrank)
						try:
							cltrank = Lunch[1].text
						except:
							cltrank = ""
						ltrating =float(''.join(ele for ele in tds[2].text if ele.isdigit() or ele == '.'))
						if cltrank.replace('.','',1).isdigit():
							user.countryLTRank = int(cltrank)
						user.ltRating = float(ltrating)
					user.save()
					# print user.id
					# break
		except:
			errors.append("error in updating data "+user.id)

		if not errors:
			response = HttpResponse(json.dumps({'status': 'success'}), mimetype="application/json")

		else:
			response = HttpResponse(json.dumps({'status': 'failure','errors': errors}), mimetype="application/json")
		# print i+1," iteration(s) complete"

	except:
		response = HttpResponse(json.dumps({'status': 'failure','errors': errors}), mimetype="application/json")

	return response

def cfTable(request,contest):
	db_name="codeforces"
	db = getDBObject(db_name)
	cursor = db.cursor()
	errors = []
	try:
		sql = "CREATE TABLE CF" + contest + " (handle varchar(100) NOT NULL UNIQUE,points DOUBLE, college_id INT, rank INT)"
		cursor.execute(sql)
		db.close()
	except MySQLdb.Error, e:
		errors.append(str(e))

	if not errors:
		response = HttpResponse(json.dumps({'status': 'success'}), mimetype="application/json")

	else:
		response = HttpResponse(json.dumps({'status': 'failure','errors': errors}), mimetype="application/json")

	return response


def fillCFTable(request,contest):
	# pdb.set_trace()
	allUsers = Codeforces.objects.all()
	db_name="codeforces"
	db = getDBObject(db_name)
	cursor = db.cursor()
	errors = []
	try:
		for user in allUsers:
			sql = "INSERT INTO CF"+contest+" (handle, college_id ) VALUES (%s,%s)" 
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

def updateCFcontestRank(request,contest,run):
	# pdb.set_trace()
	try:
		global t 
		t = int (0)
		i = 0
		while True:
			if t >= int(run):
				print t
				response = HttpResponse(json.dumps({'status': 'success','iterations':i}), mimetype="application/json")
				break
			# print t
			# print run
			ts = time.time()
			cc = "http://codeforces.com/api/contest.standings?contestId="+str(contest)
			page = urllib2.urlopen(cc).read()
			db_name="codeforces"
			db = getDBObject(db_name)
			cursor = db.cursor()
			errors = []
			page = json.loads(page)
			if page['status'] == "OK":
				try:
					for tr in page['result']['rows']:
						if tr:
							handle = tr['party']['members'][0]['handle']
							points = tr['points']
							rank = tr['rank']
							sql = "SELECT * FROM CF"+contest+" WHERE handle = '{0}'".format(handle)
							cursor.execute(sql)
							row = cursor.fetchall()
							if row:
								sql = "UPDATE CF"+contest+" SET points = '{0}' , rank = '{1}' WHERE handle = '{2}'".format(points,rank,handle)
								cursor.execute(sql)
					db.commit()
					te = time.time()
					t = t + int(te - ts)
					# print t

				except MySQLdb.Error, e:
					errors.append(str(e))

				if not errors:
					response = HttpResponse(json.dumps({'status': 'success','iterations':i+1}), mimetype="application/json")

				else:
					response = HttpResponse(json.dumps({'status': 'failure','errors': errors}), mimetype="application/json")
				# print i+1," iteration(s) complete"
				i = i +1
			else:
				response = HttpResponse(json.dumps({'status': 'failure','errors':page['comment']}), mimetype="application/json")

	except:
		response = HttpResponse(json.dumps({'status': 'failure'}), mimetype="application/json")

	return response


def updateCFRank(request):
	# pdb.set_trace()
	try:
		errors = []
		users = Codeforces.objects.all()
		try:
			for user in users:
				if user.id  > 690:
					# pdb.set_trace()
					print user.handle
					cc = "http://codeforces.com/api/user.info?handles="+str(user.handle)
					page = urllib2.urlopen(cc).read()
					page = json.loads(page)
					rank = page['result'][0]['rank']
					rating = page['result'][0]['rating']
					user.rank = rank
					user.rating = rating
					user.save()
					print user.id
					# break
		except:
			errors.append("error in updating data "+user.id)

		if not errors:
			response = HttpResponse(json.dumps({'status': 'success'}), mimetype="application/json")

		else:
			response = HttpResponse(json.dumps({'status': 'failure','errors': errors}), mimetype="application/json")
		# print i+1," iteration(s) complete"

	except:
		response = HttpResponse(json.dumps({'status': 'failure','errors': errors}), mimetype="application/json")

	return response


def updateTCRank(request):
	# pdb.set_trace()
	try:
		errors = []
		users = Topcoder.objects.all()
		try:
			for user in users:
				if user.id  == 2221:
					# pdb.set_trace()
					print user.handle
					cc = "http://community.topcoder.com/tc?module=BasicData&c=dd_rating_history&cr="+str(user.coderId)
					page = urllib2.urlopen(cc).read()
					page = bs(page)
					rows = page.find_all("row")
					size = len(rows)
					if rows:
						rating = rows[size-1].find_all("new_rating")[0].text
						orating = rows[size-1].find_all("old_rating")[0].text
						rank = rows[size-1].find_all("rank")[0].text
						user.rank = rank
						user.orating = orating
						user.rating = rating
						user.save()
					print user.id
					# break
		except:
			errors.append("error in updating data "+user.id)

		if not errors:
			response = HttpResponse(json.dumps({'status': 'success'}), mimetype="application/json")

		else:
			response = HttpResponse(json.dumps({'status': 'failure','errors': errors}), mimetype="application/json")
		# print i+1," iteration(s) complete"

	except:
		response = HttpResponse(json.dumps({'status': 'failure','errors': errors}), mimetype="application/json")

	return response