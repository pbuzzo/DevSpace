from django.urls import path

from postapp import views

urlpatterns = [
    path('add_project/', views.addpost, name='addpost'),
    path('project/<int:id>', views.post, name='post'),
    path('edit_project/<int:id>', views.post_edit, name='post_edit'),

]
