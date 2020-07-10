from django.db import models
from django.utils import timezone
from postapp.models import Post
from userapp.models import Developer
 
# Create your models here.
class Notifications(models.Model):
    data_created = models.ForeignKey(Post, on_delete=models.CASCADE)
    to_user = models.ForeignKey(Developer, on_delete=models.CASCADE)
    from_user = models.BooleanField(default=False)
