from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import *
from random import random
from django.core.files.storage import FileSystemStorage
from rest_framework.decorators import api_view
from rest_framework.response import Response
from school_app.serializers import teachers_details
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# from school_app.forms import CustomeUserCreationForm


def welcome(request):
    return render(request,'welcome.html')


def indexf(request):
    return render(request,'index.html')


def sumf(request):
    return render(request,'sum.html')


def findsum(request):
    fno = request.GET['no1']
    lno = request.GET['no2']
    sum = int(fno) + int(lno)
    return render(request,'sum.html',{'result':sum})
    return HttpResponse(sum)


def postsum(request):
    if(request.method == 'POST'):
        fno = request.POST['no1']
        lno = request.POST['no2']
        sum = int(fno) + int(lno)
        return render(request,'postsum.html',{'result':sum})

    return render(request,'postsum.html')







def adminLoginFun(request):
    if(request.method == 'POST'):
        emailID=request.POST['email1']
        password=request.POST['password1']
        try:
            user=AdminLoginData.objects.get(email=emailID)
            if(user.email==emailID and user.password==password):
                request.session['admin_id']=user.id
                return redirect('class')
            else:
                return render(request,'adminLogin.html',{'message':'Login failed'})
        except AdminLoginData.DoesNotExist:
            return render(request,'adminLogin.html',{'message':'Login failed'})
    return render(request,'adminLogin.html')

def adminLogoutFun(request):
    del request.session['admin_id']
    return redirect('adminLogin')

def classfn(request):       
    content=AddedClasses.objects.all()                            
    cl=Classes.objects.all()
    subj=Subjects.objects.all()
    teachers=Staff.objects.all()
    clTeacher=ClassTeacher.objects.all()
    subj_details=AddedSubjects.objects.select_related('classes')
    class_details=ClassTeacher.objects.select_related('teacher','classes')
    return render(request,'manage_class.html',{'key2':cl,'key3':subj,'key4':content,'teacher':teachers,'key6':subj_details,'key7':clTeacher,'key8':class_details})



def deleteClassFn(request,id):
    AddedClasses.objects.get(id=id).delete()
    return redirect('class')

def deleteSubjectFn(request,id):
    AddedSubjects.objects.get(id=id).delete()
    return redirect('class')

def deleteClassTeacherFn(request,id):
    ClassTeacher.objects.get(id=id).delete()
    return redirect('class')

def addClassFn(request):
    class_name=request.POST['classes']
    try:
        exixting_cls=AddedClasses.objects.get(classes=class_name)
        return JsonResponse({'messages':'Class already exists'})
    except AddedClasses.DoesNotExist:
        addCls=AddedClasses(classes=class_name)
        addCls.save()
        return JsonResponse({'messages':'class has been created successfully'})
    


def studentReg(request):
    if(request.method == 'POST'):
        st_fname=request.POST['name1']
        st_lname=request.POST['name2']
        st_class=request.POST['class1']
        st_contact=request.POST['contact1']
        st_address=request.POST['address1']
        st_dob=request.POST['dob1']
        st_uname=request.POST['uname']
        st_pswd=request.POST['password1']
        profile_pic=request.FILES['profPic']
        filename=str(random())+profile_pic.name
        # print(filename)
        photo=FileSystemStorage()
        photo.save(filename,profile_pic)
        stdata=Students(first_name=st_fname,last_name=st_lname,classes_id=st_class,contact=st_contact,address=st_address,dob=st_dob,user_name=st_uname,password=st_pswd,profile_pic=filename)
        stdata.save()
        return redirect('studentLogin')

    content=AddedClasses.objects.all()
    return render(request,'student_reg.html',{'class':content})



def studentLoginFn(request):
    if(request.method == 'POST'):
        username=request.POST['uname']
        password=request.POST['password1']
        try:
            user=Students.objects.get(user_name=username)
            if(user.user_name==username and user.password==password and user.status=='active'):
                request.session['student_id']=user.registration_id
                return redirect('chapters')
            else:
                return render(request,'studentLogin.html',{'message':'Login failed'})
        except Students.DoesNotExist:
            return render(request,'studentLogin.html',{'message':'Login failed'})
    return render(request,'studentLogin.html')


def stdntDashfn(request):
    user_id=request.session['student_id']
    user_data=Students.objects.get(registration_id=user_id)
    return render(request,'studentDB.html',{'datadata':user_data})




