from django.core import serializers
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from books.models import Books
from booklibrary.models import UserBook

# Create your views here.
def show_library(request):
    return render(request, 'library.html')

@csrf_exempt
def load_books_ajax(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query')  # Ambil kata kunci pencarian dari permintaan POST

        # Ambil buku dari basis data
        if search_query:
            books = Books.objects.filter(Q(title__icontains=search_query) | Q(isbn10__icontains=search_query) | Q(isbn13__icontains=search_query))
        else:
            books = Books.objects.all()

        # Serialisasi data buku ke dalam format JSON
        serialized_books = serializers.serialize('json', books)

        # Kirim data buku sebagai respons JSON
        return JsonResponse({'status': 'success', 'books': serialized_books})

    # Jika metode permintaan tidak valid
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})

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
