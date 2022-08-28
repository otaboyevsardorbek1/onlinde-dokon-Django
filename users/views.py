from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from django.contrib.auth import authenticate, login, logout

from .forms import UserLoginForm, UserRegisterForm, UserProfileFrom
from .models import User


def user_form_view(request):
    return render(request, "users/user_form.html")


def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(username=username, password=password)

            if user and user.is_active:
                login(request, user)
                return redirect("home")
    else:
        form = UserLoginForm()
    context = {
        "form": form,
    }
    return render(request, "users/user_login.html", context)

def logout_view(request):
    logout(request)
    return redirect()


def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            print(form.save())
            return redirect("login")
        else:
            print(form.errors)
    else:
        form = UserRegisterForm()
    context = {
        "form": form,
    }
    return render(request, "users/user_register.html", context)


def profile_view(request):
    form = ''
    if request.method == "POST":
        user_form = UserProfileFrom(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect("profile")
        else:
            return redirect("profile")
    else:

        if request.user.is_active:
            print(request.user)
            form = UserProfileFrom(instance=request.user)

    context = {"form": form}

    return render(request, "users/user_profile.html", context=context)
