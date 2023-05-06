# from django.shortcuts import render
# from .serializers import UserSerializer, EmailSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, JsonResponse
import json
from django.core.mail import EmailMessage, get_connection # EmailMessage creates the message, get_connection instanciates teh backend
from django.conf import settings #to access the smtp settings

# Create your views here.
@api_view(['POST'])
def send_email(request):
    # print("Request")
    # print(request.data.get('email'))
    
    data = json.loads(request.body)

    print("=============================")
    try:
        with get_connection(  
            host=settings.EMAIL_HOST, 
            port=settings.EMAIL_PORT,  
            username=settings.EMAIL_HOST_USER, 
            password=settings.EMAIL_HOST_PASSWORD, 
            use_tls=settings.EMAIL_USE_TLS  
        ) as connection:
            subject = "[Question / Comment]"
            email_from = recipient = settings.EMAIL_HOST_USER #Sending the message to myself

            message = f'''Email triggered by: {data.get('email')}
nom: {data.get('nom')}
prenom: {data.get('prenom')}
phone: {data.get('phone')}
message: {data.get('message')}
'''

            # EmailMessage(subject, message, email_from, [recipient], connection=connection).send()  
            EmailMessage(subject, message, email_from, [recipient], connection=connection).send()  

            return JsonResponse({'message': "Email sent successfully"}, status=200)
        
    except Exception as e:
        return JsonResponse({'message': 'Server Error'}, status=400) 
