from django.conf.urls import patterns, url, include

from credential import views

urlpatterns = patterns('',
    # ex: /credential/00c4ff60bb25ab37d6c32507ded42d86
    url(r'^(?P<md5_value>\d{32})/$', views.check),
)