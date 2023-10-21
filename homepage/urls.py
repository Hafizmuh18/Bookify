from django.urls import path, include
from homepage.views import *
app_name = 'homepage'

urlpatterns = [
    path('', show_homepage, name='show_homepage'),
    # path('book_review/', show_book_review, name='show_book_review'),
    path('json/', show_json, name='show_json'),
]