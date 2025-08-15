
from rest_framework import serializers
from .models import Book, Category, Author, BorrowRecord



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
        fields = ['id', 'title', 'category', 'category_name', 'author', 'author_name', 'availability_status']
    
    

class BorrowRecord_Serializer( serializers.ModelSerializer ):
    class Meta:
        model = BorrowRecord
        fields = ['id', 'book', 'member', 'borrow_date', 'returned']

    def validate(self, attrs):
        book = attrs.get('book')
        if not book.availability_status:
            raise serializers.ValidationError(
                {'book': 'You can\'t borrow this book, it\'s not available'}
            )
        
        return attrs

    def validate(self, attrs):
        # Only check book availability on creation, not update
        if self.instance is None:  # This means create
            book = attrs.get('book')
            if not book.availability_status:
                raise serializers.ValidationError(
                    {'book': 'You can\'t borrow this book, it\'s not available'}
                )
        return attrs
    
    def update(self, instance, validated_data):
        returned_status = validated_data.get('returned', instance.returned)
        if returned_status and not instance.returned:
            instance.book.availability_status = True
            instance.book.save()
        return super().update(instance, validated_data)
    

class Author_Serializer( serializers.ModelSerializer ):
    class Meta:
        model = Author
        fields = ['id', 'name', 'biography']
