from django.urls import path,include
from . import views

urlpatterns = [
path('',views.regfun,name='register' ),
path('regDetails',views.regtab,name='regDetails' ),
path('delete/<int:id>',views.delData,name='delete' ),
path('update/<int:userid>',views.updateData,name='update' ),
path('saveUpdate/<int:user_id>',views.saveUpdateData,name='saveUpdate' ),
path('viewAPI2',views.viewAPI2fn,name='viewAPI2' ),
path('postAPI2',views.postAPI2fn,name='postAPI2' ),
path('deleteAPI2',views.deleteAPI2fn,name='deleteAPI2' ),
path('updateAPI2',views.updateAPI2fn,name='updateAPI2' ),
]