from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from anime_user.models import AnimeUser

# Register your models here.

admin.site.register(AnimeUser, UserAdmin)

UserAdmin.fieldsets += ('Custom fields set', {'fields': ('about_me',)}),

