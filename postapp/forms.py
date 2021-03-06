from django.forms import modelform_factory
from postapp.models import Post


AddPostForm = modelform_factory(Post, exclude=['up_vote'])


EditPostForm = modelform_factory(Post, exclude=['up_vote'])