from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets
from restframe import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'persons', views.PersonViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = [
	url(r'^nclab_user/(?P<pk>[0-9]+)/', views.nclab_user),
	url(r'^', include(router.urls)),
]

# from rest_framework.urlpatterns import format_suffix_patterns
# urlpatterns = format_suffix_patterns(urlpatterns)