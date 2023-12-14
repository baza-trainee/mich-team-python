from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import EmailSubscribers

def email_sender(request):
    if request.method == 'POST':
        message = request.POST['message']
        name = request.POST['name']

        subscribers = EmailSubscribers.objects.all()

        for subscriber in subscribers:
            send_mail(name, message, settings.EMAIL_HOST_USER, [subscriber.email], fail_silently=False)

    return render(request, 'subscribers/email_sender.html')
