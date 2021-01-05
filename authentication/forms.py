from django import forms
from anime_user.models import AnimeUser

class SignUpForm(forms.ModelForm):
    class Meta:
        model = AnimeUser
        fields = ['id', 'username', 'password', 'about_me', 'avatar']
    # username = forms.CharField(max_length=50)
    # password = forms.CharField(widget=forms.PasswordInput)
    # about_me = forms.CharField(max_length=150, widget=forms.Textarea)
    # avatar = forms.ImageField()
class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)