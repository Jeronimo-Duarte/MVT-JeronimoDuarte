from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre= models.CharField(max_length=128)
    apellido=models.CharField(max_length=128)
    altura_cm=models.IntegerField()
    fecha_de_nacimiento=models.DateField()
