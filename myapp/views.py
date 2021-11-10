from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from random import random
from django.core.files.storage import FileSystemStorage
from datetime import date


def func(request):
    return render(request,'welcome.html')

def index(request):
    user_id=request.session['id']
    user_data=admin.objects.get(id=user_id)
    return render(request,'index.html',{'user':user_data})

def adminDB(request):
    return render(request,'adminDash.html') 

def adminRegFunc(request):
    if(request.method == 'POST'):
        name=request.POST['name1']
        dob=request.POST['dob1']
        contact=request.POST['contact1']
        pswd=request.POST['password1']
        profile_pic=request.FILES['profPic']
        filename=str(random())+profile_pic.name
        # print(filename)
        photo=FileSystemStorage()
        photo.save(filename,profile_pic)
        today=date.today()
        byear=int(dob[0:4])
        bmonth=int(dob[5:7])
        bday=int(dob[8:])
        print(bday)
        print(bmonth)
        print(byear)
        age=today.year-byear-((today.month,today.day)<(bmonth,bday))
        print(age)
        adData=Admin(name=name,dob=dob,age=age,contact=contact,password=pswd,profile_pic=filename)
        adData.save()
        return redirect('adminLogin')
    return render(request,'adminReg.html')

def adminLoginFunc(request):
    if(request.method == 'POST'):
        username=request.POST['name']
        password=request.POST['password1']
        try:
            user=Admin.objects.get(name=username)
            if(user.name==username and user.password==password):
                request.session['id']=user.id
                return redirect('adminDB')
            else:
                return render(request,'adminLogin.html',{'message':'Login failed'})
        except Admin.DoesNotExist:
            return render(request,'adminLogin.html',{'message':'Login failed'})
    return render(request,'adminLogin.html')

def studentRegFunc(request):
    if(request.method == 'POST'):
        name=request.POST['name1']
        dob=request.POST['dob1']
        contact=request.POST['contact1']
        pswd=request.POST['password1']
        profile_pic=request.FILES['profPic']
        filename=str(random())+profile_pic.name
        # print(filename)
        photo=FileSystemStorage()
        photo.save(filename,profile_pic)
        today=date.today()
        byear=int(dob[0:4])
        bmonth=int(dob[5:7])
        bday=int(dob[8:])
        print(bday)
        print(bmonth)
        print(byear)
        age=today.year-byear-((today.month,today.day)<(bmonth,bday))
        print(age)
        stData=Student(name=name,dob=dob,age=age,contact=contact,password=pswd,profile_pic=filename)
        stData.save()
        return redirect('studentLogin')
    return render(request,'studentReg.html')

def studentLoginFunc(request):
    if(request.method == 'POST'):
        username=request.POST['name']
        password=request.POST['password1']
        try:
            user=Student.objects.get(name=username)
            if(user.name==username and user.password==password):
                request.session['id']=user.id
                return redirect('studentDB')
            else:
                return render(request,'studentLogin.html',{'message':'Login failed'})
        except Student.DoesNotExist:
            return render(request,'studentLogin.html',{'message':'Login failed'})
    return render(request,'studentLogin.html')

def studentDB(request):
    user_id=request.session['id']
    user_data=Student.objects.get(id=user_id)
    return render(request,'studentDash.html',{'data':user_data})

def studentProfileFn(request):
    user_id=request.session['id']
    user_data=Student.objects.get(id=user_id)
    return render(request,'studentProfile.html',{'data':user_data})

def updatestudentProfileFn(request):
    user_id=request.session['id']
    user_data=Student.objects.get(id=user_id)
    if(request.method == 'POST'):
        name=request.POST['name1']
        dob=request.POST['dob1']
        contact=request.POST['contact1']
        pswd=request.POST['password1']
        profile_pic=request.FILES['profPic']
        filename=str(random())+profile_pic.name
        # print(filename)
        photo=FileSystemStorage()
        photo.save(filename,profile_pic)
        today=date.today()
        byear=int(dob[0:4])
        bmonth=int(dob[5:7])
        bday=int(dob[8:])
        print(bday)
        print(bmonth)
        print(byear)
        age=today.year-byear-((today.month,today.day)<(bmonth,bday))
        print(age)
        Student.objects.filter(id=user_id).update(name=name,dob=dob,age=age,contact=contact,password=pswd,profile_pic=filename)
        return redirect('studentProfile')
    return render(request,'stProfileUpdate.html',{'data':user_data})

def adminDB(request):
    user_id=request.session['id']
    user_data=Admin.objects.get(id=user_id)
    students=Student.objects.all()
    return render(request,'adminDash.html',{'data':students,'user':user_data}) 

def studentDetailsFn(request,id):
    if(request.method == 'POST'):
        marks=request.POST['mark']
        Student.objects.filter(id=id).update(marks=marks)
        return redirect('adminDB')
    user_id=request.session['id']
    user_data=Admin.objects.get(id=user_id)
    content=Student.objects.get(id=id)
    return render(request,'studentDetails.html',{'student':content,'user':user_data}) 

def adminLogoutFun(request):
    del request.session['id']
    return redirect('adminLogin')

def studentLogoutFun(request):
    del request.session['id']
    return redirect('studentLogin')





# Create your views here.
