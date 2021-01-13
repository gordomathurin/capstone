from django.db import models
from anime_user.models import AnimeUser
from anime_post.models import AnimePost


# Create your models here.

class Notification(models.Model):
    message = models.ForeignKey(AnimePost, on_delete=models.CASCADE, related_name='message', null=True, blank=True)
    follow_message = models.CharField(max_length= 100, blank=True , null=True)
    notify = models.ForeignKey(AnimeUser, on_delete=models.CASCADE)
    publisher = models.ForeignKey(AnimeUser, on_delete=models.CASCADE, related_name='publisher', default='')
    date = models.DateField(auto_now_add=True)

