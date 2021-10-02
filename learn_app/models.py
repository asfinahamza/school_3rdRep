from django.db import models

class Registration(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    contact=models.BigIntegerField()
    dob=models.DateField()

# Create your models here.
