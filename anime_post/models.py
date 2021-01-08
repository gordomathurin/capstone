from django.db import models
from django.utils import timezone
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
    post_creation = models.DateField(default=timezone.now)
    anime_genre = models.CharField(
        max_length=20, choices=GENRE_CHOICES, default="CHOOSE GENRE"
    )
    likes = models.IntegerField(default=0)
    anime_user = models.ForeignKey(
        AnimeUser, on_delete=models.CASCADE, related_name="image"
    )

    def like_totals(self):
        likes = self.like + 1
        return likes

    def __str__(self):
        return f"{self.id} - {self.image} - {self.anime_genre} - {self.likes} - {self.post_creation} - {self.image_caption}  - {self.anime_user}"

    def url_getter(sef):
        return reverse("post_details", args=[str(self.id)])


class Follow(models.Model):
    follower = models.ForeignKey(
        AnimeUser, on_delete=models.CASCADE, related_name="follower"
    )
    following = models.ForeignKey(
        AnimeUser, on_delete=models.CASCADE, related_name="following"
    )


class Feed(models.Model):
    following = models.ForeignKey(
        AnimeUser, on_delete=models.CASCADE, related_name="feed"
    )
    post = models.ForeignKey(AnimePost, on_delete=models.CASCADE, related_name="post")
    anime_user = models.ForeignKey(
        AnimeUser, on_delete=models.CASCADE, related_name="user"
    )
    date_post = models.DateField(default=timezone.now)

    def post_add(sender, instance, *args, **kwargs):
        post = instance
        anime_user = post.anime_user
        anime_follower = Follow.objects.all().filter(following=anime_user)

        for follower in anime_follower:
            feed = Feed(
                post=post,
                user=follower.follower,
                date_post=date_post,
                following=anime_user,
            )
            feed.save()


post_save.connect(Feed.post_add, sender=AnimePost)