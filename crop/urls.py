from django.urls import path, re_path, include
# from . import views
from .views import UserList
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import ObtainAuthToken


router = routers.DefaultRouter()
router.register(r'api/users', UserList)




urlpatterns = [
    re_path(r'^', include(router.urls)),
    re_path(r'^api/auth/', ObtainAuthToken.as_view()),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)




