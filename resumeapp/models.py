from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Resume(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=15)
    country = models.CharField(max_length=3)
    phone = PhoneNumberField()
    email = models.EmailField(max_length=254)
    summary = models.TextField(max_length=1000)
    school = models.CharField(max_length=75)
    school_start = models.DateField(auto_now=False, auto_now_add=False)
    school_end = models.DateField(auto_now=False, auto_now_add=False)
    skills = models.TextField(max_length=1000)
    organization = models.TextField(max_length=100)
    org_city = models.CharField(max_length=50)
    org_state = models.CharField(max_length=15)
    job_title = models.CharField(max_length=75)
    department = models.CharField(max_length=75)
    job_start = models.DateField(auto_now=False, auto_now_add=False)
    job_end = models.DateField(auto_now=False, auto_now_add=False)
    about_list = models.TextField(max_length=100)
    ref_name = models.CharField(max_length=50)
    ref_job_title = models.CharField(max_length=75)
    ref_organization = models.TextField(max_length=100)
    ref_phone = PhoneNumberField()
    ref_email = models.EmailField(max_length=254)

    def __str__(self):
        return self.name
    