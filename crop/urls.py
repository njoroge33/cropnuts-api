from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListCrate.as_view()),
    path('<int:pk>/', views.DetailCrate.as_view()),
]