from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    UserChangeForm,
)
from django import forms

from users.models import User


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UserProfileFrom(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "city",
            "region",
            "address",
        ]

    def __init__(self, *args, **kwargs):
        super(UserProfileFrom, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "border-0 w-100"
