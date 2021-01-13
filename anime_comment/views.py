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
    return HttpResponseRedirect(f"/postdetail/{comment.anime_post.id}/")


def comment_dislike_view(request, comment_id):
    comment = Comment.objects.filter(id=comment_id).first()
    comment.dislike += 1
    comment.save()
    return HttpResponseRedirect(f"/postdetail/{comment.anime_post.id}/")


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


def delete_comment_view(request, comment_id):
    comment = Comment.objects.filter(id=comment_id).first()
    if (
        request.user.id == comment.author.id
        or request.user.id == comment.post.anime_user.id
    ):
        comment.delete()
        return HttpResponseRedirect(f"/postdetail/{comment.anime_post.id}/")
    else:
        return HttpResponseForbidden(
            "You do not have permission to delete this comment"
        )


def edit_comment_view(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user.id == comment.author.id:
        if request.method == "POST":
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                data = form.cleaned_data
                comment.content = data.get("content")
                comment.save()
                return HttpResponseRedirect(f"/postdetail/{comment.anime_post.id}/")
        else:
            form = CommentForm(instance=comment)
        return render(request, "comment_form.html", {"form": form})
    else:
        return HttpResponseForbidden("You do not have permission to edit this comment")


# def edit_view(request, recipe_id):
#     html = 'edit_recipe.html'
#     edit_recipe = Recipe.objects.get(id=recipe_id)
#     init_data = {
#         'title': edit_recipe.title,
#         'description': edit_recipe.description,
#         'time_required': edit_recipe.time_required,
#         'ingredients': edit_recipe.ingredients,
#         'instructions': edit_recipe.instructions,
#     }
#     if request.user is edit_recipe.author.id or request.user.is_staff:
#         if request.method == 'POST':
#             form = EditRecipeForm(request.POST)
#             if form.is_valid():
#                 data = form.cleaned_data
#                 edit_recipe.title = form.data['title']
#                 edit_recipe.description = form.data['description']
#                 edit_recipe.time_required = form.data['time_required']
#                 edit_recipe.ingredients = form.data['ingredients']
#                 edit_recipe.instructions = form.data['instructions']
#                 edit_recipe.save()
#                 return HttpResponseRedirect(reverse('Homepage'))
#     form = EditRecipeForm(initial=init_data)
#     display_context = {'form': form}
#     return render(request, html, display_context)
