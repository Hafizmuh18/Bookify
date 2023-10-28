from django.core import serializers
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import bookMark, Book
from django.shortcuts import get_object_or_404
from books.models import Books
from django.contrib import messages
from django.http import HttpResponseBadRequest





# Create your views here.


@login_required
def show_bookmark(request):
    user = request.user
    bookmarks = Books.objects.all()

    context ={
        'bookmarks':bookmarks,
    }

    return render(request, 'show_bookmark.html', context)

def add_to_bookmark(request, book_id):
    user = request.user
    book = get_object_or_404(Book, id=book_id)
    bookmark, created = bookMark.objects.get_or_create(user=user, book=book)

    if created:
        messages.success(request, f'"{book.title}" telah ditambahkan ke bookmark Anda.')
    else:
        messages.warning(request, f'"{book.title}" sudah ada di bookmark Anda.')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
@csrf_exempt
def delete_bookmark(request, bookmark_id):
    if request.method == 'POST':
        user = request.user
        bookmark = get_object_or_404(bookMark, id=bookmark_id, user=user)
        bookmark.delete()
        messages.success(request, 'Bookmark berhasil dihapus')  
        return redirect('bookmark:show_bookmark')  
    else:
        return HttpResponseBadRequest('Metode permintaan tidak valid')
