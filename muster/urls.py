from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from muster import views

urlpatterns = patterns('', 
	url(r'^login/$', views.account_login_view, {'template': 'registration/login.html'}, name='login'),
	url(r'^register/$', views.account_register_view, {'template':'registration/register.html'}, name='register', ),
	url(r'^logout/$', views.account_logout_view, name='logout' ),
    	url(r'^$', include('django.contrib.auth.urls')),
)
