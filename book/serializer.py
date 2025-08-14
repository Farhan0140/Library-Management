
from rest_framework import serializers
from .models import Book, Category, Author



class Category_Serializer( serializers.ModelSerializer ):
    class Meta:
        model = Category
        fields = ['id', 'name']

class Book_Serializer( serializers.ModelSerializer ):
    category_name = serializers.StringRelatedField(source='category', read_only=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    author_name = serializers.StringRelatedField(source='author', read_only=True)
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = ['id', 'title', 'category', 'category_name', 'author', 'author_name']