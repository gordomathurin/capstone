from django.db import models
from django.utils import timezone
from anime_user.models import AnimeUser


# Create your models here.

REMEMBER TO REGISTER TO ADMIN PANEL!!!!!!!!!!!

class AnimePost(models.Model):
    GENRE_CHOICES = (
        ('SHONEN','SHONEN'), 
        ('SHOUJU', 'SHOUJU'), 
        ('SEINEN', 'SEINEN'),
        ('HAREM', 'HAREM'), 
        ('ISEKAI', 'ISEKAI'),
        ('MECHA', 'MECHA'), 
        ('SLICE_OF_LIFE', 'SLICE OF LIFE'),
        ('PICK_GENRE', 'CHOOSE GENRE')
    )

    post_image = models.ImageField(upload_to='images/', null=True, blank=True)
    anime_genre = models.CharField(GENRE_CHOICES, max_length=20, default='CHOOSE GENRE')
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    post_creation = models.DateField(default=timezone.now)
    image_caption = models.CharField(max_length=100)
    user_post_image = models.ForeignKey(AnimeUser, on_delete=models.CASCADE, related_name='image')

    def __str__(self):
    return f"{self.post_image} - {self.anime_genre} - {self.like} - {self.dislike} - {self.post_creation} - {self.image_caption} - {self.is_roast_or_boast} - {self.user_post_image}"

    def like_totals(self):
        return self.like - self.dislike
