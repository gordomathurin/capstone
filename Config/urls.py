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
from anime_post.views import *
from anime_comment.views import *
from authentication.views import *
from anime_notification.views import *



urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="homepage"),
    path("login/", login_view),
    path("logout/", logout_view),
    path("signup/", signup_view),
    path("profile/<str:username>/", profile_view, name="profile"),
    path("profile/<str:username>/edit/", profile_edit_view, name="profile_edit"),
    path("profile/<str:username>/delete/", delete_user, name="delete"),
    path("newpost/", new_post_view, name="newpost"),
    path("likecomment/<int:comment_id>/", comment_like_view, name="comment_like"),
    path(
        "dislikecomment/<int:comment_id>/", comment_dislike_view, name="comment_dislike"
    ),
    path("like/<uuid:post_id>/", post_like_view, name="post_like"),
    path("dislike/<uuid:post_id>/", post_dislike_view, name="post_dislike"),
    path("postdetail/<uuid:post_id>/", post_detail_view, name="anime_post_detail"),
    path("animefeed/", FeedView.as_view(), name="animefeed"),
    path("unfollow/<int:user_id>/", UnFollowView.as_view(), name="unfollow"),
    path("follow/<int:user_id>/", FollowView.as_view(), name="follow"),
    path('notifications/', notification_view, name='notifications'),


    path("editcomment/<int:comment_id>/", edit_comment_view, name="edit_comment"),
    path("deletecomment/<int:comment_id>/", delete_comment_view, name="delete_comment")
    # path("post/<int:post_id>/newcomment/", comment_form_view),
    # path("comment/<int:comment_id>/edit/", edit_comment, name="edit_comment"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# referenced tutorial for media: https://www.youtube.com/watch?v=QC2cLkHoXLk


handler404 = "anime_post.views.error_404_view"
handler500 = "anime_post.views.error_500_view"
# f5a1f5e3-0511-4881-9619-c978ef1c41c2
# ef6863e6-1324-494f-a5c2-38d4b2f1336d
# d5bd73fe-577d-41d8-b249-be38a4c59591
# d3d8229b-ca7f-4ff9-8840-bfe1a7858489