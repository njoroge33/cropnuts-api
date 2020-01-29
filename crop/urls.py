from django.urls import path, re_path, include
from . import views
from .views import SampleList
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'api/samples', SampleList)

urlpatterns = [
    re_path(r'^', include(router.urls)),
]
