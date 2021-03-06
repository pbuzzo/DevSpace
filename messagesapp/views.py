from django.shortcuts import render, reverse, HttpResponseRedirect, get_object_or_404
from postapp.models import Post
from messagesapp.models import Comment
from userapp.models import Developer
from django.views.generic import View
from messagesapp.forms import CommentAddForm
from django.contrib.auth.decorators import login_required



# view to grab all comments for a specific post based on post ID
# @login_required
class GetCommentsView(View):
    def get(self, request, id):
        html = 'index.html'
        post = Post.objects.get(id=id)
        comments = Comment.objects.filter(post=post)

        return render(
            request,
            html,
            {"post": post, "comments": comments}
        )


# view to add comment based on post ID
# @login_required --> fix here: https://bit.ly/2OwJaZk
class AddComment(View):
    def get(self, request, id):
        html = 'comment_form.html'
        form = CommentAddForm()
        post = Post.objects.get(id=id)
        return render(request, html, {'form': form, "post": post})

    def post(self, request, id):
        form = CommentAddForm(request.POST)
        current_user = Developer.objects.get(id=request.user.id)
        if request.user.is_authenticated:
            if form.is_valid():
                data = form.cleaned_data
                Comment.objects.create(
                    text=data['text'],
                    timestamp=data['timestamp'],
                    author=request.user,
                    parent_comment=Post.objects.get(id=id),
                )
                # current_user.followers.add(Developer.objects.get(id=id))
                # current_user.save()

            return HttpResponseRedirect(reverse("home"))

        return HttpResponseRedirect(reverse("home"))
