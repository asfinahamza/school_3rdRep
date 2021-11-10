from django.urls import path,include
from . import views
urlpatterns = [

    path('',views.func,name='welcome' ),
    path('index',views.index,name='index' ),
    path('studentDB',views.studentDB,name='studentDB' ),
    path('adminDB',views.adminDB,name='adminDB' ),
    path('studentLogin',views.studentLoginFunc,name='studentLogin' ),
    path('adminLogin',views.adminLoginFunc,name='adminLogin' ),
    path('adminReg',views.adminRegFunc,name='adminReg' ),
    path('studentReg',views.studentRegFunc,name='studentReg' ),
    path('studentDetails/<int:id>',views.studentDetailsFn,name='studentDetails' ),
    path('studentProfile',views.studentProfileFn,name='studentProfile' ),
    path('updatestudentProfile',views.updatestudentProfileFn,name='updatestudentProfile' ),
    path('adminLogout',views.adminLogoutFun,name='adminLogout' ),
    path('studentLogout',views.studentLogoutFun,name='studentLogout' ),

    
]
