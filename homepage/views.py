from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect, JsonResponse
# Create your views here.
from .forms import BookForm
from .models import Book
import json
from django.views.decorators.csrf import csrf_exempt
import datetime


def show_homepage(request):
    form = BookForm()
    context = {
            "form":form,
            "last_question": request.session.get('last_login', 'have not submit a question yet')
        }
    return render(request,'homepage.html',context)


@login_required(login_url='/login/')
def show_json(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

