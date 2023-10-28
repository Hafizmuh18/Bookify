from django.urls import path, include
from homepage.views import *
from bookmark.views import *

app_name = 'bookmark'

urlpatterns = [
    path('', show_bookmark, name='show_bookmark'),
    path('add_to_bookmark/<int:book_id>/', add_to_bookmark, name='add_to_bookmark'),
    path('delete/<int:bookmark_id>/', delete_bookmark, name='delete_bookmark'),



]