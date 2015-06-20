# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from util import AlipaySubmit
from config import AlipayConfig

import time, urllib, urllib2, logging, collections, mimetypes
import requests as alipay_requests

@login_required(login_url='/account/login/')
def index(request):
	return render(request, 'alipay/index.html')

def alipay_submit(request):
	if request.method == 'POST':
		alipay_requests.post(url, data=payload)


def return_view(request):
	
	local_args = dict()
	
	# basic parameter (required)
	local_args['is_success'] = request.GET.get('is_success', 'F')
	local_args['sign_type'] = request.GET.get('sign_type', 'MD5')
	local_args['sign'] = request.GET.get('sign','')

	# bussiness paremeter (optional)
	local_args['out_trade_no'] = request.GET.get('out_trade_no','')
	local_args['subject'] = request.GET.get('subject','')
	payment_type = ''
	exterface = ''
	trade_no = ''
	trade_status = ''
	notify_id = ''
	notify_time = ''
	notify_type = ''
	seller_email = ''
	buyer_email = ''
	seller_id = ''
	buyer_id = ''
	total_fee = ''
	body = ''
	extra_common_param = ''
	agent_user_id = ''
	
	return render(request, 'alipay/return_page.html', local_args)


def notify_view(request):
	pass
