# books/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Book
from .forms import UserLoginForm
from django.http import JsonResponse
import logging

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('books:book_list')
        else:
            print(form.errors)  # Print errors to the console for debugging
    else:
        form = UserLoginForm()
    return render(request, 'books/login.html', {'form': form})

@login_required
def book_list(request):
    if request.method == "POST":
        selected_books = request.POST.getlist('books')
        action = request.POST.get('action')

        if action == 'allocate':
            for b_id in selected_books:
                book = Book.objects.get(b_id=b_id)
                if book.allocation_status == 'Available':
                    book.allocation_status = 'Allocated'
                    book.save()

        elif action == 'cancel_allocate':
            for b_id in selected_books:
                book = Book.objects.get(b_id=b_id)
                if book.allocation_status == 'Allocated':
                    # Here you can also check if the user is allowed to cancel
                    book.allocation_status = 'Available'
                    book.save()

        return redirect('books:book_list')

    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

@login_required
def allocate_books(request):
    if request.method == 'POST':
        book_ids = request.POST.getlist('book_ids')
        for book_id in book_ids:
            book = Book.objects.get(id=book_id)
            book.allocation_status = True
            book.allocated_to = request.user
            book.save()
        return JsonResponse({"status": "success", "action": "allocate"})
    return JsonResponse({"status": "failed"})

@login_required
def cancel_allocate_books(request):
    if request.method == 'POST':
        book_ids = request.POST.getlist('book_ids')
        for book_id in book_ids:
            book = Book.objects.get(id=book_id)
            if book.allocated_to == request.user:
                book.allocation_status = False
                book.allocated_to = None
                book.save()
        return JsonResponse({"status": "success", "action": "cancel_allocate"})
    return JsonResponse({"status": "failed"})

# books/views.py

def home(request):
    return redirect('books:login')



logger = logging.getLogger(__name__)

@login_required
def custom_logout(request):
    logger.debug(f"User {request.user} is logging out.")
    print(f"User {request.user} logged out.")
    logout(request)
    logger.debug("User has been logged out.")
    return redirect('books:login')


@login_required
def get_book_counts(request):
    allocated_count = Book.objects.filter(allocation_status='Allocated').count()
    available_count = Book.objects.filter(allocation_status='Available').count()
    return JsonResponse({
        'allocated_count': allocated_count,
        'available_count': available_count
    })
    
    
@login_required
def check_allocation_limit(request):
    allocated_count = Book.objects.filter(allocated_to=request.user, allocation_status='Allocated').count()
    available_count = Book.objects.filter(allocation_status='Available').count()
    
    return JsonResponse({
        'allocated_count': allocated_count,
        'available_count': available_count
    })


