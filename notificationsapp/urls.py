from django.urls import path
from notificationsapp import views

urlpatterns = [
    path('notifications/', get_notifications, name='notify')
]
