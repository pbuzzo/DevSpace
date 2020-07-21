from django.db import models
from django.contrib.auth.models import AbstractUser

class Developer(AbstractUser):
    display_name = models.CharField(max_length=50, null=True, blank=True)
    headshot = models.ImageField(blank=True, upload_to='media/headshots/')
    github_link = models.URLField(max_length=200, null=True, blank=True)
    bio = models.TextField(max_length=1000)

    REQUIRED_FIELDS = ['display_name', 'headshot', 'github_link', 'bio']

    def __str__(self):
        return self.display_name
