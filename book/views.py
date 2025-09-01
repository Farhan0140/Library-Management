from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from .models import Book, BorrowRecord, Category, Author
from .serializer import Book_Serializer, BorrowRecord_Serializer, Category_Serializer, Author_Serializer, Update_Book_Serializer
from .permissions import Is_Librarian_ReadOnly


class Book_View_Set( ModelViewSet ):
    queryset = Book.objects.select_related('author', 'category').all()
    serializer_class = Book_Serializer
    permission_classes = [Is_Librarian_ReadOnly]

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category_pk')
        author_id = self.kwargs.get('author_pk')

        if category_id:
            queryset = queryset.filter(category_id=category_id)
        elif author_id:
            queryset = queryset.filter(author_id=author_id)

        return queryset
    
    @action(detail=True, methods=['get', 'patch'])
    def update_status(self, request, pk=None):
        book = self.get_object()

        if request.method == 'GET':
            serializer = Update_Book_Serializer(book)
            return Response(serializer.data)
        
        serializer = Update_Book_Serializer(book, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status': f'Book Availability Status Updated'})


class BorrowRecord_View_Set( ModelViewSet ):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecord_Serializer
    permission_classes=[IsAuthenticated]


class Category_View_Set( ModelViewSet ):
    queryset = Category.objects.all()
    serializer_class = Category_Serializer


class Author_View_Set( ModelViewSet ):
    queryset = Author.objects.all()
    serializer_class = Author_Serializer