from django import forms
from anime_user.models import AnimeUser


class SignUpForm(forms.Form):
    avatar = forms.ImageField(required=True)

    # class Meta:
    #     model = AnimeUser
    #     fields = ["id", "username", "password", "about_me", "email", "avatar"]

    username = forms.CharField(
        max_length=50, widget=forms.TextInput(attrs={"class": "form-control-sm"})
    )
    password = forms.CharField(widget=forms.PasswordInput())
    about_me = forms.CharField(
        max_length=150,
        widget=forms.Textarea(attrs={"class": "form-control-sm", "row": "2"}),
    )
    email = forms.EmailField(widget=forms.TextInput(attrs={"class": "form-control-sm"}))
    firstname = forms.CharField(
        max_length=250, widget=forms.TextInput(attrs={"class": "form-control-sm"})
    )
    lastname = forms.CharField(
        max_length=250, widget=forms.TextInput(attrs={"class": "form-control-sm"})
    )


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=50, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
