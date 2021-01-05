from django.shortcuts import render
from anime_user.models import AnimeUser
# Create your views here.

def index(request):
    data = AnimeUser.objects.all()
    return render(request, "index.html", {'data': data})

