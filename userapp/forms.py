from django import forms

class SignInForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    display_name = forms.CharField(max_length=40)
    github_link = forms.URLField(max_length=200, required=False)
