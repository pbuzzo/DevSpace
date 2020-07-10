from django.db import models
from django.utils import timezone
<<<<<<< HEAD
from postapp.models import Post
from userapp.models import Developer
 
=======
from userapp.models import Developer
from postapp.models import Post

>>>>>>> ac90dc9d23858638dd7c22070265aa4afe876142
# Create your models here.
class Notifications(models.Model):
    data_created = models.ForeignKey(Post, on_delete=models.CASCADE)
    to_user = models.ForeignKey(Developer, on_delete=models.CASCADE)
    from_user = models.BooleanField(default=False)
