from rest_framework import serializers
from . models import *
# class staff_table(serializers.ModelSerializer):
#     class Meta:
#         model=Registration
#         fields=('id','first_name','last_name','place','email','contact','dob')

class teachers_details(serializers.ModelSerializer):
    class Meta:
        model=Staff
        fields=('registration_id','first_name','last_name','email','contact','address','dob','user_name','password','profile_pic')