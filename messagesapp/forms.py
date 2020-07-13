from messagesapp.models import Comment
from django import forms


class CommentAddForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'author', 'timestamp', 'parent_comment']
