from django.urls import path
from . import views

urlpatterns = [
    path('', views.register),
    path('login', views.login),
    path('register_process', views.register_process)
]