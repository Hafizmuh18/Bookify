from django.core import serializers
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import bookMark



# Create your views here.


@login_required
def show_bookmark(request):
    user = request.user
    bookmarks = bookMark.objects.filter(user=user)

    return render(request, 'show_bookmark.html', {'bookmarks': bookmarks})

    