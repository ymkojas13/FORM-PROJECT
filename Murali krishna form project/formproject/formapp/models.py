from django.db import models

# Create your models here.
class mode(models.Model):
    name = models.CharField(max_length=70)
    password = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    contact = models.IntegerField(max_length=70)