def studentProfileFn(request):
    user_id=request.session['student_id']
    user_data=Students.objects.get(registration_id=user_id)
    class_details=Students.objects.select_related('classes')
    return render(request,'studentProfile.html',{'data':user_data,'class':class_details})

##
def chapterFunction(request):
    user_id=request.session['student_id']
    # user_data=Students.objects.get(registration_id=user_id)
    classes=Students.objects.select_related('classes').get(registration_id=user_id)
    # subject=AddedSubjects.objects.filter(classes=classes)
    # topic_list=Topic.objects.filter(subject_id=)
    # subject_details=Topic.objects.select_related('classes','subject')
    
    
    return render(request,'studentChapter.html')


def studentLogout_fn(request):
    del request.session['student_id']
    return redirect('studentLogin')

 
def staffReg(request):
    if(request.method == 'POST'):
        tr_fname=request.POST['name1']
        tr_lname=request.POST['name2']
        tr_email=request.POST['email1']
        tr_contact=request.POST['contact1']
        tr_address=request.POST['address1']
        tr_dob=request.POST['dob1']
        tr_uname=request.POST['uname']
        tr_pswd=request.POST['password1']
        profile_pic=request.FILES['profPic']
        filename=str(random())+profile_pic.name
        # print(filename)
        photo=FileSystemStorage()
        photo.save(filename,profile_pic)
        trdata=Staff(first_name=tr_fname,last_name=tr_lname,email=tr_email,contact=tr_contact,address=tr_address,dob=tr_dob,user_name=tr_uname,password=tr_pswd,profile_pic=filename)
        trdata.save()
        return redirect('staffLogin')

    return render(request,'staff_reg.html')

def staffLogin(request):
    if(request.method == 'POST'):
        username=request.POST['uname']
        password=request.POST['password1']
        try:
            user=Staff.objects.get(user_name=username)
            if(user.user_name==username and user.password==password and user.status=='active'):
                request.session['registration_id']=user.registration_id
                return redirect('chapterMN')
            else:
                return render(request,'staff_login.html',{'message':'Login failed'})
        except Staff.DoesNotExist:
            return render(request,'staff_login.html',{'message':'Login failed'})

    return render(request,'staff_login.html')

def staffLogoutFn(request):
    del request.session['registration_id']
    return redirect('staffLogin')


def trdashbdFn(request):
    user_id=request.session['registration_id']
    data=Staff.objects.get(registration_id=user_id)
    return render(request,'teacherDB.html',{'userdata':data})


def staffProfileFn(request):
    user_id=request.session['registration_id']
    data=Staff.objects.get(registration_id=user_id)
    return render(request,'staffProfile.html',{'userdata':data})




def staffManage(request):
    data=Staff.objects.all()
    return render(request,'manage_staff.html',{'key':data})


def studentManage(request):
    data=Students.objects.all()
    return render(request,'manage_student.html',{'key':data})




def chapterMnFun(request):
    if(request.method == 'POST'):
        class_id=request.POST['class_name']
        subject_id=request.POST['subject_name']
        chapter_name=request.POST['chapter']
        chapter_details=chapter(chapter=chapter_name,classes_id=class_id,subject_id=subject_id)
        chapter_details.save()
        return redirect('chapterMN')
    user_id=request.session['registration_id']
    data=Staff.objects.get(registration_id=user_id)
    class_data=AddedClasses.objects.all()
    subj_details=AddedSubjects.objects.all()
    return render(request,'chapterMgmt.html',{'userdata':data,'classdetails':class_data,'subj':subj_details})

def subjectOfClassFun(request):
    class_id=request.POST['classID']
    subject_data=AddedSubjects.objects.filter(classes_id=class_id)
    subject_details=[{'id':x.id,'subject':x.subject}for x in subject_data]
    return JsonResponse({'data':subject_details})

def chapterInSubjectFun(request):
    subj_id=request.POST['subjectID']
    chapters=Chapter.objects.filter(subject_id=subj_id)
    chapter_details=[{'id':x.id,'chapter':x.chapter}for x in chapters]
    return JsonResponse({'ch_data':chapter_details})

  
def subjectsFun(request):
    user_id=request.session['student_id']
    # student=Students.objects.get(registration_id=user_id)
    # classData=Students.objects.select_related('cl')
    # classes=Students.objects.get(classes_id=student.classes_id)   
    classes=Students.objects.select_related('classes').get(registration_id=user_id)
    subjectList=AddedSubjects.objects.filter(classes_id=classes.classes.id)
    print(subjectList)
    # subjects=AddedSubjects.objects.filter(classes_id=student.)
    # subject=AddedSubjects.objects.filter(classes_id=class_id)
    return render(request,'subjects.html',{'sub':subjectList})
    # ,{'student':student,'class':classes,'subject':subject_id}

