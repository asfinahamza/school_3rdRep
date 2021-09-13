from django.db import models

class Registration(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    contact=models.BigIntegerField()
    dob=models.DateField()

class AdminLoginData(models.Model):
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

class StaffRegistration(models.Model):
    registration_id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=50,default=None)
    last_name=models.CharField(max_length=50,default=None)
    email=models.CharField(max_length=50,default=None)
    contact=models.BigIntegerField(default=None)
    address=models.CharField(max_length=500,default=None)
    dob=models.DateField(default=None)
    user_name=models.CharField(max_length=50,default=None)
    password=models.CharField(max_length=50,default=None)
    profile_pic=models.CharField(max_length=50,blank=True)


class Staff(models.Model):
    registration_id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=50,default=None)
    last_name=models.CharField(max_length=50,default=None)
    email=models.CharField(max_length=50,default=None)
    contact=models.BigIntegerField(default=None)
    address=models.CharField(max_length=500,default=None)
    dob=models.DateField(default=None)
    user_name=models.CharField(max_length=50,default=None)
    password=models.CharField(max_length=50,default=None)
    profile_pic=models.CharField(max_length=50,blank=True)    

class RegectedStaff(models.Model):
    registration_id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=50,default=None)
    last_name=models.CharField(max_length=50,default=None)
    email=models.CharField(max_length=50,default=None)
    contact=models.BigIntegerField(default=None)
    address=models.CharField(max_length=500,default=None)
    dob=models.DateField(default=None)
    user_name=models.CharField(max_length=50,default=None)
    password=models.CharField(max_length=50,default=None)
    profile_pic=models.CharField(max_length=50,blank=True)   




class StudentRegistration(models.Model):
    registration_id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=50,default=None)
    last_name=models.CharField(max_length=50,default=None)
    classes=models.CharField(max_length=50,default=None)
    contact=models.BigIntegerField(default=None)
    address=models.CharField(max_length=500,default=None)
    dob=models.DateField(default=None)
    user_name=models.CharField(max_length=50,default=None)
    password=models.CharField(max_length=50,default=None)
    profile_pic=models.CharField(max_length=50,blank=True)

class Students(models.Model):
    registration_id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=50,default=None)
    last_name=models.CharField(max_length=50,default=None)
    classes=models.CharField(max_length=50,default=None)
    contact=models.BigIntegerField(default=None)
    address=models.CharField(max_length=500,default=None)
    dob=models.DateField(default=None)
    user_name=models.CharField(max_length=50,default=None)
    password=models.CharField(max_length=50,default=None)
    profile_pic=models.CharField(max_length=50,blank=True)

class DeclinedStudentDetails(models.Model):
    registration_id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=50,default=None)
    last_name=models.CharField(max_length=50,default=None)
    classes=models.CharField(max_length=50,default=None)
    contact=models.BigIntegerField(default=None)
    address=models.CharField(max_length=500,default=None)
    dob=models.DateField(default=None)
    user_name=models.CharField(max_length=50,default=None)
    password=models.CharField(max_length=50,default=None)
    profile_pic=models.CharField(max_length=50,blank=True)

class Teachers(models.Model):
    registration_id=models.BigIntegerField()
    email=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    contact=models.BigIntegerField()

class Classes(models.Model):
    classes=models.CharField(max_length=50)


class AddedClasses(models.Model):
    classes=models.CharField(max_length=50)

class Subjects(models.Model):
    subject=models.CharField(max_length=50)


class AddedSubjects(models.Model):
    subject=models.CharField(max_length=50)
    classes=models.ForeignKey(AddedClasses,on_delete=models.CASCADE)
    teacher=models.ForeignKey(Staff,on_delete=models.CASCADE)

class ClassTeacher(models.Model):
    classes=models.ForeignKey(AddedClasses,on_delete=models.CASCADE)
    teacher=models.ForeignKey(Staff,on_delete=models.CASCADE)

class Chapter(models.Model):
    chapter=models.CharField(max_length=50,default=None)
    classes=models.ForeignKey(AddedClasses,on_delete=models.CASCADE)
    subject=models.ForeignKey(AddedSubjects,on_delete=models.CASCADE)

class Topic(models.Model):
    chapter=models.ForeignKey(Chapter,on_delete=models.CASCADE)
    classes=models.ForeignKey(AddedClasses,on_delete=models.CASCADE)
    subject=models.ForeignKey(AddedSubjects,on_delete=models.CASCADE)
    topic_name=models.CharField(max_length=50,default=None)
    topic_file=models.CharField(max_length=50,blank=True)
   

class FileUpload(models.Model):
    name=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    pic=models.CharField(max_length=50)
    
class FormAj(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    place=models.CharField(max_length=50)



# Create your models here.
