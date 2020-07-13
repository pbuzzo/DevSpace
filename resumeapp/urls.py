from django.urls import path
from resumeapp import views

urlpatterns = [
    path('resume/<int:id>/', views.resume, name='resume'),
    path('resume/add/', views.addresume, name='addresume'),
    # path('resume/<int:id>/', views.resume, name='resume'),
    # path('resume/<int:id>/', views.resume, name='resume'),
    # path('resume/<int:id>/', views.resume, name='resume'),
    # path('resume/<int:id>/', views.resume, name='resume'),
    # path('resume/<int:id>/', views.resume, name='resume'),
    # path('resume/<int:id>/', views.resume, name='resume'),
    # path('resume/<int:id>/', views.resume, name='resume'),
    # path('resume/<int:id>/', views.resume, name='resume'),
    # path('resume/<int:id>/', views.resume, name='resume'),
]