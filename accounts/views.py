from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout

User = get_user_model()


def registerView(request):
    form = UserRegisterForm()

    try:
        if request.method == "POST":
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data.get("email")
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")

                user = User.objects.create_user(
                    email=email,
                    username=username,
                    password=password,
                )

                messages.success(request, f"Account created for {username}!")
                return redirect("signin")

    except Exception as e:
        raise e

    context = {"form": form}
    return render(request, "accounts/register.html", context)


def loginView(request):
    form = UserLoginForm()

    try:
        if request.method == "POST":
            form = UserLoginForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data.get("email")
                password = form.cleaned_data.get("password")

                user = authenticate(request, email=email, password=password)

                if user is not None:
                    login(request, user)
                    messages.success(request, f"Login successful")
                    return redirect("photos:home")

                else:
                    form.add_error(None, "Username or password incorrect")
                    return redirect("signin")

    except Exception as e:
        raise e

    context = {"form": form}
    return render(request, "accounts/login.html", context)
