from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListCrate.as_view()),
]