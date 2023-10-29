from django.core import serializers
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from .forms import ProductForm
from django.urls import reverse

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ProductForm
from django.urls import reverse
from .forms import data_donasi1
from django.http import HttpResponse
from django.core import serializers
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseNotFound
from books.models import Books 



#untuk membuat login form 
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
from django.shortcuts import get_object_or_404



def hapus_produk_ajax(request, product_id):
    if request.method == 'DELETE':
        product = get_object_or_404(data_donasi1, pk=product_id)
        product.delete()
        return HttpResponse(status=204)  # Menyatakan penghapusan berhasil
    return HttpResponse(status=400)  # Permintaan yang tidak valid

@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        judul_buku = request.POST.get("judul_buku")
        total_buku = request.POST.get("total_buku")
        resi = request.POST.get("resi")
        user = request.user

        if judul_buku and total_buku:  # Pastikan name dan total_buku tidak kosong
            new_product = data_donasi1(judul_buku=judul_buku, total_buku=total_buku, resi=resi, user=user)
            new_product.save()
            location.reload()
            return JsonResponse({'message': 'Product created successfully'})
            
        else:
            return JsonResponse({'error': 'Invalid data'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

def get_product_json(request):
    product_item = data_donasi1.objects.all()
    return HttpResponse(serializers.serialize('json', product_item))

def tambah_produk(request, product_id):
    try:
        produk = data_donasi1.objects.get(id=product_id)
        produk.total_buku += 1

        # Validasi agar jumlah produk tidak negatif
        if produk.total_buku < 0:
            produk.total_buku = 0

        produk.save()
        jumlah_item = sum([product.total_buku for product in data_donasi1.objects.all()])

        # Mengembalikan respons JSON yang berisi data jumlah produk yang baru
        return JsonResponse({'new_amount': produk.total_buku, 'new_total_item': jumlah_item})
    
    except data_donasi1.DoesNotExist:
        # Handle jika produk tidak ditemukan
        return JsonResponse({'error': 'Produk tidak ditemukan'}, status=404)

def kurang_produk(request, product_id):
    try:
        produk = data_donasi1.objects.get(id=product_id)
        produk.total_buku -= 1

        # Validasi agar jumlah produk tidak negatif
        if produk.total_buku < 0:
            produk.total_buku = 0

        produk.save()
        jumlah_item = sum([product.total_buku for product in data_donasi1.objects.all()])

        # Mengembalikan respons JSON yang berisi data jumlah produk yang baru
        return JsonResponse({'new_amount': produk.total_buku, 'new_total_item': jumlah_item})
    except data_donasi1.DoesNotExist:
        # Handle jika produk tidak ditemukan
        return JsonResponse({'error': 'Produk tidak ditemukan'}, status=404)


def hapus_produk(request, product_id):
    try:
        produk = data_donasi1.objects.get(id=product_id)
        produk.delete()
        # Redirect ke halaman yang sesuai setelah menghapus objek
        return redirect('bookdonation:show_donation')
    except data_donasi1.DoesNotExist:
        # Handle jika produk tidak ditemukan
        return redirect('bookdonation:show_donation')  # Redirect ke halaman produk setelah menghapus

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('bookdonation:login'))
    response.delete_cookie('last_login')
    return response

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("bookdonation:show_donation")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def register(request):
    form = UserCreationForm() # membuat UserCreationForm baru dari yang sudah di-impor sebelumnya dengan memasukkan QueryDict berdasarkan input dari user pada request.POST.

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() #membuat dan menyimpan data dari form tersebut. 
            messages.success(request, 'Your account has been successfully created!')
            return redirect('bookdonation:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def show_json_by_id(request, id):
    data = data_donasi1.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = data_donasi1.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml(request):
    data = data_donasi1.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = data_donasi1.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


    
@login_required(login_url='/login')
def show_donation(request):
    books = Books.objects.all()

    products = data_donasi1.objects.filter(user=request.user)

    jumlah_item = sum(product.total_buku for product in products)
    jumlah_poin =jumlah_item * 10

    jumlah_produk = products.count()
    last_login = request.COOKIES.get('last_login', 'Tidak ada informasi login sebelumnya')  # Menggunakan get untuk menghindari KeyError

    context = {
        'name': request.user.username,
        'products': products,
        'jumlah_produk': jumlah_produk,
        'jumlah_item': jumlah_item,
        'last_login': last_login,
        'jumlah_poin': jumlah_poin,
        'books' : books,
    }

    return render(request, "main.html", context)

