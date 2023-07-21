from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("/login", views.login , name="login"),
    path("", views.login , name="login"),
    path("/signup",views.sign_up ,name="signup"),
    path("/dboard",views.dboard , name="dboard"),
    path("/logout",views.logout_user , name="logout")
]
