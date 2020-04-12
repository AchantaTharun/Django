from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html')
def email(request):
    subject = request.GET['sub']
    message = request.GET['message']
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [request.GET['to'],]
    send_mail( subject, message, email_from, recipient_list )
    data="success"
    return HttpResponse(data)