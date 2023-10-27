from django.urls import path
from bookreview import views
# from bookreview.views import book_review, add_review, favorite_books
from bookreview.views import show_library

app_name = 'bookreview'

# urlpatterns = [
#     path('book/<int:book_id>/review/', book_review, name='book_review'),
#     path('book/<int:book_id>/add_review/', add_review, name='add_review'),
#     path('favorites/', favorite_books, name='favorite_books'),
# ]

urlpatterns = [
    path('', show_library, name='show_library'),
]
