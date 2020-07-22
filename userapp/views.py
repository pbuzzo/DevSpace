from django.shortcuts import render, reverse, HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import View

from userapp.models import Developer
from userapp.forms import SignInForm, SignUpForm, EditUserForm
from postapp.models import Post


class IndexView(View):
    def get(self, request):
        html = 'index.html'
        info = Developer.objects.all()
        posts = Post.objects.filter(author=request.user.id)

        return render(
            request,
            html,
            {'info': info}
        )

class DeveloperView(View):
    def get(self, request, id):
        html = 'developer.html'
        dev_info = Developer.objects.get(id=id)
        posts = Post.objects.filter(author=dev_info)

        return render(
            request,
            html,
            {'dev_info': dev_info, 'posts': posts}
        )

class FourView(View):
    def get(self, request):
        html = '404.html'
        return render(request, html)

class FiveView(View):
    def get(self, request):
        html = '500.html'
        return render(request, html)

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


@login_required
def edit_user(request, id):
    htm = 'generic_form_user.html'
    user = Developer.objects.get(id=id)
    if request.method == 'POST':
        form = EditUserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('dev_page', args=(id,)))
        return HttpResponse(f'Please return to the form and fix the following errors: {form.errors}')

    form = EditUserForm()
    return render(request, htm, {'form': form})
