from django.db import models
from django.utils import timezone
# from postapp.models import Post
from userapp.models import Developer
from datetime import datetime, timedelta



class Comment(models.Model):
    text = models.CharField(max_length=200)
    author = models.ForeignKey(Developer, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=datetime.now, blank=True)
    post = models.ForeignKey(Developer, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
