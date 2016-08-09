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
	tmp = [
		'6db46bac4c8e4cd5b4008d92e57a02e4',
		'ca6d9f3c842542c999e17f7a3f22eb1f',
		'137e0da11691498193e851ce435fa6e1',
		'dc93bb63bf2945d4abd61a6730386e98',
		'adf5f28abe334346bd76bb60a9e299ad',
		'23904f0500cc45ea8dbd3fbfff3dead0',
		'e68f18f086cc4e01a91c941771f7d1f2',
		'1dfae748bdb54bd19bb81f8a7411a96b',
		'd382ad0746bd4ac9a425e156c299b6b4',
		'55d3896077e24290bceb675de5d2cc31',
		'0e91c3750fe94641b25deba81e9dfe1f',
		'0299e38c09364d4ea99ceae5d4ff4bfb',
		'5791ba5ee781446ab24f126c01da7819',
		'02f7a24e488d4140a153e8a38c853a2d',
		'5f1858c1bb4d420085e742d3226ae88a',
		'0670af75d7214998aa49f7539829bb88',
		'3e83ee4114a642bc924d5f795d07d825',
		'888b7fa5fd754db88a74e978eb63d7c2',
		'2e2feca776f549cc84088ebffab8aba2',
		'0aefa10b6e7a4a18abe0a744ecb3f9e6'
	]
	code_list = [ 'https://desktop.nclab.com/viewer/' + s for s in tmp]
	local_args = {
		'code_list':  code_list,
	}
	return _render_template(request, 'jungle/gallery/3d.html', **local_args)

def gallery_turtle(request):
	pass

