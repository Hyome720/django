from django.db import models
from django.forms import CharField, DateTimeField, IntegerField

# Create your models here.

class articleModel(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
