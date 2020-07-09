from django.forms import modelform_factory
from postapp.models import Post

AddPostForm = modelform_factory(Post, exclude=[])

EditPostForm = modelform_factory(Post, exclude=[])