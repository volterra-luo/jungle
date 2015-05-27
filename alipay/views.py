# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# from util import AlipaySubmit
# from config import AlipayConfig

import time, urllib, urllib2, logging, collections, mimetypes

@login_required(login_url='/account/login/')
def index(request):
	return render(request, 'alipay/index.html')

def return_view(request):
	pass

def notify_view(request):
	pass
