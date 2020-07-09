from django.shortcuts import render, reverse, HttpResponseRedirect
from postapp.models import Post
from messagesapp.models import Comment
from django.views.generic import View
from messagesapp.forms import CommentAddForm


# view to grab all comments for a specific post based on post ID
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
class AddCommentView(View):
    def get(self, request):
        html = 'comment_form.html'
        form = CommentAddForm()
        return render(request, html, {'form': form})

    def post(self, request, id):
        form = CommentAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Comment.objects.create(
                text=data['text'],
                timestamp=data['timestamp'],
                author=request.user,
                post=Post.objects.get(id=id),
            )
        return HttpResponseRedirect(reverse("homepage"))
