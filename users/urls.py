from django.urls import path

from .views import user_form_view, login_view, logout_view, register_view, profile_view

urlpatterns = [
    path("user_form/", user_form_view, name="user_form"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register_view, name="register"),
    path("profile/", profile_view, name="profile"),
]
