from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .models import Book, BorrowRecord, Category, Author
from .serializer import Book_Serializer, BorrowRecord_Serializer, Category_Serializer, Author_Serializer


class Book_View_Set( ModelViewSet ):
    queryset = Book.objects.select_related('author', 'category').all()
    serializer_class = Book_Serializer

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category_pk')
        author_id = self.kwargs.get('author_pk')

        if category_id:
            queryset = queryset.filter(category_id=category_id)
        elif author_id:
            queryset = queryset.filter(author_id=author_id)

        return queryset


class BorrowRecord_View_Set( ModelViewSet ):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecord_Serializer


class Category_View_Set( ModelViewSet ):
    queryset = Category.objects.all()
    serializer_class = Category_Serializer


class Author_View_Set( ModelViewSet ):
    queryset = Author.objects.all()
    serializer_class = Author_Serializer