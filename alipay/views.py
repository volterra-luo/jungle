# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from util import AlipaySubmit
from config import AlipayConfig

import time, urllib, urllib2, logging, collections, mimetypes, requests

@login_required(login_url='/account/login/')
def index(request):
	return render(request, 'alipay/index.html')

def alipay_submit(request):
	if request.method == 'POST':
		requests.post(url, data=payload)


def return_view(request):
	pass

def notify_view(request):
	pass
