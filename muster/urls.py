from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from muster import views
from django.contrib.auth.views import (password_reset, password_reset_done, 
	password_reset_confirm, password_reset_complete)

opts = {
				'template_name': 'muster/password_reset_form.html',
				'email_template_name': 'muster/password_reset_email.html',
				'subject_template_name': 'muster/password_reset_subject.txt',
				'post_reset_redirect': 'muster:password_reset_done',
				'from_email': 'support@nclab.com.cn',
		}

urlpatterns = patterns('', 
	url(r'^login/$', views.account_login_view, {'template': 'registration/login.html'}, name='login'),
	url(r'^register/$', views.account_register_view, {'template':'registration/register.html'}, name='register', ),
	url(r'^register-a/$', views.account_register_view_a, name='register-a', ),
	url(r'^logout/$', views.account_logout_view, name='logout' ),
	
	# password reset logic
	url(r'^password_reset/$', password_reset, opts, name='password_reset' ),

	url(r'^password_reset/done/$', password_reset_done, 
		{'template_name': 'muster/password_reset_done.html'}, name='password_reset_done'),

	url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 
		password_reset_confirm, {'post_reset_redirect':'muster:password_reset_complete', 
		'template_name': 'muster/password_reset_confirm.html'}, name='password_reset_confirm'),

	url(r'^reset/done/$', password_reset_complete, 
		{'template_name': 'muster/password_reset_complete.html'}, name='password_reset_complete'),

	

	url(r'^email_verify/$', views.email_verify, name='email_verify'),

	url(r'^thank/$', views.thank_view, name='thank'),
    url(r'^$', include('django.contrib.auth.urls'), ),
)
