from django.conf.urls import patterns, url, include

from appetizer import views

urlpatterns = patterns('',
    # ex: /quiz/
    url(r'^$', views.index, name='index'),
)