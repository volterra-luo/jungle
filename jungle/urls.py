from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jungle.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^socialauth_douban/', include('social_auth.urls')),
    url(r'^quiz/',include('appetizer.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rest/',include('restframe.urls')),
    url(r'^socialauth_douban/', include('social.apps.django_app.urls', namespace='social')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
)
