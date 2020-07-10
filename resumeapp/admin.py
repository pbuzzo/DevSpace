from django.contrib import admin
from resumeapp.models import Resume, Education, Employment, References, Details

admin.site.register(Resume, Education, Employment, References, Details)
