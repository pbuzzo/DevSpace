from django.shortcuts import render, reverse, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from userapp.models import Developer
from resumeapp.models import Resume, Education, Employment, References, Details
from resumeapp.forms import ResumeForm, EducationForm, EmploymentForm, ReferencesForm, DetailsForm


def resume(request, username):
    data = Developer.objects.get(username=username)
    resume = Resume.objects.filter(author=request.user).first()
    #print(resume)
    return render(request, 'resume.html', {'data': data, 'resume': resume })


@login_required
def addresume(request):
    html = 'resume_form.html'
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Resume.objects.create(
                author=request.user,
                title=data['title'],
                name=data['name'],
                city=data['city'],
                state=data['state'],
                country=data['country'],
                phone=data['phone'],
                email=data['email'],
                summary=data['summary'],
                skills=data['skills'],
            )
            form.save()
            return HttpResponseRedirect(reverse('resume', kwargs={'username': request.user.username}))
        return HttpResponse(f'Please return to the form and fix the following errors: {form.errors}')
    
    form = ResumeForm()
    return render(request, html, {'form': form})


@login_required
def addeducation(request):
    html = 'resume_form.html'
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Education.objects.create(
                resume=data['resume'],
                school=data['school'],
                start_date=data['start_date'],
                end_date=data['end_date'],
            )
            return HttpResponseRedirect(reverse('resume',kwargs={'username': request.user.username}))
        return HttpResponse(f'Please return to the form and fix the following errors: {form.errors}')

    form = EducationForm()
    return render(request, html, {'form': form})


@login_required
def addemployment(request):
    html = 'resume_form.html'
    if request.method == 'POST':
        form = EmploymentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Employment.objects.create(
                resume=data['resume'],
                organization=data['organization'],
                city=data['city'],
                state=data['state'],
                role=data['role'],
                department=data['department'],
                start_date=data['start_date'],
                end_date=data['end_date'],
            )
            return HttpResponseRedirect(reverse('resume',kwargs={'username': request.user.username}))
        return HttpResponse(f'Please return to the form and fix the following errors: {form.errors}')

    form = EmploymentForm()
    return render(request, html, {'form': form})


@login_required
def addreferences(request):
    html = 'resume_form.html'
    if request.method == 'POST':
        form = ReferencesForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            References.objects.create(
                resume=data['resume'],
                name=data['name'],
                role=data['role'],
                organization=data['organization'],
                phone=data['phone'],
                email=data['email']
            )
            return HttpResponseRedirect(reverse('resume',kwargs={'username': request.user.username}))
        return HttpResponse(f'Please return to the form and fix the following errors: {form.errors}')

    form = ReferencesForm()
    return render(request, html, {'form': form})


@login_required
def adddetails(request):
    html = 'resume_form.html'
    if request.method == 'POST':
        form = DetailsForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Details.objects.create(
                details=data['details'],
                education=data['education'],
                employment=data['employment'],
            )
            return HttpResponseRedirect(reverse('resume',kwargs={'username': request.user.username}))
        return HttpResponse(f'Please return to the form and fix the following errors: {form.errors}')
    
    form = DetailsForm()
    return render(request, html, {'form': form})
