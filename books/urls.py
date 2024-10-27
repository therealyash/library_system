# books/urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView  # Add this import


app_name = 'books'
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('book_list/', views.book_list, name='book_list'),
    path('allocate_books/', views.allocate_books, name='allocate_books'),
    path('cancel_allocate_books/', views.cancel_allocate_books, name='cancel_allocate_books'),
    path('get_book_counts/', views.get_book_counts, name='get_book_counts'),  # Add this line
    path('check_allocation_limit/', views.check_allocation_limit, name='check_allocation_limit'),  # New URL
    path('logout/', views.custom_logout, name='logout'),  # Redirect to login page after logout

]
