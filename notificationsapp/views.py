from django.shortcuts import render, HttpResponseRedirect
from notificationsapp.models import Notifications
from userapp.models import Developer
from messagesapp.forms import CommentAddForm
from django.contrib.auth.models import User
import re

# Create your views here.
def create_notification(request):
    if request.method == 'POST':
        form = CommentAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            text = data.get('text')
            if "@" in text:
                notified_users = re.findall(r"@(\w+)", text)
                if notified_users:
                    for notified_user in notified_users:
                        recipient_user = User.objects.get(
                            username=notified_user)
                        Notifications.objects.create(
                            data_created = new_data,
                            to_user = Developer.objects.get(
                                user=recipient_user))
                return HttpResponseRedirect('home')


def get_notifications(request):
    html= notifications.htm
    user= Developer.objects.get(user=request.user)
    notification = Notifications.objects.filter(to_user=user, from_user=False)
    notifications_count=len(notification)
    for pings in notification:
        pings.from_user = True
        pings.save()

    return render(request, html, {'user': user, 'notification':notification})
