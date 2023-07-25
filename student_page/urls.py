from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("/login", views.login_user , name="login"),
    path("", views.login_user , name="login"),
    path("/signup",views.sign_up ,name="signup"),
    path("/logout",views.logout_user , name="logout"),
    path("/dboard",views.dboard , name="dboard"),
]

