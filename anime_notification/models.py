from django.db import models
from anime_user.models import AnimeUser


# Create your models here.

class Notification(models.Model):
    message = models.CharField(max_length=160)
    notify = models.ForeignKey(AnimeUser, on_delete=models.CASCADE)
    publisher = models.ForeignKey(AnimeUser, on_delete=models.CASCADE, related_name='publisher', default='')
    date = models.DateField(auto_now_add=True)

