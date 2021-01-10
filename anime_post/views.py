from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.contrib.auth.decorators import login_required
from anime_post.models import AnimePost, Likes
from anime_post.forms import NewPost
from anime_user.models import AnimeUser, Follow


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
    anime_post = AnimePost.objects.filter(id=post_id)
    like_count = AnimePost.likes

    liked = Likes.objects.filter(user=anime_user, post=post).count()

    if not like:
        like = Likes.objects.create(user=anime_user, post=post)
        like_count = like_count + 1
    else:
        Likes.objects.filter(user=anime_user, post=post).delete()
        like_count = like_count - 1

    anime_post.likes = like_count
    anime_post.save()

    return redirect("animefeed")
