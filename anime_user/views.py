from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.shortcuts import render
from anime_user.models import AnimeUser
from anime_user.forms import EditProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

# Create your views here.

def index(request):
    data = AnimeUser.objects.all()
    return render(request, "index.html", {'data': data})

def profile_view(request, username):

    anime_holder = {}
    user_insta = AnimeUser.objects.filter(username=username).first()
    profile_insta = AnimeUser.objects.get(username=username)
    user_following = request.user.followers.all()
    anime_holder['user_following'] = user_following
    anime_holder['pro'] = profile_insta
    return render(request, "anime_user_detail.html", anime_holder)

def profile_edit_view(request, username):
    user = AnimeUser.objects.filter(username=username).first()
    if request.method == "POST":
        form = EditProfileForm(request.POST)
        if form.is_valid():
                data = form.cleaned_data
                user.about_me = data.get('about_me')
                user.email = data.get('email')
                if 'avatar' in request.FILES:
                    user.avatar = request.FILES['avatar']
                user.save()
                return HttpResponseRedirect(reverse('homepage'))

    form = EditProfileForm()
    return render(request, 'edit_anime_pro.html', {'form': form} )

def delete_user(request, username):    
    A_user = AnimeUser.objects.get(username = username)
    if A_user.is_staff:
        return HttpResponseForbidden(" ⭕ Staff anime profiles cannot be deleted from the browser. Plaese See an Admin")
    elif A_user.username == request.user.username:
        A_user.delete()
        messages.success(request, "⭕ The user has been deleted")
        return redirect('homepage')
    else: 
        return HttpResponseForbidden(" ⭕ You do not have permission to delete this user")


@login_required
def follow_user(request, userid):
    to_follow = AnimeUser.objects.get(pk=userid)
    user = AnimeUser.objects.get(pk=request.user.id)
    user.followers.add(to_follow)
    user.save()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


@login_required
def unfollow_user(request, userid):
    to_unfollow = AnimeUser.objects.get(pk=userid)
    user = AnimeUser.objects.get(id=request.user.id)
    if to_unfollow in user.followers.all():
        user.followers.remove(to_unfollow)
        user.save()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))