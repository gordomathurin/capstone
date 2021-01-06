from django.shortcuts import render, HttpResponseRedirect, reverse
from django.shortcuts import render
from anime_user.models import AnimeUser
from anime_user.forms import EditProfileForm
from django.contrib import messages
# Create your views here.

def index(request):
    data = AnimeUser.objects.all()
    return render(request, "index.html", {'data': data})

def profile_view(request, username):
    # profile_insta = AnimeUser.objects.filter(username=username).first()
    # return render(request, "anime_user_detail.html", {"pro": profile_insta})

    anime_holder = {}
    user_insta = AnimeUser.objects.filter(username=username).first()
    profile_insta = AnimeUser.objects.filter(username=user_insta).first()
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
    user = AnimeUser.objects.get(username = username)
    user.delete()
    messages.success(request, "The user has been deleted")
    return render(request, 'index.html')