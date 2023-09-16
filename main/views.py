from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ItemForm
from django.urls import reverse
from main.models import Item

# Create your views here.
def show_main(request):
    products = Item.objects.all()

    context = {
        'name': 'Anisha Putri Qonitah', # Nama kamu
        'class': 'PBP D', # Kelas PBP kamu
        'products': products
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)