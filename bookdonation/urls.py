from django.urls import path, include
from homepage.views import *
from bookdonation.views import *

app_name = 'bookdonation'

urlpatterns = [
    path('', show_donation, name='show_donation'),
]