from django import forms
from anime_comment.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {"context": forms.TextInput(attrs={"class": "form-control"})}
