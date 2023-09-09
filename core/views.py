from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
# Create your views here.


def send_test_email(request):
    subject = 'Test Email'
    message = 'This is a test email sent from Django.'
    from_email = 'nagesohailehesa@gmail.com'
    recipient_list = ['nagesoh21@gmail.com']

    send_mail(subject, message, from_email, recipient_list)

    return HttpResponse('Test email sent successfully!')