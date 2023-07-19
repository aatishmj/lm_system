from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("/adminlogin",views.hello , name="hello")
]
