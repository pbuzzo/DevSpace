from django import forms
from resumeapp.models import (Resume, Education, Employment, References, Details)

class ResumeForm(forms.ModelForm):
    
    class Meta:
        model = Resume
        fields = (
            'name',
            'city',
            'state',
            'country',
            'phone',
            'email',
            'summary',
            'skills',
            # 'education',
            # 'employment',
            # 'references'
            )


class EducationForm(forms.ModelForm):
    
    class Meta:
        model = Education
        fields = (
            'resume',
            'school',
            'start_date',
            'end_date',
            'details'
        )


class EmploymentForm(forms.ModelForm):
    
    class Meta:
        model = Employment
        fields = (
            'resume',
            'organization',
            'city',
            'state',
            'role',
            'department',
            'start_date',
            'end_date',
            'details'
        )


class ReferencesForm(forms.ModelForm):
    
    class Meta:
        model = References
        fields = (
            'resume',
            'name',
            'role',
            'organization',
            'phone',
            'email'
        )


class DetailsForm(forms.ModelForm):
    
    class Meta:
        model = Details
        fields = (
            'details',
        )


class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
