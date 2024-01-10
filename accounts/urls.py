from django.urls import path
from . import views

app_name = "auth"

urlpatterns = [
    path("signup", views.registerView, name="signup"),
    path("signin", views.loginView, name="signin"),
    path("signout", views.logoutView, name="signout"),
]
