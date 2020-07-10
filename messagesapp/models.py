from django.db import models
<<<<<<< HEAD
from postapp.models import Post
=======
>>>>>>> d90d55acece211b2ecd8a22a808b8020d162a014
from userapp.models import Developer
from datetime import datetime


class Comment(models.Model):
    text = models.CharField(max_length=200)
    author = models.ForeignKey(Developer, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=datetime.now, blank=True)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE)

    class Meta:
        ordering = ['text']

    def __str__(self):
        return self.text
