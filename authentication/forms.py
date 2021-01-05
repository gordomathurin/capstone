from django import forms
from anime_user.models import AnimeUser

class SignUpForm(forms.ModelForm):
    class Meta:
        model = AnimeUser
        fields = ['username', 'password', 'about_me', 'avatar']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)