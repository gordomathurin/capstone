from django.shortcuts import render
from anime_user.models import AnimeUser
# Create your views here.

def index(request):
    data = AnimeUser.objects.all()
    return render(request, "index.html", {'data': data})

def profile_view(request, username):
    profile_insta = AnimeUser.objects.filter(username=username).first()
    return render(request, "anime_user_detail.html", {"pro": profile_insta})

    # anime_holder = {}
    # user = AnimeUser.objects.get(username=username)
    # profile_insta = AnimeUser.objects.filter(username=username).first()
    # anime_holder['pro'] = profile_insta
    # return render(request, "anime_user_detail.html", anime_holder)