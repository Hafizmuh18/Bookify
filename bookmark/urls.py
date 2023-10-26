from django.urls import path, include
from homepage.views import *
from bookmark.views import *

app_name = 'bookmark'

urlpatterns = [
    path('', show_bookmark, name='show_bookmark'),
]