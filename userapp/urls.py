from django.urls import path
from userapp import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('developer/<int:id>', views.DeveloperView.as_view(), name='dev_page'),
    path('signin/', views.signin),
    path('signup/', views.signup),
    path('signout/', views.signout),
    # path('<str:username>/', views.signed_in, name='signed_in'),
]