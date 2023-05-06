from django.db import models

# Create your models here.
class User(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=100)

class Email(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()