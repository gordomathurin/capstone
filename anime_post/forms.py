from django import forms
from anime_post.models import AnimePost


class NewPost(forms.Form):
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

    image = forms.ImageField(required=True)
    image_caption = forms.CharField(max_length=600, required=True)
    anime_genre = forms.ChoiceField(choices=GENRE_CHOICES, required=True)
