# -*- coding: utf-8 -*-
from django.http import (HttpResponse, HttpResponsePermanentRedirect, 
						HttpResponseRedirect, Http404, JsonResponse)
from django.shortcuts import render

from django.template.response import TemplateResponse
from django.template import loader

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.core.urlresolvers import reverse

from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_text, force_bytes

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)
from django.conf import settings

from muster.tokens import email_token_generator
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

			
			#subject = loader.render_to_string(subject_template_name, context)
        	# Email subject *must not* contain newlines
        	#subject = ''.join(subject.splitlines())
        	context = {
        		'protocal': 'http',
        		'host': request.META.get('HTTP_HOST'),
        		'email': email,
                'uid': urlsafe_base64_encode(force_bytes(u.pk)),
                'user': u,
                'token': email_token_generator.make_token(u),
            }
        	body = loader.render_to_string('muster/email_verify_body.txt', context)

        	send_mail('[NCLab]欢迎注册为NCLab用户.邮箱验证', body, settings.EMAIL_HOST_USER, [email], 
        		fail_silently=False, html_message=body)
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


def email_verify(request, uidb64=None, token=None):

	UserModel = get_user_model()
	uidb64 = request.GET.get('uidb64')
	token = request.GET.get('token')

	assert uidb64 is not None and token is not None  # checked by URLconf

	try:
		# urlsafe_base64_decode() decodes to bytestring on Python 3
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = UserModel._default_manager.get(pk=uid)
	except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
		user = None

	if user is not None and email_token_generator.check_token(user, token):
		p = Person.objects.get(user=user)
		p.is_verified = True
		p.save()
		return HttpResponseRedirect(reverse('muster:thank'))

	return HttpResponse('Hello world')

