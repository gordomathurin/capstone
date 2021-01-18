from django import forms
from anime_user.models import AnimeUser


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = AnimeUser
        fields = ("about_me", "email", "avatar")
