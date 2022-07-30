from re import T
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to="user_image/%Y/%m/%d")
    email = models.EmailField(unique=True, blank=True, null=True)

    def profile_image(self):
        try:
            return self.image.url
        except:
            return f"https://avatars.dicebear.com/api/bottts/:{self.username}.jpg"
