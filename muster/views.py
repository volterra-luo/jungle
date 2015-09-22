# -*- coding: utf-8 -*-
from django.http import (HttpResponse, HttpResponsePermanentRedirect, 
							Http404, JsonResponse)
from django.shortcuts import render
from django.core.mail import send_mail
from django.core.urlresolvers import reverse

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from muster.forms import RegistrationForm, LoginForm
from muster.forms import UserCreationForm2 as UserCreationForm
from muster.models import Person

@login_required
def index(request):
	return render(request, 'quiz/index.html')

def account_password_reset_view(request):
	local_args = {'BASE_TMP': 'base/v0.1/base.html' }
	return render(request, 'muster/password_reset.html', local_args)


def account_register_view_a(request):
	return JsonResponse({'foo': 'bar'})

def account_register_view(request, **args):
	username = None

	
	if request.method == 'POST':

		PTStatus = request.POST['ParentOrTeacherRole']
		form = UserCreationForm(request.POST)

		if form.is_valid():
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			u = User.objects.create_user(username=username, password=password, email=email)
			p = Person.objects.create(user=u, role=PTStatus)
			p.save()
			return HttpResponsePermanentRedirect(reverse('muster:thank'))

			

	else:
		form = UserCreationForm()

	local_args = { 'form': form, 'username': username, 'BASE_TMP': 'base/v0.1/base.html' }
	return render(request, args.get('template'), local_args )

def account_login_view(request, **args):
	next = request.REQUEST.get('next','/')
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
	local_args = {'form': form, 'BASE_TMP': 'base/v0.1/base.html', 'next':next }
	local_args.update(args)
	return render(request, args.get('template'), local_args)

@login_required
def account_logout_view(request, **args):
	logout(request)
	return HttpResponsePermanentRedirect('/')

@login_required
def thank_view(request, **args):
	local_args = { 'BASE_TMP': 'base/v0.1/base.html' }
	return render(request,'muster/thank.html', local_args)
