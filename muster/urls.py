from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from muster import views

urlpatterns = patterns('', 
	url(r'^login/$', views.account_login_view, {'template': 'registration/login.html'}, name='login'),
	url(r'^register/$', views.account_create_view, {'template':'registration/register.html'}, name='create', ),
    	url(r'^', include('django.contrib.auth.urls')),
)
