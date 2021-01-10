from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.contrib.auth.decorators import login_required
from anime_comment.helpers import add_one
from django.shortcuts import (
    render,
    HttpResponseRedirect,
    reverse,
    get_object_or_404,
    redirect,
)
from django.http import HttpResponseForbidden, HttpResponse
from anime_post.models import AnimePost
from anime_post.models import AnimePost, Likes
from anime_user.models import AnimeUser, Follow
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
            return redirect("animefeed")

        else:
            form = NewPost()

    form = NewPost()

    context = {
        "post_form": form,
    }
    return render(request, html, context)


@login_required
def like_view(request, post_id):
    anime_user = request.user
    anime_post = AnimePost.objects.get(id=post_id)
    like_count = anime_post.likes

    post_liked = Likes.objects.filter(
        anime_user=anime_user, anime_post=anime_post
    ).count()
    print(post_liked)

    if not post_liked:
        post_liked = Likes.objects.create(anime_user=anime_user, anime_post=anime_post)
        like_count = like_count + 1
    else:
        Likes.objects.filter(anime_user=anime_user, anime_post=anime_post).delete()
        like_count = like_count - 1

    anime_post.likes = like_count
    anime_post.save()

    return redirect("animefeed")


def post_form_view(request, postid):
    html = "post_detail.html"
    post = get_object_or_404(AnimePost, id=postid)
    user = request.user
    # comment :
    comments = Comment.objects.filter(post=post).order_by("date")
    # comment form:
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=false)
            comment.post = post
            comment.user = user
            comment.save()
            return HttpResponseRedirect(reverse("post_details.html", args=[postid]))
    else:
        form = CommentForm()

    context = {
        "post": post,
        "form": form,
        "comments": comments,
    }
    return HttpResponseRedirect(html, request)
