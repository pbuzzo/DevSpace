from django.urls import path
from userapp import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('developer/<int:id>', views.DeveloperView.as_view(), name='dev_page'),
    path('developer/<int:id>/edit/', views.edit_user, name='edit_user'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup),
    path('signout/', views.signout),
    path('404', views.FourView.as_view()),
    path('500', views.FiveView.as_view()),
    # path('<str:username>/', views.signed_in, name='signed_in'),
]