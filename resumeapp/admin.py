from django.contrib import admin
from resumeapp.models import Resume, Education, Employment, References, Details

admin.site.register(Resume)
admin.site.register(Education)
admin.site.register(Employment)
admin.site.register(References)
admin.site.register(Details)
