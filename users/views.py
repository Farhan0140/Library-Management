from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Member
from .serializer import Member_Serializer


class Member_View_Set( ModelViewSet ):
    queryset = Member.objects.all()
    serializer_class = Member_Serializer

