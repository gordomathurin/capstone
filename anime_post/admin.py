from django.contrib import admin
from anime_post.models import AnimePost, Feed, Likes

# Register your models here.
admin.site.register(AnimePost)
admin.site.register(Feed)
admin.site.register(Likes)