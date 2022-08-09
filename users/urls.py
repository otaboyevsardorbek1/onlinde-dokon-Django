from django.urls import path

from .views import  user_form_view, login_view, register_view

urlpatterns = [
    path('user_form/',  user_form_view, name='user_form'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
]
