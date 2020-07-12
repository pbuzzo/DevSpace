from django.shortcuts import render, reverse, HttpResponseRedirect
from postapp.models import Post
from messagesapp.models import Comment
from userapp.models import Developer
from django.views.generic import View
from messagesapp.forms import CommentAddForm
from django.contrib.auth.mixins import LoginRequiredMixin



# view to grab all comments for a specific post based on post ID
class GetCommentsView(LoginRequiredMixin, View):
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
class AddCommentView(LoginRequiredMixin, View):
    def get(self, request):
        html = 'comment_form.html'
        form = CommentAddForm()
        return render(request, html, {'form': form})

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
                    post=Post.objects.get(id=id),
                )
                current_user.followers.add(Developer.objects.get(id=id))
                current_user.save()

            return HttpResponseRedirect(reverse("homepage"))

        return HttpResponseRedirect(reverse("homepage"))
