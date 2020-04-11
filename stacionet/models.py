from django.db import models

# Create your models here.

class Stacionet(models.Model):
    stacion_id = models.CharField(max_length=100)

class Linjat(models.Model):
    stacion = models.ForeignKey(Stacionet, on_delete=models.CASCADE)
    linja_name = models.CharField(max_length=100)