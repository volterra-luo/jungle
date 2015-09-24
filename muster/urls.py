from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from muster import views

urlpatterns = patterns('', 
	url(r'^login/$', views.account_login_view, {'template': 'registration/login.html'}, name='login'),
	url(r'^register/$', views.account_register_view, {'template':'registration/register.html'}, name='register', ),
	url(r'^register-a/$', views.account_register_view_a, name='register-a', ),
	url(r'^logout/$', views.account_logout_view, name='logout' ),
	url(r'^password_reset/$', views.account_password_reset_view, name='password_reset' ),

	url(r'^email_verify/$', views.email_verify, name='email_verify'),

	url(r'^thank/$', views.thank_view, name='thank'),
    url(r'^$', include('django.contrib.auth.urls'), ),
)
