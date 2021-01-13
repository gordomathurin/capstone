from django import forms
from anime_user.models import AnimeUser


class SignUpForm(forms.Form):
    avatar = forms.ImageField(required=True)

    # class Meta:
    #     model = AnimeUser
    #     fields = ["id", "username", "password", "about_me", "email", "avatar"]

    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    about_me = forms.CharField(max_length=150, widget=forms.Textarea)
    email = forms.EmailField()
    firstname = forms.CharField(max_length=250)
    lastname = forms.CharField(max_length=250)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
