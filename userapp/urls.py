from django.urls import path
from userapp import views

urlpatterns = [
    path('', views.index, name='home'),
    path('signin/', views.signin),
    path('signup/', views.signup),
    path('signout/', views.signout),
]