from django.urls import path
from resumeapp import views

urlpatterns = [
    path('<str:username>/resume/', views.resume, name='resume'),
    path('resume/add/', views.addresume, name='addresume'),
    path('resume/add/education/', views.addeducation, name='addeducation'),
    path('resume/add/employment/', views.addemployment, name='addemployment'),
    path('resume/add/references/', views.addreferences, name='addreferences'),
    path('resume/add/details/', views.adddetails, name='adddetails'),
]