def examFunction(request):
    return render(request,'exam.html')

def questionFunction(request):
    return render(request,'question.html')

def assignmentsFunction(request):
    return render(request,'assignments.html')


def staffDetailsFunction(request,id):
    content=Staff.objects.get(registration_id=id)
    return render(request,'staffDetails.html',{'trdata':content})

def verifyStaffFunction(request,id):
    Staff.objects.filter(registration_id=id).update(status='active')
    # print(staff_data.registration_id)
    # verified_data=Staff(first_name=staff_data.first_name,last_name=staff_data.last_name,email=staff_data.email,contact=staff_data.contact,address=staff_data.address,dob=staff_data.dob,user_name=staff_data.user_name,password=staff_data.password,profile_pic=staff_data.profile_pic)
    # verified_data.save()
    # StaffRegistration.objects.get(registration_id=id).delete()
    return redirect('managestaff')

def rejectStaffFunction(request,id):
    Staff.objects.filter(registration_id=id).update(status='inactive')
    # del_data=RegectedStaff(first_name=staff_data.first_name,last_name=staff_data.last_name,email=staff_data.email,contact=staff_data.contact,address=staff_data.address,dob=staff_data.dob,user_name=staff_data.user_name,password=staff_data.password,profile_pic=staff_data.profile_pic)
    # del_data.save()
    # StaffRegistration.objects.get(registration_id=id).delete()
    return redirect('managestaff')

def studentDetailsFunction(request,id):
    content=Students.objects.get(registration_id=id)
    class_details=Students.objects.select_related('classes')
    return render(request,'studentDetails.html',{'sudent_data':content,'class_data':class_details})

def verifyStudentFunction(request,id):
    Students.objects.filter(registration_id=id).update(status='active')
    # details=Students(first_name=student_data.first_name,last_name=student_data.last_name,classes=student_data.classes,contact=student_data.contact,address=student_data.address,dob=student_data.dob,user_name=student_data.user_name,password=student_data.password,profile_pic=student_data.profile_pic)
    # details.save()
    # StudentRegistration.objects.get(registration_id=id).delete()
    return redirect('managestudent')

def declineStudentFunction(request,id):
    Students.objects.filter(registration_id=id).update(status='inactive')
    # del_data=DeclinedStudentDetails(first_name=student_data.first_name,last_name=student_data.last_name,classes=student_data.classes,contact=student_data.contact,address=student_data.address,dob=student_data.dob,user_name=student_data.user_name,password=student_data.password,profile_pic=student_data.profile_pic)
    # del_data.save()
    # StudentRegistration.objects.get(registration_id=id).delete()
    return redirect('managestudent')



        
def verifyTeacher(request,id):
    if(request.method == 'POST'):
        tr_id=request.POST['temp_id']
        tr_email=request.POST['email1']
        tr_name=request.POST['name1']
        tr_contact=request.POST['contact1']
        trdata=Teachers(registration_id=tr_id,email=tr_email,name=tr_name,contact=tr_contact)
        trdata.save()
        StaffRegistration.objects.get(id=id).delete()
        return redirect('managestaff')

    data1=StaffRegistration.objects.get(id=id)
    return render(request,'verifyTeacher.html',{'key4':data1})


def reject_staff_function(request,id):
    if(request.method == 'POST'):
        tr_id=request.POST['temp_id']
        tr_email=request.POST['email1']
        tr_name=request.POST['name1']
        tr_contact=request.POST['contact1']
        trdata=RejectedStaff(registration_id=tr_id,email=tr_email,name=tr_name,contact=tr_contact)
        trdata.save()
        StaffRegistration.objects.get(id=id).delete()
        return redirect('managestaff')
def login_fn(request):
    if(request.method=='POST'):
        user_name=request.POST['uname']
        contact=request.POST['contact1']
        try:
            user=Registration.objects.get(first_name=user_name)
            password=str(user.contact)
            if(user.first_name==user_name and password==contact):
                request.session['user_id']=user.id
                return redirect('home')
                # return render(request,'home.html',{'data':user})
            else:
                return render(request,'login.html',{'message':'login failed'})
        except Registration.DoesNotExist:
            return render(request,'login.html',{'message':'login failed'}) 
    return render(request,'login.html')

