from django.urls import path
from notificationsapp import views

urlpatterns = [
    path('notifications/', views.get_notifications, name='notify')
]
