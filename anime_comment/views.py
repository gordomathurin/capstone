from django.shortcuts import (
    render,
    HttpResponseRedirect,
    reverse,
    get_object_or_404,
    redirect,
)
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from anime_user.models import AnimeUser
from anime_post.models import AnimePost
from anime_comment.models import Comment
from anime_post.forms import NewPost
from anime_comment.forms import CommentForm
from anime_comment.helpers import add_one


def comment_like_view(request, comment_id):
    comment = Comment.objects.filter(id=comment_id).first()
    comment.likes += 1
    comment.save()
    return redirect("animefeed")
    # return HttpResponseRedirect(reverse("anime_post_detail", args=[post_id]))


def comment_dislike_view(request, comment_id):
    comment = Comment.objects.filter(id=comment_id).first()
    comment.dislike += 1
    comment.save()
    return redirect("animefeed")
    # return HttpResponseRedirect(reverse("anime_post_detail", args=[post_id]))


# def comment_likes(request, pk):
#     add_one(pk, Comment)
#     return redirect(request.META.get("HTTP_REFERER"))


# def comment_form_view(request, post_id):
#     post = get_object_or_404(AnimePost, id=post_id)
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             comment = form.save(commit=False)
#             comment.post = post
#             comment.commenter = request.user
#             comment.save()
#             return redirect("post", post.id)
#     else:
#         form = CommentForm()
#     return render(request, "comment_form.html", {"form": form})


# def del_comment(request, pk):
#     comment = Comment.objects.filter(pk=pk).first()
#     if request.user.id == comment.author.id or request.user.id == comment.post.anime_user.id:
#         comment.delete()
#         return redirect('post', comment.post.id)
#     else:
#         return HttpResponseForbidden("You do not have permission to delete this comment")


# def edit_comment(request, pk):
#     comment = get_object_or_404(Comment, pk=pk)
#     if request.user.id == comment.author.id:
#         if request.method == "POST":
#             form = CommentForm(request.POST, instance=comment)
#             if form.is_valid():
#                 data = form.cleaned_data
#                 comment.content = data.get('content')
#                 comment.save()
#                 return redirect('post', comment.post.id)
#         else:
#             form = CommentForm(instance=comment)
#         return render(request, 'comment_form.html', {'form': form})
#     else:
#         return HttpResponseForbidden("You do not have permission to edit this comment")
