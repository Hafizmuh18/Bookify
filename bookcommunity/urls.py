from django.urls import path, include
from homepage.views import *
from bookcommunity.views import *

app_name = 'bookcommunity'

urlpatterns = [
    path('', show_community, name='show_community'),
]