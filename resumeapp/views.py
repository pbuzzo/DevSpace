from django.shortcuts import render,reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from resumeapp.models import Resume, Education, Employment, References, Details
from resumeapp.forms import ResumeForm, EducationForm, EmploymentForm, ReferencesForm, DetailsForm


def resume(request, id):
    data = Resume.objects.get(id=id)
    return render(request, 'resume.htm', {'data': data})


@login_required
def addresume(request):
    html = 'generic_form.htm'
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            resume = Resume.objects.create(
                name=data['name'],
                city=data['city'],
                state=data['state'],
                country=data['country'],
                phone=data['phone'],
                email=data['email'],
                summary=data['summary'],
                skills=data['skills'],
                # education=data['education'],
                # employment=data['employment'],
                # references=data['references'],
            )
            return HttpResponseRedirect(reverse('home'))
    
    form = ResumeForm()
    return render(request, html, {'form': form})


@login_required
def addeducation(request):
    html = 'generic_form.htm'
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Education.objects.create(
                resume=data['resume'],
                school=data['school'],
                start_date=data['start_date'],
                end_date=data['end_date'],
                details=data['details']
            )
            return HttpResponseRedirect(reverse('addresume'))

    form = EducationForm()
    return render(request, html, {'form': form})
