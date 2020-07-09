from django.db import models

class Resume(models.Model):
    name = models.CharField(max_length=50)
    # phone = models.PhoneNumberField()
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=1024)
    zip_code = models.CharField(max_length=12)
    city = models.CharField(max_length=1024)
    country = models.CharField(max_length=3)
    summary = models.TextField(max_length=1000)
    job_title = models.CharField(max_length=75)

    def __str__(self):
        return self.name
    