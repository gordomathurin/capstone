from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, View
from anime_user.models import AnimeUser
from anime_post.models import AnimePost
from anime_user.forms import EditProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from anime_notification.models import Notification


# Create your views here.
@login_required
def index(request):
    html = "index.html"
    data = AnimeUser.objects.all()
    anime_post = AnimePost.objects.filter(anime_user=request.user)
    context = {"data": data, "posts": anime_post}
    return render(request, html, context)


@login_required
def profile_view(request, username):
    anime_holder = {}
    user_insta = AnimeUser.objects.filter(username=username).first()
    profile_insta = AnimeUser.objects.get(username=username)
    user_following = request.user.follower.all()
    notifications = Notification.objects.filter(notify=profile_insta)
    anime_holder["user_following"] = user_following
    anime_holder["pro"] = profile_insta
    anime_holder["notifications"] = notifications


    return render(request, "anime_user_detail.html", anime_holder)


@login_required
def profile_edit_view(request, username):
    user = AnimeUser.objects.filter(username=username).first()
    if request.method == "POST":
        form = EditProfileForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user.about_me = data.get("about_me")
            user.email = data.get("email")
            if "avatar" in request.FILES:
                user.avatar = request.FILES["avatar"]
            user.save()
            return HttpResponseRedirect(reverse("homepage"))

    form = EditProfileForm()
    return render(request, "edit_anime_pro.html", {"form": form})


@login_required
def delete_user(request, username):
    A_user = AnimeUser.objects.get(username=username)
    if A_user.is_staff:
        return HttpResponseForbidden(
            " ⭕ Staff anime profiles cannot be deleted from the browser. Plaese See an Admin"
        )
    elif A_user.username == request.user.username:
        A_user.delete()
        messages.success(request, "⭕ The user has been deleted")
        return redirect("homepage")
    else:
        return HttpResponseForbidden(
            " ⭕ You do not have permission to delete this user"
        )


class FeedView(LoginRequiredMixin, View):
    def get(self, request):
        html = "anime_feed_view.html"
        anime_user = request.user
        posts = AnimePost.objects.filter(anime_user=anime_user)
        follower_post = AnimePost.objects.filter(
            anime_user__in=anime_user.follower.all()
        )

        total_post = posts | follower_post
        total_post = total_post.order_by("-post_creation")
        context = {"posts": total_post}
        return render(request, html, context)


class FollowView(LoginRequiredMixin, View):
    def get(self, request, user_id):
        current_anime_user = request.user
        user_to_follow = AnimeUser.objects.get(id=user_id)
        current_anime_user.follower.add(user_to_follow)
        Notification.objects.create(
            follow_message = "started following you ❤️",
            notify = user_to_follow,
            publisher = current_anime_user
        )
        
        current_anime_user.save()
        return redirect("animefeed")


class UnFollowView(LoginRequiredMixin, View):
    def get(self, request, user_id):
        current_anime_user = request.user
        user_to_follow = AnimeUser.objects.get(id=user_id)
        current_anime_user.follower.remove(user_to_follow)
        current_anime_user.save()
        return redirect("animefeed")