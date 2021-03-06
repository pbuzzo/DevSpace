"""capstoneproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from userapp.urls import urlpatterns as user_urls
from postapp.urls import urlpatterns as post_urls
from notificationsapp.urls import urlpatterns as notify_urls
from messagesapp.urls import urlpatterns as comment_urls
from resumeapp.urls import urlpatterns as resume_urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += user_urls
urlpatterns += post_urls
urlpatterns += resume_urls
urlpatterns += notify_urls
urlpatterns += comment_urls
