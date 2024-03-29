from django.shortcuts import render, redirect
from .models import Category, Photo
from django.contrib.auth.decorators import login_required
from user_profile.models import UserProfile


@login_required(login_url="auth:signin")
def GalleryHomeView(request):
    category = request.GET.get("category")

    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)

    categories = Category.objects.all()
    context = {"categories": categories, "photos": photos}
    return render(request, "photos/gallery.html", context)


def PhotoView(request, pk):
    photo = Photo.objects.get(id=pk)
    user = photo.user
    user_profile = UserProfile.objects.get(user=user)
    context = {"photo": photo, "user": user, "profile": user_profile}
    return render(request, "photos/photo.html", context)


def AddPhotoView(request):
    categories = Category.objects.all()

    if request.method == "POST":
        data = request.POST
        image = request.FILES.get("image")
        if data["category"] != "none":
            category = Category.objects.get(id=data["category"])
        elif data["category_new"] != "":
            category, created = Category.objects.get_or_create(
                name=data["category_new"]
            )
        else:
            category = None

        photo = Photo.objects.create(
            category=category,
            description=data["description"],
            image=image,
        )
        return redirect("home")

    context = {"categories": categories}
    return render(request, "photos/add.html", context)
