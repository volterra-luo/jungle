# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

_digit = set(map(chr, range(48, 58)))
_upper = set(map(chr, range(65, 91)))
_lower = set(map(chr, range(97,123)))

def _render_template(request,page,**args):
	local_args = {'BASE_TMP':'base/v0.1/base.html'}
	args.update(local_args)
	return render(request,page,args)

def home(request):
	local_args = {}
	return _render_template(request, 'jungle/index.html', **local_args)

def status(request):
	local_args = {}
	return _render_template(request, 'jungle/status.html', **local_args)

def resource(request):
	local_args = {}
	return _render_template(request, 'jungle/resource.html', **local_args)

def gallery_karel(request):
	tmp = ['1c4b18282e444213b5c1f00f0b3dfcc5',
			'def3d57bce774383a941ac0197ea24ac',
			'f2c2e25f8c5b49ba860875e105eb1b42',
			'ed107867442847e4aee1a808511d4a34',
			'6df2e74de05740e38bed7fbafb2a2dfd',
			'8c379caa43f045da9f7a4b6acfbd6111',
			'398858b365b04107bb6c369d79d9eff9',
			'422e4f74abe24b048012b4ebd6966290',
			'74c932679fc54cd1a189c098b33c92b6',
			'ff276abe2ce84d9e82ed8ee8f8e5a5b7',
			'c82937fb17ad4203ad091005bc662269',
			'c8715d67b0c04a4da5c8b62ca12dc592',
			'66f4eb62c6d648adaf1cdf222c0e74fb'
		]
	tmp2 = [
		'bea4d443198140a78e7e33a9e53a2ba9',
		'1730b6a35bb941adb1924d07d582f2a4',
		'5c242a8a015243e597c3d0c995e460a1',
		'b07e0ed416584946ac87b72341189cb3',
		'4fe6928d5bee48c8b4cc09d24fa94527',
		'b3d73f5ee9e047d2b3b1d6cdeb72e9ad',
		'0d3e602797e74c8eb2a8090bd4d9093a',
		'7127358708d04231bb11fe6853e73c2e',
		'e539dc3441194386aa048bacca2bf0bb',
		'2847066647514f63b5f038e337b6c542'
	]
	code_list = [ 'https://desktop.nclab.com/viewer/' + s for s in tmp]
	manual_list = [ 'https://desktop.nclab.com/viewer/' + s for s in tmp2]
	local_args = { 
		'code_list':  code_list,
		'manual_list': manual_list
	}
	return _render_template(request, 'jungle/gallery/karel.html', **local_args)

def gallery_3d(request):
	pass

def gallery_turtle(request):
	pass

