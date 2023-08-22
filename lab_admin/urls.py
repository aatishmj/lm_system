from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.hello , name="hello"),
    path("/adminpage",views.admin_dash, name="adminpage"),
    path("/query" ,views.problem , name="problem"),
    path("/software" ,views.s_page , name="s_issue"),
    path("/hardware" ,views.h_page , name="h_issue"),
]
