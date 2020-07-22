from django.shortcuts import render, reverse, HttpResponseRedirect, get_object_or_404
from postapp.models import Post
from messagesapp.models import Comment
from userapp.models import Developer
from notificationsapp.models import Notifications
from django.views.generic import View
from messagesapp.forms import CommentAddForm
from django.contrib.auth.decorators import login_required



class GetCommentsView(View):
    def get(self, request, id):
        html = 'index.html'
        # grab post by ID
        post = Post.objects.get(id=id)
        # grab all comments by specified post
        comments = Comment.objects.filter(post=post)

        return render(
            request,
            html,
            {"post": post, "comments": comments}
        )


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
                # Create comment
                Comment.objects.create(
                    text=data['text'],
                    timestamp=data['timestamp'],
                    author=request.user,
                    parent_comment=Post.objects.get(id=id),
                )
                # Create notif. when comment is created
                parent_post = Post.objects.get(id=id)
                Notifications.objects.create(
                    data_created = Comment.objects.get(text=data['text']),
                    to_user = parent_post.author
                )

            return HttpResponseRedirect(reverse("home"))

        return HttpResponseRedirect(reverse("home"))
