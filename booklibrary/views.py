from django.core import serializers
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from books.models import Books
from booklibrary.models import UserBook

# Create your views here.
def show_library(request):
    books = Books.objects.all()
    # userstatus = UserBook.objects.filter(user=request.user, status = 'not_started')

    context = {
        'books' : books,
        # 'userstatus' : userstatus
    }

    return render(request, 'library.html', context)

@login_required
def get_user_bookshelf(request):
    user = request.user
    user_books = UserBook.objects.filter(user=request.user)

    books_data = []

    for user_book in user_books:
        book = user_book.book
        books_data.append({
            'title': book.title,
            'thumbnail': book.thumbnail,
            'genre': book.genre,
            'ratings_avg': book.ratings_avg,
            'ratings_count': book.ratings_count,
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

        # You can set additional details for the UserBook instance here if needed
        # For example, you might want to update the status to "reading" here
        if created:
            user_book.status = 'reading'
            user_book.save()

            return JsonResponse({'status': 'success', 'message': 'Book added to shelf successfully!'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Book is already in your shelf!'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request.'})
