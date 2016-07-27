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
