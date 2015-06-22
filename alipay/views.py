# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from util import AlipaySubmit
from config import AlipayConfig

import time, urllib, urllib2, logging, collections, mimetypes
import requests as alipay_requests

RETURN_URL_BASE = 'http://jungle.nclab.com.cn/alipay/'
ALIPAY_GATEWAY_NEW = "https://mapi.alipay.com/gateway.do?"

@login_required(login_url='/account/login/')
def index(request):
	return render(request, 'alipay/index.html')

def alipay_submit(request):
	payload = dict()
	# basic parameter (required)
	payload['service'] = 'create_direct_pay_by_user'
	payload['partner'] = AlipayConfig.partner
	payload['_input_charset'] = AlipayConfig.input_charset
	payload['sign_type'] = AlipayConfig.sign_type
	payload['sign'] = ''
	payload['return_url'] = RETURN_URL_BASE + 'receive_return/'

	# business parameter (required)
	payload['out_trade_no'] = ''
	payload['subject'] = ''
	payload['payment_type'] = 1
	payload['total_fee'] = 0.01
	payload['seller_id'] = ''

	# # business parameter (optional)
	payload['token'] = ''

	royalty_user = 'uid2088123456789012'
	royalty_fee = str(payload['total_fee'] * 0.01)
	royalty_word = u'分你的(share with you)'
	royalty_str = '^'.join([royalty_user,royalty_fee,royalty_word])
	payload['royalty_type'] = 10
	payload['royalty_parameters'] = royalty_str

	req_param = AlipaySubmit.buildRequestPara(payload)
	
	url = ALIPAY_GATEWAY_NEW + ''

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
