from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .models import Book
from .serializer import Book_Serializer


class Book_View_Set( ModelViewSet ):
    queryset = Book.objects.select_related('author', 'category').all()
    serializer_class = Book_Serializer

