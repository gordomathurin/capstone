from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from anime_user.models import AnimeUser, Follow

# Register your models here.

admin.site.register(AnimeUser, UserAdmin)
admin.site.register(Follow)


UserAdmin.fieldsets += (
    ("Custom fields set", {"fields": ("about_me", "avatar", "followers")}),
)
