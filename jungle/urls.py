from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^quiz/',include('appetizer.urls')),
    url(r'^dimension/admin/', include(admin.site.urls)),

    url(r'^api/', include('restframe.urls', namespace='api')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #url(r'^rest/',include('restframe.urls')),
    
    url(r'^socialauth_douban/', include('social.apps.django_app.urls', namespace='social')),

    url(r'^account/', include('muster.urls', namespace='muster')),
    #url(r'^accounts/login/$', 'appetizer.views.account_login_view', {'template':'registration/login.html'}, name='login'),
    #url(r'^accounts/register/$', 'appetizer.views.account_create_view', {'template':'registration/register.html'}, name='create', ),
    #url(r'^accounts/', include('django.contrib.auth.urls')),


    url(r'^zinnia/', include('zinnia.urls', namespace='zinnia')),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^fun/', include('fun.urls', namespace='fun')),

    # vedio system
    url(r'^vod/', include('vedio.urls',namespace='vod')),

    # payment system
    url(r'^alipay/', include('alipay.urls', namespace='alipay')),

    url(r'^credential/', include('credential.urls', namespace='certify')),
    url(r'^status/$', 'jungle.views.status', name='status'),
    url(r'^resource/$', 'jungle.views.resource', name='resource'),
    url(r'^gallery/karel/$', 'jungle.views.gallery_karel', name='gallery_karel'),
    url(r'^gallery/3d/$', 'jungle.views.gallery_3d', name='gallery_3d'),
    url(r'^gallery/turtle/$', 'jungle.views.gallery_turtle', name='gallery_turtle'),
    url(r'^$', 'jungle.views.home', name='home'),
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    # url(r'^socialauth_douban/', include('social_auth.urls')),
)
