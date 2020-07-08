from django.db import models
from django.utils import timezone
 
# Create your models here.
class Notifications(models.Model):
    data_created = models.DateTimeField(default=timezone.now)
    to_user = models.BooleanField(default=False)
    from_user = models.BooleanField(default=False)