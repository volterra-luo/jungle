from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets
from restframe import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'persons', views.PersonViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = [
	url(r'^', include(router.urls)),
]