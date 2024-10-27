# books/models.py
from django.contrib.auth.models import User
from django.db import models

class Book(models.Model):
    b_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication = models.CharField(max_length=255)
    allocation_status = models.CharField(max_length=50, default='Available')  # Using CharField for status
    allocated_to = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.book_name
