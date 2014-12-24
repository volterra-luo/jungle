from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',	
    url(r'^quiz/',include('appetizer.urls')),
    url(r'^dimension/admin/', include(admin.site.urls)),
    url(r'^rest/',include('restframe.urls')),
    url(r'^socialauth_douban/', include('social.apps.django_app.urls', namespace='social')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/register/$', 'appetizer.views.account_create_view', 
    	{'template':'registration/register.html'}, name='create', ),
    url(r'^credential/', include('credential.urls', namespace='certify')),
    url(r'^$', 'jungle.views.home', name='home'),
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    # url(r'^socialauth_douban/', include('social_auth.urls')),
)
