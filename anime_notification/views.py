from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from anime_notification.models import Notification
import copy
# referenced article : https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/
# Create your views here.


@login_required
def notification_view(request):
    notifications = Notification.objects.filter(notify=request.user.id)
    count = notifications.count()
    notifications_holder = copy.copy(notifications)
    Notification.objects.filter(notify=request.user.id).delete()
    return render(request, 'notifications.html',{'notifications': notifications_holder,
                                                 'count': count,
    })
