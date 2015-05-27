from django.conf.urls import patterns, include, url

from alipay import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^receive_return/$', views.return_view, name='return_url'),
    url(r'^receive_notify/$', views.notify_view, name='notify_url'),
)