def home_fn(request):
    user_id=request.session['user_id']
    data=Registration.objects.get(id=user_id)
    return render(request,'home.html',{'userdata':data})

def profile_fn(request):
    try:
        user_id=request.session['user_id']
        data=Registration.objects.get(id=user_id)
        return render(request,'profile.html',{'userdata':data})
    except:
        return render(request,'login.html',{'message':'login to your account'})

def logout_fn(request):
    del request.session['user_id']
    return redirect('login')

def subjMg(request):
    classData=AddedClasses.objects.all()
    subj=Subjects.objects.all() 
    teachers=Staff.objects.all() 
    subj_details=AddedSubjects.objects.select_related('classes')
    return render(request,'subjectMgmt.html',{'key4':classData,'key3':subj,'teacher':teachers,'key6':subj_details})



def addsubjectfn(request):
    subjects=request.POST['subject']
    classID=request.POST['class']
    teacherID=request.POST['staff']
    addsubj=AddedSubjects(subject=subjects, classes_id=classID,teacher_id=teacherID)
    addsubj.save()
    return JsonResponse({'message':'data inserted successfully'})

def AssignClassTeacherfn(request):
    class_id=request.POST['class_name']
    teachers_id=request.POST['class_teacher']
    class_teacher=ClassTeacher(classes_id=class_id,teacher_id=teachers_id)
    class_teacher.save()
    return JsonResponse({'result':'data inserted successfully'})

def addTopicFun(request):
    if(request.method=='POST'):
        class_id=request.POST['class_name']
        subject_id=request.POST['subject_name'] 
        chapter=request.POST['chapter']
        title=request.POST['topic_title']
        files=request.FILES['file_content']
        filename=str(random())+files.name
        # print(filename)
        photo=FileSystemStorage()
        photo.save(filename,files)
        topic=Topic(chapter_id=chapter,classes_id=class_id,subject_id=subject_id,topic_name=title,topic_file=filename)
        topic.save()
        return render(request,'topicMN.html',{'message':'topic uploaded successfully'})
    user_id=request.session['registration_id']
    data=Staff.objects.get(registration_id=user_id)
    class_data=AddedClasses.objects.all()
    subj_details=AddedSubjects.objects.all()
    chapter_details=Chapter.objects.all()
    return render(request,'topicMN.html',{'userdata':data,'classdetails':class_data,'subj':subj_details})

def fileupload(request):
    if(request.method=='POST'):
        name=request.POST['name1'] 
        place=request.POST['place1'] 
        pic=request.FILES['pic1'] 
        # print(pic.name)
        filename=str(random())+pic.name
        # print(filename)
        photo=FileSystemStorage()
        photo.save(filename,pic)
        data=FileUpload(name=name,place=place,pic=filename)
        data.save()
        return render(request,'fileup.html',{'meassage':'sucessfully uploaded'})
    return render(request,'fileup.html')

def fileupload_table(request):
    details=FileUpload.objects.all()
    
    return render(request,'pictable.html',{'data':details})

@api_view(['GET'])
def viewAPIfn(request):
    data=Staff.objects.all()
    regdata=[{'id':x.registration_id,'first_name':x.first_name,'last_name':x.last_name,'email':x.email,'contact':x.contact,'address':x.address,'dob':x.dob,'username':x.user_name,'password':x.password,'profile_pic':x.profile_pic}for x in data]
    return JsonResponse({'result':regdata})

@api_view(['POST'])
def sendAPIfn(request):
    data=request.data
    saveData=Staff(first_name=data['fname'],last_name=data['lname'],email=data['email'],contact=data['contact'],address=data['address'],dob=data['dob'],user_name=data['uname'],password=data['password'],profile_pic=data['pic'])
    saveData.save()
    return Response('Data inserted successfully')


@api_view(['POST'])
def deleteAPIfn(request):
    data=request.data
    Staff.objects.get(registration_id=data['registration_id']).delete()
    return Response('data deleted successfully')

@api_view(['POST'])
def updateAPIfn(request):
    data=request.data
    Staff.objects.filter(registration_id=data['registration_id']).update(first_name=data['fname'],last_name=data['lname'],email=data['email'],contact=data['contact'],address=data['address'],dob=data['dob'],user_name=data['uname'],password=data['password'],profile_pic=data['pic'])
    return Response('Data updated successfully')


