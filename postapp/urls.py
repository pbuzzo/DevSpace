from django.conf.urls import url

from postapp import views

urlpatterns = [
    path('add_project.html', views.addpost, name='addpost'),
    path('project/<int:id>', views.post, name='post'),
    path('edit_project/<int:id>', views.post_edit, name='edit_project'),

    
]
