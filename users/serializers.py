
from rest_framework import serializers

from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, UserSerializer as BaseUserSerializer

from .models import Member, User

class Member_Serializer( serializers.ModelSerializer ):

    class Meta:
        model = Member
        fields = ['id', 'name', 'email', 'phone_number']


class UserCreateSerializer( BaseUserCreateSerializer ):
    class Meta( BaseUserCreateSerializer.Meta ):
        model = User
        fields = ['id', 'first_name', 'last_name', 'phone', 'address', 'email', 'password']


class UserSerializer( BaseUserSerializer ):
    class Meta( BaseUserSerializer.Meta ):
        ref_name='CustomUser'
        model = User
        fields = ['id', 'first_name', 'last_name', 'phone', 'address', 'email']