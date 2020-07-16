from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from userapp.models import Developer


class Resume(models.Model):
    author = models.ForeignKey(Developer, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=15)
    country = models.CharField(max_length=3)
    phone = PhoneNumberField()
    email = models.EmailField(max_length=254)
    summary = models.TextField(max_length=1000)
    skills = models.TextField(max_length=1000, blank=True)
   
    def __str__(self):
        return self.title


class Education(models.Model):
    resume = models.ForeignKey('Resume', on_delete=models.CASCADE)
    school = models.CharField(max_length=75)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    details = models.ForeignKey('Details', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.school


class Employment(models.Model):
    resume = models.ForeignKey('Resume', on_delete=models.CASCADE)
    organization = models.TextField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=15)
    role = models.CharField(max_length=75)
    department = models.CharField(max_length=75)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    details = models.ForeignKey('Details', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.organization


class References(models.Model):
    resume = models.ForeignKey('Resume', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=75, blank=True)
    organization = models.TextField(max_length=100, blank=True)
    phone = PhoneNumberField()
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.name


class Details(models.Model):
    details = models.TextField(max_length=100)

    def __str__(self):
        return self.details
