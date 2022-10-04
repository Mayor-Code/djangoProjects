from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail


def sendEmail(request):
    sender = request.POST['sender']
    recipient = request.POST['recipient']
    subject = request.POST['subject']
    content = request.POST['content']

    send_mail(subject ,content, sender , [recipient], fail_silently=False)
# Create your views here.
