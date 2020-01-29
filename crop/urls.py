from django.urls import path, re_path, include
from .views import UserList, ListCrate
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api/users', UserList)
router.register(r'api/crates', ListCrate)


urlpatterns = [
    re_path(r'^', include(router.urls)),
]
