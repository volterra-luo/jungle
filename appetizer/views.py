# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from appetizer.forms import UserCreationForm

@login_required
def index(request):
   return render(request, 'quiz/index.html')

def account_create_view(request, **args):
	if request.method == 'POST':

		form = UserCreationForm(request.POST)

		if form.is_valid():
			return HttpResponsePermanentRedirect('/account/create/success/')

	else:
		form = UserCreationForm()

	username = None
	local_args = { 'form': form, 'username': username, 'BASE_TMP': 'base/v0.1/base.html' }
	return render(request, args.get('template'), local_args )

def account_login_view(request, **args):
	if request.method == 'POST':
		pass
	else:
		form = UserCreationForm()

	local_args = {'form': form, 'BASE_TMP': 'base/v0.1/base.html'}
	return render(request, args.get('template'), local_args)