# student_registration API
@api_view(['GET'])
def viewStudentAPIfn(request):
    student_details=Students.objects.all()
    st_data=[{'id':x.registration_id,'first_name':x.first_name,'last_name':x.last_name,'classes':x.classes.classes,'contact':x.contact,'address':x.address,'dob':x.dob,'username':x.user_name,'password':x.password,'profile_pic':x.profile_pic}for x in student_details]
    return JsonResponse({'data':st_data})
@api_view(['POST'])
def postStudentAPIfn(request):
    data=request.data
    st_data=Students(first_name=data['fname'],last_name=data['lname'],classes_id=data['classes'],contact=data['contact'],address=data['address'],dob=data['dob'],user_name=data['uname'],password=data['password'],profile_pic=data['pic'])
    st_data.save()
    return Response('Data inserted successfully')

@api_view(['POST'])
def deleteStudentAPIfn(request):
    data=request.data
    Students.objects.get(registration_id=data['id']).delete()
    return Response('data deleted succuessfully')

@api_view(['POST'])
def updateStudentAPIfn(request):
    data=request.data
    Students.objects.filter(registration_id=data['id']).update(first_name=data['fname'],last_name=data['lname'],classes_id=data['classes'],contact=data['contact'],address=data['address'],dob=data['dob'],user_name=data['uname'],password=data['password'],profile_pic=data['pic'])
    return Response('data updated succuessfully')


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

# @csrf_exempt
# def staff_tablefn(request,id=0):
#     if(request.method=='GET'):
#         staff_data=Registration.objects.all()
#         staff_serializer=staff_table(staff_data,many='True')
#         return JsonResponse(staff_serializer.data,safe=False)
#     elif(request.method=='POST'):
#         user_details=JSONParser().parse(request)
#         dataSerializer=staff_table(data=user_details)
#         if(dataSerializer.is_valid()):
#             dataSerializer.save()
#             return JsonResponse('data inserted successfully',safe=False)
#         return JsonResponse('registration failed',safe=False)
#     elif(request.method=='DELETE'):
#         Registration.objects.get(id=id).delete()
#         return JsonResponse('data deleted successfully',safe=False)
#     elif(request.method=='PUT'):
#         upData=JSONParser().parse(request)
#         data_update=Registration.objects.get(id=upData['id'])
#         ser_data=staff_table(data_update,upData)
#         if(ser_data.is_valid()):
#             ser_data.save()
#             return JsonResponse('data updated successfully',safe=False)
#         else:
#             return JsonResponse('data updation failed',safe=False)
    
@csrf_exempt
def teachers_details_fn(request):
    if(request.method=='GET'):
        teachers_data=Staff.objects.all()
        tr_serializer=teachers_details(teachers_data,many='True')
        return JsonResponse(tr_serializer.data,safe=False)
    elif(request.method=='POST'):
        tr_data=JSONParser().parse(request)
        teachers_srlzr=teachers_details(data=tr_data)
        if(teachers_srlzr.is_valid()):
            teachers_srlzr.save()
            return JsonResponse('data insertion successfull',safe=False)
        return JsonResponse('registration failed',safe=False)
    
        
        
    




def weatherFn(request):
    return render(request,'weather.html')

def check_email_fn(request):
    user_email=request.POST['email']
    user=Registration.objects.get(email=user_email)
    if(user.email==user_email):
        return JsonResponse({'message':'email already exists'})

def formAjaxFun(request):
    return render(request,'form_ajax.html')

def testAjaxFun(request):
    name=request.POST['name']
    place=request.POST['place']
    email=request.POST['email']
    details=FormAj(name=name,email=email,place=place)
    details.save()
    return JsonResponse({'message':'data inserted successfully'})

def taableAjaxFn(request):
    return render(request,'formAjTable.html')

def ajaxdataFn(request):
    data=FormAj.objects.all()
    userdetails=[{'id':x.id,'name':x.name,'place':x.place,'email':x.email}for x in data] 
    return JsonResponse({'data':userdetails})   

def deleteAjDataFun(request):
    id=request.POST['id']
    FormAj.objects.get(id=id).delete()
    return JsonResponse({'message':'data deleted successfully'})
def updateAjDataFn(request):
    id=request.POST['id']
    data=FormAj.objects.get(id=id)
    details=[{'id':data.id,'name':data.name,'place':data.place,'email':data.email}]
    return JsonResponse({'data':details})

@login_required()
def dashboardFun(request):
    return render(request,'accounts/profile.html')

def admRegister(request):
    form=UserCreationForm()
    return render(request,'registration/create.html',{'form':form}) 




        

    # Create your views here.  