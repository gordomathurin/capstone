"""Config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from anime_user.views import *
from authentication.views import signup_view, logout_view, login_view
from anime_post.views import *
from anime_comment.views import *


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="homepage"),
    path("login/", login_view),
    path("logout/", logout_view),
    path("signup/", signup_view),
    path("profile/<str:username>/", profile_view, name="profile"),
    path("profile/<str:username>/edit/", profile_edit_view, name="profile_edit"),
    path("profile/<str:username>/delete/", delete_user, name="delete"),
    path("user/unfollow/<int:userid>/", unfollow_user, name="unfollow"),
    path("user/follow/<int:userid>/", follow_user, name="follow"),
    path("newpost/", new_post_view, name="newpost"),
    path("animefeed/", anime_feed_view, name="animefeed"),
    path('post/<int:post_id>/newcomment/', comment_form_view),
    path('comment/<int:pk>/delete/', del_comment, name='del_comment'),
    path('comment/<int:pk>/edit/', edit_comment, name='del_comment'),
    path('comment/<int:pk>/like/', comment_likes, name='like'),
   

    # path("<str:username>/post_detail/", ImagePostDetail, name="image_detail"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# referenced tutorial for media: https://www.youtube.com/watch?v=QC2cLkHoXLk