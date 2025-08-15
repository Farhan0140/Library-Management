from django.db import models
from users.models import Member


class Category( models.Model ):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class Author( models.Model ):
    name = models.CharField(max_length=200)
    biography = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class Book( models.Model ):
    title = models.CharField(max_length=250)
    availability_status = models.BooleanField(default=True)
    published_date = models.DateField(blank=True, null=True)
    isbn = models.CharField(max_length=13, unique=True)

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books',
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='books',
    )

    def __str__(self):
        return f"{self.title} by {self.author}"
    

class BorrowRecord( models.Model ):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='borrow_records',
    )

    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name='borrow_records',
    )

    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(blank=True, null=True)
    returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.book} Borrowed by {self.member}"
