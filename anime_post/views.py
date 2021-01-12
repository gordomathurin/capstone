from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.contrib.auth.decorators import login_required
from anime_post.helpers import add_one
from django.shortcuts import (
    render,
    HttpResponseRedirect,
    reverse,
    get_object_or_404,
    redirect,
)
from django.http import HttpResponseForbidden, HttpResponse
from anime_post.models import AnimePost
from anime_user.models import AnimeUser
from anime_comment.models import Comment
from anime_post.forms import NewPost
from anime_comment.forms import CommentForm
from anime_post.forms import NewPost


# Create your views here.
@login_required
def new_post_view(request):
    html = "post_image.html"
    anime_user = request.user

    if request.method == "POST":
        form = NewPost(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data.get("image")
            image_caption = form.cleaned_data.get("image_caption")
            anime_genre = form.cleaned_data.get("anime_genre")

            holder, created = AnimePost.objects.get_or_create(
                image=image, image_caption=image_caption, anime_user=anime_user
            )
            holder.save()
            return redirect("homepage")

        else:
            form = NewPost()

    form = NewPost()

    context = {
        "post_form": form,
    }
    return render(request, html, context)


def post_detail_view(request, post_id):
    html = "post_detail.html"
    anime_post = get_object_or_404(AnimePost, id=post_id)
    anime_user = request.user

    comments = Comment.objects.filter(anime_post=anime_post).order_by("created_on")

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = anime_post
            comment.author = anime_user
            comment.anime_post_id = post_id
            comment.save()
            return HttpResponseRedirect(reverse("anime_post_detail", args=[post_id]))

    else:
        form = CommentForm()

    context = {
        "post": anime_post,
        "form": form,
        "comments": comments,
    }
    # return HttpResponseRedirect(html, request)
    return render(request, html, context)


def post_like_view(request, post_id):
    anime_post = get_object_or_404(AnimePost, id=post_id)
    # anime_post = AnimePost.objects.filter(id=post_id).first()
    anime_post.likes += 1
    anime_post.save()
    # return redirect("animefeed")
    return HttpResponseRedirect(reverse("anime_post_detail", args=[post_id]))


def post_dislike_view(request, post_id):
    anime_post = get_object_or_404(AnimePost, id=post_id)
    # anime_post = AnimePost.objects.filter(id=post_id).first()
    anime_post.dislikes += 1
    anime_post.save()
    # return redirect("animefeed")
    return HttpResponseRedirect(reverse("anime_post_detail", args=[post_id]))