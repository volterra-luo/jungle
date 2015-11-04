from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from blog import views

urlpatterns = patterns('',
	url(r'^tutorial/$', views.detail ),
	url(r'^react/$', views.react_view ),
	url(r'^$', views.index, name='index' ),
)