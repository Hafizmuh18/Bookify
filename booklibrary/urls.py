from django.urls import path, include
from homepage.views import *
from booklibrary.views import *

app_name = 'booklibrary'

urlpatterns = [
    path('', show_library, name='show_library'),
]