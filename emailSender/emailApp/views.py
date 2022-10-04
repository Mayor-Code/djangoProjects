from django.shortcuts import render, redirect
from django.core.mail import send_mail


def sendEmail(request):
    sender = request.POST['sender']
    recipient = request.POST['recipient']
    subject = request.POST['subject']
    content = request.POST['content']

    send_mail(subject, content, sender, [recipient, ], fail_silently=False)
    return redirect('/')
# Create your views here.
