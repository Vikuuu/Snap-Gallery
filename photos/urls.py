from django.urls import path
from . import views


urlpatterns = [
    path("", views.GalleryHomeView, name="home"),
    path("add/", views.AddPhotoView, name="add-photo"),
    path("photo/<str:pk>", views.PhotoView, name="photo"),
]
