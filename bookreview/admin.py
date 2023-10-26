from django.contrib import admin
from .models import Book, Review, Favorite

# Register your models here.
admin.site.register(Review)
admin.site.register(Favorite)
admin.site.register(Book)