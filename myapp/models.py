from django.db import models
# Create your models here.


class Student(models.Model): 
    name=models.CharField(max_length=50,default=None)
    dob=models.DateField(default=None)
    age = models.CharField(max_length=200,null=True)
    contact=models.BigIntegerField(default=None)
    marks=models.CharField(max_length=200,null=True)
    password=models.CharField(max_length=50,default=None)
    profile_pic=models.CharField(max_length=50,blank=True)

class Admin(models.Model):
    name=models.CharField(max_length=50,default=None)
    dob=models.DateField(default=None)
    age = models.CharField(max_length=200,null=True)
    contact=models.BigIntegerField(default=None)
    password=models.CharField(max_length=50,default=None)
    profile_pic=models.CharField(max_length=50,blank=True)

class staff(models.Model): 
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    contact=models.IntegerField()
class Questions(models.Model): 
    question=models.CharField(max_length=1000)
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=50)
    option3=models.CharField(max_length=50)
    option4=models.CharField(max_length=50)
    answer=models.CharField(max_length=50)
class UserReg(models.Model): 
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    dob=models.DateField()
    
class login(models.Model): 
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    userid=models.ForeignKey(UserReg,on_delete=models.CASCADE)
class demoReg(models.Model): 
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    contact_no=models.BigIntegerField()


    


