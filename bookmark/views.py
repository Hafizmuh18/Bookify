from django.core import serializers
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Bookmark
from django.shortcuts import get_object_or_404
from django.urls import reverse
from booklibrary.models import UserBook
from django.contrib import messages



@login_required
def show_bookmark(request):
    user = request.user
    bookmarks = Bookmark.objects.all()


    context ={
        'bookmarks':bookmarks,
    }

    return render(request, 'show_bookmark.html', context)

def add_bookmark(request, book_id):
    book = get_object_or_404(UserBook, id=book_id)
    user = request.user
    
    # Cek apakah buku tersebut sudah ada dalam bookmark pengguna
    if not Bookmark.objects.filter(user=user, book=book).exists():
        # Buat objek Bookmark baru dan simpan ke database
        bookmark = Bookmark(user=user, book=book)
        bookmark.save()
        
        # Tambahkan pesan sukses jika Anda menggunakan Django messages
        messages.success(request, f'"{book.book.title}" telah ditambahkan ke bookmark Anda.')
    else:
        # Tambahkan pesan peringatan jika buku sudah ada dalam bookmark
        messages.warning(request, f'"{book.book.title}" sudah ada di bookmark Anda.')
    
    # Redirect ke halaman yang sesuai
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def delete_bookmark(request, book_id):
    bookmark = get_object_or_404(Bookmark, id=book_id)
    bookmark.delete()

    return HttpResponseRedirect(reverse('bookmark:show_bookmark'))

def show_json(request):
    data = Bookmark.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")