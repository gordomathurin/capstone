from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractUser
# referenced article for auto_now_add : https://stackoverflow.com/questions/1737017/django-auto-now-and-auto-now-add
#  referenced article for uplaod_to : https://stackoverflow.com/questions/34563454/django-imagefield-upload-to-path/34563512
# Create your models here.

class AnimeUser(AbstractUser):
    about_me = models.TextField(null=True, blank=True, verbose_name="About Me")
    avatar = models.ImageField(upload_to='images/', null=True, blank=True)
    created_on = models.DateField(auto_now_add=True)
