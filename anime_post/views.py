from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse
from anime_post.models import AnimePost
from anime_post.forms import PostImage
from anime_user.models import AnimeUser


# Create your views here.
@login_required
def AddImage(request):
    user = request.user
    post_image = AnimePost.objects.filter(user=user)

    all_post = []

    for post in post_image:
        all_post.append(post.image)

    post_items = (
        AnimePost.objects.filter(id_in=all_post).all().order_by("-post_creation")
    )
    template = loader.get_template("post_image")

    context = {
        "post_items": post_items,
    }

    return HttpResponse(template.render(context, request))


def ImagePostDetail(request, username):
    pass