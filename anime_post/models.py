from django.db import models
from datetime import date
from django.db.models.signals import post_save
from anime_user.models import AnimeUser
from helpers.helper_file import *
import uuid


# Create your models here.
class AnimePost(models.Model):
    GENRE_CHOICES = (
        ("PICK_GENRE", "CHOOSE GENRE"),
        ("SHONEN", "SHONEN"),
        ("SHOUJU", "SHOUJU"),
        ("SEINEN", "SEINEN"),
        ("HAREM", "HAREM"),
        ("ISEKAI", "ISEKAI"),
        ("MECHA", "MECHA"),
        ("SLICE_OF_LIFE", "SLICE OF LIFE"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to=folder_path, null=True, blank=True)
    image_caption = models.TextField(max_length=600)
    post_creation = models.DateField(auto_now_add=True)
    anime_genre = models.CharField(
        max_length=20, choices=GENRE_CHOICES, default="CHOOSE GENRE"
    )
    anime_user = models.ForeignKey(
        AnimeUser, on_delete=models.CASCADE, related_name="image"
    )
    likes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.id} - {self.image} - {self.anime_genre} - {self.likes} - {self.post_creation} - {self.image_caption}  - {self.anime_user}"
