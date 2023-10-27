from django.core import serializers
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from books.models import Books
from booklibrary.models import UserBook

# Create your views here.
# MAIN PAGE
def show_library(request):
    books = Books.objects.all()
    # userstatus = UserBook.objects.filter(user=request.user, status = 'not_started')

    context = {
        'books' : books,
        # 'userstatus' : userstatus
    }

    return render(request, 'library.html', context)

# SHOW USER'S BOOKSHELF
@login_required
def get_user_bookshelf(request):
    user = request.user
    user_books = UserBook.objects.filter(user=request.user)

    books_data = []

    for user_book in user_books:
        book = user_book.book
        books_data.append({
            'id' : book.id,
            'title': book.title,
            'author': book.author,
            'published_year': book.published_year,
            'genre': book.genre,
            'pages' : book.pages,
            'description': book.description,
            'thumbnail': book.thumbnail,
            'ratings_avg': book.ratings_avg,
            'ratings_count': book.ratings_count,
            'isbn10': book.isbn10,
            'isbn13': book.isbn13,
            'status': user_book.get_status_display()
        })

    return JsonResponse(books_data, safe=False)

from django.http import JsonResponse

# BORROW BOOK
def borrow_book(request):
    if request.method == 'POST':
        user = request.user
        book_id = request.POST.get('book_id')
        book = Books.objects.get(id=book_id)

        # Create or get a UserBook instance
        user_book, created = UserBook.objects.get_or_create(user=user, book=book)

        if created:
            user_book.status = 'reading'
            user_book.save()

            return JsonResponse({'status': 'success', 'message': 'Book added to shelf successfully!'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Book is already in your shelf!'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request.'})

# COMPLETE READING
def complete_reading(request):
    if request.method == 'POST':
        user = request.user
        book_id = request.POST.get('book_id')
        book = Books.objects.get(id=book_id)

        # Get a UserBook instance
        user_book = UserBook.objects.filter(user=user, book=book).first()

        if user_book:
            user_book.status = 'completed'
            user_book.save()
            return JsonResponse({'status': 'success', 'message': 'Status updated successfully!'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Book is not in your shelf!'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request.'})
# REREADING BOOK
def re_read_book(request):
    if request.method == 'POST':
        user = request.user
        book_id = request.POST.get('book_id')
        book = Books.objects.get(id=book_id)

        # Get a UserBook instance
        user_book = UserBook.objects.filter(user=user, book=book).first()

        if user_book:
            user_book.status = 'reading'
            user_book.save()

            return JsonResponse({'status': 'success', 'message': 'Book status updated to currently reading!'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Book not found in your shelf!'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request.'})
