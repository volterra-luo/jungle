from django.conf.urls import patterns, url

from appetizer import views

urlpatterns = patterns('',
    # ex: /quiz/
    url(r'^$', views.index, name='index'),
)