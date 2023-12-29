from django.shortcuts import render


def GalleryHomeView(request):
    return render(request, "photos/gallery.html")


def PhotoView(request, pk):
    return render(request, "photos/photo.html")


def AddPhotoView(request):
    return render(request, "photos/add.html")
