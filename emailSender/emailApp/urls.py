from django.urls import path
from .views import sendEmail

app_name = "emailApp"

urlpatterns = [
    path('sendmail/', sendEmail, name='sendemail')
]