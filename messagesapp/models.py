from django.db import models

from postapp.models import Post
from userapp.models import Developer
from datetime import datetime


class Comment(models.Model):
    text = models.CharField(max_length=200)
    author = models.ForeignKey(Developer, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=datetime.now, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        ordering = ['text']

    def __str__(self):
        return self.text
