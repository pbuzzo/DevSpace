from django.db import models
from django.utils import timezone
from messagesapp.models import Comment

# Create your models here.
class Post(models.Model):
    html = 'h'
    javascript = 'js'
    react = 'r'
    python = 'p'
    django = 'd'

    language_choices = {
        (html, 'HTML'),
        (javascript, 'JavaScript'),
        (react, 'React'),
        (python, 'Python'),
        (django, 'Django')

    }

    post_type = models.CharField(
        max_length=10,
        choices=language_choices,
        default=html,
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    live_url = models.URLField()
    repo_url = models.URLField()
    screen_shot = models.ImageField()
    up_vote = models.IntegerField(default=0)
    comment = models.ManyToManyField(Comment, blank=True)
    post_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
