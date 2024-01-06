from django.urls import path
from . import views


urlpatterns = [
    path("signup", views.registerView, name="signup"),
    path("signin", views.loginView, name="signin"),
    path("signout", views.loginView, name="signout"),
]
