from django.shortcuts import render
from anime_user.models import AnimeUser
# Create your views here.

def index(request):
    data = AnimeUser.objects.all()
    return render(request, "index.html", {'data': data})

def profile_view(request, username):
    profile_insta = AnimeUser.objects.filter(username=username).first()
    return render(request, "anime_user_detail.html", {"pro": profile_insta})