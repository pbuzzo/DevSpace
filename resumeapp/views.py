from django.shortcuts import render,reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from userapp.models import Developer
from resumeapp.models import Resume, Education, Employment, References, Details
from resumeapp.forms import ResumeForm, EducationForm, EmploymentForm, ReferencesForm, DetailsForm


def resume(request, username):
    username = request.user.username
    data = Developer.objects.get(username=username)
    return render(request, 'resume.htm', {'data': data})


@login_required
def addresume(request, id):
    data = Developer.objects.get(id=id)
    html = 'resume_form.htm'
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            resume = Resume.objects.create(
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
            resume.save()
            return HttpResponseRedirect(reverse('addeducation'))
    
    form = ResumeForm()
    return render(request, html, {'form': form})


@login_required
def addeducation(request, id):
    data = Developer.objects.get(id=id)
    html = 'resume_form.htm'
    print(Resume.title)
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Education.objects.create(
                resume=Resume.title,
                school=data['school'],
                start_date=data['start_date'],
                end_date=data['end_date'],
                details=data['details']
            )
            return HttpResponseRedirect(reverse('addresume'))

    form = EducationForm()
    return render(request, html, {'form': form})


@login_required
def addemployment(request, id):
    data = Developer.objects.get(id=id)
    html = 'resume_form.htm'
    print(Resume.title)
    if request.method == 'POST':
        form = EmploymentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Employment.objects.create(
                resume=Resume.title,
                organization=data['organization'],
                city=data['city'],
                state=data['state'],
                role=data['role'],
                department=data['department'],
                start_date=data['start_date'],
                end_date=data['end_date'],
                details=data['details']
            )
            return HttpResponseRedirect(reverse('addresume'))

    form = EmploymentForm()
    return render(request, html, {'form': form})


@login_required
def addreferences(request, id):
    data = Developer.objects.get(id=id)
    html = 'resume_form.htm'
    print(Resume.title)
    if request.method == 'POST':
        form = ReferencesForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            References.objects.create(
                resume=Resume.title,
                name=data['name'],
                role=data['role'],
                organization=data['organization'],
                phone=data['phone'],
                email=data['email']
            )
            return HttpResponseRedirect(reverse('addresume'))

    form = ReferencesForm()
    return render(request, html, {'form': form})
