from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from userapp.models import Developer
from userapp.forms import SignInForm, SignUpForm
from postapp.models import Post

def index(request):
    info = Developer.objects.all()
    return render(request, 'index.html', {'info': info})


# @login_required
# def signed_in(request, username):
#     info = Developer.objects.get(username=request.user.username)
#     # post = Post.objects.get(author=username)
#     return render(request, 'signedin.html', {'info': info})


def signin(request):
    htm = 'generic_form_user.html'
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password']
                )
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            return HttpResponse(f'Please return to the form and fix the following errors: {form.errors}')

    form = SignInForm()
    return render(request, htm, {'form': form})


def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def signup(request):
    htm = 'generic_form_user.html'

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = Developer.objects.create_user(
                username=data['username'],
                password=data['password'],
                display_name=data['display_name'],
                github_link=data['github_link'],
            )
            return HttpResponseRedirect(reverse('home'))

    form = SignUpForm()
    return render(request, htm, {'form': form})
