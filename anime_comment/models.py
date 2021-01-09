from django.db import models
from datetime import date
from anime_user.models import AnimeUser
from anime_post.models import AnimePost

# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey(
        AnimePost, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        AnimeUser, on_delete=models.CASCADE, related_name="author")
    content = models.CharField(max_length=300, verbose_name="comment")
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    

