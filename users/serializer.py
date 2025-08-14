
from rest_framework import serializers
from .models import Member

class Member_Serializer( serializers.ModelSerializer ):

    class Meta:
        model = Member
        fields = ['id', 'name', 'email', 'phone_number']