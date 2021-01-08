from django import forms
from anime_post.models import AnimePost


class PostImage(forms.Form):
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

    add_image = forms.ImageField(required=True)
    image_caption = forms.CharField(max_length=100)
    anime_genre = forms.ChoiceField(choices=GENRE_CHOICES)