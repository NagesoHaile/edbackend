
from .models import User
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User 
        fields = ('email','first_name','last_name')
        read_only_fields = ('email')
        
class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User 
        fields = ('id','first_name','middle_name','last_name','email','password')