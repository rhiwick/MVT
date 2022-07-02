import email
from django.db import models

# Create your models here.

class Familiares(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=40)
    nacimiento = models.DateField(null=True)
    edad = models.IntegerField()
    email = models.EmailField()
 
