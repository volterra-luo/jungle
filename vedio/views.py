# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

def _render_template(request,page,**args):
	local_args = {'BASE_TMP':'base/v0.1/base.html'}
	args.update(local_args)
	return render(request,page,args)

def index(request):
	local_args = {}
	return _render_template(request, 'vedio/index.html', **local_args)

