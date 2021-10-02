from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import *
from random import random
from django.core.files.storage import FileSystemStorage
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# from school_app.forms import CustomeUserCreationForm

# Create your views here.
def regfun(request):
    print(request)
    if(request.method=='POST'):
        fname=request.POST['name1']
        lname=request.POST['name2']
        place=request.POST['place']
        email=request.POST['email']
        contact=request.POST['contact']
        dob=request.POST['dob']
        details=Registration(first_name=fname,last_name=lname,place=place,email=email,contact=contact,dob=dob)
        details.save()
        return redirect('regDetails')
    return render(request,'register.html')

def regtab(request):
    content=Registration.objects.all()
    return render(request,'regtable.html',{'key':content})

def delData(request,id):
    Registration.objects.get(id=id).delete()
    return redirect('regDetails')

def updateData(request,userid):
    content=Registration.objects.get(id=userid)
    return render(request,'updateReg.html',{'key1':content})



def saveUpdateData(request,user_id):
    if(request.method == 'POST'):
        n1=request.POST['fname']
        n2=request.POST['lname']
        pl=request.POST['place']
        em=request.POST['email']
        cnt=request.POST['contact']
        Registration.objects.filter(id=user_id).update(first_name=n1,last_name=n2,place=pl,email=em,contact=cnt)
        return redirect('regDetails')

@api_view(['GET'])
def viewAPI2fn(request):
    user_details=Registration.objects.all()
    userdata=[{'fname':x.first_name,'lname':x.last_name,'place':x.place,'mailID':x.email,'contact':x.contact,'dob':x.dob}for x in user_details]
    return JsonResponse({'data':userdata})

@api_view(['POST'])
def postAPI2fn(request):
    data=request.data
    user_details=Registration(first_name=data['fname'],last_name=data['lname'],place=data['place'],email=data['mailID'],contact=data['contact'],dob=data['dob'])
    user_details.save()
    return Response('data inserted successfully')

@api_view(['POST'])
def deleteAPI2fn(request):
    data=request.data
    Registration.objects.get(id=data['id']).delete()
    return Response('data deleted succuessfully')

@api_view(['POST'])
def updateAPI2fn(request):
    data=request.data
    Registration.objects.filter(id=data['id']).update(first_name=data['fname'],last_name=data['lname'],place=data['place'],email=data['mailID'],contact=data['contact'],dob=data['dob'])
    return Response('data updated succuessfully')

