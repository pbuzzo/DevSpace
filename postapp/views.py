from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, get_object_or_404
from messagesapp.models import Comment
from postapp.forms import AddPostForm, EditPostForm
from postapp.models import Post
from django.http import HttpResponseRedirect


# Create your views here.
@login_required
def addpost(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    return render(request, 'generic_form.html', {'form': form})


def post(request, id):
    post = get_object_or_404(Post, pk=id)
    comments = Comment.objects.filter(parent_comment=post)
    return render(request, 'post.html', {'post': post, 'comments': comments})


@login_required
def post_edit(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        form = EditPostForm(request.POST, instance=post)
        form.save()
        return HttpResponseRedirect(reverse('post', args=(id,)))

    form = EditPostForm(instance=post)
    return render(request, 'generic_form.html', {'form': form})

def up_vote(request, post_id):
    post = Post.objects.get(id=post_id)
    post.up_vote += 1
    post.save()
    return HttpResponseRedirect(reverse('post', args=(post_id,)))