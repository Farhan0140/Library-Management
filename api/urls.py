from django.urls import path, include

from rest_framework_nested import routers

from book.views import Book_View_Set, BorrowRecord_View_Set, Category_View_Set, Author_View_Set
from users.views import Member_View_Set


router = routers.DefaultRouter()
router.register('books', Book_View_Set, basename='books')
router.register('members', Member_View_Set, basename='members')
router.register('borrow-record', BorrowRecord_View_Set)
router.register('categories', Category_View_Set, basename='category')
router.register('author', Author_View_Set, basename='author')


category_router = routers.NestedDefaultRouter(router, 'categories', lookup='category')
category_router.register('books', Book_View_Set, basename='category-books')

author_router = routers.NestedDefaultRouter(router, 'author', lookup='author')
author_router.register('books', Book_View_Set, basename='author-books')


urlpatterns = [
    path('', include(router.urls)),
    path('', include(category_router.urls)),
    path('', include(author_router.urls)),
]