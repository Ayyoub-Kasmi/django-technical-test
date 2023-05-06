from django.urls import path 
from .views import send_email

urlpatterns = [
    path('email/send', send_email),
]