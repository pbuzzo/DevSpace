from django.db import models
from django.utils import timezone
 
# Create your models here.
class Notifications(models.Model):
    data_created = models.ForeignKey(Post, on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, on_delete=models.CASCADE)
    from_user = models.BooleanField(default=False)
