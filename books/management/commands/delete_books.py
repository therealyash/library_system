# books/management/commands/delete_books.py
from django.core.management.base import BaseCommand
from books.models import Book

class Command(BaseCommand):
    help = 'Delete all books from the database'

    def handle(self, *args, **options):
        Book.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("All books deleted successfully!"))
