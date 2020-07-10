from django.shortcuts import render

# Create your views here.
def create_notification(request):


def get_notifications(request):
    html= 
    user=User.objects.get(user=request.user)
    notification = Notifications.objects.filter(to_user=user, from_user=False)
    for pings in notification:
        pings.from_user = True
        pings.save()

    return render(request, html, {'user': user, 'notification':notification})
