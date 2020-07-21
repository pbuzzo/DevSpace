from django import forms
from userapp.models import Developer

class SignInForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    display_name = forms.CharField(max_length=40)
    github_link = forms.URLField(max_length=200, required=False)


class EditUserForm(forms.ModelForm):
    
    class Meta:
        model = Developer
        fields = (
            'display_name',
            'headshot',
            'github_link',
            'bio',
        )

    
# class ContactForm(forms.Form):
#     name = forms.CharField()
#     message = forms.CharField(widget=forms.Textarea)

#     def send_email(self):
#         # send email using the self.cleaned_data dictionary
#         pass