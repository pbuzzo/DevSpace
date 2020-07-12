from django import forms

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
            'education',
            'skills',
            'employment',
            'references'
            )


class EducationForm(forms.ModelForm):
    
    class Meta:
        model = Education
        fields = (
            'school',
            'start_date',
            'end_date',
            'details'
        )


class EmploymentForm(forms.ModelForm):
    
    class Meta:
        model = Employment
        fields = (
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
            'details'
        )
