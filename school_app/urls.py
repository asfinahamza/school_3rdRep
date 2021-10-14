from django.urls import path,include
from . import views
urlpatterns = [

    
    path('',views.welcome,name='welcome' ),
    path('adminLogin',views.adminLoginFun,name='adminLogin' ),
    path('adminLogout',views.adminLogoutFun,name='adminLogout' ),
    path('index',views.indexf,name='index' ),
    path('sum2',views.sumf,name='sum2' ),
    path('fsum',views.findsum,name='fsum' ),
    path('psum',views.postsum,name='psum' ),
    
    
    path('class',views.classfn,name='class' ),
    path('addClass',views.addClassFn,name='addClass' ),
    path('addsubject',views.addsubjectfn,name='addsubject' ),
    path('AssignClassTeacher',views.AssignClassTeacherfn,name='AssignClassTeacher' ),
    path('studentReg',views.studentReg,name='studentReg' ),
    path('studentLogin',views.studentLoginFn,name='studentLogin' ),
    path('studentlogout',views.studentLogout_fn,name='studentlogout' ),
    path('studentProfile',views.studentProfileFn,name='studentProfile' ),
    path('staffReg',views.staffReg,name='staffReg' ),
    path('staffLogin',views.staffLogin,name='staffLogin' ),
    path('staffLogout',views.staffLogoutFn,name='staffLogout' ),
    path('staffProfile',views.staffProfileFn,name='staffProfile' ),
    path('addTopic',views.addTopicFun,name='addTopic' ),
    path('managestaff',views.staffManage,name='managestaff' ),
    path('staffDetails/<int:id>',views.staffDetailsFunction,name='staffDetails' ),
    path('verifyStaff/<int:id>',views.verifyStaffFunction,name='verifyStaff' ),
    path('rejectStaff/<int:id>',views.rejectStaffFunction,name='rejectStaff' ),
    path('verifyStudent/<int:id>',views.verifyStudentFunction,name='verifyStudent' ),
    path('declineStudent/<int:id>',views.declineStudentFunction,name='declineStudent' ),
    path('managestudent',views.studentManage,name='managestudent' ),
    path('studentDetails/<int:id>',views.studentDetailsFunction,name='studentDetails' ),
    path('deleteClass/<int:id>',views.deleteClassFn,name='deleteClass' ),
    path('deleteSubject/<int:id>',views.deleteSubjectFn,name='deleteSubject' ),
    path('deleteClassTeacher/<int:id>',views.deleteClassTeacherFn,name='deleteClassTeacher' ),
    path('trdash',views.trdashbdFn,name='trdash' ),
    path('chapterMN',views.chapterMnFun,name='chapterMN' ),
    path('subjectOfClass',views.subjectOfClassFun,name='subjectOfClass' ),
    path('chapterInSubject',views.chapterInSubjectFun,name='chapterInSubject' ),
    path('subjectMN',views.subjMg,name='subjectMN' ),
    path('subjects',views.subjectsFun,name='subjects'),
    path('chapters',views.chapterFunction,name='chapters' ),
    path('exam',views.examFunction,name='exam' ),
    path('question',views.questionFunction,name='question' ),
    path('assignments',views.assignmentsFunction,name='assignments' ),
    path('studentDash',views.stdntDashfn,name='studentDash' ),
    path('verifyTeacher/<int:id>',views.verifyTeacher,name='verifyTeacher' ),
    path('rejectStaff/<int:id>',views.reject_staff_function,name='rejectStaff' ),
    path('login',views.login_fn,name='login' ),
    path('user_profile',views.profile_fn,name='user_profile' ),
    path('home',views.home_fn,name='home' ),
    path('logout',views.logout_fn,name='logout' ),
    path('upload',views.fileupload,name='upload' ),
    path('uploadtable',views.fileupload_table,name='uploadtable' ),
    path('viewAPI',views.viewAPIfn,name='viewAPI' ),
    path('postAPI',views.sendAPIfn,name='postAPI' ),
    path('deleteAPI',views.deleteAPIfn,name='deleteAPI' ),
    path('updateAPI',views.updateAPIfn,name='updateAPI' ),
    path('viewStudentAPI',views.viewStudentAPIfn,name='viewStudentAPI' ),
    path('postStudentAPI',views.postStudentAPIfn,name='postStudentAPI' ),
    path('deleteStudentAPI',views.deleteStudentAPIfn,name='deleteStudentAPI' ),
    path('updateStudentAPI',views.updateStudentAPIfn,name='updateStudentAPI' ),
    # path('staff_table',views.staff_tablefn,name='staff_table' ),
    # path('staff_table/<int:id>',views.staff_tablefn,name='staff_table' ),
    path('teachers_details',views.teachers_details_fn,name='teachers_details' ),
    path('weather',views.weatherFn,name='weather' ),
    path('check_email',views.check_email_fn,name='check_email' ),
    path('formAjax',views.formAjaxFun,name='formtAjax'),
    path('testAjax',views.testAjaxFun,name='testAjax'),
    path('taableAjax',views.taableAjaxFn,name='taableAjax'),
    path('ajaxdata',views.ajaxdataFn,name='ajaxdata'),
    path('deleteAjData',views.deleteAjDataFun,name='deleteAjData'),
    path('updateAjData',views.updateAjDataFn,name='updateAjData'),
    path('dashboard',views.dashboardFun,name='dashboard'),
    path('admRegister',views.admRegister,name='admRegister'),
    
]