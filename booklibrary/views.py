from django.core import serializers
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from books.models import Books

# Create your views here.
def show_library(request):
    books = Books.objects.all()

    context = {
        'books' : books,
    }

    return render(request, 'library.html', context)