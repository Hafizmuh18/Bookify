from atexit import register
from django.contrib import admin

from homepage.forms import BookForm
from .models import Book
# Register your models here.
admin.site.register(Book)