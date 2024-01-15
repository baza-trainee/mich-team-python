from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import EmailSubscribers


def email_sender(request):
    """
        View for sending emails to subscribers.

        This view handles POST requests containing a 'message' and 'name' in the request body.
        It retrieves the list of email subscribers and sends the provided message to each subscriber.

        The email is sent using Django's send_mail function.

        Args:
            request (django.http.HttpRequest): The incoming HTTP request.

        Returns:
            django.shortcuts.render: The rendered HTML response.

        Example:
        ```
        POST /email_sender/
        {
            "message": "Hello Subscribers!",
            "name": "Admin"
        }
        ```
        """
    if request.method == 'POST':
        message = request.POST['message']
        name = request.POST['name']

        subscribers = EmailSubscribers.objects.all()

        for subscriber in subscribers:
            send_mail(name, message, settings.EMAIL_HOST_USER, [subscriber.email], fail_silently=False)

    return render(request, 'subscribers/email_sender.html')
