from django.urls import path
from . import views

app_name = "photos"

urlpatterns = [
    path("home/", views.GalleryHomeView, name="home"),
    path("add/", views.AddPhotoView, name="add-photo"),
    path("photo/<str:pk>", views.PhotoView, name="photo"),
]
