from django.db import models
from django.utils import timezone

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
    proj_url = models.URLField()
    screen_shot = models.ImageField()
    up_vote = models.IntegerField(default=0)
    # https://stackoverflow.com/questions/4379042/django-circular-model-import-issue
    comment = models.ManyToManyField('messagesapp.Comment', related_name='comment', blank=True)
    post_time = models.DateTimeField(default=timezone.now)