from django.urls import path
from messagesapp import views

urlpatterns = [
    path('commentadd/<int:id>/', views.AddComment.as_view(), name="comment_add_view"),
]
