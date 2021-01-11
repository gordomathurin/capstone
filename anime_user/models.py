from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractUser


class AnimeUser(AbstractUser):
    about_me = models.TextField(null=True, blank=True, verbose_name="About Me")
    avatar = models.ImageField(upload_to="images/", null=True, blank=True)
    created_on = models.DateField(auto_now_add=True)
    username = models.CharField(max_length=60, unique=True)
    email = models.EmailField(blank=True, null=True)
    follower = models.ManyToManyField("self", symmetrical=False)

    USERNAME_FIELD = "username"

    def __str__(self):
        return f"@{self.username}"
