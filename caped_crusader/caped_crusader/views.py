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
