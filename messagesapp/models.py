from django.db import models
from userapp.models import Developer
from datetime import datetime
# from postapp.models import Post


class Comment(models.Model):
    text = models.CharField(max_length=200)
    author = models.ForeignKey(Developer, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=datetime.now, blank=True)
    # parent_comment = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE)

    class Meta:
        ordering = ['text']

    def __str__(self):
        return self.text
