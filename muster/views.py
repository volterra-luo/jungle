# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect, Http404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from muster.forms import RegistrationForm, UserCreationForm,  LoginForm

@login_required
def index(request):
   return render(request, 'quiz/index.html')

def account_register_view(request, **args):
	if request.method == 'POST':

		form = UserCreationForm(request.POST)

		if form.is_valid():
			form.save()
			return HttpResponsePermanentRedirect('/')

	else:
		form = UserCreationForm()

	username = None
	local_args = { 'form': form, 'username': username, 'BASE_TMP': 'base/v0.1/base.html' }
	return render(request, args.get('template'), local_args )

def account_login_view(request, **args):
	next = request.REQUEST.get('next', '/')
	if request.method == 'POST':
		if request.session.test_cookie_worked():
			request.session.delete_test_cookie()
		else:
			return HttpResponse("Please enable cookies and try again.")

		form = LoginForm(request.POST)
		if form.is_valid():
			login(request, form.user)
			request.session.set_test_cookie()
			return HttpResponsePermanentRedirect(next)
	else:
		form = LoginForm()
		
	request.session.set_test_cookie()	
	local_args = {'form': form, 'BASE_TMP': 'base/v0.1/base.html'}
	local_args.update(args)
	return render(request, args.get('template'), local_args)

@login_required
def account_logout_view(request, **args):
	logout(request)
	return HttpResponsePermanentRedirect('/')
