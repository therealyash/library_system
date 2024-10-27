# books/management/commands/add_books.py
from django.core.management.base import BaseCommand
from books.models import Book

class Command(BaseCommand):
    help = 'Add sample books to the database'

    def handle(self, *args, **options):
        book_data = [
            
    {'b_id': 1, 'book_name': 'The Alchemist', 'author': 'Paulo Coelho', 'publication': 'HarperCollins', 'allocation_status': 'Available'},
    {'b_id': 2, 'book_name': 'The God of Small Things', 'author': 'Arundhati Roy', 'publication': 'Random House', 'allocation_status': 'Available'},
    {'b_id': 3, 'book_name': 'Chetan Bhagat Collection', 'author': 'Chetan Bhagat', 'publication': 'Rupa Publications', 'allocation_status': 'Available'},
    {'b_id': 4, 'book_name': 'Two States', 'author': 'Chetan Bhagat', 'publication': 'Rupa Publications', 'allocation_status': 'Available'},
    {'b_id': 5, 'book_name': 'The Immortals of Meluha', 'author': 'Amish Tripathi', 'publication': 'Westland', 'allocation_status': 'Available'},
    {'b_id': 6, 'book_name': 'The Train to Pakistan', 'author': 'Khushwant Singh', 'publication': 'Penguin Books', 'allocation_status': 'Available'},
    {'b_id': 7, 'book_name': 'The White Tiger', 'author': 'Aravind Adiga', 'publication': 'Free Press', 'allocation_status': 'Available'},
    {'b_id': 8, 'book_name': 'A Suitable Boy', 'author': 'Vikram Seth', 'publication': 'Penguin Books', 'allocation_status': 'Available'},
    {'b_id': 9, 'book_name': 'Five Point Someone', 'author': 'Chetan Bhagat', 'publication': 'Rupa Publications', 'allocation_status': 'Available'},
    {'b_id': 10, 'book_name': 'The Bhagat Singh Reader', 'author': 'Bhagat Singh', 'publication': 'Roli Books', 'allocation_status': 'Available'},
    {'b_id': 11, 'book_name': 'Life Is What You Make It', 'author': 'Preeti Shenoy', 'publication': 'Westland', 'allocation_status': 'Available'},
    {'b_id': 12, 'book_name': 'The 3 Mistakes of My Life', 'author': 'Chetan Bhagat', 'publication': 'Rupa Publications', 'allocation_status': 'Available'},
    {'b_id': 13, 'book_name': 'What Young India Wants', 'author': 'Chetan Bhagat', 'publication': 'Rupa Publications', 'allocation_status': 'Available'},
    {'b_id': 14, 'book_name': 'The Palace of Illusions', 'author': 'Chitra Banerjee Divakaruni', 'publication': 'Picador', 'allocation_status': 'Available'},
    {'b_id': 15, 'book_name': 'The Boy Who Knew Too Much', 'author': 'Vikram Chandra', 'publication': 'HarperCollins', 'allocation_status': 'Available'},
    {'b_id': 16, 'book_name': "The Orphan Master's Son", 'author': 'Adam Johnson', 'publication': 'Random House', 'allocation_status': 'Available'},
    {'b_id': 17, 'book_name': 'When a Panther Meets a Little Girl', 'author': 'Sujata Bhatt', 'publication': 'Katha', 'allocation_status': 'Available'},
    {'b_id': 18, 'book_name': 'Train to Pakistan', 'author': 'Khushwant Singh', 'publication': 'Penguin India', 'allocation_status': 'Available'},
    {'b_id': 19, 'book_name': 'The Secret of the Nagas', 'author': 'Amish Tripathi', 'publication': 'Westland', 'allocation_status': 'Available'},
    {'b_id': 20, 'book_name': 'The Simoquin Prophecies', 'author': 'Samit Basu', 'publication': 'Penguin India', 'allocation_status': 'Available'},
    {'b_id': 21, 'book_name': 'Brahmastra', 'author': 'Ravi Subramanian', 'publication': 'Westland', 'allocation_status': 'Available'},
    {'b_id': 22, 'book_name': 'The Best of Me', 'author': 'Nicholas Sparks', 'publication': 'Sphere', 'allocation_status': 'Available'},
    {'b_id': 23, 'book_name': "God's Own Country", 'author': 'Sanjay Bahadur', 'publication': 'Hachette India', 'allocation_status': 'Available'},
    {'b_id': 24, 'book_name': 'Chai, Chai: Travels in Places Where You Stop But Never Get Off', 'author': 'Rishad Saam Mehta', 'publication': 'Hachette India', 'allocation_status': 'Available'},
    {'b_id': 25, 'book_name': 'The Art of Racing in the Rain', 'author': 'Garth Stein', 'publication': 'HarperCollins', 'allocation_status': 'Available'},
    {'b_id': 26, 'book_name': 'Me Before You', 'author': 'Jojo Moyes', 'publication': 'Penguin Books', 'allocation_status': 'Available'},
    {'b_id': 27, 'book_name': 'A Thousand Splendid Suns', 'author': 'Khaled Hosseini', 'publication': 'Bloomsbury', 'allocation_status': 'Available'},
    {'b_id': 28, 'book_name': 'The Kite Runner', 'author': 'Khaled Hosseini', 'publication': 'Bloomsbury', 'allocation_status': 'Available'},
    {'b_id': 29, 'book_name': 'Educated', 'author': 'Tara Westover', 'publication': 'Random House', 'allocation_status': 'Available'},
    {'b_id': 30, 'book_name': 'The Great Indian Novel', 'author': 'Shashi Tharoor', 'publication': 'Penguin India', 'allocation_status': 'Available'},
    
    ]

        for book in book_data:
            Book.objects.create(**book)

        self.stdout.write(self.style.SUCCESS("30 books added successfully!"))
