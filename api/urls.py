from django.urls import path, include

from rest_framework.routers import DefaultRouter

from book.views import Book_View_Set
from users.views import Member_View_Set


router = DefaultRouter()
router.register('books', Book_View_Set)
router.register('users', Member_View_Set)


urlpatterns = [
    path('', include(router.urls)),
]