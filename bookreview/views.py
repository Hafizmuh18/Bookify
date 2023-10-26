from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import Book, Review, Favorite
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.

@login_required
def book_review(request, book_id):
    book = Book.objects.get(pk=book_id)
    reviews = Review.objects.filter(book=book)
    return render(request, 'bookreview/book_review.html', {'book': book, 'reviews': reviews})

@login_required
def add_review(request, book_id):
    book = Book.objects.get(pk=book_id)
    if request.method == 'POST':
        rating = request.POST['rating']
        comment = request.POST['comment']
        user = request.user
        review = Review(book=book, user=user, rating=rating, comment=comment)
        review.save()
        return redirect('book_review', book_id=book_id)
    return render(request, 'bookreview/add_review.html', {'book': book})

@login_required
def favorite_books(request):
    user = request.user
    favorites = Favorite.objects.filter(user=user)
    return render(request, 'bookreview/favorite_books.html', {'favorites': favorites})
